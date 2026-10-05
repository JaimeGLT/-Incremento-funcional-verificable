import json
import os


class RepositorioJSON:
    """Guarda las solicitudes en un archivo JSON. Sin ruta, solo en memoria."""

    def __init__(self, ruta=None):
        self.ruta = ruta
        self.datos = {}
        if ruta and os.path.exists(ruta):
            with open(ruta, encoding="utf-8") as f:
                self.datos = json.load(f)

    def siguiente_numero(self):
        return len(self.datos) + 1

    def obtener(self, codigo):
        return self.datos.get(codigo)

    def guardar(self, solicitud):
        self.datos[solicitud["codigo"]] = solicitud
        if self.ruta:
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump(self.datos, f, ensure_ascii=False, indent=2)
