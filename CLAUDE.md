# CLAUDE.md — reglas para editar este repositorio

Este repositorio es un **skill de instrucciones** (Markdown), no un programa. Las reglas de abajo protegen el español original y la capa multiidioma.

## Idiomas

- **No escribas frases fijas nuevas en `flujo.md`** (avisos, cabeceras, notas, encabezados, sugerencias): añádelas como clave nueva en `skills/cie11-formulacion-clinica/idioma-es.md` y tradúcelas en `idioma-en.md` e `idioma-fr.md`, con los mismos marcadores `{nombre}` y los mismos textos entre comillas invertidas. Una clave por frase completa; no compongas frases con trozos traducidos.
- **El español es la referencia.** Sus frases son literales de `flujo.md`; no las reescribas en el catálogo. El aviso de IA de cada idioma es la línea ya aprobada del bloque trilingüe de `flujo.md`.
- **No se traducen** el trigger, los nombres de modo, los códigos CIE-11, los nombres de fichero ni la numeración de pasos.
- **Todo añadido** a `flujo.md` o `SKILL.md` que sirva a la capa de idioma va entre `<!-- i18n:inicio -->` y `<!-- i18n:fin -->`. Las únicas líneas del español original que se pueden modificar están listadas en `REEMPLAZOS` de `tests/test_idiomas.py`.
- **No toques el frontmatter de `SKILL.md`**: su conjunto de claves es cerrado (ChatGPT, claude.ai y la Skills API fallan con error duro ante una clave desconocida) y la `description` debe quedar por debajo de 500 caracteres (Mistral).
- Las traducciones las redacta una IA: indícalo siempre y no las presentes como revisadas.
- **Revisión humana obligatoria del diff** de cualquier cambio dentro de un bloque `i18n` o de un catálogo que toque reglas clínicas o de seguridad (Puertas 1 y 2, «no documentado ≠ ausente», paso 5, aviso de población, nota final, aviso de IA). Las pruebas solo comprueban la forma de esos textos, no su sentido clínico: un bloque `i18n` puede contener cualquier instrucción y las pruebas lo ignoran.
- Las capas de idioma no se dan por verificadas hasta ejecutar los escenarios de `tests/escenarios.md` en una plataforma real y anotarlo en su tabla de registro.

## Comprobar antes de entregar

```bash
python3 scripts/validar_idiomas.py        # los catálogos están completos y coherentes
python3 -m unittest discover -s tests -v  # validador, catálogos, español invariante y paquete
```

GitHub ejecuta esas mismas dos comprobaciones en cada pull request (`.github/workflows/tests.yml`); si fallan, no fusiones. Para que GitHub lo impida de verdad hay que activar en el repositorio una protección de la rama `main` que exija la comprobación «Pruebas» (Settings → Branches); sin ella, el aviso en rojo no bloquea. El workflow existe porque el PR #11 se fusionó sin pasar por las pruebas y dejó `main` en rojo.

Si subes la versión, cámbiala a la vez en `plugin.json`, `.claude-plugin/plugin.json` y `.claude-plugin/marketplace.json`, y añade la entrada al `CHANGELOG.md`.

## Añadir un idioma

Copia `idioma-es.md` como `idioma-<xx>.md`, traduce los valores (no las claves) y ejecuta el validador: dice qué falta. No hay que tocar `build-dist.sh`: el paquete incluye todos los `*.md` de la carpeta del skill.
