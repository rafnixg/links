# Tasks: Clean Unused Files

## Phase 1: Analysis
- [x] Review build.py and setup.py to confirm which files are actually used
- [x] Check for references to assets/, docs/, public_export/ in code
- [x] Verify if src/linkbio/templates/ is used for packaging vs templates/ for build

## Phase 2: Identify Files to Remove
- [x] Consolidate templates: move to src/linkbio/templates/ and update build.py
- [x] Remove root templates/ directory
- [x] Confirm removal of unused assets/ directory - kept as used
- [x] Confirm removal of docs/INSTALL.md if not referenced - removed
- [x] Confirm removal of public_export/ if outdated - removed (was a file)

## Phase 3: Backup and Remove
- [x] Create git commit before removal for safety
- [x] Remove identified files/directories
- [x] Update .gitignore if needed - not needed

## Phase 4: Validation
- [x] Run build.py to ensure no breakage
- [x] Run tests to confirm functionality
- [x] Verify only src/linkbio/templates/ remains</content>
<parameter name="filePath">c:\projectos\links\openspec\changes\clean-unused-files\tasks.md