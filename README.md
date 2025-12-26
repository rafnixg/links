# LinkBioSite

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyPI Version](https://img.shields.io/pypi/v/linkbiosite.svg)](https://pypi.org/project/linkbiosite/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Jinja2](https://img.shields.io/badge/Jinja2-3.0+-orange.svg)](https://jinja.palletsprojects.com/)
[![GitHub stars](https://img.shields.io/github/stars/rafnixg/links.svg?style=social&label=Star)](https://github.com/rafnixg/links)
[![GitHub forks](https://img.shields.io/github/forks/rafnixg/links.svg?style=social&label=Fork)](https://github.com/rafnixg/links/fork)

A modern, brutalist-designed static site generator for creating beautiful link bio pages. Built with Python and Jinja2 templates, featuring 2026 design trends with cosmic midnight color palettes and experimental layouts.

## ✨ Features

- 🎨 **2026 Brutalist Design**: Raw edges, asymmetrical layouts, and bold typography
- 🌙 Cosmic midnight color palette with high contrast
- 🚀 Built with Python and Jinja2 templating
- 📱 Mobile-friendly responsive layout
- 🐳 Static site generation for fast hosting
- 📊 Analytics integration ready
- 🔍 SEO optimized with meta tags
- ✨ **Motion Design**: Subtle animations and interactive hovers
- ♿ **Accessibility**: Reduced motion support
- 🛠️ **Library API**: Use as a Python library or CLI tool
- 🐳 **Docker Support**: Multi-stage builds for development and production

## 🚀 Quick Start

### Installation

Install LinkBioSite using pip:

```bash
pip install linkbiosite
```

Or install from source for development:

```bash
git clone https://github.com/rafnixg/links.git
cd links
pip install -e .
```

### Create Your First Link Bio

1. Initialize a new project:
```bash
linkbiosite init my-bio
cd my-bio
```

2. Edit `data.json` with your information:
```json
{
  "bio": {
    "name": "Your Name",
    "greeting": "Hi, I'm Your Name",
    "subtitle": "Your awesome subtitle",
    "handle": "@yourhandle",
    "avatar": "/avatar.png",
    "avatar_alt": "YN"
  },
  "links": {
    "Social": [
      {"text": "Website", "tag": "globe", "url": "https://example.com"},
      {"text": "Twitter", "tag": "twitter", "url": "https://twitter.com/yourhandle"}
    ]
  }
}
```

3. Build your site:
```bash
linkbiosite build
```

4. Serve locally for development:
```bash
linkbiosite serve
```

Your link bio will be available at http://localhost:8000

## 💻 Usage

### Command Line Interface

LinkBioSite provides a comprehensive CLI for all operations:

```bash
# Initialize a new project
linkbiosite init [directory]

# Build the static site
linkbiosite build [--output OUTPUT_DIR]

# Serve locally for development
linkbiosite serve [--port PORT] [--host HOST]

# Show help
linkbiosite --help
```

### Python API

Use LinkBioSite as a Python library:

```python
from linkbiosite import build, init, serve

# Initialize a new project
init("my-bio-project")

# Build the site
output_dir = build()

# Serve for development
serve(port=8000)
```

### Advanced Usage

```python
from linkbiosite import LinkBioSiteGenerator

# Create a custom generator
generator = LinkBioSiteGenerator(project_root="/path/to/project")

# Build with custom output directory
output_path = generator.build_site(output_dir="/custom/output")

# Load and validate data
data = generator.load_data()
generator.validate_data(data)
```

## 🐳 Docker Usage

### Development

Build and run the development container:

```bash
# Build development image
docker build --target runtime -t linkbio:dev .

# Run with volume mounting
docker run -it --rm \
  -v $(pwd):/app/project \
  -v $(pwd)/public:/app/output \
  -p 8000:8000 \
  linkbiosite:dev \
  linkbiosite serve --host 0.0.0.0
```

### Production

Build and run the production container:

```bash
# Build production image
docker build --target production -t linkbiosite:prod .

# Run nginx server
docker run -d -p 80:80 linkbiosite:prod
```

## 📁 Project Structure

When you initialize a new LinkBioSite project, you'll get:

```
my-bio/
├── data.json          # Site configuration and content
├── templates/         # Jinja2 templates
│   ├── index.html     # Main page template
│   └── styles.css     # CSS styles
├── assets/            # Static assets (images, etc.)
└── public/            # Generated site (after build)
```

## 🛠️ Technologies

- **Language**: Python 3.8+
- **Templating**: Jinja2 3.0+
- **Styling**: CSS3 with brutalist design
- **Containerization**: Docker with multi-stage builds
- **Package Management**: Modern Python packaging (pyproject.toml)

## 📖 Configuration

### data.json Structure

```json
{
  "bio": {
    "name": "Your Name",
    "greeting": "Welcome message",
    "subtitle": "Your subtitle",
    "handle": "@yourhandle",
    "avatar": "/path/to/avatar.png",
    "avatar_alt": "Alt text for avatar"
  },
  "links": {
    "Category Name": [
      {
        "text": "Link Text",
        "tag": "icon-name",
        "url": "https://example.com"
      }
    ]
  },
  "footer": {
    "copyright": "© {year} Your Name. All rights reserved."
  },
  "analytics": {},
  "meta": {
    "title": "Page Title",
    "description": "Page description for SEO"
  }
}
```

### Custom Templates

LinkBio uses Jinja2 templates. Customize `templates/index.html` and `templates/styles.css` to match your design needs.

## 👤 Author

**Rafnix Guzmán**

- Website: [rafnixg.dev](https://rafnixg.dev)
- Twitter: [@rafnixg](https://twitter.com/rafnixg)
- GitHub: [@rafnixg](https://github.com/rafnixg)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Show your support

Give a ⭐️ if this project helped you!

## 📚 Documentation

For detailed documentation, visit [linkbio.readthedocs.io](https://linkbio.readthedocs.io) (coming soon).

## 🙏 Acknowledgments

- Inspired by 2026 design trends
- Built with modern Python packaging
- Thanks to the Jinja2 and Python communities```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Building the Site

To generate the static site:

```bash
python build.py
```

The generated site will be in the `public/` directory.

### Development Mode

Run the application in development mode with hot reload:
```bash
reflex run
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000

### Export Static Files

Export the public files to the `public` folder:
```bash
./public_export
```

### Production Mode

Run the application in production mode:
```bash
reflex run --env prod
```

## 🐳 Docker Deployment

Build and run the application using Docker:

```bash
# Build the Docker image
docker build -t reflex-links:latest .

# Run the container
docker run -d -p 8000:8000 -p 3000:3000 --name links reflex-links:latest
```

Access the application at http://localhost:3000

## 📁 Project Structure

```
links/
├── link_bio/           # Main application code
│   ├── components/     # Reusable UI components
│   ├── styles/         # CSS styles and theme
│   ├── views/          # Page views (header, footer, links)
│   └── link_bio.py     # Main application file
├── assets/             # Static assets (images, icons)
├── public/             # Public files
├── requirements.txt    # Python dependencies
├── rxconfig.py         # Reflex configuration
└── Dockerfile          # Docker configuration
```

## 🛠️ Technologies

- **Static Site Generator**: Custom Python/Jinja2 SSG
- **Language**: Python 3.11+
- **Templating**: Jinja2 3.1.2
- **Styling**: CSS3 with animations and brutalist design
- **Analytics**: Umami Analytics
- **Containerization**: Docker

## 👤 Author

**Rafnix Guzmán**

- Website: [links.rafnixg.dev](https://links.rafnixg.dev)
- Twitter: [@rafnixg](https://twitter.com/rafnixg)
- GitHub: [@rafnixg](https://github.com/rafnixg)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/rafnixg/links/issues).

## 📝 License

This project is open source and available for personal and commercial use.

## ⭐ Show your support

Give a ⭐️ if this project helped you!
