CATEGORIAS = ("Hardware", "Software", "Red", "Acceso", "Otro")
PRIORIDADES = ("Baja", "Media", "Alta")
ESTADOS = ("Registrada", "Asignada", "En proceso", "Resuelta", "Cerrada")


class ErrorValidacion(Exception):
    """Datos incorrectos o incompletos. Guarda la lista de mensajes."""

    def __init__(self, errores):
        self.errores = list(errores)
        super().__init__(" ".join(self.errores))


class NoEncontrada(Exception):
    """No existe una solicitud con el código dado."""


def validar_nueva(solicitante, categoria, descripcion, prioridad):
    errores = []
    if not (solicitante or "").strip():
        errores.append("El solicitante es obligatorio.")
    if not (descripcion or "").strip():
        errores.append("La descripción es obligatoria.")
    if categoria not in CATEGORIAS:
        errores.append(f"Categoría inválida. Use una de: {', '.join(CATEGORIAS)}.")
    if prioridad not in PRIORIDADES:
        errores.append(f"Prioridad inválida. Use una de: {', '.join(PRIORIDADES)}.")
    if errores:
        raise ErrorValidacion(errores)
