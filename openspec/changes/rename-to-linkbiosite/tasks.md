# Tasks: Rename to LinkBioSite

## Phase 1: Project Structure Rename
- [x] Rename `src/linkbio/` directory to `src/linkbiosite/`
- [x] Update all import statements in Python files
- [x] Update MANIFEST.in paths
- [x] Update setup.py package references
- [x] Update pyproject.toml package configuration

## Phase 2: Code Refactoring
- [x] Rename `LinkBioGenerator` class to `LinkBioSiteGenerator`
- [x] Update all class references and instantiations
- [x] Update module docstrings and comments
- [x] Update CLI command name and help text
- [x] Update entry points in pyproject.toml and setup.py

## Phase 3: Metadata Updates
- [x] Update package name in pyproject.toml and setup.py
- [x] Update project URLs and repository links
- [x] Update author and maintainer information
- [x] Update description and keywords
- [x] Update version and release information

## Phase 4: Documentation Updates
- [x] Update README.md with new package name and commands
- [x] Update CHANGELOG.md with rename information
- [x] Update all code examples and usage instructions
- [x] Update docstrings and inline documentation
- [x] Update test file names and content

## Phase 5: Testing and Validation
- [x] Update all test imports and references
- [x] Run full test suite to ensure functionality
- [x] Test CLI commands with new name
- [x] Test package installation with new name
- [x] Validate all imports work correctly

## Phase 6: Final Cleanup
- [x] Remove any remaining references to old name
- [x] Update .gitignore and other config files if needed
- [x] Test Docker build with new package name
- [x] Update CI/CD configuration if present
- [x] Final documentation review