"""
LinkBioSite Command Line Interface

Provides CLI commands for building, initializing, and serving Link Bio sites.
"""

import argparse
import sys
import http.server
import socketserver
from pathlib import Path
from typing import Optional
from urllib.parse import unquote

from .core import LinkBioSiteGenerator, build
from .data import load_data, save_data


def create_parser() -> argparse.ArgumentParser:
    """Create the main argument parser."""
    parser = argparse.ArgumentParser(
        description="LinkBioSite - Static Site Generator for Link Bio Pages", prog="linkbiosite"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Build command
    build_parser = subparsers.add_parser("build", help="Build the static site")
    build_parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="public",
        help="Output directory for built site (default: public)",
    )
    build_parser.add_argument(
        "--config", "-c", type=str, help="Path to data.json configuration file"
    )

    # Init command
    init_parser = subparsers.add_parser(
        "init", help="Initialize a new Link Bio Site project"
    )
    init_parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to initialize (default: current directory)",
    )
    init_parser.add_argument(
        "--template",
        choices=["minimal", "full"],
        default="full",
        help="Project template to use (default: full)",
    )

    # Serve command
    serve_parser = subparsers.add_parser(
        "serve", help="Serve the site locally for development"
    )
    serve_parser.add_argument(
        "--port", "-p", type=int, default=8000, help="Port to serve on (default: 8000)"
    )
    serve_parser.add_argument(
        "--host", default="localhost", help="Host to bind to (default: localhost)"
    )
    serve_parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="public",
        help="Directory containing built site (default: public)",
    )

    return parser


def handle_build(args: argparse.Namespace) -> int:
    """Handle the build command."""
    try:
        output_dir = build(output_dir=args.output)
        print(f"[SUCCESS] Site built successfully in {output_dir}")
        return 0
    except Exception as e:
        print(f"[ERROR] Build failed: {e}", file=sys.stderr)
        return 1


def handle_init(args: argparse.Namespace) -> int:
    """Handle the init command."""
    try:
        target_dir = Path(args.directory)

        if target_dir.exists() and list(target_dir.iterdir()):
            print(f"[ERROR] Directory {target_dir} is not empty", file=sys.stderr)
            return 1

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

        print(f"[SUCCESS] New Link Bio Site project initialized in {target_dir}")
        print("Next steps:")
        print("1. Edit data.json with your information")
        print("2. Customize templates/index.html and templates/styles.css")
        print("3. Add your avatar to assets/avatar.png")
        print("4. Run 'linkbio build' to generate your site")

        return 0

    except Exception as e:
        print(f"[ERROR] Init failed: {e}", file=sys.stderr)
        return 1


def handle_serve(args: argparse.Namespace) -> int:
    """Handle the serve command."""
    try:
        output_dir = Path(args.output)
        if not output_dir.exists():
            print(
                f"✗ Output directory {output_dir} does not exist. Run 'linkbio build' first.",
                file=sys.stderr,
            )
            return 1

        class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                # Suppress log messages
                pass

        with socketserver.TCPServer(
            (args.host, args.port), QuietHTTPRequestHandler
        ) as httpd:
            print(f"✓ Serving site at http://{args.host}:{args.port}")
            print("Press Ctrl+C to stop")
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n✓ Server stopped")
        return 0
    except Exception as e:
        print(f"✗ Serve failed: {e}", file=sys.stderr)
        return 1


def main() -> int:
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    commands = {
        "build": handle_build,
        "init": handle_init,
        "serve": handle_serve,
    }

    handler = commands.get(args.command)
    if handler:
        return handler(args)
    else:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
