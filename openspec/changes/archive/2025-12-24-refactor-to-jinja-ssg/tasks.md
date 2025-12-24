# Tasks: Refactor to Jinja-Based SSG

## Phase 1: Analysis and Planning
- [x] Extract current link data and configuration from Reflex components
- [x] Analyze existing templates and components for conversion to Jinja
- [x] Identify static assets (CSS, JS, images) to preserve
- [x] Document current site structure and pages

## Phase 2: Data Layer Implementation
- [x] Create data models for links, bio information, and site config
- [x] Implement data loading from configuration files (JSON/YAML)
- [x] Add data validation and error handling
- [x] Create sample data files for testing

## Phase 3: Template Conversion
- [x] Convert main page template from Reflex to Jinja
- [x] Convert component templates (header, footer, links, etc.) to Jinja partials
- [x] Implement responsive design in Jinja templates
- [x] Add template inheritance and includes for reusability

## Phase 4: Build System Development
- [x] Create `build.py` script for site generation
- [x] Implement template rendering with data injection
- [x] Add static asset copying functionality
- [x] Add build configuration and command-line options

## Phase 5: Styling and Assets
- [x] Extract and preserve CSS styles
- [x] Ensure mobile responsiveness in generated HTML
- [x] Optimize assets for production (minification if needed)
- [x] Test cross-browser compatibility

## Phase 6: Testing and Validation
- [x] Generate test site and compare with current Reflex output
- [x] Test all links and navigation
- [x] Validate responsive design on multiple devices
- [x] Performance testing (load times, file sizes)

## Phase 7: Deployment and Documentation
- [x] Update Dockerfile and deployment scripts for static hosting
- [x] Update README with new build and development instructions
- [x] Remove Reflex dependencies from requirements.txt
- [x] Add new dependencies (Jinja2, etc.)

## Phase 8: Cleanup
- [x] Remove all Reflex-related code and files
- [x] Update .gitignore for new structure
- [x] Final validation and testing

## Phase 9: Design Fidelity Improvements
- [x] Add Lucide icons to link buttons matching original Reflex design
- [x] Implement color schemes for buttons based on link tags (globe: lime, rss: lime, linkedin: sky, etc.)
- [x] Update avatar to display image with proper fallback text
- [x] Match exact typography and spacing from original Reflex styles
- [x] Ensure HTML structure matches Reflex-generated output
- [x] Add any missing CSS classes or styles for pixel-perfect match
- [x] Test visual comparison with original site screenshot/design