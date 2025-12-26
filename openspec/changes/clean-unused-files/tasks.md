# Tasks: Clean Unused Files

## Phase 1: Analysis
- [ ] Review build.py and setup.py to confirm which files are actually used
- [ ] Check for references to assets/, docs/, public_export/ in code
- [ ] Verify if src/linkbio/templates/ is used for packaging vs templates/ for build

## Phase 2: Identify Files to Remove
- [ ] Confirm removal of duplicate src/linkbio/templates/ (keep templates/ for build)
- [ ] Confirm removal of unused assets/ directory
- [ ] Confirm removal of docs/INSTALL.md if not referenced
- [ ] Confirm removal of public_export/ if outdated

## Phase 3: Backup and Remove
- [ ] Create git commit before removal for safety
- [ ] Remove identified files/directories
- [ ] Update .gitignore if needed

## Phase 4: Validation
- [ ] Run build.py to ensure no breakage
- [ ] Run tests to confirm functionality
- [ ] Check repository size reduction</content>
<parameter name="filePath">c:\projectos\links\openspec\changes\clean-unused-files\tasks.md