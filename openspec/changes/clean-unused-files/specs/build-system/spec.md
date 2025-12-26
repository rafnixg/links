# Build System

## MODIFIED Requirements

### Requirement: Clean File Structure
The build system SHALL maintain a clean file structure with consolidated templates in the package directory.

#### Scenario: Consolidate Templates
Given the build system and package use templates
When duplicate template directories exist
Then consolidate to single src/linkbio/templates/ location

#### Scenario: Remove Unused Assets
Given assets are not referenced in the build process
When assets/ directory exists
Then remove it to reduce clutter - kept as used

#### Scenario: Remove Outdated Documentation
Given INSTALL.md is not used
When docs/INSTALL.md exists
Then remove it for cleaner docs</content>
<parameter name="filePath">c:\projectos\links\openspec\changes\clean-unused-files\specs\build-system\spec.md