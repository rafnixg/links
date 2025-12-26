# Build System

## MODIFIED Requirements

### Requirement: Clean File Structure
The build system SHALL maintain a clean file structure without unnecessary duplicate or unused files.

#### Scenario: Duplicate Templates
Given the build system uses templates/ for static site generation
When duplicate templates exist in src/linkbio/templates/
Then remove the duplicate to avoid confusion

#### Scenario: Unused Assets
Given assets are not referenced in the build process
When assets/ directory exists
Then remove it to reduce clutter

#### Scenario: Outdated Documentation
Given INSTALL.md is not used
When docs/INSTALL.md exists
Then remove it for cleaner docs</content>
<parameter name="filePath">c:\projectos\links\openspec\changes\clean-unused-files\specs\build-system\spec.md