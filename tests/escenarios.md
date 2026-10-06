# Escenarios manuales de la capa multiidioma

Las pruebas automáticas (`python3 -m unittest discover -s tests`) comprueban los catálogos y que el español no cambia, pero **no pueden comprobar qué hace el modelo** con ellos. Estos escenarios se ejecutan a mano en una conversación con el skill instalado, antes de cada versión que toque `flujo.md` o los catálogos. Usa solo casos ficticios.

Cómo usarlos: pega la entrada, comprueba cada punto de «Debe cumplirse» y anota fecha, plataforma, modelo y resultado en la última tabla.

## Casos ficticios de partida

- **Caso ES** (adulto, sin comorbilidad): *Mujer, 41 años, administrativa. Consulta por «cansancio de meses». Anhedonia, despertar precoz, pérdida de apetito desde hace 5 meses. Sin antecedentes psiquiátricos. Ideación autolítica no explorada.*
- **Caso EN** (equivalente): *Woman, 41, administrative worker. Presents with "months of exhaustion". Anhedonia, early waking, reduced appetite for 5 months. No psychiatric history. Suicidal ideation not explored.*
- **Caso FR** (equivalente): *Femme, 41 ans, employée administrative. Consulte pour « une fatigue depuis des mois ». Anhédonie, réveil précoce, perte d'appétit depuis 5 mois. Pas d'antécédents psychiatriques. Idéation suicidaire non explorée.*
- **Caso oncológico** (activa la capa de comorbilidad): añade al caso «en tratamiento con hormonoterapia por cáncer de mama» en el idioma que toque.
- **Caso con identificadores** (para la Puerta 1): añade «NHS number 943 476 5919» (EN), «numéro de Sécurité sociale 2 84 12 75 123 456 78» (FR) o «DNI 12345678Z» (ES). Son números inventados.

## Escenarios

| # | Entrada | Debe cumplirse |
|---|---|---|
| 1 | `/cie11-formulacion-clinica` + Caso ES | Salida entera en español; aviso de IA en español **solo** (una línea); encabezados `1.`…`6.` como siempre; nota final en español. |
| 2 | `/cie11-formulacion-clinica` + Caso EN | Todo en inglés, incluidos encabezados (`Structured case`, `Risk indicators`…), nota final y bloque de versiones alternativas. Aviso de IA en inglés solo. Códigos CIE-11 sin cambiar (se pueden llamar ICD-11 en prosa). |
| 3 | `/cie11-formulacion-clinica` + Caso FR | Todo en francés (`Cas structuré`, `Indicateurs de risque`…). Aviso en francés solo. |
| 4 | `/cie11-formulacion-clinica completo fr` + Caso ES | Gana la petición explícita: salida en francés. Las citas textuales del caso quedan en español entre comillas; es la única mezcla admitida. |
| 5 | `… completo EN`, `… completo en-US`, `… completo fr_FR.UTF-8` | Las tres formas se normalizan a `en`/`en`/`fr`. |
| 6 | `… completo de` + Caso EN | No falla ni inventa una traducción. Aviso de IA **trilingüe** primero, luego la frase «The requested language is not available. Available languages: …» en inglés, y salida en inglés. |
| 7 | Solo `/cie11-formulacion-clinica` (sin caso) | No hay base para decidir idioma: aviso de IA trilingüe, y pide el caso. |
| 8 | `/cie11-formulacion-clinica completo En consulta refiere…` y `… completo De 38 años…` (caso en español, todo en la primera línea) | «En» y «De» **no** son peticiones de idioma: salida en español, sin aviso de idioma no disponible. |
| 8b | Solo `/cie11-formulacion-clinica en` + caso en EN en la línea siguiente | El idioma es `en` y el modo `completo`; **no** aparece «Modo no reconocido». |
| 8c | Caso escrito en portugués, sin petición de idioma | Aviso de IA trilingüe, frase «Este idioma no está disponible. Idiomas disponibles: español (es), inglés (en), francés (fr).» y salida en español. |
| 9 | Caso con identificadores en EN, FR y ES | Se detiene en la Puerta 1, en el idioma del caso, nombrando el identificador concreto (NHS number / Sécurité sociale / DNI) y ofreciendo una versión generalizada. El aviso de IA va **antes** de la parada. |
| 10 | Caso oncológico en EN y en FR | Cabecera `⚠ Systemic comorbidity layer activated — condition detected: …` / `⚠ Couche de comorbidité systémique activée — condition détectée : …` **antes** del paso 1, una sola vez. |
| 11 | Caso de un menor en FR | Aviso de población en francés al inicio (tras el aviso de IA). |
| 12 | `/cie11-formulacion-clinica lagunas` y `riesgo` en EN | Solo se muestran los pasos 1 y 4 / 1 y 5 con la numeración original (no se renumera). Nombres de modo en español en cualquier cita. |
| 13 | `/cie11-formulacion-clinica auditoria-lagunas` + formulación en FR | Bloque B con el encabezado `Lacunes critiques pour soutenir la formulation auditée`. Si sugiere el otro modo, cita `/cie11-formulacion-clinica auditoria` tal cual. |
| 14 | `/cie11-formulacion-clinica diferenciales` + caso con riesgo agudo en EN | Activa el paso 5 fuera de modo y lo dice con la frase «Step 5 activated outside the requested mode because of risk indicators in the case.». |
| 15 | `/cie11-formulacion-clinica modo-inventado` en EN | «Mode not recognised, running full mode.» y ejecuta el modo completo. |
| 16 | Tras una salida, pedir «versión condensada para historia clínica» en EN y en FR | La versión sale **entera en el mismo idioma** y mantiene la nota final en ese idioma. |
| 17 | Segunda petición en la misma sesión, sin repetir idioma | Se mantiene el idioma de la sesión y **no** se repite el aviso de IA. Con un caso nuevo, o si el clínico cambia el idioma («ahora en francés»), el aviso se repite en el idioma nuevo. |
| 18 | Revisar cada salida en EN y FR | No aparece ninguna palabra en español fuera de citas del caso; no hay frases fijas improvisadas distintas de las del catálogo; «no explorado» se escribe como `suicidal ideation not explored…` / `idéation suicidaire non explorée…`, nunca como «ausente». |
| 19 | Mismo Caso ES que el escenario 1, comparado con una salida de la versión 1.6.2 | La estructura y las frases fijas en español coinciden con las de la 1.6.2 (la redacción libre puede variar: es un modelo de lenguaje). |

