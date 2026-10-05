# Matriz de trazabilidad
| Req | Funcionalidad | Código | Prueba | Rama |
|---|---|---|---|---|
| 1 | Registrar solicitud (solicitante, categoría, descripción, prioridad) | `servicio.registrar` | test_registro_inicia_en_estado_registrada, test_flujo_completo | feature/registro |
| 2 | Código único | `servicio.registrar`, `repositorio.siguiente_numero` | test_codigo_unico, test_persistencia_entre_instancias | feature/registro |
| 3 | Consultar por código | `servicio.consultar` | test_consulta_por_codigo, test_flujo_completo | feature/consulta |
| 4 | Asignar técnico | `servicio.asignar_tecnico` | test_asignar_tecnico_y_estado_con_historial | feature/gestion |
| 5 | Actualizar estado | `servicio.actualizar_estado` | test_asignar_tecnico_y_estado_con_historial, test_estado_invalido | feature/gestion |
| 6 | Historial de cambios | `servicio._cambiar` | test_asignar_tecnico_y_estado_con_historial, test_flujo_completo | feature/gestion |
| 7 | Validar obligatorios | `validacion.validar_nueva` | test_error_datos_incompletos | feature/registro |
| 8 | Mensajes comprensibles | `validacion`, `cli` | test_cli_errores_comprensibles | feature/cli |
| — | Caso código inexistente | `servicio.consultar` | test_consulta_codigo_inexistente | feature/consulta |
