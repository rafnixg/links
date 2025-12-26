# Proposal: Rename to LinkBioSite

## Why
The project name "linkbio" is too generic and doesn't clearly convey that this is a static site generator for link bio pages. Renaming to "linkbiosite" (LinkBioSite) provides better clarity about the project's purpose and makes it more discoverable for users looking for link bio site generators.

## What Changes
- Rename package from `linkbio` to `linkbiosite`
- Rename CLI command from `linkbio` to `linkbiosite`
- Rename main class from `LinkBioGenerator` to `LinkBioSiteGenerator`
- Update all imports, references, and documentation
- Update project metadata, URLs, and package configuration
- Rename source directory from `src/linkbio/` to `src/linkbiosite/`
- Update all documentation and examples

## Impact
- **Breaking Change**: All existing installations and usage will break
- **Migration Required**: Users will need to update imports and CLI commands
- **Package Name**: New package name on PyPI and installation commands
- **URLs**: All GitHub URLs and documentation links will change
- **Backwards Compatibility**: None - this is a complete rebrand

## Alternatives Considered
- Keep current name: Maintains existing user base but lacks clarity
- Use different name: "biolinks", "linkpage", etc. - "linkbiosite" is most descriptive
- Versioned rename: Could cause confusion with multiple names

## Implementation Plan
See `tasks.md` for detailed implementation steps.
See `design.md` for technical considerations.
See spec deltas for detailed requirements.