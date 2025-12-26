"""
LinkBio - Static Site Generator for Link Bio Pages

A modern, brutalist-designed static site generator for creating beautiful link bio pages.
Built with Python and Jinja2 templates.

Example:
    >>> from linkbio import build
    >>> build()  # Build site in current directory
    'public'
"""

from .core import LinkBioGenerator, build, init, serve
from .data import load_data, validate_data, save_data
from .cli import main as cli_main

__version__ = "0.1.0"
__author__ = "Rafnix Guzmán"
__email__ = "rafnixg@gmail.com"

__all__ = [
    "LinkBioGenerator",
    "build",
    "init",
    "serve",
    "load_data",
    "validate_data",
    "save_data",
    "cli_main",
]