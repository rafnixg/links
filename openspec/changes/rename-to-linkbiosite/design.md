# Design: Rename to LinkBioSite

## Context
The current project name "linkbio" lacks specificity and doesn't clearly communicate that this is a static site generator for creating link bio pages. The rename to "linkbiosite" provides better discoverability and clarity of purpose.

## Goals / Non-Goals
- **Goals**:
  - Provide clear, descriptive project naming
  - Improve discoverability for users seeking link bio solutions
  - Maintain all existing functionality
  - Ensure clean, consistent naming throughout codebase

- **Non-Goals**:
  - Change core functionality or features
  - Maintain backwards compatibility
  - Preserve existing user installations

## Decisions

### Package Naming
- **Decision**: Use "linkbiosite" as the package name
- **Rationale**: More descriptive than "linkbio", clearly indicates it's a site generator
- **Alternatives**: "biolinks", "linkpage", "biosite" - "linkbiosite" is most specific

### Class Naming
- **Decision**: Rename `LinkBioGenerator` to `LinkBioSiteGenerator`
- **Rationale**: Consistency with package name, clearer purpose
- **Impact**: Breaking change for API users

### CLI Command
- **Decision**: Change command from `linkbio` to `linkbiosite`
- **Rationale**: Direct mapping to package name
- **Migration**: Users must update their scripts and habits

### Directory Structure
- **Decision**: Rename `src/linkbio/` to `src/linkbiosite/`
- **Rationale**: Consistency with package name
- **Implementation**: Requires updating all import paths

## Risks / Trade-offs

### Breaking Changes
- **Risk**: All existing users will experience breaking changes
- **Mitigation**: Clear migration guide, major version bump
- **Trade-off**: Better naming vs user convenience

### Discoverability
- **Benefit**: New users can more easily find the project
- **Cost**: Existing users must adapt to new name

### Maintenance
- **Risk**: Potential for missed references during rename
- **Mitigation**: Comprehensive search and replace, thorough testing

## Migration Plan

### Phase 1: Code Changes
1. Rename directory structure
2. Update all imports and references
3. Update configuration files

### Phase 2: Package Updates
1. Update package metadata
2. Change entry points
3. Update documentation

### Phase 3: User Migration
1. Provide migration guide
2. Update installation instructions
3. Communicate changes clearly

## Open Questions
- Should we provide a compatibility shim for the old name?
- How to handle existing PyPI package name?
- Timeline for the rename and communication plan?