# Catálogo de frases fijas — español (idioma por defecto y referencia)

Cada `##` es una clave. Las frases de este catálogo salen **literales de `flujo.md`**
(la prueba `test_frases_es_son_literales_de_flujo` lo comprueba); las claves
`idioma_no_disponible`, `sugerencia_auditoria`, `puerta1_*` y `glosario` son texto
añadido por la capa de idioma. Las claves `lbl_*`, `urg_*`, `recordatorio_riesgo` y
`especificadores_por_determinar` son los rótulos y frases que el flujo prescribe; `sin_datos_documentados`
es texto añadido por la capa de idioma. Los nombres de `categorias` son los oficiales de la OMS
(CIE-11 MMS, versión 2024-01, «Simple Tabulation» en español, inglés y francés), copiados sin retocar. Los demás idiomas (`idioma-en.md`, `idioma-fr.md`…)
deben tener exactamente estas claves, los mismos marcadores `{nombre}` y los mismos
textos entre comillas invertidas. Valídalo con `python3 scripts/validar_idiomas.py`.

## modo_no_reconocido
Modo no reconocido, ejecuto modo completo.

## paso5_fuera_de_modo
Activado paso 5 fuera de modo por señales de riesgo en el caso.

## aviso_poblacion
Este flujo no está calibrado para población infanto-juvenil; las consideraciones siguientes deben revisarse con un especialista en esa área.

## aviso_notas
El material aportado tiene formato de notas; algunos apartados quedarán parcialmente vacíos. Si dispone de un relato más estructurado, el flujo aprovechará mejor la información.

## cabecera_comorbilidad
⚠ *Capa de comorbilidad sistémica activada — condición detectada: {condicion}.*
*Las consideraciones específicas se aplican a lo largo de los pasos posteriores.*

## no_documentado
[no documentado en el caso]

## nota_final
Este documento es un andamio de formulación, no un diagnóstico. La decisión clínica corresponde al profesional responsable del caso. Texto generado con asistencia de IA; requiere revisión humana antes de cualquier uso clínico.

## aviso_ia
**Aviso:** esta respuesta se elabora con asistencia de IA. Es un apoyo para el profesional responsable del caso y debe revisarla un profesional cualificado antes de cualquier decisión clínica.

## versiones_alternativas
*Si lo solicitas, puedo generar adicionalmente:*
- *Versión condensada para historia clínica* (formato de informe: motivo de consulta, antecedentes, exploración, impresión diagnóstica con códigos CIE-11, plan; sin cuestionamiento epistémico ni metacomentarios).
- *Versión sintética para supervisión* (5-10 líneas con hipótesis principales, lagunas críticas y señales de riesgo, para discusión rápida).

## auditoria_solida
La formulación es sólida en sus principales líneas; las consideraciones siguientes son matices, no objeciones de fondo.

## sugerencia_auditoria
Para un análisis de errores específicos de la formulación, invoca `/cie11-formulacion-clinica auditoria`.

## sugerencia_auditoria_lagunas
Para un análisis focalizado en lo que falta, invoca `/cie11-formulacion-clinica auditoria-lagunas`.

## sospecha_desarrollada
Sospecha desarrollada en H1; aquí solo se consigna como elemento que requiere coordinación con el equipo prescriptor

## no_explorado_ideacion
ideación autolítica no explorada en esta entrevista

## idioma_no_disponible
Este idioma no está disponible. Idiomas disponibles: {idiomas}.

## enc_1
Caso estructurado

## enc_2
Hipótesis diagnósticas a considerar

## enc_2a
Hipótesis principales (con especificadores cuando proceda)

## enc_2b
Hipótesis a vigilar (si procede)

## enc_3
Diagnóstico diferencial obligatorio

## enc_4
Lagunas de información y plan de exploración

## enc_4a
Lagunas detectadas

## enc_4b
Plan de exploración priorizado

## enc_5
Señales de riesgo

## enc_6
Cuestionamiento epistémico

## enc_A
Detección de errores específicos

## enc_B
Lagunas críticas para sostener la formulación auditada

## enc_nota_final
Nota final

## puerta1_identificadores
Por ejemplo, DNI/NIE, número de historia clínica y número de tarjeta sanitaria o de afiliación a la Seguridad Social, u otros identificadores equivalentes de la jurisdicción del clínico.

