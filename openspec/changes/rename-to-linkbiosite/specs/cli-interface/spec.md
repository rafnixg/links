# CLI Interface

## MODIFIED Requirements

### Requirement: CLI-001
The system SHALL provide a command-line interface accessible via the `linkbiosite` command.

#### Scenario: Build Command
Given a data configuration file and output directory,
When the user runs `linkbiosite build data.json output/`,
Then the system generates a static site in the output directory.

#### Scenario: Init Command
Given a project name,
When the user runs `linkbiosite init my-site`,
Then the system creates a new project structure with default templates and configuration.

#### Scenario: Serve Command
Given a built site directory,
When the user runs `linkbiosite serve output/`,
Then the system starts a local development server on port 8000.

### Requirement: CLI-002
The CLI SHALL provide comprehensive help mentioning the linkbiosite branding.

#### Scenario: Global Help
When the user runs `linkbiosite --help`,
Then the system displays "LinkBioSite" in the description and help text.

#### Scenario: Command Help
When the user runs `linkbiosite build --help`,
Then the system displays help text with correct command references.