# Project Context

## Purpose
LinkBioSite is a modern, brutalist-designed static site generator for creating beautiful link bio pages. It provides a clean, mobile-friendly interface for visitors to access various online presences and content, featuring 2026 design trends with cosmic midnight color palettes and experimental layouts.

## Tech Stack
- **Language**: Python 3.8+
- **Framework**: Jinja2 templating engine
- **Packaging**: Modern Python packaging with pyproject.toml
- **Containerization**: Docker with multi-stage builds
- **Testing**: pytest with comprehensive test coverage
- **Code Quality**: Black formatting, isort, flake8, mypy

## Project Conventions

### Code Style
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Use type hints where appropriate
- Keep line lengths under 88 characters (Black formatter default)
- Use kebab-case for file names, PascalCase for classes

### Architecture Patterns
- **Library Structure**: Code organized in `src/linkbiosite/` package
- **API Design**: Clean public API with `linkbiosite.build()`, `linkbiosite.init()`, `linkbiosite.serve()`
- **CLI Interface**: Command-line interface accessible via `linkbiosite` command
- **Template System**: Jinja2 templates in `src/linkbiosite/templates/`
- **Asset Management**: Static assets in `src/linkbiosite/assets/`

### Testing Strategy
- Unit tests for core functionality and utilities
- Integration tests for build process and CLI commands
- Test coverage reporting with pytest-cov
- Validate package installation and imports
- Manual testing for generated site functionality

### Git Workflow
- Use feature branches for new work
- Squash commits for clean history
- Use descriptive commit messages
- Tag releases for deployment
- OpenSpec for change management and specifications

## Domain Context
LinkBioSite is a static site generator for creating personal link bio pages. The domain involves:
- Social media link aggregation and display
- Personal project showcase and navigation
- Content discovery facilitation
- Mobile-first responsive design
- SEO optimization for discoverability
- Modern web design trends implementation

## Important Constraints
- Must be fully responsive and mobile-friendly
- SEO optimized with proper meta tags and structured data
- Dark theme with cosmic midnight color palette
- Fast loading times through static site generation
- Docker containerization for consistent deployment
- Brutalist design elements with 2026 trends
- Accessibility compliance with reduced motion support

## External Dependencies
- **GitHub**: For repository hosting and CI/CD
- **Docker Hub**: For container image distribution
- **PyPI**: For package distribution
- **Jinja2**: For template rendering
- **pytest**: For testing framework
