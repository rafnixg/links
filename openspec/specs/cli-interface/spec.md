# CLI Interface Specification

## ADDED Requirements

### Requirement: CLI-001
The system shall provide a command-line interface accessible via the `linkbio` command.

#### Scenario: Build Command
Given a data configuration file and output directory,
When the user runs `linkbio build data.json output/`,
Then the system generates a static site in the output directory.

#### Scenario: Init Command
Given a project name,
When the user runs `linkbio init my-site`,
Then the system creates a new project structure with default templates and configuration.

#### Scenario: Serve Command
Given a built site directory,
When the user runs `linkbio serve output/`,
Then the system starts a local development server on port 8000.

### Requirement: CLI-002
The CLI shall provide comprehensive help for all commands.

#### Scenario: Global Help
When the user runs `linkbio --help`,
Then the system displays available commands and usage information.

#### Scenario: Command Help
When the user runs `linkbio build --help`,
Then the system displays detailed help for the build command including options.

### Requirement: CLI-003
The CLI shall provide clear error messages and exit codes.

#### Scenario: Invalid Arguments
When the user provides invalid arguments,
Then the system displays an error message and exits with code 1.

#### Scenario: Missing Files
When required files are missing,
Then the system displays a helpful error message and exits with code 1.