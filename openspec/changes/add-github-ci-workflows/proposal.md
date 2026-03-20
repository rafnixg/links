# Proposal: Add GitHub Actions workflows for static build and PyPI publish

Change-id: add-github-ci-workflows

Summary
-------
Se propone añadir dos flujos de trabajo de GitHub Actions:

- Un workflow que, en la rama `main`, ejecuta la build de los archivos estáticos del proyecto y actualiza la carpeta `public/` con los artefactos resultantes.
- Un workflow que se activa únicamente cuando se crea una Release en GitHub y publica el paquete en PyPI (solo en la release que cumple los requisitos).

Motivación
----------
Automatizar la generación de los activos estáticos y la publicación en PyPI para reducir trabajo manual y asegurar reproducibilidad en cada release.

Alcance
-------
- Documentación del cambio en OpenSpec (`proposal.md`, `tasks.md`, `design.md`) y dos spec deltas (una por capacidad).
- No se implementan las acciones en esta fase: esto es la etapa de propuesta y especificación. La implementación será un cambio separado tras la aprobación.

Guardrails
---------
- Mantener implementaciones mínimas y claras: primero CI simple y robusto, luego mejoras si se piden.
- No introducir secretos en los repositorios; usar GitHub Secrets para credenciales de PyPI.
- Evitar cambios que rompan la build local.

Entregables
-----------
- `openspec/changes/add-github-ci-workflows/proposal.md`
- `openspec/changes/add-github-ci-workflows/tasks.md`
- `openspec/changes/add-github-ci-workflows/design.md`
- `openspec/changes/add-github-ci-workflows/specs/static-build/spec.md`
- `openspec/changes/add-github-ci-workflows/specs/pypi-publish/spec.md`

Validación
----------
- Ejecutar `openspec validate add-github-ci-workflows --strict` (o el comando del flujo de trabajo de OpenSpec) y resolver errores.
- Revisión y aprobación por el mantenedor antes de la implementación.

Riesgos conocidos
-----------------
- Requiere que el repositorio tenga comandos reproducibles para generar los estáticos. Si faltan scripts, la implementación necesitará pequeños ajustes.

Dependencias
------------
- Definir `PYPI_API_TOKEN` (secret) en GitHub para publicar a PyPI.
- Confirmar el comando de build de activos estáticos (por ejemplo `linkbiosite build` o `make build`).

Solicito aprobación para pasar a la etapa de implementación (crear workflows en `.github/workflows/`).
