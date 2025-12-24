# Project Context

## Purpose
This project is a modern and responsive personal bio links page built with Reflex, serving as a centralized hub for Rafnix Guzmán's social media profiles, projects, and articles. It provides a clean, mobile-friendly interface for visitors to access various online presences and content.

## Tech Stack
- **Language**: Python 3.11+
- **Framework**: Reflex 0.4.8 (full-stack Python web framework)
- **Frontend Build**: Next.js (used internally by Reflex)
- **Containerization**: Docker
- **Analytics**: Umami Analytics
- **Deployment**: Docker containers

## Project Conventions

### Code Style
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Components follow Reflex naming conventions (e.g., PascalCase for component classes)
- Use type hints where appropriate
- Keep line lengths under 88 characters (Black formatter default)

### Architecture Patterns
- **Component-based architecture**: UI broken into reusable components in `link_bio/components/`
- **View separation**: Page sections organized in `link_bio/views/`
- **Style isolation**: CSS styles centralized in `link_bio/styles/`
- **Reflex app structure**: Main app in `link_bio.py`, config in `rxconfig.py`

### Testing Strategy
- Unit tests for individual components and utilities
- Integration tests for page rendering and interactions
- Manual testing for responsive design across devices
- Validate builds and exports work correctly

### Git Workflow
- Use feature branches for new work
- Squash commits for clean history
- Use descriptive commit messages
- Tag releases for deployment

## Domain Context
This is a personal branding and networking tool. The domain involves:
- Social media link aggregation
- Personal project showcase
- Content discovery facilitation
- Mobile-first user experience
- SEO optimization for discoverability

## Important Constraints
- Must be fully responsive and mobile-friendly
- SEO optimized with proper meta tags
- Dark theme as primary interface
- Fast loading times (static export capability)
- Docker containerization for consistent deployment

## External Dependencies
- **Umami Analytics**: For visitor tracking and insights
- **GitHub**: For repository hosting and CI/CD
- **Docker Hub**: For container image distribution
