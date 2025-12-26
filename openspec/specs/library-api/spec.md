# Library API Specification

## ADDED Requirements

### Requirement: LIB-001
The library shall provide a `linkbio.build()` function for programmatic usage.

#### Scenario: Basic Build
Given site data as a dictionary and output directory,
When calling `linkbio.build(data, output_dir)`,
Then the function generates static files in the output directory.

#### Scenario: Custom Templates
Given custom template directory,
When calling `linkbio.build(data, output_dir, templates_dir=custom_templates)`,
Then the function uses custom templates for generation.

### Requirement: LIB-002
The library shall provide utilities for loading site data.

#### Scenario: JSON File Loading
Given a JSON file path,
When calling `linkbio.load_data('data.json')`,
Then the function returns parsed site data as a dictionary.

#### Scenario: Data Validation
Given site data,
When calling `linkbio.validate_data(data)`,
Then the function validates required fields and returns validation results.

### Requirement: LIB-003
The library shall provide template management functionality.

#### Scenario: Template Discovery
When calling `linkbio.get_available_templates()`,
Then the function returns a list of available template names.

#### Scenario: Custom Template Loading
Given a template directory,
When calling `linkbio.load_templates(template_dir)`,
Then the function loads and returns Jinja2 template objects.

### Requirement: LIB-004
The library shall provide proper error handling and exceptions.

#### Scenario: Build Errors
When build fails due to invalid data,
Then the function raises `linkbio.BuildError` with descriptive message.

#### Scenario: Template Errors
When template rendering fails,
Then the function raises `linkbio.TemplateError` with context information.