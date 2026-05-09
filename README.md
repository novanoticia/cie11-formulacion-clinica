# cie11-formulacion-clinica

Skill para asistentes conversacionales (Claude, Anthropic) de **apoyo a la formulación clínica** de casos en psiquiatría y psicología clínica, basado en **CIE-11** como referencia diagnóstica primaria. Recibe un caso pseudonimizado ya entrevistado y devuelve un andamio estructurado de hipótesis razonadas, diferenciales obligatorios, lagunas con plan de exploración, señales de riesgo y cuestionamiento epistémico. **No diagnostica.**

> **Autor:** Pablo · [mindandhealth.org](https://mindandhealth.org) · [github.com/novanoticia](https://github.com/novanoticia)
> **Licencia:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es)
> **Versión actual:** v1.5

---

## Antes de empezar: lee la guía

Antes de probar el skill, conviene leer la guía profesional. Explica filosofía de diseño, marco ético-legal (RGPD, MDR 2017/745, copyright), arquitectura del flujo, los seis pasos del razonamiento, modos de invocación, capas condicionales (variantes de entrada, comorbilidad sistémica), limitaciones conocidas y sesgos identificados:

📄 **[Guía para profesionales (PDF, v1.5)](./docs/cie11-formulacion-clinica-guia-profesional-v1.5.pdf)**

Es un documento de unas 22 páginas pensado para leer una vez antes del primer uso. Sin esa lectura, hay riesgo de tratar la herramienta como caja negra: la salida del skill está bien redactada y produce la tentación de aceptarla sin más, lo cual es justamente lo que hay que resistir.

---

## Estado del proyecto

Versión **1.5**. Probado únicamente con casos sintéticos diseñados para someter el flujo a tensión: un caso depresivo con condición tiroidea y consumo, un caso ansioso-somático con sospecha traumática, un caso oncológico con hormonoterapia para verificar la activación de la capa transversal de comorbilidad, y un ejercicio de modo `auditoria` sobre formulación ya hecha.

> **No validado con casos reales por clínicos habilitados.** Pendiente de prueba en supervisión y formación reales antes de cualquier uso institucional.

---

## Audiencia esperada

Profesionales habilitados en **psiquiatría** y **psicología clínica** que quieran usar la herramienta como apoyo de razonamiento tras la entrevista: para forzar el descarte activo de orgánico/iatrogénico/reactivo, detectar lagunas accionables, organizar un plan de exploración priorizado, o someter una formulación propia a auditoría epistémica.

**No es para autodiagnóstico, no es para uso por personas no cualificadas profesionalmente, no sustituye la entrevista directa, no sustituye los protocolos del centro, no es producto sanitario en el sentido del MDR 2017/745.**

---

## Sobre el autor

