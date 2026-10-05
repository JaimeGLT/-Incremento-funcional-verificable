import contextlib
import io
import os
import tempfile
import unittest

from solicitudes.cli import main
from solicitudes.repositorio import RepositorioJSON
from solicitudes.servicio import ServicioSolicitudes


def ejecutar(ruta, *argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        codigo = main(list(argv), ruta_db=ruta)
    return codigo, out.getvalue(), err.getvalue()


class Base(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.ruta = os.path.join(self.dir.name, "db.json")

    def tearDown(self):
        self.dir.cleanup()


class TestIntegracion(Base):
    def test_persistencia_entre_instancias(self):
        codigo = ServicioSolicitudes(RepositorioJSON(self.ruta)).registrar(
            "Ana", "Red", "Sin internet", "Media")["codigo"]
        otra = ServicioSolicitudes(RepositorioJSON(self.ruta))
        self.assertEqual(otra.consultar(codigo)["categoria"], "Red")
        self.assertEqual(otra.registrar("Beto", "Red", "Lento", "Baja")["codigo"], "SOL-0002")

    def test_cli_errores_comprensibles(self):
        rc, _, err = ejecutar(self.ruta, "registrar", "--solicitante", "Ana")
        self.assertEqual(rc, 1)
        self.assertIn("La descripción es obligatoria.", err)
        rc, _, err = ejecutar(self.ruta, "consultar", "SOL-9999")
        self.assertEqual(rc, 1)
        self.assertIn("No existe una solicitud", err)


class TestAceptacion(Base):
    def test_flujo_completo(self):
        rc, out, _ = ejecutar(self.ruta, "registrar", "--solicitante", "Ana",
                              "--categoria", "Hardware", "--descripcion", "Pantalla rota",
                              "--prioridad", "Alta")
        self.assertEqual(rc, 0)
        codigo = out.split()[-1]
        self.assertEqual(ejecutar(self.ruta, "asignar", codigo, "Luis")[0], 0)
        self.assertEqual(ejecutar(self.ruta, "estado", codigo, "En proceso")[0], 0)
        self.assertEqual(ejecutar(self.ruta, "estado", codigo, "Resuelta")[0], 0)
        rc, out, _ = ejecutar(self.ruta, "consultar", codigo)
        self.assertEqual(rc, 0)
        self.assertIn("Estado:      Resuelta", out)
        self.assertIn("Técnico:     Luis", out)
        self.assertIn("Solicitud registrada", out)
        self.assertIn("Estado: Asignada -> En proceso", out)


if __name__ == "__main__":
    unittest.main()