## puerta1_marco_legal
Por ejemplo, RGPD y LOPDGDD, o la normativa de protección de datos que sea aplicable (los datos de salud son una categoría especial de datos).

## glosario
- andamio de formulación
- clínico responsable del caso
- hipótesis principales
- hipótesis a vigilar
- diagnóstico diferencial
- lagunas de información
- plan de exploración
- señales de riesgo
- cuestionamiento epistémico
- pseudonimización
- identificadores directos e indirectos
- no documentado en el caso
- no explorado
- capa de comorbilidad sistémica
- CIE-11
- puerta de entrada
- mediación clínica

## lbl_3_organicas
Causas orgánicas

## lbl_3_sustancias
Sustancias y medicación

## lbl_3_psiquiatricos
Otros trastornos psiquiátricos primarios

## lbl_3_reaccion
Reacción a circunstancias vitales

## lbl_4b_consulta
Para próxima consulta (entrevista clínica)

## lbl_4b_pruebas
Pruebas complementarias y exploración objetiva

## lbl_4b_fuentes
Información de fuentes externas

## urg_necesaria
necesaria antes de cerrar formulación

## urg_util
útil en próximas semanas

## urg_opcional
opcional si persiste duda

## lbl_5_explicitas
Señales explícitas

## lbl_5_implicitas
Señales implícitas o subumbrales

## lbl_5_protectores
Factores protectores

## recordatorio_riesgo
Recordatorio: si el caso describe riesgo agudo o inminente, este flujo no sustituye los protocolos de evaluación de riesgo del centro ni la valoración clínica directa.

## especificadores_por_determinar
especificadores por determinar tras ampliar exploración

## sin_datos_documentados
sin datos documentados en el caso

## categorias
- 6A60 | Trastorno bipolar de tipo I
- 6A61 | Trastorno bipolar de tipo II
- 6A70 | Trastorno depresivo de episodio único
- 6A71 | Trastorno depresivo recurrente
- 6A72 | Trastorno distímico
- 6A73 | Trastorno mixto de depresión y ansiedad
- 6B00 | Trastorno de ansiedad generalizada
- 6B04 | Trastorno de ansiedad social
- 6B40 | Trastorno de estrés postraumático
- 6B43 | Trastorno de adaptación
- 6C40 | Trastornos debidos al uso de alcohol
- 6C40.1 | Patrón nocivo de uso de alcohol
- 6E60 | Síndrome de neurodesarrollo secundario
- 6E61 | Síndrome psicótico secundario
- 6E62 | Síndrome secundario del estado del ánimo
- 6E63 | Síndrome de ansiedad secundario

## lbl_1_demograficos
Datos demográficos relevantes

## lbl_1_motivo
Motivo de consulta

## lbl_1_cronologia
Cronología del cuadro actual

## lbl_1_sintomas
Síntomas referidos

## lbl_1_ant_psiquiatricos
Antecedentes psiquiátricos personales

## lbl_1_ant_medicos
Antecedentes médicos y medicación actual

## lbl_1_sustancias
Consumo de sustancias

## lbl_1_ant_familiares
Antecedentes familiares

## lbl_1_psicosocial
Situación psicosocial

## lbl_1_exploracion
Exploración psicopatológica

## lbl_1_pendientes
Datos pendientes de recabar

## lbl_1_referido
Referido por el paciente

## lbl_1_observado
Observado por el clínico

## lbl_2_a_favor
A favor

## lbl_2_en_contra
En contra / matiza

## lbl_2_especificadores
Especificadores aplicables

## lbl_4a_marcadas
Marcadas por el clínico

## lbl_4a_detectadas
Detectadas por el flujo

## lbl_prioritario
Prioritario

## lbl_5_no_exploradas
Señales no exploradas en la entrevista (no documentado ≠ ausente)

## lbl_hc_antecedentes
Antecedentes

## lbl_hc_exploracion
Exploración

## lbl_hc_impresion
Impresión diagnóstica

## lbl_hc_plan
Plan

## lbl_version_hc
Versión condensada para historia clínica

## lbl_version_supervision
Versión sintética para supervisión
