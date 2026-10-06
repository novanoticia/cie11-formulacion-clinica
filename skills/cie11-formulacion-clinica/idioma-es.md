# Catálogo de frases fijas — español (idioma por defecto y referencia)

Cada `##` es una clave. Las frases de este catálogo salen **literales de `flujo.md`**
(la prueba `test_frases_es_son_literales_de_flujo` lo comprueba); las claves
`idioma_no_disponible`, `sugerencia_auditoria`, `puerta1_*` y `glosario` son texto
añadido por la capa de idioma. Los demás idiomas (`idioma-en.md`, `idioma-fr.md`…)
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
El idioma solicitado no está disponible. Idiomas disponibles: {idiomas}.

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
DNI/NIE, número de historia clínica y número de tarjeta sanitaria o de afiliación a la Seguridad Social.

## puerta1_marco_legal
RGPD y LOPDGDD (los datos de salud son una categoría especial de datos).

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
