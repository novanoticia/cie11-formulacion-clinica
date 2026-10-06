# CHANGELOG

Todos los cambios notables de este proyecto se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y el proyecto se adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [1.7.0] — 2026-10-06

Función nueva compatible: **el skill responde en español, inglés o francés**. **No cambia el razonamiento clínico**: ni los pasos, ni las puertas, ni los modos. El español sigue igual: sus ficheros solo cambian de forma aditiva (bloques marcados con `<!-- i18n:inicio -->` / `<!-- i18n:fin -->`) y en dos líneas que se indican abajo; una prueba lo comprueba contra el hash de la versión 1.6.2.

### Añadido

- **Selección de idioma** (`flujo.md` §0.0): petición explícita (una palabra tras el modo, o en lenguaje natural; acepta `EN`, `en-US`, `fr_FR`), idioma del caso, español. Se mantiene durante la sesión. Un idioma no disponible no da error: se responde en el idioma del caso (o en español) y se avisa.
- **Catálogos de frases fijas** `idioma-es.md`, `idioma-en.md` e `idioma-fr.md` (31 claves cada uno: avisos, cabeceras, nota final, encabezados de los pasos, versiones alternativas, ejemplos de identificadores y marco legal de la Puerta 1 por país, y glosario de 17 términos). Añadir un idioma es soltar un `idioma-<xx>.md`.
- **Validador** `scripts/validar_idiomas.py` (mismas claves, marcadores con nombre, textos de máquina idénticos, sin vacíos, glosario con el mismo número de entradas) y **pruebas** en `tests/` (`python3 -m unittest discover -s tests`), con la línea base del español en `tests/linea_base.json`.
- `README.en.md` y `README.fr.md` (versiones breves), sección «Idiomas» en el README y `CLAUDE.md` con las reglas para editar el repositorio.

### Cambiado

- **Aviso de asistencia de IA:** pasa de ser siempre trilingüe a mostrarse **una sola vez, en el idioma elegido** (clave `aviso_ia`). El bloque trilingüe se conserva como respaldo si el clínico pide un idioma que no existe o no hay base para decidir el idioma. Los textos en inglés y francés son los mismos ya aprobados en la 1.6.2.
- **Líneas del español original modificadas:** la viñeta «Redacción fija» del aviso de IA en `flujo.md` y el paso 2 de «Cómo usarlo» en `SKILL.md`. Nada más.
- Sugerencia cruzada entre `auditoria` y `auditoria-lagunas`: ahora tiene frase fija en los dos sentidos.
- Versión 1.7.0 en `plugin.json`, `.claude-plugin/plugin.json` y `.claude-plugin/marketplace.json`.

### Limitaciones conocidas

- **Las traducciones al inglés y al francés las ha redactado una IA y no las ha revisado una persona nativa ni un clínico.** Requieren revisión humana antes de cualquier uso profesional.
- La guía PDF (v1.5), el CHANGELOG, SECURITY y el README completo siguen solo en español.
- La salida la genera un modelo de lenguaje: las frases fijas salen del catálogo, pero el resto del texto puede variar entre ejecuciones.

---

## [1.6.2] — 2026-09-29

Cambio pequeño de comportamiento por cumplimiento normativo: el skill se usa en un ámbito de alto riesgo (salud mental, diagnóstico), donde la política del directorio de plugins de Claude exige informar de que se usa IA al comienzo de cada sesión. **No cambia el razonamiento clínico**: ni los pasos, ni las puertas, ni los modos, ni la nota final.

### Añadido

- **Aviso de asistencia de IA al inicio de la primera respuesta de cada sesión**, con redacción fija **en español, inglés y francés**, siempre juntos, y antes de cualquier otra cosa, incluso si la respuesta es solo una parada por la Puerta 1 o la Puerta 2. Se muestra una vez por sesión, o de nuevo si el clínico presenta un caso nuevo. No sustituye la nota final, que sigue siendo obligatoria. Detalle en `flujo.md` y paso 2 de `SKILL.md`.
- `SECURITY.md`: cómo informar de una vulnerabilidad (aviso privado de GitHub o contacto por la web del autor), qué se considera un problema de seguridad en un plugin de instrucciones y qué esperar como respuesta.
- README: tres ejemplos de uso con un caso ficticio pseudonimizado (formulación completa, diagnóstico diferencial y auditoría de lagunas).

### Cambiado

- Versión 1.6.2 en `plugin.json`, `.claude-plugin/plugin.json` y `.claude-plugin/marketplace.json`.
- Paquete de la *Release* regenerado con el `SKILL.md` y el `flujo.md` nuevos.

