# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-26

### Added
- **Library Structure**: Refactored from flat script to proper Python library with `src/linkbio/` package
- **CLI Interface**: Added command-line interface with `linkbio build`, `linkbio init`, and `linkbio serve` commands
- **Modern Packaging**: Implemented `pyproject.toml` with proper dependency management
- **Docker Optimization**: Multi-stage builds and volume mounting support
- **Type Hints**: Added comprehensive type annotations throughout the codebase
- **Fallback Templates**: Automatic fallback to package templates when project templates missing

### Changed
- **Project Structure**: Moved from `build.py` script to `src/linkbio/core.py` library module
- **Import System**: Updated to use proper Python package imports
- **Build Process**: Enhanced with better error handling and validation
- **Templates**: Moved to `src/linkbio/templates/` within package
- **Assets**: Relocated to `src/linkbio/assets/` for proper packaging

### Removed
- **Legacy Scripts**: Removed standalone `build.py` and `data_loader.py` scripts
- **Unused Files**: Cleaned up redundant configuration and temporary files

### Fixed
- **Import Issues**: Resolved RuntimeWarning in CLI by removing premature imports
- **PATH Issues**: Improved installation instructions for user vs system installs
- **Template Resolution**: Fixed fallback logic for missing project templates

### Technical
- **Python 3.8+**: Minimum version requirement
- **Jinja2**: Template engine for HTML generation
- **pytest**: Testing framework with 14 passing tests
- **Black**: Code formatting for PEP8 compliance
- **Docker**: Containerized deployment with nginx