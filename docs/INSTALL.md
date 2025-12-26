# Installation Guide

## From PyPI (Recommended)

```bash
pip install linkbio
```

## From Source

```bash
git clone https://github.com/rafnixg/linkbio.git
cd linkbio
pip install -e .
```

## Development Installation

```bash
git clone https://github.com/rafnixg/linkbio.git
cd linkbio
pip install -e ".[dev]"
```

## Docker Installation

```bash
# Development
docker build --target runtime -t linkbio:dev .

# Production
docker build --target production -t linkbio:prod .
```

## System Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

## Dependencies

- Jinja2 >= 3.0.0

## Optional Dependencies

- pytest >= 7.0.0 (for testing)
- black, isort, flake8, mypy (for development)
- sphinx (for documentation)