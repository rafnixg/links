# Links Bio Rafnix Guzmán

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Reflex](https://img.shields.io/badge/Reflex-0.4.8-purple.svg)](https://reflex.dev/)
[![GitHub stars](https://img.shields.io/github/stars/rafnixg/links.svg?style=social&label=Star)](https://github.com/rafnixg/links)
[![GitHub forks](https://img.shields.io/github/forks/rafnixg/links.svg?style=social&label=Fork)](https://github.com/rafnixg/links/fork)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/rafnixg/links)

A modern and responsive personal bio links page built with [Reflex](https://reflex.dev/), a Python web framework. This project serves as a centralized hub for all social media profiles, projects, and articles.

## ✨ Features

- 🎨 Modern and responsive design
- 🌙 Dark theme interface
- 🚀 Built with Python and Reflex framework
- 📱 Mobile-friendly responsive layout
- 🐳 Docker support for easy deployment
- 📊 Analytics integration with Umami
- 🔍 SEO optimized with meta tags

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

- **Framework**: [Reflex 0.4.8](https://reflex.dev/) - Full-stack Python framework
- **Language**: Python 3.11+
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
