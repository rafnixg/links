"""
Tests for LinkBio CLI functionality.
"""

import subprocess
import sys
from pathlib import Path
import pytest
import tempfile


class TestCLI:
    """Test the LinkBio CLI commands."""

    def test_cli_help(self):
        """Test that CLI help works."""
        result = subprocess.run(
            [sys.executable, "-m", "linkbio.cli", "--help"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )

        assert result.returncode == 0
        assert "LinkBio" in result.stdout
        assert "Available commands" in result.stdout

    def test_cli_init(self):
        """Test CLI init command."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = subprocess.run(
                [sys.executable, "-m", "linkbio.cli", "init", tmpdir],
                capture_output=True,
                text=True,
            )

            assert result.returncode == 0
            assert "New Link Bio project initialized" in result.stdout

            # Check that files were created
            tmpdir_path = Path(tmpdir)
            assert (tmpdir_path / "data.json").exists()
            assert (tmpdir_path / "templates").exists()
            assert (tmpdir_path / "assets").exists()
            assert (tmpdir_path / "templates" / "index.html").exists()
            assert (tmpdir_path / "templates" / "styles.css").exists()

    def test_cli_build(self):
        """Test CLI build command."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)

            # First init a project
            result_init = subprocess.run(
                [sys.executable, "-m", "linkbio.cli", "init", str(tmpdir_path)],
                capture_output=True,
                text=True,
            )

            assert result_init.returncode == 0

            # Then build it
            result_build = subprocess.run(
                [sys.executable, "-m", "linkbio.cli", "build"],
                capture_output=True,
                text=True,
                cwd=tmpdir_path,
            )

            assert result_build.returncode == 0
            assert "Site built successfully" in result_build.stdout

            # Check that public directory was created
            assert (tmpdir_path / "public").exists()
            assert (tmpdir_path / "public" / "index.html").exists()
            assert (tmpdir_path / "public" / "styles.css").exists()

    def test_cli_init_existing_directory(self):
        """Test CLI init in existing non-empty directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)

            # Create a file to make directory non-empty
            (tmpdir_path / "existing.txt").write_text("existing")

            result = subprocess.run(
                [sys.executable, "-m", "linkbio.cli", "init", str(tmpdir_path)],
                capture_output=True,
                text=True,
            )

            assert result.returncode == 1
            assert "is not empty" in result.stderr
