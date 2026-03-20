# Design: GitHub Actions for static build and PyPI publish

Objetivo de diseño
------------------
Definir la arquitectura de dos workflows claros y robustos que cumplan con los requisitos del proyecto y los guardrails del repositorio.

Workflow: Build estáticos (rama `main`)
-------------------------------------
- Trigger: `push` a `main` (opcional: `workflow_dispatch` para ejecuciones manuales).
- Pasos principales:
  - `actions/checkout` para obtener el repo.
  - Configurar entorno (por ejemplo `actions/setup-python` si la build usa Python, o `actions/setup-node` si usa Node).
  - Instalar dependencias de build (por ejemplo `pip install .[dev]` o `npm ci`).
  - Ejecutar comando de build estático reproducible (ej: `linkbiosite build`, `python -m linkbiosite build`, o `npm run build`).
  - Copiar/artifactar los archivos generados hacia la ruta `public/` en el repo.
  - Commit y push de los cambios en `public/` (usar un bot/usuario de CI y proteger contra loops de CI): crear un commit con mensaje claro y evitar re-trigger infinito (`[ci skip]` o condicional para no ejecutar en commits generados por CI).

Decisiones y consideraciones
----------------------------
- Autenticación para push: usar un token GitHub con scope `repo` guardado en `GITHUB_TOKEN` (o `PAT`) con cuidado para evitar loops. Recomendado: usar `GITHUB_TOKEN` y condicionales para no re-disparar la build en commits hechos por el workflow.
- Evitar sobrescribir manualmente `public/` en commits subidos por terceros sin revisión.

Workflow: Publicar a PyPI (cuando exista Release)
-------------------------------------------------
- Trigger: `release` con `types: [published]` o `created` según la política del equipo.
- Pasos principales:
  - `actions/checkout`
  - Setup Python
  - Build paquete (`python -m build` o `python -m pip wheel` / `twine` compatible)
  - Autenticación PyPI: usar `PYPI_API_TOKEN` guardado en GitHub Secrets.
  - `twine upload` a PyPI (o TestPyPI en modo dry-run si la release está marcada así).

Seguridad
--------
- Requerir `PYPI_API_TOKEN` secret; fallar de forma segura si no existe.
- Hacer que el workflow solo se ejecute en releases aprobadas (por ejemplo, `published` y no drafts).

Fallbacks y pruebas locales
--------------------------
- Validar pasos con `act` o revisiones en repositorio de pruebas antes de desplegar a producción.
