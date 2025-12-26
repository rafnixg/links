"""
LinkBioSite Static Site Generator Core Module

This module provides the core functionality for generating static link bio sites.
"""

import json
import os
import shutil
import http.server
import socketserver
from datetime import date
from pathlib import Path
from typing import Dict, Any, Optional
from jinja2 import Environment, FileSystemLoader

from .data import save_data


class LinkBioSiteGenerator:
    """Main class for generating Link Bio static sites."""

    def __init__(self, project_root: Optional[Path] = None):
        """
        Initialize the Link Bio generator.

        Args:
            project_root: Root directory of the project. Defaults to current directory.
        """
        self.project_root = project_root or Path.cwd()
        self.templates_dir = self.project_root / "templates"
        if not self.templates_dir.exists():
            self.templates_dir = Path(__file__).parent / "templates"
        self.assets_dir = self.project_root / "assets"
        self.data_file = self.project_root / "data.json"

    def load_data(self) -> Dict[str, Any]:
        """
        Load site data from data.json file.

        Returns:
            Dictionary containing site configuration and data.

        Raises:
            FileNotFoundError: If data.json is not found.
            json.JSONDecodeError: If data.json contains invalid JSON.
        """
        if not self.data_file.exists():
            raise FileNotFoundError(f"Data file not found: {self.data_file}")

        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Add dynamic data
        if "footer" in data and "copyright" in data["footer"]:
            data["footer"]["copyright"] = data["footer"]["copyright"].format(
                year=date.today().year
            )

        return data

    def validate_data(self, data: Dict[str, Any]) -> bool:
        """
        Validate the structure of loaded data.

        Args:
            data: Data dictionary to validate.

        Returns:
            True if validation passes.

        Raises:
            ValueError: If required keys are missing or data structure is invalid.
        """
        required_keys = ["bio", "links", "footer", "analytics", "meta"]
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing required key: {key}")

        # Check bio section
        bio_required = [
            "name",
            "greeting",
            "subtitle",
            "handle",
            "avatar",
            "avatar_alt",
        ]
        for key in bio_required:
            if key not in data["bio"]:
                raise ValueError(f"Missing bio key: {key}")

        return True

    def setup_jinja(self) -> Environment:
        """
        Setup Jinja2 environment for template rendering.

        Returns:
            Configured Jinja2 Environment instance.

        Raises:
            FileNotFoundError: If templates directory doesn't exist.
        """
        if not self.templates_dir.exists():
            raise FileNotFoundError(
                f"Templates directory not found: {self.templates_dir}"
            )

        env = Environment(loader=FileSystemLoader(self.templates_dir))
        return env

    def render_template(
        self,
        env: Environment,
        template_name: str,
        data: Dict[str, Any],
        output_path: Path,
    ) -> None:
        """
        Render a template with data to specified output path.

        Args:
            env: Jinja2 environment instance.
            template_name: Name of the template file.
            data: Data dictionary for template rendering.
            output_path: Path where rendered content should be saved.
        """
        template = env.get_template(template_name)
        rendered = template.render(**data)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered)

    def copy_assets(self, source_dir: Path, dest_dir: Path) -> None:
        """
        Copy static assets from source to destination directory.

        Args:
            source_dir: Source directory containing assets.
            dest_dir: Destination directory for assets.
        """
        if source_dir.exists():
            shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True)

    def copy_static_files(self, output_dir: Path) -> None:
        """
        Copy static files like CSS to output directory.

        Args:
            output_dir: Output directory for static files.
        """
        # Copy styles.css
        styles_src = self.templates_dir / "styles.css"
        styles_dest = output_dir / "styles.css"
        if styles_src.exists():
            shutil.copy2(styles_src, styles_dest)

    def build_site(self, output_dir: Optional[Path] = None) -> Path:
        """
        Build the complete static site.

        Args:
            output_dir: Output directory for built site. Defaults to 'public'.

        Returns:
            Path to the built site directory.

        Raises:
            Exception: If build process fails.
        """
        output_dir = output_dir or self.project_root / "public"

        try:
            # Clean output directory
            if output_dir.exists():
                shutil.rmtree(output_dir)
            output_dir.mkdir(parents=True)

            # Load and validate data
            data = self.load_data()
            self.validate_data(data)

            # Setup Jinja environment
            env = self.setup_jinja()

            # Render main page
            self.render_template(env, "index.html", data, output_dir / "index.html")

            # Copy assets
            self.copy_assets(self.assets_dir, output_dir / "assets")

            # Copy static files
            self.copy_static_files(output_dir)

            # Copy existing public assets if any (for CSS/JS)
            existing_public = self.project_root / "public_export"
            if existing_public.exists():
                self.copy_assets(existing_public / "assets", output_dir / "assets")

            print(f"Site built successfully in {output_dir}")
            return output_dir

        except Exception as e:
            raise Exception(f"Build failed: {str(e)}") from e


