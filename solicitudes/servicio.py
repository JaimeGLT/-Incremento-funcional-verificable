from datetime import datetime

from .repositorio import RepositorioJSON
from .validacion import NoEncontrada, validar_nueva


def _ahora():
    return datetime.now().isoformat(timespec="seconds")


class ServicioSolicitudes:
    def __init__(self, repositorio=None):
        self.repo = repositorio or RepositorioJSON()

    def registrar(self, solicitante, categoria, descripcion, prioridad):
        validar_nueva(solicitante, categoria, descripcion, prioridad)
        codigo = f"SOL-{self.repo.siguiente_numero():04d}"
        solicitud = {
            "codigo": codigo,
            "solicitante": solicitante.strip(),
            "categoria": categoria,
            "descripcion": descripcion.strip(),
            "prioridad": prioridad,
            "estado": "Registrada",
            "tecnico": None,
            "historial": [{"fecha": _ahora(), "cambio": "Solicitud registrada"}],
        }
        self.repo.guardar(solicitud)
        return solicitud

    def consultar(self, codigo):
        solicitud = self.repo.obtener((codigo or "").strip().upper())
        if solicitud is None:
            raise NoEncontrada(f"No existe una solicitud con el código '{codigo}'.")
        return solicitud