---

## [1.6.1] — 2026-09-29

Ajustes para el directorio de plugins de Claude. **No toca el contenido clínico**: ni el `SKILL.md`, ni el flujo, ni la plantilla, ni las salvaguardas.

### Corregido

- El validador del directorio retenía el envío por `BINARIES_NOT_INSPECTED`: no puede inspeccionar el `.zip` y el `.skill` de `dist/`. Los binarios salen del repositorio.

### Añadido

- Icono del plugin (PNG de 512 × 512, en la carpeta de manifiestos de Claude), generado con asistencia de ChatGPT (OpenAI) y revisado por el autor; la mención figura en el README.
- Sección «Privacidad» en el README: qué recoge el plugin (nada), qué trata la plataforma donde se use y qué datos no introducir.

### Cambiado

- `dist/` pasa a `.gitignore`. Los paquetes se siguen generando con `scripts/build-dist.sh` y se publican como adjuntos de cada *Release*; los enlaces de descarga del README apuntan ahora a la última *Release*.
- Versión 1.6.1 en `plugin.json`, `.claude-plugin/plugin.json` y `.claude-plugin/marketplace.json`.

---

## [1.6.0] — 2026-08-07

Cambio de empaquetado. **No toca el contenido clínico**: ni el `SKILL.md`, ni el flujo de seis pasos, ni la plantilla, ni las capas condicionales, ni las salvaguardas. Solo cambia dónde viven los archivos y cómo se instala.

### Corregido