def build(project_root: Optional[str] = None, output_dir: Optional[str] = None) -> str:
    """
    Convenience function to build a Link Bio site.

    Args:
        project_root: Root directory of the project. Defaults to current directory.
        output_dir: Output directory for built site. Defaults to 'public'.

    Returns:
        Path to the built site directory as string.
    """
    root_path = Path(project_root) if project_root else None
    output_path = Path(output_dir) if output_dir else None

    generator = LinkBioSiteGenerator(root_path)
    result_path = generator.build_site(output_path)

    return str(result_path)


def init(project_dir: str = ".", template: str = "full") -> str:
    """
    Initialize a new Link Bio Site project in the specified directory.

    Args:
        project_dir: Directory to initialize the project in.
        template: Template to use ('minimal' or 'full').

    Returns:
        Path to the initialized project directory.

    Raises:
        ValueError: If directory is not empty or template is invalid.
    """
    target_dir = Path(project_dir)

    if target_dir.exists() and list(target_dir.iterdir()):
        raise ValueError(f"Directory {target_dir} is not empty")

    target_dir.mkdir(parents=True, exist_ok=True)

    # Create basic directory structure
    (target_dir / "templates").mkdir(exist_ok=True)
    (target_dir / "assets").mkdir(exist_ok=True)

    # Create sample data.json
    sample_data = {
        "bio": {
            "name": "Your Name",
            "greeting": "Hi, I'm Your Name",
            "subtitle": "Your subtitle here",
            "handle": "@yourhandle",
            "avatar": "/avatar.png",
            "avatar_alt": "YN",
        },
        "links": {
            "Social": [
                {"text": "Website", "tag": "globe", "url": "https://example.com"}
            ]
        },
        "footer": {"copyright": "© {year} Your Name. All rights reserved."},
        "analytics": {},
        "meta": {"title": "Link Bio", "description": "My personal link bio"},
    }

    save_data(sample_data, target_dir / "data.json")

    # Create basic template
    template_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ meta.title }}</title>
    <meta name="description" content="{{ meta.description }}">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>{{ bio.greeting }}</h1>
        <p>{{ bio.subtitle }}</p>
    </header>

    <main>
        {% for category, links in links.items() %}
        <section>
            <h2>{{ category }}</h2>
            <ul>
                {% for link in links %}
                <li><a href="{{ link.url }}">{{ link.text }}</a></li>
                {% endfor %}
            </ul>
        </section>
        {% endfor %}
    </main>

    <footer>
        <p>{{ footer.copyright }}</p>
    </footer>
</body>
</html>"""

    with open(target_dir / "templates" / "index.html", "w") as f:
        f.write(template_content)

    # Create basic CSS
    css_content = """body {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

header {
    text-align: center;
    margin-bottom: 40px;
}

main section {
    margin-bottom: 30px;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

a {
    display: inline-block;
    padding: 10px 20px;
    background: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
}

a:hover {
    background: #0056b3;
}"""

    with open(target_dir / "templates" / "styles.css", "w") as f:
        f.write(css_content)

    return str(target_dir)


def serve(
    host: str = "localhost", port: int = 8000, output_dir: str = "public"
) -> None:
    """
    Serve the built site locally for development.

    Args:
        host: Host to bind to.
        port: Port to serve on.
        output_dir: Directory containing the built site.

    Raises:
        FileNotFoundError: If output directory doesn't exist.
    """
    output_path = Path(output_dir)
    if not output_path.exists():
        raise FileNotFoundError(
            f"Output directory {output_path} does not exist. Run build() first."
        )

    # Change to output directory for serving
    original_cwd = Path.cwd()
    os.chdir(output_path)

    try:

        class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                # Suppress log messages
                pass

        with socketserver.TCPServer((host, port), QuietHTTPRequestHandler) as httpd:
            print(f"Serving site at http://{host}:{port}")
            print("Press Ctrl+C to stop")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped")
    finally:
        os.chdir(original_cwd)
