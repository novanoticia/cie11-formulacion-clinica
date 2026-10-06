#!/usr/bin/env python3
"""Valida los catálogos de idioma del skill (idioma-<código>.md).

Uso:  python3 scripts/validar_idiomas.py [carpeta]

Sin argumentos valida skills/cie11-formulacion-clinica/. Sale con código 0 si
todo está bien y con 1 si hay problemas, listando qué falta en cada idioma.

Formato de un catálogo: un `## clave` por frase, seguido de su texto. El catálogo
de referencia (es) fija las claves, los marcadores y los códigos de máquina que
todos los demás idiomas deben conservar.

Marcadores: solo con nombre (`{condicion}`). Las llaves literales se escriben
dobles (`{{` y `}}`). Lo que va entre comillas invertidas (modos, comandos) es un
contrato de máquina y no se traduce.
"""
import re
import sys
from pathlib import Path

REFERENCIA = "es"
CARPETA_SKILL = Path(__file__).resolve().parent.parent / "skills" / "cie11-formulacion-clinica"

_NOMBRE_FICHERO = re.compile(r"^idioma-(.+)\.md$")
_CODIGO = re.compile(r"^[a-z]{2,3}$")
_MARCADOR = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)\}")
_CODIGO_MAQUINA = re.compile(r"`([^`]+)`")


def _secciones(texto):
    """Devuelve [(clave, texto)] en orden, incluidas las claves repetidas."""
    secciones, clave, lineas = [], None, []
    for linea in texto.splitlines():
        m = re.match(r"^##\s+(\S.*?)\s*$", linea)
        if m and not linea.startswith("###"):
            if clave is not None:
                secciones.append((clave, "\n".join(lineas).strip()))
            clave, lineas = m.group(1), []
        elif clave is not None:
            lineas.append(linea)
    if clave is not None:
        secciones.append((clave, "\n".join(lineas).strip()))
    return secciones


def parse_catalogo(texto):
    return dict(_secciones(texto))


def _sin_escapes(texto):
    return texto.replace("{{", "").replace("}}", "")


def marcadores(texto):
    return set(_MARCADOR.findall(_sin_escapes(texto)))


def problemas_marcadores(texto):
    """Llaves que no son un marcador con nombre ni una llave literal escapada."""
    resto = _MARCADOR.sub("", _sin_escapes(texto))
    return [f"llaves no válidas: {m!r}" for m in re.findall(r"\{[^{}]*\}?|\}", resto)]


def _entradas(texto):
    """Número de viñetas (- ...) de una lista, como la del glosario."""
    return sum(1 for linea in texto.splitlines() if linea.lstrip().startswith("- "))


def codigos_de_maquina(texto):
    return set(_CODIGO_MAQUINA.findall(texto))


def descubrir(carpeta):
    """{código: ruta} de los catálogos con nombre válido."""
    catalogos = {}
    for ruta in sorted(Path(carpeta).glob("idioma-*.md")):
        codigo = _NOMBRE_FICHERO.match(ruta.name).group(1)
        if _CODIGO.match(codigo):
            catalogos[codigo] = ruta
    return catalogos


def _validar_uno(codigo, texto):
    problemas = []
    secciones = _secciones(texto)
    if not secciones:
        return [f"{codigo}: el catálogo no define ninguna clave (## clave)"]
    vistas = set()
    for clave, valor in secciones:
        if clave in vistas:
            problemas.append(f"{codigo}: clave duplicada '{clave}'")
        vistas.add(clave)
        if not valor:
            problemas.append(f"{codigo}: la clave '{clave}' está vacía")
        if valor.count("`") % 2:
            problemas.append(f"{codigo}: clave '{clave}': comillas invertidas sin cerrar")
        for p in problemas_marcadores(valor):
            problemas.append(f"{codigo}: clave '{clave}': {p}")
    return problemas


def validar(carpeta):
    """Lista de problemas; vacía si todos los catálogos son correctos."""
    carpeta = Path(carpeta)
    problemas = []
    for ruta in sorted(carpeta.glob("idioma-*.md")):
        codigo = _NOMBRE_FICHERO.match(ruta.name).group(1)
        if not _CODIGO.match(codigo):
            problemas.append(f"{ruta.name}: código de idioma no válido "
                             f"(se espera idioma-<xx>.md en minúsculas, p. ej. idioma-fr.md)")
    catalogos = descubrir(carpeta)
    if REFERENCIA not in catalogos:
        return problemas + [f"falta el catálogo de referencia idioma-{REFERENCIA}.md"]

    textos = {c: r.read_text(encoding="utf-8") for c, r in catalogos.items()}
    for codigo, texto in textos.items():
        problemas += _validar_uno(codigo, texto)

    ref = parse_catalogo(textos[REFERENCIA])
    for codigo, texto in textos.items():
        if codigo == REFERENCIA:
            continue
        datos = parse_catalogo(texto)
        for clave in ref:
            if clave not in datos:
                problemas.append(f"{codigo}: falta la clave '{clave}' (definida en {REFERENCIA})")
        for clave in datos:
            if clave not in ref:
                problemas.append(f"{codigo}: sobra la clave '{clave}' (no existe en {REFERENCIA})")
        for clave in ref.keys() & datos.keys():
            if clave == "glosario" and _entradas(datos[clave]) != _entradas(ref[clave]):
                problemas.append(
                    f"{codigo}: clave 'glosario': {_entradas(datos[clave])} entradas, "
                    f"{REFERENCIA} tiene {_entradas(ref[clave])} (misma lista, mismo orden)")
            if marcadores(datos[clave]) != marcadores(ref[clave]):
                problemas.append(
                    f"{codigo}: clave '{clave}': marcadores {sorted(marcadores(datos[clave]))} "
                    f"distintos de los de {REFERENCIA} {sorted(marcadores(ref[clave]))}")
            if codigos_de_maquina(datos[clave]) != codigos_de_maquina(ref[clave]):
                problemas.append(
                    f"{codigo}: clave '{clave}': los textos entre comillas invertidas "
                    f"(contrato de máquina) deben ser idénticos a los de {REFERENCIA}")
    return problemas


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    carpeta = Path(argv[0]) if argv else CARPETA_SKILL
    problemas = validar(carpeta)
    if problemas:
        print(f"❌ {len(problemas)} problema(s) en los catálogos de idioma de {carpeta}:",
              file=sys.stderr)
        for p in problemas:
            print(f"   - {p}", file=sys.stderr)
        return 1
    codigos = sorted(descubrir(carpeta))
    claves = len(parse_catalogo((carpeta / f"idioma-{REFERENCIA}.md").read_text(encoding="utf-8")))
    print(f"✅ Catálogos correctos: {', '.join(codigos)} ({claves} claves cada uno)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
