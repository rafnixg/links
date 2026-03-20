## ADDED Requirements

Requirement: Static build workflow
---------------------------------
The repository must provide a GitHub Actions workflow that builds the project's static assets when changes are pushed to the `main` branch and updates the `public/` directory with the build output.

#### Scenario: Build runs on push to main
- Given a commit is pushed to `main`
- When the static build workflow runs
- Then the build command executes successfully and generates static assets in a known output directory
- And the workflow updates `public/` in the repository with the generated output as a single commit

#### Scenario: CI-created commit does not loop
- Given the workflow commits `public/` back to the repo
- When the commit is created by the workflow
- Then the workflow must not re-trigger an endless build loop (e.g., by using `[ci skip]` or by checking commit actor)

Validation Notes
- The spec requires confirmation of the exact build command; implementer should confirm `linkbiosite build` or equivalent.
