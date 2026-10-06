# cie11-formulacion-clinica

> 🌐 **Languages:** [Español](./README.md) (full documentation) · English · [Français](./README.fr.md)

A skill for AI assistants (Claude, and also ChatGPT, Perplexity and Mistral AI Skills) that **supports the clinical formulation** of cases in psychiatry and clinical psychology, using **ICD-11** as the primary diagnostic reference. It takes a pseudonymised case that a qualified professional has already interviewed and returns a structured scaffold: reasoned hypotheses, mandatory differential diagnosis, information gaps with an assessment plan, risk indicators and epistemic questioning. **It does not diagnose.**

> **Author:** Pablo · [mindandhealth.org](https://mindandhealth.org) · [github.com/novanoticia](https://github.com/novanoticia)
> **Licence:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
> **Current version:** v1.7

> **This is a short version.** The full documentation (installation for each platform, the six modes, safeguards, privacy, references and the professional guide) is in Spanish in the [main README](./README.md).

## Who it is for

Qualified professionals in **psychiatry** and **clinical psychology** who want a reasoning aid after the interview. **It is not for self-diagnosis, not for people without professional qualifications, and not a medical device** under Regulation (EU) 2017/745. It does not replace the clinical interview, clinical judgement or your centre's protocols.

## Language of the output

The skill answers in **Spanish, English or French**. The language is chosen in this order: (1) an explicit request, with a word after the mode (`/cie11-formulacion-clinica completo en`) or in plain language ("in French"); (2) the language in which you write the case; (3) Spanish. If the requested language is not available, it tells you and continues in the language of the case (or in Spanish).

**Not translated:** the trigger and the mode names (`completo`, `diferenciales`, `lagunas`, `riesgo`, `auditoria`, `auditoria-lagunas`), ICD-11 codes and file names. Quotations from the case are kept in their original language.

## Install and use

Install it from the repository or from the package attached to each Release; the step-by-step instructions for each platform are in the [main README](./README.md#instalación). Then invoke it with `/cie11-formulacion-clinica [mode]` followed by the case, for example:

```
/cie11-formulacion-clinica diferenciales en
```

**Always work with pseudonymised cases.** Do not enter identifiable data about real patients. The text you type is processed by the AI platform you choose, under its own terms and privacy policy; this project collects, stores and sends no data.

## Limitations and disclaimer

This is an **experimental methodological tool, not validated with real cases by qualified clinicians**. It is calibrated for adults, not for emergencies or acute risk assessment. Its output is a scaffold of hypotheses for the responsible clinician to weigh; any real use with sensitive data is the sole responsibility of the professional using it and must comply with the applicable legal framework.

## AI assistance and review

This skill was produced with the assistance of **Claude (Anthropic)**, under the author's direction and responsibility. The **English and French translations were written by an AI and have not been reviewed by a native speaker or by a clinician**; they require human review before any professional use.

## Licence

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). See [`LICENSE`](./LICENSE).