Desarrollado por **Pablo** ([mindandhealth.org](https://mindandhealth.org), GitHub: [novanoticia](https://github.com/novanoticia)) — **no profesional sanitario en ejercicio**. Es un proyecto personal con interés autodidacta en marcos clínicos contextuales (ACT, PBT, modelos dialógicos), nosografía CIE-11, razonamiento clínico, y crítica de la mediación algorítmica de la información sensible.

El skill se ha construido con **asistencia de Claude (Anthropic)**. Las decisiones de diseño, la dirección y la responsabilidad del contenido corresponden al autor humano. Requiere validación profesional antes de cualquier uso real con pacientes.

---

## Qué hace

Recibe un caso pseudonimizado ya entrevistado por un profesional habilitado y devuelve, en este orden (modo `completo`):

1. **Caso estructurado** en un esquema fijo de once apartados (demografía, motivo, cronología, síntomas, antecedentes psiquiátricos, médicos, sustancias, familiares, psicosocial, exploración, pendientes).
2. **Hipótesis diagnósticas a considerar**, separando hipótesis principales (con códigos CIE-11 y especificadores aplicables) de hipótesis a vigilar.
3. **Diagnóstico diferencial obligatorio** (orgánico, sustancias, otros primarios, reactivo) con descartes anclados al caso concreto.
4. **Lagunas de información y plan de exploración priorizado** (próxima cita, pruebas complementarias, fuentes externas).
5. **Señales de riesgo** sobrias, distinguiendo lo explícito, lo no explorado y los factores protectores.
6. **Cuestionamiento epistémico** (2-3 ángulos: dimensional, contextual-funcional, dialógico, comparado CIE/DSM, supuestos del relato, sesgos de género/clase/cultura/edad).

**Modos disponibles:**

- `completo` (default) — los seis pasos.
- `diferenciales` — pasos 1, 2 y 3.
- `lagunas` — pasos 1 y 4.
- `riesgo` — pasos 1 y 5.
- `auditoria` — pasos 1, 6 y bloque A: detección de errores específicos en una formulación ya hecha.
- `auditoria-lagunas` — paso 1 y bloque B: lagunas críticas para sostener una formulación ya hecha.

**Capas condicionales que se activan automáticamente:**

- **Variantes de entrada**: caso ya estructurado, prosa narrativa, o notas en bruto. El paso 1 se ajusta sin exigir un formato concreto.
- **Capa transversal de comorbilidad sistémica**: cuando el caso menciona oncológico activo, embarazo/posparto, dolor crónico, neurológico relevante, endocrinopatías complejas, VIH/hepatitis, inmunodepresión, insuficiencia orgánica avanzada o cardiopatía con limitación funcional, los pasos 2-6 se ejecutan con consideraciones específicas (regla de parsimonia clínica, ampliación del diferencial iatrogénico, lectura "respuesta adaptativa a enfermedad médica" como ángulo obligatorio).
- **Salvaguarda de seguridad clínica**: si el caso muestra señales de riesgo agudo evidentes pero el modo elegido no incluye el paso 5, el flujo lo activa de todos modos y lo indica.

Detalle completo en [`SKILL.md`](./SKILL.md), lógica del razonamiento en [`flujo.md`](./flujo.md), formato de entrada en [`plantilla-caso.md`](./plantilla-caso.md), y discusión exhaustiva en la guía PDF.

---

## Qué NO hace

- **No emite diagnóstico definitivo.** Genera un andamio de hipótesis a contrastar por el clínico responsable. Usa siempre formulaciones tipo *"el cuadro orienta a considerar X"*, nunca *"el paciente tiene X"*.
- **No reproduce criterios diagnósticos de la CIE-11 ni del DSM-5-TR.** Referencia categorías por nombre y código (p. ej., 6A71, 6B40, 6E60), no por enumeración de criterios. La verificación de los criterios formales contra el manual oficial es responsabilidad del clínico.
- **No propone tratamiento farmacológico ni protocolos psicoterapéuticos específicos.**
- **No procesa datos identificables de pacientes.** Trabaja siempre con casos pseudonimizados. La "Puerta 1" del flujo detiene el procesamiento si detecta identificadores directos o combinaciones identificadoras indirectas (localidad concreta + cargo único + dato familiar específico, por ejemplo).
- **No es un producto sanitario en el sentido del Reglamento (UE) 2017/745.** Funciona como apoyo reflexivo y educativo, no como herramienta diagnóstica certificada.
- **No sustituye el juicio clínico, la entrevista directa ni los protocolos del centro.**
- **No está calibrado para población infanto-juvenil** sin revisión específica.
- **No está calibrado para urgencias** ni para evaluación de riesgo agudo.

---

## Instalación

Hay tres formas de usar el skill, según dónde quieras invocarlo. La primera es la más sencilla.

### Opción 1 — Claude.ai (web, app de escritorio o móvil)

Es la vía recomendada y más rápida.

1. Descarga el paquete de instalación: **[`dist/cie11-formulacion-clinica.zip`](./dist/cie11-formulacion-clinica.zip)**.
2. En Claude.ai, ve a **Ajustes → Capacidades → Skills**.
3. Asegúrate de que **Code execution and file creation** está activado.
4. Pulsa **Subir skill** (o *Upload skill*).
5. Selecciona el archivo `.zip` descargado.
6. El skill aparece en tu lista de Skills, activado por defecto.

A partir de ese momento, el skill se invoca con `/cie11-formulacion-clinica` seguido opcionalmente del modo (`completo`, `diferenciales`, `lagunas`, `riesgo`, `auditoria`, `auditoria-lagunas`) en cualquier conversación. Recomendado: hazlo en una **Conversación Temporal** para minimizar la huella de los datos sensibles.

> El archivo equivalente con extensión `.skill` (**[`dist/cie11-formulacion-clinica.skill`](./dist/cie11-formulacion-clinica.skill)**) es el mismo paquete con extensión alternativa, presente para compatibilidad con marketplaces de terceros (Agensi, etc.). Para Claude.ai oficial hay que renombrarlo a `.zip` antes de subirlo, o simplemente usar directamente el `.zip`.

### Opción 2 — Claude Code (línea de comandos)

Para usar el skill desde Claude Code en tu Mac:

```bash
# Skills personales (disponibles en cualquier proyecto)
mkdir -p ~/.claude/skills
cd ~/.claude/skills
unzip /ruta/a/cie11-formulacion-clinica.zip

# O bien, skills del proyecto actual
mkdir -p .claude/skills
cd .claude/skills
unzip /ruta/a/cie11-formulacion-clinica.zip
```

Tras descomprimir tendrás `~/.claude/skills/cie11-formulacion-clinica/` con todos los archivos. Claude Code lo detecta automáticamente; se invoca igual que en la app: `/cie11-formulacion-clinica [modo]`.

### Opción 3 — Otras inteligencias artificiales

El skill es texto Markdown. Cualquier asistente conversacional capaz de seguir instrucciones extensas puede aplicarlo, pegándolo como prompt inicial.

1. Abre una conversación efímera o temporal en la IA correspondiente:
   - **ChatGPT**: *Temporary Chat*.
   - **Mistral LeChat**: conversación efímera.
   - **Google Gemini**: chat temporal cuando esté disponible.
   - **LLM local** (Ollama, LM Studio): cualquier sesión nueva.
2. Pega como primer mensaje el contenido concatenado de:
   - `SKILL.md`
   - `flujo.md`
   - `plantilla-caso.md`
3. Añade al final del bloque: *«Sigue este protocolo. Espera mi caso.»*
4. La IA debería confirmar que el protocolo está cargado. A partir de ahí, invoca con `/cie11-formulacion-clinica [modo]` o describe el modo en lenguaje natural si la IA no soporta comandos de barra.

> Avisos por plataforma:
> - **Meta AI en WhatsApp**: no recomendado para casos clínicos por la integración con la cuenta del usuario y la falta de un modo temporal verificable.
> - **Modelos pequeños** (≤ 7B parámetros): tienden a alucinar códigos diagnósticos, omitir especificadores y producir hipótesis con falsa confianza sin las atenuaciones que el flujo exige. Prefiere modelos de razonamiento de tamaño medio o grande.
> - **El modo `auditoria`** puede aplicarse a textos producidos por cualquier IA para revisar su solidez con un segundo modelo distinto del primero.

### Modo recomendado de uso (cualquier opción)

Independientemente de cómo lo instales:

1. **Activa Conversación Temporal o equivalente** antes de pegar nada sensible.
2. **Pseudonimiza el caso primero.** El skill detendrá el procesamiento si detecta identificadores, pero la primera barrera real es la limpieza previa. Para esto puedes usar el skill complementario [seudonimizador-clinico-juridico](https://github.com/novanoticia/seudonimizador-clinico-juridico) del mismo autor, o hacerlo manualmente: nombres por iniciales no contextualizables, localidad concreta por descriptor genérico, fechas exactas por intervalos, eliminar referencias a centros sanitarios específicos.
3. **Invoca** con `/cie11-formulacion-clinica` (modo `completo` por defecto) o especificando modo: `/cie11-formulacion-clinica diferenciales`, `lagunas`, `riesgo`, `auditoria`, `auditoria-lagunas`.
4. **Verifica críticamente la salida.** Especialmente: paso 5 (señales de riesgo no exploradas), paso 4b (plan de exploración), paso 6 (cuestionamiento epistémico). La salida está bien redactada por diseño; eso no la convierte en correcta.
5. **Cierra la conversación** una vez tengas el resultado en tus notas locales.

> La Conversación Temporal es una capa de privacidad de interfaz, no una bóveda criptográfica. Reduce la exposición pero no la elimina. Para usos que requieran cumplimiento RGPD pleno (publicación, peritaje, expediente), considera procesamiento local (LLM en máquina propia) y revisión humana experta como capas adicionales.

---

## Estructura del repositorio

```
cie11-formulacion-clinica/
├── SKILL.md                 # Descriptor del skill: trigger y resumen
├── flujo.md                 # Flujo de razonamiento de seis pasos + apéndice canónico
├── plantilla-caso.md        # Formato de entrada para el clínico
├── LICENSE                  # CC BY 4.0
├── README.md                # Este archivo
├── CHANGELOG.md             # Historial de versiones
├── .gitignore
├── dist/
│   ├── cie11-formulacion-clinica.zip    # Paquete de instalación para Claude.ai
│   └── cie11-formulacion-clinica.skill  # Mismo paquete, extensión alternativa
└── docs/
    └── cie11-formulacion-clinica-guia-profesional-v1.5.pdf
```

El paquete de `dist/` es ligero (≈ 21 KB): contiene solo los archivos que el skill necesita en tiempo de ejecución (SKILL.md, flujo.md, plantilla-caso.md) más LICENSE.

---

## Encadenamiento con otros skills

Está pensado para encadenarse con los skills de seudonimización y formulación jurídica del mismo autor:

- Caso clínico crudo (con identificadores) → `/seudonimizar A` → `/cie11-formulacion-clinica`.
- Formulación clínica ya hecha → `/cie11-formulacion-clinica auditoria` para someterla a revisión epistémica.
- Formulación clínica ya hecha → `/cie11-formulacion-clinica auditoria-lagunas` para identificar qué falta para sostenerla.

---

## Disclaimer

Este skill es una **herramienta metodológica experimental sin validación formal con casos reales**. Lo que produce es un andamio de hipótesis a contrastar; no es un diagnóstico ni un informe clínico. El uso real con datos sensibles es responsabilidad exclusiva del profesional habilitado que lo emplee y debe ajustarse al marco normativo aplicable (RGPD, LOPDGDD, código deontológico de la profesión, secreto profesional).

Ni el autor ni la herramienta ofrecen garantía alguna sobre la exactitud, idoneidad o consecuencias derivadas de su uso. Cualquier uso por personas no cualificadas profesionalmente queda fuera del alcance previsto del proyecto y bajo entera responsabilidad de quien lo realice.

---

## Referencias y atribuciones

Este skill referencia, sin reproducir literalmente, las siguientes obras y marcos:

- **CIE-11** — *International Classification of Diseases, 11th Revision*, Organización Mundial de la Salud (OMS), 2022. Capítulo 06 *Mental, behavioural or neurodevelopmental disorders*. Publicado bajo licencia Creative Commons BY-ND.
- **DSM-5-TR** — *Diagnostic and Statistical Manual of Mental Disorders*, Fifth Edition, Text Revision (American Psychiatric Association, 2022). Citado nominativamente como referencia secundaria, sin reproducir contenido protegido.
- **HiTOP** — *Hierarchical Taxonomy of Psychopathology* (Kotov et al., 2017). Marco dimensional citado en el cuestionamiento epistémico.
- **ACT / Process-Based Therapy** — Hayes & Hofmann (2018). Marco contextual-funcional citado en el cuestionamiento epistémico.
- **Diálogos Abiertos** — Seikkula y col. Marco dialógico citado en el cuestionamiento epistémico.
- **RGPD** — Reglamento (UE) 2016/679. Citado para encuadrar el tratamiento de datos pseudonimizados.
- **MDR 2017/745** — Reglamento (UE) 2017/745 sobre productos sanitarios. Citado para delimitar lo que el skill no es.

Toda referencia es nominativa y conceptual. El usuario es responsable de cumplir las condiciones de licencia o derechos de autor de cualquier material consultado a partir de estas referencias.

---

## Asistencia de IA

Este skill ha sido elaborado con asistencia de **Claude (Anthropic)**. Su contenido refleja decisiones, criterios y revisión del autor humano, pero requiere revisión profesional adicional antes de cualquier uso real con pacientes.

---

## Licencia

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Texto resumido en [`LICENSE`](./LICENSE).

Eres libre de:

- **Compartir** — copiar y redistribuir el material en cualquier medio o formato.
- **Adaptar** — remezclar, transformar y construir a partir del material para cualquier propósito, incluso comercialmente.

Bajo el siguiente término:

- **Atribución** — Debes dar crédito de manera adecuada, proporcionar un enlace a la licencia, e indicar si se han realizado cambios. Puedes hacerlo en cualquier forma razonable, pero no de forma tal que sugiera que tienes el apoyo del licenciante o lo recibes por el uso que haces.

---

## Cómo citarlo

Si lo referencias en un trabajo o adaptación:

> Pablo (2026). *cie11-formulacion-clinica* (v1.5). Skill de apoyo a la formulación clínica basado en CIE-11. mindandhealth.org · github.com/novanoticia/cie11-formulacion-clinica

---

## Feedback y contribuciones

Cualquier feedback profesional es valioso, especialmente sobre: salidas que han resultado clínicamente útiles, salidas pobres o engañosas, detección fallida de identificadores indirectos, activación incorrecta de la capa de comorbilidad, sugerencias de modos adicionales, sesgos detectados que no estén ya listados en la sección 9 de la guía PDF.

El autor puede ser contactado a través de [mindandhealth.org](https://mindandhealth.org). Issues y pull requests en GitHub también son bienvenidos. Las contribuciones de **clínicos habilitados** que quieran probar el skill con casos reales son especialmente valoradas.

Más detalles sobre cómo dar feedback en la guía PDF.
