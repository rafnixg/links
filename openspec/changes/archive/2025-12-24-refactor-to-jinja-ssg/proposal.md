# Proposal: Refactor to Jinja-Based Static Site Generator

## Summary
Refactor the entire link bio project from using Reflex (a Python web framework) to a custom-built Static Site Generator (SSG) using Jinja2 for templating. This change aims to simplify the architecture, improve build times, and enable static hosting while maintaining the core functionality of displaying personal links and bio information.

## Motivation
- **Performance**: Static sites load faster and require no server-side processing.
- **Simplicity**: Remove dependency on Reflex framework, reducing complexity.
- **Hosting**: Enable deployment to static hosting services (e.g., GitHub Pages, Netlify).
- **Customization**: Full control over the build process and output.
- **Maintenance**: Easier to maintain a custom SSG than a full web framework.

## Scope
- Replace all Reflex components and views with Jinja templates.
- Implement a custom Python-based SSG script.
- Preserve existing link data and structure.
- Maintain responsive design and mobile-friendliness.
- Update build and deployment processes.

## Impact
- **Breaking Change**: Complete rewrite of the application architecture.
- **Dependencies**: Remove Reflex, add Jinja2 and other SSG dependencies.
- **Workflow**: Change from dynamic web app to static site generation.
- **Features**: All existing features (link display, bio, responsive design) will be reimplemented.

## Alternatives Considered
- Keep Reflex: Maintains current functionality but doesn't address performance/simplicity goals.
- Use existing SSG (e.g., Jekyll, Hugo): Would require learning new tools and may not integrate well with Python data sources.
- Hybrid approach: Keep some dynamic elements, but increases complexity.

## Implementation Plan
See `tasks.md` for detailed implementation steps.
See `design.md` for architectural decisions.
See spec deltas for detailed requirements.