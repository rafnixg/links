## ADDED Requirements

Requirement: Publish to PyPI on release
--------------------------------------
The repository must provide a GitHub Actions workflow that publishes the package to PyPI when a GitHub Release is published.

#### Scenario: Release triggers publish
- Given a GitHub Release is published (not draft)
- When the publish workflow runs
- Then the workflow builds the distributable package and uploads it to PyPI using a secret token

#### Scenario: Missing secret fails safely
- Given no `PYPI_API_TOKEN` exists in repository secrets
- When the publish workflow is triggered
- Then the workflow should fail with a clear message and must not attempt unauthenticated uploads

Validation Notes
- Ensure `PYPI_API_TOKEN` is documented for maintainers and stored in GitHub Secrets.
- Prefer `twine` for upload and `python -m build` for package building.
