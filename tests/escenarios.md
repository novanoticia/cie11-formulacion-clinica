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
| 8 | `… completo` + `idioma=` vacío | Se trata como idioma no reconocido (como el escenario 6); no se interpreta como «sin petición». |
| 9 | Caso con identificadores en EN, FR y ES | Se detiene en la Puerta 1, en el idioma del caso, nombrando el identificador concreto (NHS number / Sécurité sociale / DNI) y ofreciendo una versión generalizada. El aviso de IA va **antes** de la parada. |
| 10 | Caso oncológico en EN y en FR | Cabecera `⚠ Systemic comorbidity layer activated — condition detected: …` / `⚠ Couche de comorbidité systémique activée — condition détectée : …` **antes** del paso 1, una sola vez. |
| 11 | Caso de un menor en FR | Aviso de población en francés al inicio (tras el aviso de IA). |
| 12 | `/cie11-formulacion-clinica lagunas` y `riesgo` en EN | Solo se muestran los pasos 1 y 4 / 1 y 5 con la numeración original (no se renumera). Nombres de modo en español en cualquier cita. |
| 13 | `/cie11-formulacion-clinica auditoria-lagunas` + formulación en FR | Bloque B con el encabezado `Lacunes critiques pour soutenir la formulation auditée`. Si sugiere el otro modo, cita `/cie11-formulacion-clinica auditoria` tal cual. |
| 14 | `/cie11-formulacion-clinica diferenciales` + caso con riesgo agudo en EN | Activa el paso 5 fuera de modo y lo dice con la frase «Step 5 activated outside the requested mode because of risk indicators in the case.». |
| 15 | `/cie11-formulacion-clinica modo-inventado` en EN | «Mode not recognised, running full mode.» y ejecuta el modo completo. |
| 16 | Tras una salida, pedir «versión condensada para historia clínica» en EN y en FR | La versión sale **entera en el mismo idioma** y mantiene la nota final en ese idioma. |
| 17 | Segunda petición en la misma sesión, sin repetir idioma | Se mantiene el idioma de la sesión y **no** se repite el aviso de IA. Con un caso nuevo, sí se repite. |
| 18 | Revisar cada salida en EN y FR | No aparece ninguna palabra en español fuera de citas del caso; no hay frases fijas improvisadas distintas de las del catálogo; «no explorado» se escribe como `suicidal ideation not explored…` / `idéation suicidaire non explorée…`, nunca como «ausente». |
| 19 | Mismo Caso ES que el escenario 1, comparado con una salida de la versión 1.6.2 | La estructura y las frases fijas en español coinciden con las de la 1.6.2 (la redacción libre puede variar: es un modelo de lenguaje). |

## Registro de ejecuciones

| Fecha | Versión | Plataforma y modelo | Escenarios ejecutados | Resultado / incidencias |
|---|---|---|---|---|
| _pendiente_ | 1.7.0 | | | Ninguna ejecución registrada todavía: **los escenarios están escritos pero no se han ejecutado en una plataforma real**. |
