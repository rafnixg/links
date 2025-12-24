# Links Bio Rafnix Guzmán

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Jinja2](https://img.shields.io/badge/Jinja2-3.1.2-orange.svg)](https://jinja.palletsprojects.com/)
[![GitHub stars](https://img.shields.io/github/stars/rafnixg/links.svg?style=social&label=Star)](https://github.com/rafnixg/links)
[![GitHub forks](https://img.shields.io/github/forks/rafnixg/links.svg?style=social&label=Fork)](https://github.com/rafnixg/links/fork)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/rafnixg/links)

A modern and responsive personal bio links page built with a custom Static Site Generator using Jinja2 templating. This project serves as a centralized hub for all social media profiles, projects, and articles.

## ✨ Features

- 🎨 **2026 Brutalist Design**: Raw edges, asymmetrical layouts, and bold typography with cosmic midnight color palette by sections
- 🌙 Dark theme interface with high contrast
- 🚀 Built with Python and Jinja2 templating
- 📱 Mobile-friendly responsive layout with experimental positioning
- 🐳 Static site generation for fast hosting
- 📊 Analytics integration with Umami
- 🔍 SEO optimized with meta tags
- ✨ **Motion Design**: Subtle animations, floating elements, and interactive hovers
- ♿ **Accessibility**: Reduced motion support and GPU-accelerated animations

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rafnixg/links.git
cd links
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

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
