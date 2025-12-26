# LinkBioSite

[![PyPI version](https://badge.fury.io/py/linkbiosite.svg)](https://pypi.org/project/linkbiosite/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/rafnixg/links.svg)](https://github.com/rafnixg/links/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/rafnixg/links.svg)](https://github.com/rafnixg/links/network)

A modern, brutalist-designed static site generator for creating beautiful link bio pages. Features 2026 design trends with cosmic midnight color palettes, experimental layouts, and smooth animations.

## ✨ Features

- 🎨 **Brutalist Design**: Cosmic midnight color palette with experimental layouts
- ✨ **Motion Design**: Scroll-triggered animations, hover effects, and micro-interactions
- 📝 **Dynamic Typography**: Text reveals, floating elements, and responsive animations
- 📱 **Mobile-First**: Optimized for all devices with clean, accessible interfaces
- ⚡ **Static Generation**: Fast, lightweight sites with no runtime dependencies
- 💻 **CLI Interface**: Easy-to-use command-line tools for development and deployment
- 🐳 **Docker Support**: Containerized builds for consistent deployment
- 🔒 **Type-Safe**: Full type hints and modern Python practices

## 🚀 Quick Start

### Installation

Install LinkBioSite from PyPI:

```bash
pip install linkbiosite
```

Or install from source:

```bash
git clone https://github.com/rafnixg/links.git
cd links
pip install -e .
```

### Create Your First Site

1. **Initialize a new project:**
   ```bash
   linkbiosite init
   ```

2. **Edit your data** in `data.json`:
   ```json
   {
     "name": "Your Name",
     "bio": "Your bio here",
     "links": [
       {"title": "Website", "url": "https://example.com"},
       {"title": "Twitter", "url": "https://twitter.com/username"}
     ]
   }
   ```

3. **Build your site:**
   ```bash
   linkbiosite build
   ```

4. **Serve locally:**
   ```bash
   linkbiosite serve
   ```

Your site will be available at `http://localhost:8000`

## 📖 Usage

### Command Line Interface

```bash
linkbiosite --help          # Show help
linkbiosite init            # Initialize new project
linkbiosite build           # Build static site
linkbiosite serve           # Serve locally for development
```

### Python API

```python
from linkbiosite import LinkBioSiteGenerator

# Create generator
generator = LinkBioSiteGenerator()

# Build site
generator.build_site()
```

## 🏗️ Project Structure

After running `linkbiosite init`, your project will look like:

```
your-project/
├── [`data.json`](data.json )          # Your profile data
├── templates/         # Custom templates (optional)
│   ├── base.html
│   ├── index.html
│   └── styles.css
└── public/            # Generated site (after build)
    ├── index.html
    └── styles.css
```

## 🎨 Customization

### Templates

LinkBioSite uses Jinja2 templates. Customize by modifying files in the `templates/` directory.

### Styling

Edit `templates/styles.css` to customize the brutalist design. The default theme features:
- Cosmic midnight color palette (#0a0a0a, #ffffff, #ff6b6b)
- Experimental typography with glow effects
- Smooth animations and transitions

### Data Format

Your `data.json` supports:

```json
{
  "name": "Your Name",
  "bio": "Short bio",
  "avatar": "path/to/avatar.jpg",
  "links": [
    {
      "title": "Link Title",
      "url": "https://example.com",
      "icon": "optional-icon-class"
    }
  ],
  "social": {
    "twitter": "@username",
    "github": "username"
  }
}
```

## 🐳 Docker

Build and run with Docker:

```bash
# Build image
docker build -t linkbiosite .

# Run container
docker run -p 8000:8000 linkbiosite
```

## 🧪 Development

### Setup Development Environment

```bash
git clone https://github.com/rafnixg/links.git
cd links
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Code Quality

```bash
black .          # Format code
isort .          # Sort imports
flake8 .         # Lint code
mypy .           # Type check
```

## 📚 Documentation

Full documentation is available at [https://linkbiosite.readthedocs.io/](https://linkbiosite.readthedocs.io/)

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Jinja2](https://jinja.palletsprojects.com/) templating
- Inspired by modern web design trends
- Community contributions and feedback

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/rafnixg/links/issues)
- **Discussions**: [GitHub Discussions](https://github.com/rafnixg/links/discussions)
- **Email**: rafnixg@gmail.com

---

**LinkBioSite** - Create stunning link bio pages with modern design ✨
