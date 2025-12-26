"""
Tests for LinkBio core functionality.
"""

import json
import tempfile
from pathlib import Path
import pytest
from linkbio.core import LinkBioGenerator
from linkbio.data import load_data, validate_data, save_data


class TestLinkBioGenerator:
    """Test the LinkBioGenerator class."""

    def test_init_default(self):
        """Test generator initialization with default values."""
        generator = LinkBioGenerator()
        assert generator.project_root == Path.cwd()
        # Templates dir falls back to package if project doesn't have it
        expected_templates = Path.cwd() / 'templates'
        if not expected_templates.exists():
            expected_templates = Path(__file__).parent.parent / 'src' / 'linkbio' / 'templates'
        assert generator.templates_dir == expected_templates
        assert generator.assets_dir == Path.cwd() / 'assets'
        assert generator.data_file == Path.cwd() / 'data.json'

    def test_init_custom_root(self):
        """Test generator initialization with custom project root."""
        custom_root = Path("/tmp/test")
        generator = LinkBioGenerator(custom_root)
        assert generator.project_root == custom_root
        # Templates dir falls back to package if project doesn't have it
        expected_templates = custom_root / 'templates'
        if not expected_templates.exists():
            expected_templates = Path(__file__).parent.parent / 'src' / 'linkbio' / 'templates'
        assert generator.templates_dir == expected_templates
        assert generator.assets_dir == custom_root / 'assets'
        assert generator.data_file == custom_root / 'data.json'

    def test_load_data_missing_file(self):
        """Test loading data when file doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = LinkBioGenerator(Path(tmpdir))
            with pytest.raises(FileNotFoundError):
                generator.load_data()

    def test_load_data_valid(self):
        """Test loading valid data."""
        sample_data = {
            "bio": {"name": "Test", "greeting": "Hi", "subtitle": "Test", "handle": "@test", "avatar": "/test.png", "avatar_alt": "T"},
            "links": {"Test": [{"text": "Test", "tag": "test", "url": "https://test.com"}]},
            "footer": {"copyright": "© {year} Test"},
            "analytics": {},
            "meta": {"title": "Test", "description": "Test"}
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            data_file = tmpdir / 'data.json'

            with open(data_file, 'w') as f:
                json.dump(sample_data, f)

            generator = LinkBioGenerator(tmpdir)
            data = generator.load_data()

            assert data['bio']['name'] == 'Test'
            assert '{year}' not in data['footer']['copyright']  # Year should be replaced

    def test_validate_data_valid(self):
        """Test validating correct data structure."""
        valid_data = {
            "bio": {"name": "Test", "greeting": "Hi", "subtitle": "Test", "handle": "@test", "avatar": "/test.png", "avatar_alt": "T"},
            "links": {"Test": []},
            "footer": {},
            "analytics": {},
            "meta": {}
        }

        generator = LinkBioGenerator()
        assert generator.validate_data(valid_data) is True

    def test_validate_data_missing_key(self):
        """Test validating data with missing required key."""
        invalid_data = {
            "bio": {"name": "Test", "greeting": "Hi", "subtitle": "Test", "handle": "@test", "avatar": "/test.png", "avatar_alt": "T"},
            "links": {"Test": []},
            # Missing footer, analytics, meta
        }

        generator = LinkBioGenerator()
        with pytest.raises(ValueError, match="Missing required key"):
            generator.validate_data(invalid_data)

    def test_validate_data_missing_bio_field(self):
        """Test validating data with missing bio field."""
        invalid_data = {
            "bio": {"name": "Test"},  # Missing required bio fields
            "links": {"Test": []},
            "footer": {},
            "analytics": {},
            "meta": {}
        }

        generator = LinkBioGenerator()
        with pytest.raises(ValueError, match="Missing bio key"):
            generator.validate_data(invalid_data)


class TestDataFunctions:
    """Test data loading, validation, and saving functions."""

    def test_load_data_from_file(self):
        """Test loading data from a specific file."""
        sample_data = {
            "bio": {"name": "Test", "greeting": "Hi", "subtitle": "Test", "handle": "@test", "avatar": "/test.png", "avatar_alt": "T"},
            "links": {"Test": []},
            "footer": {"copyright": "© {year} Test"},
            "analytics": {},
            "meta": {"title": "Test", "description": "Test"}
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            data_file = tmpdir / 'test.json'

            with open(data_file, 'w') as f:
                json.dump(sample_data, f)

            data = load_data(data_file)
            assert data['bio']['name'] == 'Test'
            assert '2025' in data['footer']['copyright']  # Year should be replaced

    def test_save_data(self):
        """Test saving data to file."""
        sample_data = {
            "bio": {"name": "Test", "greeting": "Hi", "subtitle": "Test", "handle": "@test", "avatar": "/test.png", "avatar_alt": "T"},
            "links": {"Test": []},
            "footer": {},
            "analytics": {},
            "meta": {}
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            data_file = tmpdir / 'test.json'

            save_data(sample_data, data_file)

            # Verify file was created and contains correct data
            assert data_file.exists()
            with open(data_file, 'r') as f:
                loaded_data = json.load(f)
            assert loaded_data['bio']['name'] == 'Test'

    def test_validate_data_function(self):
        """Test the standalone validate_data function."""
        valid_data = {
            "bio": {"name": "Test", "greeting": "Hi", "subtitle": "Test", "handle": "@test", "avatar": "/test.png", "avatar_alt": "T"},
            "links": {"Test": []},
            "footer": {},
            "analytics": {},
            "meta": {}
        }

        assert validate_data(valid_data) is True

        invalid_data = {"invalid": "data"}
        with pytest.raises(ValueError):
            validate_data(invalid_data)