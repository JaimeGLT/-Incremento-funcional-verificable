import unittest

from solicitudes.servicio import ServicioSolicitudes
from solicitudes.validacion import ErrorValidacion

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


if __name__ == "__main__":
    unittest.main()
