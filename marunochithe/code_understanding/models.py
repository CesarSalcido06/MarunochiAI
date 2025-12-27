"""Data models for code understanding."""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple
from enum import Enum
import uuid


class ChunkType(str, Enum):
    """Type of code chunk."""
    FILE = "file"
    CLASS = "class"
    METHOD = "method"
    FUNCTION = "function"


class Language(str, Enum):
    """Supported programming languages."""
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"
    UNKNOWN = "unknown"


@dataclass
class Function:
    """Represents a function/method in code."""
    name: str
    start_line: int
    end_line: int
    docstring: Optional[str] = None
    signature: Optional[str] = None
    parameters: List[str] = field(default_factory=list)
    return_type: Optional[str] = None


@dataclass
class Class:
    """Represents a class in code."""
    name: str
    start_line: int
    end_line: int
    docstring: Optional[str] = None
    methods: List[Function] = field(default_factory=list)
    attributes: List[str] = field(default_factory=list)
    base_classes: List[str] = field(default_factory=list)


@dataclass
class ParsedFile:
    """Result of parsing a code file."""
    filepath: str
    language: Language
    functions: List[Function] = field(default_factory=list)
    classes: List[Class] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    top_level_vars: List[str] = field(default_factory=list)
    docstrings: List[str] = field(default_factory=list)
    raw_content: str = ""


@dataclass
class CodeChunk:
    """A semantic chunk of code for indexing."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    content: str = ""
    filepath: str = ""
    language: Language = Language.UNKNOWN
    chunk_type: ChunkType = ChunkType.FILE
    parent_id: Optional[str] = None
    name: str = ""
    signature: Optional[str] = None
    docstring: Optional[str] = None
    dependencies: List[str] = field(default_factory=list)
    line_range: Tuple[int, int] = (0, 0)
    last_modified: float = 0.0

    def to_dict(self) -> dict:
        """Convert to dictionary for storage."""
        return {
            'id': self.id,
            'content': self.content,
            'filepath': self.filepath,
            'language': self.language.value,
            'chunk_type': self.chunk_type.value,
            'parent_id': self.parent_id,
            'name': self.name,
            'signature': self.signature,
            'docstring': self.docstring,
            'dependencies': self.dependencies,
            'line_range': self.line_range,
            'last_modified': self.last_modified,
        }


@dataclass
class SearchResult:
    """Result from code search."""
    chunk_id: str
    filepath: str
    name: str
    content: str
    similarity: float
    line_range: Tuple[int, int]
    language: Language
    chunk_type: ChunkType
    docstring: Optional[str] = None
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary for API response."""
        return {
            'chunk_id': self.chunk_id,
            'filepath': self.filepath,
            'name': self.name,
            'content': self.content,
            'similarity': self.similarity,
            'line_range': self.line_range,
            'language': self.language.value,
            'chunk_type': self.chunk_type.value,
            'docstring': self.docstring,
            'metadata': self.metadata,
        }
