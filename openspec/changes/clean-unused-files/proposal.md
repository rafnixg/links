# Proposal: Clean Unused Files

## Summary
Consolidate templates into a single location (src/linkbio/templates/) and remove other unnecessary files and directories from the codebase to reduce clutter and improve maintainability.

## Motivation
- **Reduce Clutter**: Eliminate files that are not used in the current build process or development workflow.
- **Improve Maintainability**: A cleaner codebase is easier to navigate and understand.
- **Avoid Confusion**: Remove duplicates that could lead to inconsistencies.

## Scope
- Consolidate templates into src/linkbio/templates/ and update build.py
- Remove root templates/ directory
- Remove unused docs/INSTALL.md
- Remove public_export file
- Ensure no breaking changes to build or functionality.

## Impact
- **Codebase Size**: Reduction in repository size.
- **Build Process**: No changes, as removed files are not used.
- **Maintenance**: Easier to manage remaining files.

## Alternatives Considered
- Keep all files for potential future use: Increases clutter.
- Move to separate branch: Unnecessary complexity.

## Implementation Plan
See `tasks.md` for detailed implementation steps.</content>
<parameter name="filePath">c:\projectos\links\openspec\changes\clean-unused-files\proposal.md