# Tasks: Refactor to Library Structure

## Phase 1: Project Structure Setup
- [x] Create `src/linkbio/` package directory structure
- [x] Create `src/linkbio/__init__.py` with package initialization
- [x] Create `tests/` directory for test suite
- [x] Create `docs/` directory for documentation
- [x] Update `.gitignore` for new structure

## Phase 2: Code Migration
- [x] Move `build.py` logic to `src/linkbio/core.py`
- [x] Move `data_loader.py` to `src/linkbio/data.py`
- [x] Move `templates/` to `src/linkbio/templates/`
- [x] Move `assets/` to `src/linkbio/assets/`
- [x] Update `__init__.py` with proper API exports

## Phase 3: Library API Design
- [x] Define public API in `__init__.py`
- [x] Create `linkbio.build()` function
- [x] Create `linkbio.init()` for new projects
- [x] Create `linkbio.serve()` for local development
- [x] Add type hints and docstrings

## Phase 4: Packaging Configuration
- [x] Create `pyproject.toml` with modern packaging
- [x] Create `setup.py` for backward compatibility
- [x] Create `MANIFEST.in` for data files
- [x] Update `requirements.txt` with proper dependencies
- [x] Test package installation with `pip install -e .`

## Phase 5: Docker Updates
- [x] Update Dockerfile for multi-stage library build
- [x] Optimize Docker image size
- [x] Add support for volume mounting
- [x] Test Docker build and run
- [x] Update `.dockerignore` for new structure

## Phase 6: Documentation Updates
- [x] Update README.md with library usage instructions
- [x] Add installation guide for pip users
- [x] Create CLI usage examples
- [x] Add Docker deployment instructions
- [x] Create migration guide for existing users

## Phase 7: Testing and Validation
- [x] Create unit tests for core functionality
- [x] Test CLI commands work correctly
- [x] Validate Docker container builds and runs
- [x] Test backward compatibility with existing build.py
- [x] Run integration tests with sample data

## Phase 8: Final Polish
- [ ] Update project metadata and version
- [ ] Create changelog for the refactoring
- [ ] Update CI/CD configuration if needed
- [ ] Final documentation review
- [ ] Release preparation