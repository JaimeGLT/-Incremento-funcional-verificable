import argparse
import os
import sys

from .repositorio import RepositorioJSON
from .servicio import ServicioSolicitudes
from .validacion import CATEGORIAS, PRIORIDADES, ErrorValidacion, NoEncontrada


def _mostrar(s):
    print(f"Código:      {s['codigo']}")
    print(f"Solicitante: {s['solicitante']}")
    print(f"Categoría:   {s['categoria']}")
    print(f"Prioridad:   {s['prioridad']}")
    print(f"Descripción: {s['descripcion']}")
    print(f"Estado:      {s['estado']}")
    print(f"Técnico:     {s['tecnico'] or '(sin asignar)'}")
    print("Historial:")
    for h in s["historial"]:
        print(f"  {h['fecha']}  {h['cambio']}")


def _parser():
    p = argparse.ArgumentParser(prog="solicitudes")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("registrar")
    r.add_argument("--solicitante", default="")
    r.add_argument("--categoria", default="", help="/".join(CATEGORIAS))
    r.add_argument("--descripcion", default="")
    r.add_argument("--prioridad", default="", help="/".join(PRIORIDADES))
    c = sub.add_parser("consultar")
    c.add_argument("codigo")
    a = sub.add_parser("asignar")
    a.add_argument("codigo")
    a.add_argument("tecnico")
    e = sub.add_parser("estado")
    e.add_argument("codigo")
    e.add_argument("estado")
    return p


def main(argv=None, ruta_db=None):
    args = _parser().parse_args(argv)
    ruta = ruta_db or os.environ.get("SOLICITUDES_DB", "datos.json")
    servicio = ServicioSolicitudes(RepositorioJSON(ruta))
    try:
        if args.cmd == "registrar":
            s = servicio.registrar(args.solicitante, args.categoria, args.descripcion, args.prioridad)
            print(f"Solicitud registrada con código {s['codigo']}")
        elif args.cmd == "consultar":
            _mostrar(servicio.consultar(args.codigo))
        elif args.cmd == "asignar":
            servicio.asignar_tecnico(args.codigo, args.tecnico)
            print("Técnico asignado.")
        else:
            servicio.actualizar_estado(args.codigo, args.estado)
            print("Estado actualizado.")
    except ErrorValidacion as err:
        for m in err.errores:
            print(f"Error: {m}", file=sys.stderr)
        return 1
    except NoEncontrada as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1
    return 0
