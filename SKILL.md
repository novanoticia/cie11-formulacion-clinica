---
name: cie11-formulacion-clinica
description: Apoya a clínicos (psiquiatría, psicología clínica) a estructurar la formulación de casos ya entrevistados, usando CIE-11 como referencia diagnóstica primaria. **Trigger principal y obligatorio: "/cie11-formulacion-clinica"**. Activa este skill SIEMPRE que el usuario escriba ese comando exacto, en cualquier contexto. Soporta modos: completo (default), diferenciales, lagunas, riesgo, auditoria, auditoria-lagunas. Activa también el skill cuando el usuario pida explícitamente apoyo a la formulación clínica de un caso, organizar hipótesis diagnósticas razonadas, identificar diferenciales obligatorios, detectar lagunas o cuestionar epistemológicamente una formulación, mediante expresiones como "formula este caso", "estructura este caso", "qué diferenciales debería considerar" o "audita esta formulación clínica". NO se activa para autodiagnóstico, autodescripciones del propio usuario sin mediación clínica, ni cuando el caso contenga datos identificables de pacientes reales.
author: Pablo
homepage: https://mindandhealth.org
repository: https://github.com/novanoticia
license: CC BY 4.0
---

# Formulación Clínica (CIE-11)

**Autor:** Pablo
**Web:** [mindandhealth.org](https://mindandhealth.org) · [github.com/novanoticia](https://github.com/novanoticia)
**Licencia:** Creative Commons Atribución 4.0 Internacional (CC BY 4.0)
**Diseño asistido por IA (Claude, Anthropic). El diseño, las decisiones arquitectónicas y la dirección son responsabilidad del autor.**

---

Skill de apoyo a la formulación de casos clínicos basado en **CIE-11** como referencia diagnóstica primaria. **No diagnostica.** Genera un andamio de hipótesis a contrastar por el clínico responsable.

## Por qué CIE-11

- Marco oficial en España y la mayoría de sistemas sanitarios públicos.
- Publicado por la OMS bajo licencia CC BY-ND, con un régimen de uso mucho más amigable que el DSM-5-TR (propiedad APA).
- Permite distribución y referencia de categorías y códigos sin los riesgos legales asociados al manual estadounidense.
- Incluye dimensión transcultural y un capítulo de salud mental (06) más actualizado que el equivalente del DSM en varias áreas.

El skill no transcribe criterios de ninguno de los dos manuales. La razón ya no es solo legal: convertir el razonamiento clínico en checklist desactiva la utilidad del juicio profesional.

## Para qué sirve

Recibe un caso ya entrevistado por un profesional habilitado y devuelve, en este orden (modo completo):

1. Caso estructurado en formato consistente.
2. Hipótesis diagnósticas a considerar (códigos CIE-11; DSM-5-TR solo si aporta matiz), separando hipótesis principales de hipótesis a vigilar, con especificadores cuando proceda.
3. Diagnóstico diferencial obligatorio (orgánico, sustancias, otros primarios, reactivo).
4. Lagunas de información con plan de exploración priorizado.
5. Señales de riesgo a vigilar.
6. Cuestionamiento epistémico (2-3 ángulos seleccionados).

## Modos de invocación

El skill admite seis modos. La sintaxis es `/cie11-formulacion-clinica [modo]` seguido del caso.

- **`completo`** (default). Ejecuta los seis pasos.
- **`diferenciales`**. Solo pasos 1, 2 y 3.
- **`lagunas`**. Solo pasos 1 y 4.
- **`riesgo`**. Solo pasos 1 y 5.
- **`auditoria`**. Pasos 1, 6, y bloque A (detección de errores específicos en la formulación auditada). Para someter una formulación a crítica desde fuera.
- **`auditoria-lagunas`**. Paso 1 y bloque B (lagunas críticas para sostener la formulación auditada). Más operativo, más rápido. Para evaluar qué falta sin desplegar cuestionamiento epistémico.

El paso 1 (caso estructurado) se ejecuta siempre. La nota final es obligatoria en todos los modos. Si el caso muestra señales de riesgo agudo, el flujo activa el paso 5 fuera de modo aunque no se haya pedido. La seguridad clínica está por encima del modo elegido.

Los dos modos de auditoría se diseñan para invocarse por separado, no juntos. Si el clínico necesita ambos análisis, se ejecutan en dos pasadas. Cada modo sugiere el otro al final cuando detecta que aporta valor complementario.

## Capacidades (acumuladas hasta v1.5)

- **Detección de identificadores indirectos** con regla estructural (localidad concreta + cargo único + dato familiar específico = identificación automática). Cuando se detecta, el flujo ofrece una versión generalizada del caso para confirmación, en lugar de limitarse a listar cambios.
- **Variantes de entrada.** Procesa tres formatos: caso ya estructurado (no reescribe innecesariamente), prosa narrativa (reorganiza al esquema de 11 apartados), notas en bruto o transcripción (extrae lo posible y marca lagunas con generosidad).
- **Capa transversal de comorbilidad sistémica** con cabecera explícita en la salida cuando se activa. Aplica consideraciones específicas en pasos 2-6: descarte activo de cuadro secundario, ampliación del diferencial iatrogénico con peso clínico, lectura "respuesta adaptativa a enfermedad médica" como ángulo obligatorio en paso 6 (estructura "1 obligatorio + 1-2 a elección"). Aplica regla de parsimonia clínica.
- **Regla anti-redundancia entre pasos 2 y 3.** Cuando una hipótesis principal coincide con una sospecha del paso 3, no se duplica desarrollo: se trata en el paso donde aporta más y se referencia en el otro.
- **Modos de auditoría diferenciados.** `auditoria` se centra en errores específicos de la formulación (descartes prematuros, diferenciales no considerados, descartes orgánicos insuficientes, supuestos no fundamentados, saltos lógicos). `auditoria-lagunas` se centra en qué falta para sostener la formulación. Cada modo hace una cosa y la hace bien; sugieren el otro cuando es complementario.
- **Versiones alternativas opcionales.** Tras la salida principal, ofrece (no genera automáticamente) versión condensada para historia clínica y versión sintética para supervisión.

## Para qué NO sirve

- Autodiagnóstico o autodescripción no mediada por clínico.
- Reproducción literal de criterios diagnósticos de la CIE-11 ni del DSM-5-TR.
- Diagnóstico definitivo, prescripción farmacológica, decisiones de tratamiento.
- Sustitución del juicio clínico, de la entrevista directa o de los protocolos del centro.
- Procesamiento de datos identificables de pacientes (RGPD, datos de salud categoría especial). Trabajar siempre con casos pseudonimizados.

## Cómo usarlo

1. Lee `flujo.md` antes de procesar cualquier caso.
2. Detecta si el usuario ha indicado un modo; si no, asume `completo`.
3. Verifica las dos puertas de entrada: pseudonimización (con detección de identificadores indirectos) y mediación clínica.
4. Detecta tipo de entrada (estructurada / prosa / notas) y ajusta paso 1.
5. Detecta si la capa de comorbilidad sistémica debe activarse.
6. Sigue los pasos correspondientes al modo, en orden, sin saltar ninguno.
7. Devuelve la salida con el formato y los encabezados especificados, incluida la nota final obligatoria y el bloque de versiones alternativas opcionales.

## Archivos del skill

- `SKILL.md` — este descriptor.
- `flujo.md` — flujo de razonamiento de seis pasos con reglas duras transversales y un caso resuelto canónico como apéndice de referencia.
- `plantilla-caso.md` — formato esperado de entrada como referencia para el clínico.
- `LICENSE` — texto íntegro de la licencia CC BY-NC-SA 4.0 y atribución sugerida.

## Limitaciones conocidas

- Calibrado para población adulta. No usar en infanto-juvenil sin revisión específica.
- No calibrado para urgencias ni para evaluación de riesgo agudo.
- No reemplaza pruebas estandarizadas, escalas validadas ni exploración complementaria.
- Pendiente de validación con casos reales por clínicos habilitados antes de uso en consulta.

## Instalación

Si recibes el skill empaquetado como `cie11-formulacion-clinica.skill`:

```bash
mkdir -p ~/.claude/skills/cie11-formulacion-clinica/
unzip cie11-formulacion-clinica.skill -d ~/.claude/skills/cie11-formulacion-clinica/
```

Después, invocar con `/cie11-formulacion-clinica [modo]` en una conversación con un entorno compatible con skills.

## Versión

v1.5 — división del modo `auditoria` en dos modos diferenciados (`auditoria` para errores y `auditoria-lagunas` para lagunas). Cada modo hace una sola cosa, evitando que el modelo se incline hacia uno de los sub-bloques y deje el otro pobre. Sigue pendiente de validación con casos reales por clínicos habilitados.

## Historial de versiones

- **v1.0** — primer borrador funcional con seis pasos.
- **v1.1** — referencia primaria CIE-11, especificadores en hipótesis, plan de exploración priorizado.
- **v1.2** — modos de invocación con salvaguarda de seguridad clínica, ejemplo canónico como apéndice del flujo.
- **v1.3** — identificadores indirectos, variantes de entrada, capa de comorbilidad sistémica, versiones exportables.
- **v1.4** — refinamientos tras testeo: cabecera de comorbilidad, regla anti-redundancia, estructura "1+1-2" en paso 6, salida pre-pseudonimización, regla estructural en Puerta 1, bloque de auditoría ampliado.
- **v1.5** — `auditoria` partido en `auditoria` (errores) y `auditoria-lagunas` (qué falta). Sugerencia cruzada entre ambos.
