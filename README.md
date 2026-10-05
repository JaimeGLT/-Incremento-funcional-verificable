# Sistema de solicitudes

Incremento que permite registrar una solicitud, consultarla por código, asignar técnico,
actualizar estado y ver el historial de cambios. Python 3.8+, solo biblioteca estándar.

## Ejecución
```bash
python -m solicitudes registrar --solicitante "Ana" --categoria Hardware \
    --descripcion "Pantalla rota" --prioridad Alta     # imprime SOL-0001
python -m solicitudes asignar SOL-0001 "Luis"
python -m solicitudes estado SOL-0001 "En proceso"
python -m solicitudes consultar SOL-0001               # datos + historial
```
- Categorías: Hardware, Software, Red, Acceso, Otro. Prioridades: Baja, Media, Alta.
- Estados: Registrada, Asignada, En proceso, Resuelta, Cerrada.
- Datos en `datos.json` (ignorado por git). Otra ruta: variable `SOLICITUDES_DB`.
- No hay credenciales en el código; cualquier configuración va en variables de entorno.

## Pruebas
```bash
python -m unittest -v
```

## Flujo de trabajo del equipo
- `main` protegida por acuerdo: nadie hace commit directo; solo merges `--no-ff` de ramas.
- Una rama por funcionalidad: `feature/registro`, `feature/consulta`, `feature/gestion`, `feature/cli`, `feature/docs`.
- Otro integrante revisa la rama (checklist en `docs/REVISION.md`) antes de integrar.
- Commits descriptivos. Ver evidencia en `docs/evidencia_historial.txt`.
- En GitHub/GitLab: activar "branch protection" en `main` (PR + 1 aprobación) y subir con `git push -u origin --all`.

## Entregables
`docs/TRAZABILIDAD.md` (matriz), `docs/PRUEBAS.md` (casos y resultados), `docs/evidencia_historial.txt`.