- **El paquete de `dist/` estaba roto y no se había detectado.** Dos defectos a la vez: contenía el frontmatter anterior a la v1.5.3, con `author`, `homepage` y `repository` al nivel superior, claves que el conjunto cerrado de [Agent Skills](https://agentskills.io/specification) no permite y que hacen **fallar la subida con error duro** en ChatGPT, claude.ai y la Skills API; y los archivos iban **planos en la raíz del zip**, sin la carpeta contenedora que el estándar exige y que ChatGPT rechaza. El arreglo del frontmatter llegó al árbol pero nadie regeneró `dist/`, así que el paquete descargable seguía sin poder instalarse.

### Añadido

- El repositorio es ahora un **plugin conforme a [Agent Plugins 1.0.0](https://agent-plugins.org/specification)**, el formato portátil de la Agentic AI Foundation. Se añaden `plugin.json` (portable, con el `$schema` canónico), `.claude-plugin/plugin.json` (Claude Code) y `.claude-plugin/marketplace.json`, que es el que permite instalarlo con `/plugin marketplace add` — sin él, ese comando falla con «Este repositorio no es un marketplace».
- **Opción 2 de instalación: ChatGPT.** Se documenta el flujo completo, incluidos sus requisitos de forma y el plan necesario.
- **Opción 6: instalación como plugin** en Claude Code y Cowork, con la tabla de invocación con `/`.
- `scripts/build-dist.sh`: el paquete se armaba a mano, que es exactamente por lo que llevaba meses desactualizado. Ahora se regenera con un script y el `.skill` queda como copia byte a byte del `.zip`.

### Cambiado

- El skill pasa de la raíz a `skills/cie11-formulacion-clinica/`, junto con `flujo.md` y `plantilla-caso.md`: es la ubicación fija que el §6.1 de la spec exige para descubrir skills. Los acompañantes quedan planos al lado del `SKILL.md`, no bajo `references/`, porque el cuerpo los referencia por nombre pelado.
- Enlaces y árbol del repositorio en el README actualizados a la ruta nueva.

---

## [1.5.2] — 2026-05-31

### Añadido
- Compatibilidad con **Mistral AI (Skills)**: documentada como Opción 3 de instalación en el README (descomprimir el paquete y seleccionar la carpeta en el espacio *Work*). La frase de apertura incluye Mistral.

### Cambiado
- `description` del `SKILL.md` reescrita y reducida a menos de 500 caracteres (479) para cumplir el límite de Mistral, conservando el trigger principal, los modos y los límites de seguridad (no autodiagnóstico, no datos identificables). Paquete `dist/` regenerado en consecuencia.

---

## [1.5.1] — 2026-05-31

### Corregido
- Frontmatter YAML del `SKILL.md`: el campo `description` pasa a bloque escalar (`>-`) para evitar el error «mapping values are not allowed in this context» en parsers estrictos (p. ej. el de Perplexity). El texto de la descripción y los triggers de activación no cambian.
- Paquete de `dist/` (`.zip` y `.skill`) regenerado con el `SKILL.md` corregido; la versión anterior embebía el descriptor que fallaba al instalar.

### Añadido
- README: **Perplexity (Skills)** documentado como Opción 2 de instalación; la frase de apertura deja de limitar el skill a Claude.

---

## [1.5] — 2026-05-08

### Añadido
- División del modo `auditoria` en dos modos diferenciados:
  - `auditoria`: paso 1 + paso 6 + bloque A (detección de errores específicos en una formulación ya hecha).
  - `auditoria-lagunas`: paso 1 + bloque B (lagunas críticas para sostener una formulación ya hecha).
- Sugerencia cruzada entre ambos modos al final de cada salida.
- Autoría explícita en frontmatter YAML del `SKILL.md` y en cabecera de `flujo.md` (Pablo, mindandhealth.org, github.com/novanoticia).
- Archivo `LICENSE` con texto íntegro de CC BY 4.0 y atribución sugerida.
- Guía profesional en PDF (22 páginas): filosofía de diseño, marco ético-legal, arquitectura, los seis pasos del flujo, modos de invocación, capas condicionales, limitaciones conocidas y sesgos identificados.
- Estructura de repositorio con subdirectorios `dist/` y `docs/`.
- README.md con instalación detallada (Claude.ai, Claude Code, otras IAs).

### Cambiado
- Licencia de **CC BY-NC-SA 4.0** a **CC BY 4.0** (más permisiva, máxima difusión, uso comercial permitido manteniendo atribución).

---

## [1.4] — Iteración interna

### Añadido
- Cabecera explícita ⚠ antes del paso 1 cuando se activa la capa de comorbilidad sistémica (sustituye al formato anterior con corchetes embebidos).
- Regla anti-redundancia entre pasos 2 y 3: cuando una hipótesis principal coincide con una sospecha del diferencial, no se duplica el desarrollo.
- Estructura "1 ángulo obligatorio + 1-2 a elección" en el paso 6 cuando la capa transversal de comorbilidad está activa.
- Salida pre-pseudonimización en Puerta 1: cuando se detecta identificador indirecto, el flujo ofrece una versión generalizada para confirmación, no solo lista de cambios.
- Regla estructural reforzada para Puerta 1: localidad concreta + cargo único + dato familiar específico = identificación automática, independientemente del reconocimiento del topónimo.
- Bloque de auditoría ampliado en modo `auditoria`: detección de errores específicos (descartes prematuros, diferenciales no considerados, descartes orgánicos insuficientes, supuestos no fundamentados, saltos lógicos) y mini-bloque de lagunas críticas.

---

## [1.3]

### Añadido
- Detección de identificadores indirectos (combinaciones que en conjunto identifican).
- Variantes de entrada: caso ya estructurado (Tipo A), prosa narrativa (Tipo B), notas en bruto o transcripción (Tipo C).
- Capa transversal de comorbilidad sistémica (oncológico, embarazo/posparto, dolor crónico, neurológico, endocrinopatías complejas, VIH/hepatitis, inmunodepresión, insuficiencia orgánica, cardiopatía con limitación funcional, enfermedad inflamatoria sistémica).
- Versiones alternativas opcionales tras la salida principal: condensada para historia clínica y sintética para supervisión.

---

## [1.2]

### Añadido
- Modos de invocación con salvaguarda de seguridad clínica: si el caso muestra señales de riesgo agudo aunque el modo no incluya el paso 5, el flujo lo ejecuta de todos modos.
- Modos `completo` (default), `diferenciales`, `lagunas`, `riesgo`, `auditoria`.
- Apéndice canónico en `flujo.md` con un caso resuelto de referencia para guiar la imitación de estilo y nivel de concisión.

---

## [1.1]

### Cambiado
- Referencia diagnóstica primaria pasa de DSM-5-TR a **CIE-11** (Organización Mundial de la Salud). DSM-5-TR queda como referencia secundaria invocable solo cuando difiere de forma clínicamente relevante.

### Añadido
- Especificadores integrados en hipótesis principales (curso, gravedad, características asociadas).
- Plan de exploración priorizado en el paso 4 (próxima cita / pruebas complementarias / fuentes externas, con urgencia relativa).

---

## [1.0]

### Añadido
- Primer borrador funcional con seis pasos: caso estructurado, hipótesis a considerar, diagnóstico diferencial obligatorio, lagunas, señales de riesgo, cuestionamiento epistémico.
- Dos puertas de entrada: pseudonimización y mediación clínica.
- Reglas duras transversales: no diagnóstico, no transcripción de criterios, no propuesta de tratamiento, "no documentado ≠ ausente".
- Formato de salida fijo con encabezados numerados y nota final obligatoria.
