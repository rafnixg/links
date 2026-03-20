1. Revisar `openspec/project.md` y `pyproject.toml` para confirmar comandos reproducibles de build. Validado.
2. Crear `proposal.md`, `tasks.md`, `design.md` y dos spec deltas (esta tarea).
3. Ejecutar `openspec validate add-github-ci-workflows --strict` y resolver issues.
4. Solicitar revisión y aprobación del mantenedor.
5. (Tras aprobación) Implementar workflows en `.github/workflows/`:
   - `build-static.yml` (push a `main`)
   - `publish-pypi-on-release.yml` (on: release)
6. Añadir pruebas de integración mínima (si procede): ejecutar la acción localmente con `act` o revisar ejecuciones en GitHub Actions.
7. Crear PR con cambios y cerrar la task tras merge.

Validación / Criterios de aceptación
-----------------------------------
- `openspec validate` no debe reportar errores.
- El workflow `build-static.yml` debe ejecutar la build sin errores en `main` y actualizar `public/` con los artefactos esperados.
- `publish-pypi-on-release.yml` debe publicarse solo cuando exista token `PYPI_API_TOKEN` y la release esté marcada para publicación.
