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
| 2026-10-06 | 1.7.0 (con los arreglos de los hallazgos 1, 4 y 5) | **Simulación con subagentes de Claude**, ronda 2 (**no es una plataforma real**) | 2 y 3 repetidos; 4, 5, 10, 11, 12, 13, 14, 15; y los de varios turnos 16 (versión HC en inglés y versión de supervisión en francés) y 17 (cambio a francés en la misma sesión) | Cumplidos según lo diseñado: aviso único y primero en el idioma correcto; encabezados completos (2a/2b sin abreviar); `sin_datos_documentados` usada; petición `fr` y `fr_FR.UTF-8` normalizadas; cabecera de comorbilidad una sola vez y antes del paso 1 (10); aviso de población tras el de IA (11); `riesgo` solo con pasos 1 y 5 (12); bloque B con su encabezado (13); **riesgo agudo fuera de modo activado, sin proponer conducta y con el recordatorio de riesgo (14)**; modo inventado (15); sin repetir el aviso al pedir una versión (16) y aviso nuevo en francés al cambiar de idioma (17). 0 marcadores de laguna de otro idioma. Incidencias: ver «Hallazgos de la ronda 2». |
| 2026-10-06 | 1.7.0 (con `categorias` y las 26 claves `lbl_*`) | **Simulación con subagentes de Claude**, ronda 3 (**no es una plataforma real**) | Caso ES, caso EN, caso FR completos y la versión para historia clínica en francés | **Arreglos confirmados en la práctica.** Los nombres de categoría salen con el nombre oficial de la OMS de su idioma (es 5/5, en 4/4, fr 6 de 7), sin nombres ingleses dentro de prosa francesa; la sigla es la de cada idioma (CIE-11, ICD-11, CIM-11); los 39 rótulos `lbl_*`/`urg_*` salen literales en las tres; la versión para historia clínica en francés sale íntegra en francés con `lbl_hc_*`. Incidencias: ver «Hallazgos de la ronda 3». |
| _pendiente_ | 1.7.0 | Plataforma real (Claude.ai, ChatGPT, Mistral…) | todos | **Ninguna ejecución en plataforma real registrada.** Las simulaciones no sustituyen esta prueba: los agentes leyeron todos los ficheros del paquete, y una plataforma puede cargar solo `SKILL.md` y no los `idioma-*.md`. |

## Hallazgos de la simulación (2026-10-06)

Instrucciones que los agentes tuvieron que resolver por su cuenta (no son fallos de la capa de idioma, pero afectan a la coherencia entre ejecuciones):

- **«Comando sin caso» y paradas de las puertas:** el flujo no dice si llevan nota final ni versiones alternativas. Todos los agentes pusieron la nota final y omitieron las versiones, y añadieron por su cuenta recordatorios sobre modos, idioma y pseudonimización. *Corregido en `flujo.md` §0.0 (respuestas de parada); pendiente de re-simular.*
- **Aviso de notas (Tipo B/C):** con el mismo caso breve y telegráfico, unas ejecuciones lo trataron como Tipo C (con `aviso_notas`) y otras como Tipo B. Ambigüedad previa del flujo («Ante duda, asume B» frente a «frases sueltas → C»). *Resuelto en 1.7.0 con un criterio de recuento en §0.6 (más de la mitad de las oraciones sin verbo conjugado → Tipo C); pendiente de re-simular.*
- **Códigos CIE-11:** todos los agentes sustituyeron de memoria los del apéndice (6A60.1, 6E60-6E61) por 6A61 y 6E62. No está verificado contra la OMS (tarea aparte). *Resuelto en el PR #11, que los corrigió en el apéndice tras verificarlos contra la OMS.*
- **Frases sin clave:** «ninguna señal explícita documentada» se improvisó con redacciones distintas; el título de 2a/2b se abrevió en una ejecución (escenario 6). *Corregido: clave `sin_datos_documentados` y regla de encabezados sin abreviar; pendiente de re-simular.*
- **Vocabulario del caso:** en la salida en español del caso en portugués se coló «anedonia».
- **Nombres de categoría CIE-11:** un agente usó nombres franceses sabiendo que no estaba seguro de la traducción oficial, en lugar de código y nombre inglés. *Corregido: la regla pasa a «ante la menor duda, nunca traduzcas el nombre»; pendiente de re-simular.*
- **No simulados en la ronda 1:** 4, 5, 10-19. La ronda 2 los cubrió salvo el 19 (comparar con una salida de la 1.6.2).

