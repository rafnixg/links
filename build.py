#!/usr/bin/env python3
"""
Static Site Generator for Link Bio
"""

import os
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from data_loader import load_data, validate_data

def setup_jinja():
    """Setup Jinja environment"""
    template_dir = Path(__file__).parent / 'src' / 'linkbio' / 'templates'
    env = Environment(loader=FileSystemLoader(template_dir))
    return env

def render_template(env, template_name, data, output_path):
    """Render a template with data to output path"""
    template = env.get_template(template_name)
    rendered = template.render(**data)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered)

def copy_assets(source_dir, dest_dir):
    """Copy static assets to output directory"""
    if source_dir.exists():
        shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True)

def copy_static_files(project_root, output_dir):
    """Copy static files like CSS"""
    # Copy styles.css
    styles_src = project_root / 'src' / 'linkbio' / 'templates' / 'styles.css'
    styles_dest = output_dir / 'styles.css'
    if styles_src.exists():
        shutil.copy2(styles_src, styles_dest)

def build_site():
    """Build the static site"""
    # Setup
    project_root = Path(__file__).parent
    output_dir = project_root / 'public'
    assets_dir = project_root / 'assets'
    
    # Clean output
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir()
    
    # Load and validate data
    data = load_data()
    validate_data(data)
    
    # Setup Jinja
    env = setup_jinja()
    
    # Render main page
    render_template(env, 'index.html', data, output_dir / 'index.html')
    
    # Copy assets
    copy_assets(assets_dir, output_dir / 'assets')
    
    # Copy static files
    copy_static_files(project_root, output_dir)
    
    # Copy existing public assets if any (for CSS/JS)
    existing_public = project_root / 'public_export'
    if existing_public.exists():
        copy_assets(existing_public / 'assets', output_dir / 'assets')
    
    print(f"Site built successfully in {output_dir}")

if __name__ == "__main__":
    build_site()