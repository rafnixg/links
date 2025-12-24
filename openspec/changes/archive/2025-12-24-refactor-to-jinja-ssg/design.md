# Design: Custom Jinja-Based SSG Architecture

## Overview
The new architecture replaces the Reflex full-stack web framework with a custom Static Site Generator that uses Jinja2 for templating. The SSG will process data sources (e.g., link configurations) and generate static HTML/CSS/JS files.

## Key Components

### 1. Data Layer
- **Source**: Python data structures or configuration files (e.g., JSON, YAML) containing link information, bio data, and site configuration.
- **Processing**: Python scripts to load and validate data.

### 2. Template Engine
- **Technology**: Jinja2 templating engine.
- **Templates**: HTML templates with Jinja syntax for dynamic content insertion.
- **Assets**: Static CSS, JS, images copied to output directory.

### 3. Build System
- **Script**: Custom Python script (`build.py`) that orchestrates the generation process.
- **Steps**:
  1. Load data from sources.
  2. Render templates with data.
  3. Copy static assets.
  4. Generate output files in `public/` directory.

### 4. Output Structure
- Maintain similar structure to current `public/` folder.
- Static HTML files for each page.
- CSS and JS assets.

## Trade-offs

### Advantages
- **Performance**: No runtime overhead, fast loading.
- **Security**: No server-side vulnerabilities.
- **Scalability**: Easy to host and cache.
- **Version Control**: Entire site in git.

### Disadvantages
- **Dynamic Features**: Loss of any dynamic functionality (if any existed).
- **Build Time**: Must rebuild entire site for changes.
- **Complexity**: Custom build system requires maintenance.

## Data Flow
1. Configuration files (links, bio) → Python data structures
2. Data + Jinja templates → Rendered HTML
3. Static assets → Copied to output
4. Output directory → Ready for deployment

## Migration Strategy
- Extract data from current Reflex components.
- Convert Reflex templates to Jinja templates.
- Implement build script to replicate current functionality.
- Test generated output matches current behavior.

## Dependencies
- Jinja2: Templating
- Python standard library: File operations, data processing
- Optional: Markdown processing, CSS preprocessing if needed