## Hallazgos de la ronda 2 (2026-10-06)

Los agentes tuvieron que resolver por su cuenta, o produjeron, lo siguiente:

- **Nombre de la clasificación en francés** *(resuelto: regla de la sigla según el glosario; pendiente de re-simular)*: «CIE-11» (sigla española) aparece en 4 de 7 salidas francesas en lugar de «CIM-11»; en inglés es siempre «ICD-11». La regla «no se traducen los códigos CIE-11» se lee como «deja la cadena CIE-11». Ambigüedad de redacción.
- **Nombres de categoría CIE-11 en inglés dentro de prosa francesa** *(resuelto: clave `categorias` con los nombres oficiales de la OMS; pendiente de re-simular)* (6 de 7 salidas francesas, p. ej. «**H1 — Single episode depressive disorder** (CIE-11 6A70)»): consecuencia directa de la regla «ante la menor duda, nunca traduzcas el nombre». Evita inventar traducciones, pero rompe «un solo idioma en toda la salida», también en la versión para historia clínica.
- **Rótulos sin clave en el catálogo** *(resuelto: 26 claves `lbl_*`; pendiente de re-simular)*, traducidos por cada agente a su manera: las 11 etiquetas del paso 1, el grupo «no explorado» del paso 5, «A favor / En contra / matiza», «Prioritario», «Gravedad», «Especificadores», encabezados de las versiones para historia clínica y supervisión.
- **Aviso de notas (Tipo B/C):** con casos telegráficos casi idénticos, unas ejecuciones lo muestran y otras no (ambigüedad previa del flujo). *Resuelto en 1.7.0 con un criterio de recuento en §0.6; pendiente de re-simular.*
- **Colocación sin definir:** dónde va la frase de «paso 5 fuera de modo» y el aviso de notas respecto a la cabecera ⚠.
- **`sospecha_desarrollada`:** un agente reordenó las hipótesis (la secundaria como H1) para poder usar la frase literal «Sospecha desarrollada en H1»; la frase presupone una jerarquía que el flujo dice no establecer todavía.
- **Códigos CIE-11 del apéndice:** los agentes usaron 6E62 y 6A61 (ahora coinciden con el apéndice corregido en el PR #11). Los demás códigos (6A70, 6A72, 6B43, 6B00…) los asignaron de memoria; no se han verificado.
- **Dato clínico no presente en el caso:** en la salida 4 aparecen «transición perimenopáusica» y «pérdida de peso» como cosas a explorar «sin datos documentados» (no como hechos del caso). Correcto, pero conviene vigilarlo.

## Hallazgos de la ronda 3 (2026-10-06)

- **Un nombre oficial parafraseado** (1 de 7 en francés): 6A73 salió como «trouble mixte anxieux et dépressif» en lugar de «Trouble anxieux et dépressif mixte». La regla dice «usa exactamente el nombre de esa lista»; un modelo puede parafrasear igualmente. *Reforzado: «copiado letra por letra y con el mismo orden de palabras»; pendiente de re-simular.*
- **Aviso de notas (Tipo B/C), con el mismo caso en tres idiomas:** el español y el inglés lo trataron como Tipo C (con `aviso_notas`) y el francés como Tipo B (sin él). Es la ambigüedad previa del flujo («Ante duda, asume B» frente a «frases sueltas → C») y es el único hallazgo recurrente que sigue abierto. Corregirlo exige una regla determinista en el español original (no en la capa de idioma): decisión del autor. *Resuelto en 1.7.0 con un criterio de recuento en §0.6; pendiente de re-simular.*
- **Rótulo todavía sin clave:** en la versión para historia clínica, el agente puso «Tableau actuel» (la enfermedad actual) por su cuenta. *Resuelto: clave `lbl_hc_enfermedad_actual`.*
- **Hipótesis mínimas:** los tres agentes mantuvieron 6E62 como H2 con base débil para llegar al mínimo de 2 («entre 2 y 4» frente a la regla anti-inflación). Contradicción previa del flujo. *Resuelto: «entre 1 y 4; solo las que los datos sostienen»; pendiente de re-simular.*

