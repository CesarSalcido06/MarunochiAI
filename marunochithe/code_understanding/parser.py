"""Tree-sitter based code parser for multi-language AST extraction."""

import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from loguru import logger

try:
    import tree_sitter_python as ts_python
    import tree_sitter_javascript as ts_javascript
    import tree_sitter_typescript as ts_typescript
    from tree_sitter import Language, Parser, Node
    TREE_SITTER_AVAILABLE = True
except ImportError:
    TREE_SITTER_AVAILABLE = False
    logger.warning("tree-sitter not available, parser functionality will be limited")

from .models import ParsedFile, Function, Class, Language as LangEnum


class CodeParser:
    """Multi-language AST parsing using tree-sitter."""

    def __init__(self):
        """Initialize parser with supported languages."""
        self.parsers: Dict[str, Parser] = {}
        self.cache: Dict[str, Tuple[float, ParsedFile]] = {}  # filepath -> (mtime, parsed)

        if TREE_SITTER_AVAILABLE:
            self._init_parsers()
        else:
            logger.warning("Tree-sitter parsers not initialized")

    def _init_parsers(self) -> None:
        """Initialize tree-sitter parsers for each language."""
        try:
            # Python
            PY_LANGUAGE = Language(ts_python.language())
            py_parser = Parser(PY_LANGUAGE)
            self.parsers['python'] = py_parser

            # JavaScript
            JS_LANGUAGE = Language(ts_javascript.language())
            js_parser = Parser(JS_LANGUAGE)
            self.parsers['javascript'] = js_parser

            # TypeScript
            TS_LANGUAGE = Language(ts_typescript.language_typescript())
            ts_parser = Parser(TS_LANGUAGE)
            self.parsers['typescript'] = ts_parser

            logger.info(f"Initialized parsers for: {list(self.parsers.keys())}")
        except Exception as e:
            logger.error(f"Failed to initialize parsers: {e}")

    async def parse_file(self, filepath: str) -> Optional[ParsedFile]:
        """
        Parse code file to structured AST.

        Args:
            filepath: Path to code file

        Returns:
            ParsedFile with extracted structure, or None on error
        """
        try:
            path = Path(filepath).expanduser().resolve()

            if not path.exists():
                logger.error(f"File not found: {filepath}")
                return None

            # Determine language from extension
            language = self._detect_language(path)
            if language == LangEnum.UNKNOWN or language.value not in self.parsers:
                logger.debug(f"Unsupported language for {filepath}")
                return None

            # Read file content
            content = path.read_text(encoding='utf-8')

            # Parse with tree-sitter
            parser = self.parsers[language.value]
            tree = parser.parse(bytes(content, 'utf8'))

            # Extract code elements
            parsed = ParsedFile(
                filepath=str(path),
                language=language,
                raw_content=content
            )

            # Extract functions, classes, imports
            root_node = tree.root_node
            parsed.functions = self._extract_functions(root_node, content, language)
            parsed.classes = self._extract_classes(root_node, content, language)
            parsed.imports = self._extract_imports(root_node, content, language)
            parsed.docstrings = self._extract_docstrings(root_node, content, language)

            return parsed

        except Exception as e:
            logger.error(f"Failed to parse {filepath}: {e}")
            return None

    async def parse_file_cached(self, filepath: str) -> Optional[ParsedFile]:
        """
        Parse file with mtime-based caching.

        Args:
            filepath: Path to code file

        Returns:
            ParsedFile from cache if unchanged, otherwise fresh parse
        """
        try:
            path = Path(filepath).expanduser().resolve()
            mtime = path.stat().st_mtime

            # Check cache
            if filepath in self.cache:
                cached_mtime, cached_parsed = self.cache[filepath]
                if cached_mtime == mtime:
                    logger.debug(f"Cache hit for {filepath}")
                    return cached_parsed

            # Parse fresh
            parsed = await self.parse_file(filepath)
            if parsed:
                self.cache[filepath] = (mtime, parsed)

            return parsed

        except Exception as e:
            logger.error(f"Cache read failed for {filepath}: {e}")
            return await self.parse_file(filepath)

    def _detect_language(self, path: Path) -> LangEnum:
        """Detect programming language from file extension."""
        ext_map = {
            '.py': LangEnum.PYTHON,
            '.js': LangEnum.JAVASCRIPT,
            '.jsx': LangEnum.JAVASCRIPT,
            '.ts': LangEnum.TYPESCRIPT,
            '.tsx': LangEnum.TYPESCRIPT,
        }
        return ext_map.get(path.suffix, LangEnum.UNKNOWN)

    def _extract_functions(
        self,
        node: Node,
        source: str,
        language: LangEnum
    ) -> List[Function]:
        """Extract function/method definitions from AST."""
        functions = []

        function_types = {
            LangEnum.PYTHON: ['function_definition'],
            LangEnum.JAVASCRIPT: ['function_declaration', 'arrow_function', 'function'],
            LangEnum.TYPESCRIPT: ['function_declaration', 'arrow_function', 'method_definition'],
        }

        valid_types = function_types.get(language, [])

        def traverse(n: Node) -> None:
            if n.type in valid_types:
                func = self._parse_function(n, source, language)
                if func:
                    functions.append(func)

            for child in n.children:
                traverse(child)

        traverse(node)
        return functions

    def _parse_function(
        self,
        node: Node,
        source: str,
        language: LangEnum
    ) -> Optional[Function]:
        """Parse a function node into Function object."""
        try:
            name = self._get_node_name(node, source)
            docstring = self._get_docstring(node, source, language)

            return Function(
                name=name or 'anonymous',
                start_line=node.start_point[0] + 1,  # 1-indexed
                end_line=node.end_point[0] + 1,
                docstring=docstring,
                signature=self._get_node_text(node, source)[:200],  # First 200 chars
            )
        except Exception as e:
            logger.debug(f"Failed to parse function: {e}")
            return None

    def _extract_classes(
        self,
        node: Node,
        source: str,
        language: LangEnum
    ) -> List[Class]:
        """Extract class definitions from AST."""
        classes = []

        class_types = {
            LangEnum.PYTHON: ['class_definition'],
            LangEnum.JAVASCRIPT: ['class_declaration'],
            LangEnum.TYPESCRIPT: ['class_declaration'],
        }

        valid_types = class_types.get(language, [])

        def traverse(n: Node) -> None:
            if n.type in valid_types:
                cls = self._parse_class(n, source, language)
                if cls:
                    classes.append(cls)

            for child in n.children:
                traverse(child)

        traverse(node)
        return classes

    def _parse_class(
        self,
        node: Node,
        source: str,
        language: LangEnum
    ) -> Optional[Class]:
        """Parse a class node into Class object."""
        try:
            name = self._get_node_name(node, source)
            docstring = self._get_docstring(node, source, language)

            # Extract methods (functions within class)
            methods = []

            def extract_methods(n: Node) -> None:
                """Recursively extract methods from class body."""
                if n.type in ['function_definition', 'method_definition']:
                    method = self._parse_function(n, source, language)
                    if method:
                        methods.append(method)
                for child in n.children:
                    extract_methods(child)

            # Look for methods in class body
            for child in node.children:
                if child.type == 'block':  # Python: methods are in block
                    extract_methods(child)
                elif child.type in ['function_definition', 'method_definition']:
                    # Direct children (some languages)
                    method = self._parse_function(child, source, language)
                    if method:
                        methods.append(method)

            return Class(
                name=name or 'AnonymousClass',
                start_line=node.start_point[0] + 1,
                end_line=node.end_point[0] + 1,
                docstring=docstring,
                methods=methods,
            )
        except Exception as e:
            logger.debug(f"Failed to parse class: {e}")
            return None

    def _extract_imports(
        self,
        node: Node,
        source: str,
        language: LangEnum
    ) -> List[str]:
        """Extract import statements."""
        imports = []

        import_types = {
            LangEnum.PYTHON: ['import_statement', 'import_from_statement'],
            LangEnum.JAVASCRIPT: ['import_statement'],
            LangEnum.TYPESCRIPT: ['import_statement'],
        }

        valid_types = import_types.get(language, [])

        def traverse(n: Node) -> None:
            if n.type in valid_types:
                import_text = self._get_node_text(n, source)
                if import_text:
                    imports.append(import_text)

            for child in n.children:
                traverse(child)

        traverse(node)
        return imports

    def _extract_docstrings(
        self,
        node: Node,
        source: str,
        language: LangEnum
    ) -> List[str]:
        """Extract docstrings/comments."""
        docstrings = []

        # Python docstrings
        if language == LangEnum.PYTHON:
            for child in node.children:
                if child.type == 'expression_statement':
                    for expr_child in child.children:
                        if expr_child.type == 'string':
                            text = self._get_node_text(expr_child, source)
                            if text:
                                docstrings.append(text)

        return docstrings

    def _get_node_name(self, node: Node, source: str) -> Optional[str]:
        """Get the name identifier from a node."""
        for child in node.children:
            if child.type == 'identifier' or child.type == 'property_identifier':
                return self._get_node_text(child, source)
        return None

    def _get_docstring(
        self,
        node: Node,
        source: str,
        language: LangEnum
    ) -> Optional[str]:
        """Extract docstring from a function/class node."""
        if language == LangEnum.PYTHON:
            # Python docstring is first expression statement with a string
            for child in node.children:
                if child.type == 'block':
                    for block_child in child.children:
                        if block_child.type == 'expression_statement':
                            for expr_child in block_child.children:
                                if expr_child.type == 'string':
                                    text = self._get_node_text(expr_child, source)
                                    # Clean up quotes
                                    if text:
                                        return text.strip('"""').strip("'''").strip('"').strip("'").strip()

        # JavaScript/TypeScript comments (simplified)
        # Could be enhanced to parse JSDoc comments

        return None

    def _get_node_text(self, node: Node, source: str) -> str:
        """Get the text content of a node."""
        return source[node.start_byte:node.end_byte]

    def clear_cache(self) -> None:
        """Clear the parse cache."""
        self.cache.clear()
        logger.debug("Parse cache cleared")