## Registro de ejecuciones

| Fecha | Versión | Plataforma y modelo | Escenarios ejecutados | Resultado / incidencias |
|---|---|---|---|---|
| 2026-10-06 | 1.7.0 | **Simulación con subagentes de Claude** (contexto limpio, solo el paquete instalado; **no es una plataforma real**) | 1, 2, 3, 6, 7, 8, 8b, 8c, 9 | Cumplidos según lo diseñado. Idioma, aviso de IA (uno solo, o trilingüe en 6, 7 y 8c), encabezados, nota final, marcador de laguna y Puerta 1 correctos; sin mezcla de idiomas; 27-29 de 31 claves del catálogo usadas literalmente. Incidencias: ver «Hallazgos de la simulación» más abajo. |
| _pendiente_ | 1.7.0 | Plataforma real (Claude.ai, ChatGPT, Mistral…) | todos | **Ninguna ejecución en plataforma real registrada.** Las simulaciones no sustituyen esta prueba: los agentes leyeron todos los ficheros del paquete, y una plataforma puede cargar solo `SKILL.md` y no los `idioma-*.md`. |

## Hallazgos de la simulación (2026-10-06)

Instrucciones que los agentes tuvieron que resolver por su cuenta (no son fallos de la capa de idioma, pero afectan a la coherencia entre ejecuciones):

- **«Comando sin caso» y paradas de las puertas:** el flujo no dice si llevan nota final ni versiones alternativas. Todos los agentes pusieron la nota final y omitieron las versiones, y añadieron por su cuenta recordatorios sobre modos, idioma y pseudonimización.
- **Aviso de notas (Tipo B/C):** con el mismo caso breve y telegráfico, unas ejecuciones lo trataron como Tipo C (con `aviso_notas`) y otras como Tipo B. Ambigüedad previa del flujo («Ante duda, asume B» frente a «frases sueltas → C»).
- **Códigos CIE-11:** todos los agentes sustituyeron de memoria los del apéndice (6A60.1, 6E60-6E61) por 6A61 y 6E62. No está verificado contra la OMS (tarea aparte).
- **Frases sin clave:** «ninguna señal explícita documentada» se improvisó con redacciones distintas; el título de 2a/2b se abrevió en una ejecución (escenario 6).
- **Vocabulario del caso:** en la salida en español del caso en portugués se coló «anedonia».
- **Nombres de categoría CIE-11:** un agente usó nombres franceses sabiendo que no estaba seguro de la traducción oficial, en lugar de código y nombre inglés.
- **No simulados:** 4, 5, 10-19 (todo lo que no es la primera respuesta de una sesión).
