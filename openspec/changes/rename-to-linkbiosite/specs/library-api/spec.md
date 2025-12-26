# Library API

## MODIFIED Requirements

### Requirement: LIB-001
The library SHALL provide a `linkbiosite.build()` function for programmatic usage.

#### Scenario: Basic Build
Given site data as a dictionary and output directory,
When calling `linkbiosite.build(data, output_dir)`,
Then the function generates static files in the output directory.

#### Scenario: Custom Templates
Given custom template directory,
When calling `linkbiosite.build(data, output_dir, templates_dir=custom_templates)`,
Then the function uses custom templates for generation.

### Requirement: LIB-002
The library SHALL provide a `LinkBioSiteGenerator` class.

#### Scenario: Generator Instantiation
Given import statement,
When calling `from linkbiosite import LinkBioSiteGenerator`,
Then the LinkBioSiteGenerator class is available.

#### Scenario: Generator Usage
Given generator instance,
When calling `generator = LinkBioSiteGenerator()`,
Then a properly configured generator is created.

### Requirement: LIB-003
The library SHALL be organized under the `linkbiosite` package.

#### Scenario: Package Imports
Given package import,
When calling `import linkbiosite`,
Then all public API functions are available.

#### Scenario: Submodule Imports
Given submodule import,
When calling `from linkbiosite.core import build`,
Then the build function is available.