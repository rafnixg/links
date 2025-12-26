# Proposal: Clean Unused Files

## Summary
Remove unnecessary files and directories from the codebase to reduce clutter and improve maintainability. This includes duplicate template directories, unused assets, and outdated documentation.

## Motivation
- **Reduce Clutter**: Eliminate files that are not used in the current build process or development workflow.
- **Improve Maintainability**: A cleaner codebase is easier to navigate and understand.
- **Avoid Confusion**: Remove duplicates that could lead to inconsistencies.

## Scope
- Identify and remove duplicate template directories (src/linkbio/templates/ vs templates/).
- Remove unused assets/ directory.
- Remove unused docs/INSTALL.md.
- Remove public_export/ if it's outdated.
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