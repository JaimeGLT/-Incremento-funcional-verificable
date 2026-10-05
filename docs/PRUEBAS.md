# Casos y resultados de prueba

| Tipo | Prueba | Caso |
|---|---|---|
| Unitaria | test_codigo_unico | Dos registros → códigos distintos |
| Unitaria | test_registro_inicia_en_estado_registrada | Estado inicial e historial |
| Unitaria | test_error_datos_incompletos | Solicitante y descripción vacíos → 2 mensajes |
| Unitaria | test_consulta_codigo_inexistente | SOL-9999 → NoEncontrada |
| Unitaria | test_consulta_por_codigo, test_asignar_tecnico_y_estado_con_historial, test_estado_invalido | Consulta, gestión, estado inválido |
| Integración | test_persistencia_entre_instancias | JSON conserva y continúa numeración |
| Integración | test_cli_errores_comprensibles | CLI: datos incompletos y código inexistente, salida 1 |
| Aceptación | test_flujo_completo | Registrar → asignar → estados → consultar |

## Resultado (2026-10-05)
```
test_flujo_completo (tests.test_integracion.TestAceptacion.test_flujo_completo) ... ok
test_cli_errores_comprensibles (tests.test_integracion.TestIntegracion.test_cli_errores_comprensibles) ... ok
test_persistencia_entre_instancias (tests.test_integracion.TestIntegracion.test_persistencia_entre_instancias) ... ok
test_asignar_tecnico_y_estado_con_historial (tests.test_unitarias.TestUnitarias.test_asignar_tecnico_y_estado_con_historial) ... ok
test_codigo_unico (tests.test_unitarias.TestUnitarias.test_codigo_unico) ... ok
test_consulta_codigo_inexistente (tests.test_unitarias.TestUnitarias.test_consulta_codigo_inexistente) ... ok
test_consulta_por_codigo (tests.test_unitarias.TestUnitarias.test_consulta_por_codigo) ... ok
test_error_datos_incompletos (tests.test_unitarias.TestUnitarias.test_error_datos_incompletos) ... ok
test_estado_invalido (tests.test_unitarias.TestUnitarias.test_estado_invalido) ... ok
test_registro_inicia_en_estado_registrada (tests.test_unitarias.TestUnitarias.test_registro_inicia_en_estado_registrada) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.009s

OK
```
