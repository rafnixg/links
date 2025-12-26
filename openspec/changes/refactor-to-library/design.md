# Design: Library Structure Refactoring

## Overview
This design outlines the transformation of the Link Bio SSG from a flat project structure to a proper Python library with organized source code, improved packaging, and enhanced deployment capabilities.

## Architectural Decisions

### 1. Package Structure
```
src/
├── linkbio/
│   ├── __init__.py          # Package initialization
│   ├── cli.py              # Command-line interface
│   ├── core.py             # Core SSG functionality
│   ├── templates/          # Jinja2 templates
│   ├── static/             # Static assets
│   ├── data/               # Data models and loaders
│   └── utils/              # Utility functions
├── tests/                  # Test suite
└── docs/                   # Documentation
```

### 2. Library API Design
- **Simple Interface**: `linkbio.build(site_data, output_dir)`
- **CLI Tool**: `linkbio` command for easy usage
- **Configurable**: Support for custom templates and themes
- **Extensible**: Plugin system for custom functionality

### 3. Docker Strategy
- **Multi-stage Build**: Separate build and runtime stages
- **Library Installation**: Install as package rather than copying files
- **Minimal Runtime**: Only include necessary runtime dependencies
- **Volume Mounting**: Support for external data and templates

## Technical Implementation

### Package Configuration
- **setup.py/setup.cfg**: Standard Python packaging
- **pyproject.toml**: Modern Python project configuration
- **MANIFEST.in**: Include templates and static files
- **requirements.txt**: Runtime dependencies

### CLI Interface
```bash
# Build site
linkbio build data.json output/

# Serve locally
linkbio serve output/

# Create new site
linkbio init my-site/
```

### Docker Optimization
```dockerfile
# Build stage
FROM python:3.11-slim as builder
COPY . /app
RUN pip install build && python -m build

# Runtime stage
FROM python:3.11-slim
COPY --from=builder /app/dist/*.whl /tmp/
RUN pip install /tmp/*.whl
```

## Trade-offs

### Advantages
- **Maintainability**: Clear separation of concerns
- **Reusability**: Can be used as a dependency in other projects
- **Distribution**: Easy installation via pip
- **Testing**: Better test organization and coverage
- **Documentation**: Clear API documentation

### Disadvantages
- **Complexity**: More files and configuration to manage
- **Learning Curve**: Users need to understand library usage
- **Migration**: Existing users need to adapt
- **Dependencies**: More careful dependency management

## Migration Strategy
1. **Phase 1**: Create new structure alongside existing code
2. **Phase 2**: Migrate functionality to library structure
3. **Phase 3**: Update build scripts and Docker
4. **Phase 4**: Update documentation and examples
5. **Phase 5**: Deprecate old structure with migration guide

## Compatibility
- **Backward Compatible**: Existing build.py continues to work
- **Gradual Migration**: Support both old and new structures
- **Clear Documentation**: Migration guides for users