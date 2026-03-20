# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-26

### Added
- **Library Structure**: Refactored from flat script to proper Python library with `src/linkbiosite/` package
- **CLI Interface**: Added command-line interface with `linkbiosite build`, `linkbiosite init`, and `linkbiosite serve` commands
- **Modern Packaging**: Implemented `pyproject.toml` with proper dependency management
- **Docker Optimization**: Multi-stage builds and volume mounting support
- **Type Hints**: Added comprehensive type annotations throughout the codebase
- **Fallback Templates**: Automatic fallback to package templates when project templates missing

### Changed
- **Project Structure**: Moved from `build.py` script to `src/linkbiosite/core.py` library module
- **Import System**: Updated to use proper Python package imports
- **Build Process**: Enhanced with better error handling and validation
- **Templates**: Moved to `src/linkbiosite/templates/` within package
- **Assets**: Relocated to `src/linkbiosite/assets/` for proper packaging
- **Project Rename**: Renamed from "linkbio" to "linkbiosite" for better clarity and discoverability

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

## [3.1.0] - 2026-03-19

### Changed
- **Version bump**: Synchronised package metadata across `pyproject.toml`, `setup.py`, and `src/linkbiosite/__init__.py` to `3.1.0`.
- **CI / CD**: Added GitHub Actions workflows for building the static site and for publishing to PyPI on release.

### Added
- `.github/workflows/build-static.yml` — workflow to build the site and update `public/` from CI.
- `.github/workflows/publish-pypi-on-release.yml` — workflow to publish a PyPI release when a GitHub Release is created.
- `openspec/changes/add-github-ci-workflows/*` — design/proposal/specs and tasks describing the new CI workflows.

### Documentation
- Updated `README.md` and other documentation to reference the new workflows and packaging improvements.

### Technical
- Bumped project version to `3.1.0` (no functional code changes beyond packaging/metadata updates).
