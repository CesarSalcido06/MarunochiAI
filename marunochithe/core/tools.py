"""Basic tools for file operations, git, and terminal execution."""

import asyncio
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
from loguru import logger
import git


class ToolRegistry:
    """Registry of available tools for the agent."""

    @staticmethod
    async def read_file(filepath: str) -> Dict[str, str]:
        """
        Read file contents.

        Args:
            filepath: Path to file

        Returns:
            Dict with content and metadata
        """
        try:
            path = Path(filepath).expanduser().resolve()

            if not path.exists():
                return {"error": f"File not found: {filepath}", "content": ""}

            if not path.is_file():
                return {"error": f"Not a file: {filepath}", "content": ""}

            content = path.read_text(encoding="utf-8")

            return {
                "filepath": str(path),
                "content": content,
                "lines": len(content.splitlines()),
                "size": len(content),
            }

        except Exception as e:
            logger.error(f"Failed to read {filepath}: {e}")
            return {"error": str(e), "content": ""}

    @staticmethod
    async def write_file(filepath: str, content: str, create_dirs: bool = True) -> Dict[str, str]:
        """
        Write content to file.

        Args:
            filepath: Path to file
            content: Content to write
            create_dirs: Create parent directories if needed

        Returns:
            Dict with status
        """
        try:
            path = Path(filepath).expanduser().resolve()

            if create_dirs:
                path.parent.mkdir(parents=True, exist_ok=True)

            path.write_text(content, encoding="utf-8")

            return {
                "filepath": str(path),
                "status": "success",
                "bytes_written": len(content.encode("utf-8")),
            }

        except Exception as e:
            logger.error(f"Failed to write {filepath}: {e}")
            return {"error": str(e), "status": "failed"}

    @staticmethod
    async def run_command(
        command: str,
        cwd: Optional[str] = None,
        timeout: int = 30
    ) -> Dict[str, str]:
        """
        Execute shell command.

        Args:
            command: Command to execute
            cwd: Working directory
            timeout: Timeout in seconds

        Returns:
            Dict with stdout, stderr, return_code
        """
        try:
            logger.info(f"Executing: {command}")

            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=cwd
            )

            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=timeout
            )

            return {
                "stdout": stdout.decode("utf-8"),
                "stderr": stderr.decode("utf-8"),
                "return_code": process.returncode,
                "command": command,
            }

        except asyncio.TimeoutError:
            logger.error(f"Command timed out: {command}")
            return {
                "error": f"Command timed out after {timeout}s",
                "return_code": -1,
            }
        except Exception as e:
            logger.error(f"Command failed: {e}")
            return {"error": str(e), "return_code": -1}

    @staticmethod
    async def git_status(repo_path: str = ".") -> Dict[str, any]:
        """
        Get git repository status.

        Args:
            repo_path: Path to repository

        Returns:
            Dict with git status information
        """
        try:
            repo = git.Repo(repo_path)

            modified = [item.a_path for item in repo.index.diff(None)]
            staged = [item.a_path for item in repo.index.diff("HEAD")]
            untracked = repo.untracked_files

            return {
                "branch": repo.active_branch.name,
                "modified": modified,
                "staged": staged,
                "untracked": untracked,
                "is_dirty": repo.is_dirty(),
                "head_commit": str(repo.head.commit)[:8],
            }

        except git.exc.InvalidGitRepositoryError:
            return {"error": "Not a git repository"}
        except Exception as e:
            logger.error(f"Git status failed: {e}")
            return {"error": str(e)}

    @staticmethod
    async def git_commit(
        message: str,
        repo_path: str = ".",
        add_all: bool = False
    ) -> Dict[str, str]:
        """
        Create git commit.

        Args:
            message: Commit message
            repo_path: Path to repository
            add_all: Stage all changes before committing

        Returns:
            Dict with commit info
        """
        try:
            repo = git.Repo(repo_path)

            if add_all:
                repo.git.add(A=True)

            commit = repo.index.commit(message)

            return {
                "commit_hash": str(commit)[:8],
                "message": message,
                "files_changed": len(commit.stats.files),
                "status": "success",
            }

        except Exception as e:
            logger.error(f"Git commit failed: {e}")
            return {"error": str(e), "status": "failed"}

    @staticmethod
    async def list_directory(dirpath: str, pattern: str = "*") -> Dict[str, List[str]]:
        """
        List files in directory.

        Args:
            dirpath: Directory path
            pattern: Glob pattern (default: all files)

        Returns:
            Dict with files and directories
        """
        try:
            path = Path(dirpath).expanduser().resolve()

            if not path.exists():
                return {"error": f"Directory not found: {dirpath}"}

            if not path.is_dir():
                return {"error": f"Not a directory: {dirpath}"}

            files = []
            directories = []

            for item in path.glob(pattern):
                if item.is_file():
                    files.append(str(item.relative_to(path)))
                elif item.is_dir():
                    directories.append(str(item.relative_to(path)))

            return {
                "path": str(path),
                "files": sorted(files),
                "directories": sorted(directories),
                "total": len(files) + len(directories),
            }

        except Exception as e:
            logger.error(f"List directory failed: {e}")
            return {"error": str(e)}
