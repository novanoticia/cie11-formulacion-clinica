# Política de seguridad

## Qué es este proyecto, a efectos de seguridad

Un plugin de instrucciones: archivos de texto (Markdown) —el skill, su flujo, la plantilla y los catálogos de idioma—, sin código ejecutable en el paquete, sin servidores MCP, sin conectores y sin llamadas de red. No recoge, guarda ni envía datos (véase «Privacidad» en el [README](./README.md#privacidad)).

Por eso el riesgo técnico es bajo, pero no nulo. Lo que sí puede fallar y conviene comunicar:

- **Instrucciones que provoquen un comportamiento inseguro** (por ejemplo, que el flujo no detecte identificadores de pacientes, omita una salvaguarda clínica o emita un diagnóstico categórico).
- **Contenido que induzca a Claude u otra IA a ejecutar acciones no pedidas** o a obtener instrucciones de fuentes externas.
- **Cualquier archivo del repositorio que no sea texto legible**, o que contenga código, enlaces inesperados o instrucciones ocultas.
- **Una fuga de datos personales** en el repositorio (por ejemplo, un caso real en un ejemplo).

## Cómo informar de una vulnerabilidad

Usa, por este orden de preferencia:

1. **Aviso privado de GitHub:** pestaña **Security** → **Report a vulnerability** en [este repositorio](https://github.com/novanoticia/cie11-formulacion-clinica/security/advisories/new). Solo lo ve el autor.
2. **Contacto a través de [mindandhealth.org](https://mindandhealth.org)**, indicando en el asunto «Seguridad: cie11-formulacion-clinica».

**Por favor, no publiques el detalle en una *issue* pública** hasta que se haya corregido, y **no incluyas datos reales de pacientes** en ningún informe: usa un caso ficticio o pseudonimizado.

Incluye, si puedes: qué has observado, en qué archivo o paso del flujo, cómo reproducirlo y qué plataforma y modelo usabas.

## Qué puedes esperar

- Acuse de recibo en un plazo razonable (este es un proyecto de una sola persona, sin equipo de guardia).
- Si el problema se confirma, corrección en una nueva versión y nota en el [CHANGELOG](./CHANGELOG.md), con reconocimiento a quien lo comunicó si lo desea.
- Si el problema no se considera una vulnerabilidad, una respuesta con el motivo.

## Versiones con soporte

Solo la versión más reciente publicada en la sección *Releases*.
