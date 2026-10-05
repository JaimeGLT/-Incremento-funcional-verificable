import unittest

from solicitudes.servicio import ServicioSolicitudes
from solicitudes.validacion import ErrorValidacion, NoEncontrada

DATOS = ("Ana", "Software", "No abre el correo", "Alta")


class TestUnitarias(unittest.TestCase):
    def test_codigo_unico(self):
        s = ServicioSolicitudes()
        self.assertNotEqual(s.registrar(*DATOS)["codigo"], s.registrar(*DATOS)["codigo"])

    def test_registro_inicia_en_estado_registrada(self):
        sol = ServicioSolicitudes().registrar(*DATOS)
        self.assertEqual(sol["estado"], "Registrada")
        self.assertEqual(len(sol["historial"]), 1)

    def test_error_datos_incompletos(self):
        with self.assertRaises(ErrorValidacion) as ctx:
            ServicioSolicitudes().registrar("", "Software", "  ", "Alta")
        self.assertEqual(len(ctx.exception.errores), 2)
        self.assertIn("solicitante es obligatorio", str(ctx.exception))

    def test_consulta_codigo_inexistente(self):
        with self.assertRaises(NoEncontrada) as ctx:
            ServicioSolicitudes().consultar("SOL-9999")
        self.assertIn("No existe una solicitud", str(ctx.exception))

    def test_consulta_por_codigo(self):
        s = ServicioSolicitudes()
        codigo = s.registrar(*DATOS)["codigo"]
        self.assertEqual(s.consultar(codigo)["solicitante"], "Ana")

    def test_asignar_tecnico_y_estado_con_historial(self):
        s = ServicioSolicitudes()
        codigo = s.registrar(*DATOS)["codigo"]
        s.asignar_tecnico(codigo, "Luis")
        sol = s.actualizar_estado(codigo, "Resuelta")
        self.assertEqual((sol["tecnico"], sol["estado"]), ("Luis", "Resuelta"))
        self.assertEqual(len(sol["historial"]), 4)

    def test_estado_invalido(self):
        s = ServicioSolicitudes()
        codigo = s.registrar(*DATOS)["codigo"]
        with self.assertRaises(ErrorValidacion):
            s.actualizar_estado(codigo, "Volando")


if __name__ == "__main__":
    unittest.main()
