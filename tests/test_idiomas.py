"""Pruebas de la capa multiidioma.

Ejecutar desde la raíz del repositorio:  python3 -m unittest discover -s tests -v

Tres bloques:
  1. El validador detecta catálogos defectuosos (datos sintéticos).
  2. Los catálogos reales (es/en/fr) pasan el validador y cubren todo el texto fijo.
  3. El idioma por defecto (es) no cambia respecto a la línea base (tests/linea_base.json).
"""
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "skills" / "cie11-formulacion-clinica"
BASE = json.loads((RAIZ / "tests" / "linea_base.json").read_text(encoding="utf-8"))


def cargar_validador():
    ruta = RAIZ / "scripts" / "validar_idiomas.py"
    spec = importlib.util.spec_from_file_location("validar_idiomas", ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def sha(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


# Claves que el catálogo de referencia (es) debe definir. Es el contrato entre
# flujo.md y los catálogos: si se añade texto fijo nuevo, se añade aquí.
CLAVES = [
    "modo_no_reconocido", "paso5_fuera_de_modo", "aviso_poblacion", "aviso_notas",
    "cabecera_comorbilidad", "no_documentado", "nota_final", "aviso_ia", "versiones_alternativas",
    "auditoria_solida", "sugerencia_auditoria", "sugerencia_auditoria_lagunas",
    "sospecha_desarrollada", "no_explorado_ideacion", "idioma_no_disponible",
    "enc_1", "enc_2", "enc_2a", "enc_2b", "enc_3", "enc_4", "enc_4a", "enc_4b",
    "enc_5", "enc_6", "enc_A", "enc_B", "enc_nota_final",
    "puerta1_identificadores", "puerta1_marco_legal", "glosario",
    "lbl_3_organicas", "lbl_3_sustancias", "lbl_3_psiquiatricos", "lbl_3_reaccion",
    "lbl_4b_consulta", "lbl_4b_pruebas", "lbl_4b_fuentes",
    "urg_necesaria", "urg_util", "urg_opcional",
    "lbl_5_explicitas", "lbl_5_implicitas", "lbl_5_protectores",
    "recordatorio_riesgo", "especificadores_por_determinar", "sin_datos_documentados",
]
# Claves cuyo texto en español no figura literal en flujo.md (se añaden con la capa de idioma).
SIN_LITERAL_EN_FLUJO = {"idioma_no_disponible", "sugerencia_auditoria", "sin_datos_documentados",
                        "puerta1_identificadores", "puerta1_marco_legal", "glosario"}
# Frases en cursiva entrecomillada de flujo.md que son etiquetas, no texto para personas.
NO_SON_FRASE = {"1 + 1-2"}

# Únicas líneas del español original que se modifican (aparte de los bloques i18n).
# Cada par es (nueva, vieja): restaurando la nueva por la vieja se recupera la línea base.
REEMPLAZOS = {
    "flujo.md": [(
        "- **Redacción fija.** Usa la clave `aviso_ia` del catálogo del idioma elegido "
        "(véase §0.0): un solo aviso, en ese idioma, sin resumirlo, suavizarlo ni mezclarlo "
        "con el contenido del paso 1. Si el clínico pidió un idioma que no existe, o no hay "
        "base para decidir el idioma, usa el bloque de los tres idiomas de arriba, juntos y "
        "en ese orden. El resto de la salida sigue el idioma elegido (véase §0.0).",
        "- **Redacción fija y en los tres idiomas** (español, inglés y francés), siempre "
        "juntos y en ese orden, sin importar en qué idioma escriba el clínico. No los "
        "resumas, no los suavices, no omitas ninguno ni los mezcles con el contenido del "
        "paso 1. El resto de la salida sigue siendo en español."),
        # Corrección clínica de dos códigos CIE-11 del apéndice (PR #11). Contenido clínico,
        # verificado por esa sesión contra la tabulación simple de la OMS 2024-01.
        ("(CIE-11 6E62).", "(CIE-11 6E60-6E61)."),
        ("(CIE-11 6A61)", "(CIE-11 6A60.1)")],
    "SKILL.md": [(
        "abre con el aviso de asistencia de IA en el idioma elegido (véase «Aviso de "
        "asistencia de IA» y §0.0 en `flujo.md`), antes",
        "abre con el aviso de asistencia de IA, en español, inglés y francés (véase «Aviso "
        "de asistencia de IA» en `flujo.md`), antes"),
        # Corrección de deriva de versión (sección «## Versión»; el frontmatter no se toca).
        ("v1.7.0 — versión vigente (cambios en el historial de versiones y en `CHANGELOG.md`). "
         "Mantiene la compatibilidad con Mistral AI (`description` < 500 caracteres) y con "
         "parsers YAML estrictos (Perplexity: `description` como bloque escalar `>-`). Base "
         "funcional en v1.5",
         "v1.5.2 — compatibilidad con Mistral AI (`description` < 500 caracteres) y con "
         "parsers YAML estrictos (Perplexity: `description` como bloque escalar `>-`); paquete "
         "`dist/` regenerado. Base funcional en v1.5")],
    # Decisión de diseño del autor: coherencia con la Puerta 1 de flujo.md (las iniciales
    # en contextos identificables son rechazo automático). Cambio de contenido de seguridad.
    "plantilla-caso.md": [(
        'usar un código neutro sin relación con el nombre (p. ej., "Caso A, 38 años").',
        'usar pseudónimo o iniciales no reconocibles (p. ej., "M.R., 38 años").')],
}


def normaliza(texto):
    texto = re.sub(r"(?m)^>\s?", "", texto).replace("**", "")  # sin citas ni negrita
    return re.sub(r"\s+", " ", texto).strip()


def catalogo(claves, **sobrescribe):
    """Genera un catálogo sintético con las claves dadas."""
    valores = {k: f"texto {k}" for k in claves}
    valores.update(sobrescribe)
    return "# catálogo\n\n" + "".join(f"## {k}\n{v}\n\n" for k, v in valores.items() if v is not None)


class TestValidadorSintetico(unittest.TestCase):
    """El validador debe detectar cada tipo de defecto y decir qué falta."""

    def setUp(self):
        self.V = cargar_validador()
        self.dir = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.dir)

    def escribe(self, codigo, texto):
        (self.dir / f"idioma-{codigo}.md").write_text(texto, encoding="utf-8")

    def test_parse_catalogo(self):
        datos = self.V.parse_catalogo("# t\n\n## a\nuno\ndos\n\n## b\ntres\n")
        self.assertEqual(datos, {"a": "uno\ndos", "b": "tres"})

    def test_catalogo_correcto_sin_problemas(self):
        self.escribe("es", catalogo(["a", "b"], a="hola {x}"))
        self.escribe("en", catalogo(["a", "b"], a="hello {x}"))
        self.assertEqual(self.V.validar(self.dir), [])

    def test_clave_que_falta(self):
        self.escribe("es", catalogo(["a", "b"]))
        self.escribe("en", catalogo(["a"]))
        problemas = "\n".join(self.V.validar(self.dir))
        self.assertIn("en", problemas)
        self.assertIn("b", problemas)

    def test_clave_sobrante(self):
        self.escribe("es", catalogo(["a"]))
        self.escribe("en", catalogo(["a", "z"]))
        self.assertIn("z", "\n".join(self.V.validar(self.dir)))

    def test_marcadores_distintos(self):
        self.escribe("es", catalogo(["a"], a="hola {x}"))
        self.escribe("en", catalogo(["a"], a="hello {y}"))
        self.assertTrue(self.V.validar(self.dir))

    def test_valor_vacio_en_idioma_traducido(self):
        self.escribe("es", catalogo(["a"]))
        self.escribe("en", catalogo(["a"], a="   "))
        self.assertTrue(self.V.validar(self.dir))

    def test_valor_vacio_en_idioma_por_defecto(self):
        self.escribe("es", catalogo(["a"], a=""))
        self.escribe("en", catalogo(["a"]))
        self.assertTrue(self.V.validar(self.dir))

    def test_marcadores_solo_con_nombre(self):
        for malo in ("{}", "{0}", "{a.b}", "{a[0]}", "{ x }"):
            with self.subTest(marcador=malo):
                self.escribe("es", catalogo(["a"], a=f"hola {malo}"))
                self.escribe("en", catalogo(["a"], a=f"hello {malo}"))
                self.assertTrue(self.V.validar(self.dir), malo)

    def test_llaves_sin_cerrar(self):
        self.escribe("es", catalogo(["a"], a="hola {x"))
        self.escribe("en", catalogo(["a"], a="hello {x"))
        self.assertTrue(self.V.validar(self.dir))

    def test_clave_duplicada(self):
        self.escribe("es", "## a\nuno\n\n## a\ndos\n")
        self.assertTrue(self.V.validar(self.dir))

    def test_idioma_nuevo_se_autodescubre_y_dice_que_falta(self):
        self.escribe("es", catalogo(["a", "b"]))
        self.escribe("pt", catalogo(["a"]))
        self.assertIn("pt", self.V.descubrir(self.dir))
        problemas = "\n".join(self.V.validar(self.dir))
        self.assertIn("pt", problemas)
        self.assertIn("b", problemas)

    def test_sin_catalogo_de_referencia(self):
        self.escribe("en", catalogo(["a"]))
        self.assertTrue(self.V.validar(self.dir))

    def test_nombre_de_fichero_invalido_se_reporta(self):
        self.escribe("es", catalogo(["a"]))
        (self.dir / "idioma-EN_US.md").write_text(catalogo(["a"]), encoding="utf-8")
        self.assertTrue(self.V.validar(self.dir))

    def test_glosario_mismo_numero_de_entradas(self):
        self.escribe("es", catalogo(["glosario"], glosario="- uno\n- dos"))
        self.escribe("en", catalogo(["glosario"], glosario="- one"))
        problemas = "\n".join(self.V.validar(self.dir))
        self.assertIn("glosario", problemas)

    def test_glosario_correcto_no_da_problemas(self):
        self.escribe("es", catalogo(["glosario"], glosario="- uno\n- dos"))
        self.escribe("en", catalogo(["glosario"], glosario="- one\n- two"))
        self.assertEqual(self.V.validar(self.dir), [])

    def test_comillas_invertidas_sin_cerrar(self):
        self.escribe("es", catalogo(["a"], a="invoca `auditoria"))
        self.escribe("en", catalogo(["a"], a="invoke `auditoria"))
        self.assertIn("comillas invertidas", "\n".join(self.V.validar(self.dir)))

    def test_codigos_de_maquina_identicos_entre_idiomas(self):
        # Lo que va entre comillas invertidas (modos, comandos) es contrato: no se traduce.
        self.escribe("es", catalogo(["a"], a="invoca `auditoria`"))
        self.escribe("en", catalogo(["a"], a="invoke `audit`"))
        self.assertTrue(self.V.validar(self.dir))


class TestCatalogosReales(unittest.TestCase):
    def setUp(self):
        self.V = cargar_validador()

    def test_existen_es_en_fr(self):
        self.assertLessEqual({"es", "en", "fr"}, set(self.V.descubrir(SKILL)))

    def test_validador_sin_problemas(self):
        self.assertEqual(self.V.validar(SKILL), [])

    def test_el_catalogo_es_define_todas_las_claves_del_contrato(self):
        datos = self.V.parse_catalogo((SKILL / "idioma-es.md").read_text(encoding="utf-8"))
        self.assertEqual(sorted(datos), sorted(CLAVES))

    def test_frases_es_son_literales_de_flujo(self):
        flujo = normaliza((SKILL / "flujo.md").read_text(encoding="utf-8"))
        datos = self.V.parse_catalogo((SKILL / "idioma-es.md").read_text(encoding="utf-8"))
        for clave in CLAVES:
            if clave in SIN_LITERAL_EN_FLUJO:
                continue
            with self.subTest(clave=clave):
                frase = normaliza(datos[clave].replace("{condicion}", "[descripción breve]"))
                self.assertIn(frase, flujo)

    def test_ningun_mensaje_fijo_queda_fuera_del_catalogo(self):
        flujo = (SKILL / "flujo.md").read_text(encoding="utf-8").split("## Apéndice")[0]
        es = normaliza((SKILL / "idioma-es.md").read_text(encoding="utf-8"))
        for frase in re.findall(r'\*"([^"]+)"\*', flujo):
            if frase in NO_SON_FRASE:
                continue
            with self.subTest(frase=frase[:50]):
                self.assertIn(normaliza(frase.replace("[descripción breve]", "{condicion}")), es)

    def test_flujo_declara_la_regla_de_idioma_y_no_hay_otra_salida_en_espanol(self):
        flujo = (SKILL / "flujo.md").read_text(encoding="utf-8")
        self.assertIn("<!-- i18n:inicio -->", flujo)
        for nueva, vieja in REEMPLAZOS["flujo.md"]:
            self.assertIn(nueva, flujo)
            self.assertNotIn(vieja, flujo)

    def datos(self, codigo):
        return self.V.parse_catalogo((SKILL / f"idioma-{codigo}.md").read_text(encoding="utf-8"))

    def test_claves_criticas_conservan_la_forma(self):
        # Forma, no sentido: la revisión del sentido clínico es humana (véase CLAUDE.md).
        frases = lambda s: len(re.findall(r"[.;]\s|[.;]$", s))
        es = self.datos("es")
        for codigo in ("en", "fr"):
            d = self.datos(codigo)
            with self.subTest(idioma=codigo):
                self.assertTrue(d["no_documentado"].startswith("[") and d["no_documentado"].endswith("]"))
                self.assertTrue(d["cabecera_comorbilidad"].startswith("⚠"))
                self.assertEqual(len(d["cabecera_comorbilidad"].splitlines()), 2)
                for clave in ("nota_final", "aviso_poblacion", "paso5_fuera_de_modo",
                              "recordatorio_riesgo", "aviso_notas"):
                    self.assertEqual(frases(d[clave]), frases(es[clave]), clave)
                    self.assertEqual(re.findall(r"\d+", d[clave]), re.findall(r"\d+", es[clave]), clave)

    def test_puerta1_son_ejemplos_no_una_jurisdiccion(self):
        for codigo, giro in (("es", "por ejemplo"), ("en", "for example"), ("fr", "par exemple")):
            d = self.datos(codigo)
            for clave in ("puerta1_identificadores", "puerta1_marco_legal"):
                with self.subTest(idioma=codigo, clave=clave):
                    self.assertIn(giro, d[clave].lower())

    def test_idioma_no_disponible_vale_para_pedido_y_para_detectado(self):
        for codigo in ("es", "en", "fr"):
            with self.subTest(idioma=codigo):
                self.assertNotRegex(self.datos(codigo)["idioma_no_disponible"].lower(),
                                    r"solicitad|requested|demandée")

    def test_regla_de_idioma_cierra_las_ambiguedades_de_la_revision(self):
        flujo = (SKILL / "flujo.md").read_text(encoding="utf-8")
        bloque = re.search(r"(?s)<!-- i18n:inicio -->\n## 0\.0.*?<!-- i18n:fin -->", flujo).group(0)
        for centinela in (
            "última palabra de la primera línea",        # código delimitado: «completo En consulta…» no es inglés
            "dos o tres letras",
            "solo si existe el fichero",                  # sin rutas arbitrarias
            "no es un modo pero es un código de idioma",  # «/cie11… en» sin modo
            "el caso está escrito en un idioma sin catálogo",  # caso en pt/ca/it
            "o cambie el idioma de la salida",            # el aviso se repite al cambiar de idioma
            "jurisdicción",                               # idioma ≠ país
            "El apéndice es solo un modelo de estructura",
            "(clave `no_documentado`)",
            "`sugerencia_auditoria`",
            # Hallazgos 1, 4 y 5 de la simulación de escenarios (2026-10-06)
            "llevan la nota final y no llevan versiones alternativas",  # paradas y comando sin caso
            "`sin_datos_documentados`",                                  # rótulo sin datos: frase fija
            "sin abreviar",                                              # enc_2a/enc_2b completos
            "nunca traduzcas el nombre",                                 # nombre de categoría dudoso
        ):
            with self.subTest(centinela=centinela):
                self.assertIn(centinela, bloque)

    def test_marcadores_i18n_emparejados(self):
        for nombre in ("flujo.md", "SKILL.md"):
            texto = (SKILL / nombre).read_text(encoding="utf-8")
            marcas = re.findall(r"<!-- i18n:(inicio|fin) -->", texto)
            with self.subTest(fichero=nombre):
                self.assertTrue(marcas)
                self.assertEqual(marcas, ["inicio", "fin"] * (len(marcas) // 2))

    def test_documentacion_no_promete_mas_de_lo_verificado(self):
        readme = (RAIZ / "README.md").read_text(encoding="utf-8")
        cambios = (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertNotIn("propios de cada país", readme)
        self.assertNotIn("por país", cambios)
        for nombre, texto in (("README", readme), ("CHANGELOG", cambios)):
            with self.subTest(doc=nombre):
                self.assertIn("escenarios.md", texto)
                self.assertIn("no se han ejecutado", texto)

    def test_bloque_trilingue_del_aviso_sigue_como_respaldo(self):
        flujo = (SKILL / "flujo.md").read_text(encoding="utf-8")
        for inicio in ("> **Aviso:**", "> **Notice:**", "> **Avertissement :**"):
            self.assertIn(inicio, flujo)

    def test_aviso_ia_de_cada_idioma_es_el_texto_aprobado_del_bloque_trilingue(self):
        # El aviso por idioma no se reescribe: es la línea ya aprobada del bloque trilingüe.
        flujo = normaliza((SKILL / "flujo.md").read_text(encoding="utf-8"))
        for codigo in ("es", "en", "fr"):
            with self.subTest(idioma=codigo):
                datos = self.V.parse_catalogo(
                    (SKILL / f"idioma-{codigo}.md").read_text(encoding="utf-8"))
                self.assertIn(normaliza(datos["aviso_ia"]), flujo)


class TestEspanolInvariante(unittest.TestCase):
    """El idioma por defecto no cambia: solo se admiten añadidos marcados y una frase."""

    def restaurado(self, nombre):
        texto = (SKILL / nombre).read_text(encoding="utf-8")
        texto = re.sub(r"(?s)<!-- i18n:inicio -->.*?<!-- i18n:fin -->\n", "", texto)
        for nueva, vieja in REEMPLAZOS.get(nombre, []):
            texto = texto.replace(nueva, vieja)
        return texto

    def test_ficheros_del_skill_identicos_a_la_linea_base(self):
        for nombre, esperado in BASE["ficheros"].items():
            with self.subTest(fichero=nombre):
                self.assertEqual(sha(self.restaurado(nombre)), esperado)

    @unittest.skipUnless(shutil.which("git"), "falta git")
    def test_espanol_identico_al_commit_base_de_git(self):
        # Defensa adicional: si alguien recalculara linea_base.json, esto lo detectaría.
        ok = subprocess.run(["git", "cat-file", "-e", f"{BASE['commit']}^{{commit}}"],
                            cwd=RAIZ, capture_output=True).returncode == 0
        if not ok:
            self.skipTest("el commit base no está en este clon")
        for nombre in BASE["ficheros"]:
            original = subprocess.run(
                ["git", "show", f"{BASE['commit']}:skills/cie11-formulacion-clinica/{nombre}"],
                cwd=RAIZ, capture_output=True, check=True).stdout.decode("utf-8")
            with self.subTest(fichero=nombre):
                self.assertEqual(self.restaurado(nombre), original)

    def test_frontmatter_intacto_y_cerrado(self):
        texto = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        fm = re.match(r"---\n.*?\n---\n", texto, re.S).group(0)
        self.assertEqual(sha(fm), BASE["frontmatter_skill"])
        claves = set(re.findall(r"(?m)^([a-z-]+):", fm))
        self.assertLessEqual(claves, {"name", "description", "license", "compatibility",
                                      "metadata", "allowed-tools", "author", "homepage",
                                      "repository"})
        desc = re.search(r"description: >-\n((?:  .*\n)+)", fm).group(1)
        self.assertLess(len(" ".join(l.strip() for l in desc.splitlines())), 500)

    def test_manifiestos_solo_cambian_la_version(self):
        for ruta, esperado in BASE["manifiestos"].items():
            with self.subTest(manifiesto=ruta):
                texto = (RAIZ / ruta).read_text(encoding="utf-8").replace("1.7.0", "1.6.2")
                self.assertEqual(sha(texto), esperado)

    def test_version_1_7_0_en_los_tres_manifiestos(self):
        for ruta in BASE["manifiestos"]:
            with self.subTest(manifiesto=ruta):
                self.assertIn('"version": "1.7.0"', (RAIZ / ruta).read_text(encoding="utf-8"))

    @unittest.skipUnless(shutil.which("zip") and shutil.which("unzip"), "faltan zip/unzip")
    def test_el_paquete_contiene_exactamente_lo_esperado(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            (tmp / "scripts").mkdir()
            shutil.copy(RAIZ / "scripts" / "build-dist.sh", tmp / "scripts")
            shutil.copy(RAIZ / "LICENSE", tmp)
            shutil.copytree(RAIZ / "skills", tmp / "skills")
            subprocess.run(["bash", str(tmp / "scripts" / "build-dist.sh")],
                           check=True, capture_output=True, cwd=tmp)
            listado = subprocess.run(
                ["unzip", "-Z1", str(tmp / "dist" / "cie11-formulacion-clinica.zip")],
                check=True, capture_output=True, text=True).stdout.split()
        esperado = {"cie11-formulacion-clinica/" + n for n in
                    ["SKILL.md", "flujo.md", "plantilla-caso.md", "LICENSE",
                     "idioma-es.md", "idioma-en.md", "idioma-fr.md"]}
        self.assertEqual(set(listado) - {"cie11-formulacion-clinica/"}, esperado)


class TestIntegracionContinua(unittest.TestCase):
    """El #11 dejó main en rojo porque nada ejecutaba estas pruebas al fusionar."""

    def test_workflow_ejecuta_validador_y_pruebas_con_historial_completo(self):
        ruta = RAIZ / ".github" / "workflows" / "tests.yml"
        self.assertTrue(ruta.exists(), "falta .github/workflows/tests.yml")
        texto = ruta.read_text(encoding="utf-8")
        for orden in ("python3 scripts/validar_idiomas.py", "python3 -m unittest discover -s tests"):
            with self.subTest(orden=orden):
                self.assertIn(orden, texto)
        self.assertIn("pull_request", texto)      # se ejecuta antes de fusionar
        self.assertIn("fetch-depth: 0", texto)    # el commit base debe existir para comparar el español
        self.assertIn("contents: read", texto)    # permisos mínimos


if __name__ == "__main__":
    unittest.main()
