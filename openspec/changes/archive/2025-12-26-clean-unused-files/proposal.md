# Proposal: Clean Unused Files

## Why
Consolidate templates into a single location (src/linkbio/templates/) and remove other unnecessary files and directories from the codebase to reduce clutter and improve maintainability.

## What Changes
- Consolidate templates into src/linkbio/templates/ and update build.py
- Remove root templates/ directory
- Remove unused docs/INSTALL.md
- Remove public_export file
- Ensure no breaking changes to build or functionality
- **Maintenance**: Easier to manage remaining files.

## Alternatives Considered
- Keep all files for potential future use: Increases clutter.
- Move to separate branch: Unnecessary complexity.

## Implementation Plan
See `tasks.md` for detailed implementation steps.</content>
<parameter name="filePath">c:\projectos\links\openspec\changes\clean-unused-files\proposal.md