# cie11-formulacion-clinica

> 🌐 **Langues :** [Español](./README.md) (documentation complète) · [English](./README.en.md) · Français

Un skill pour assistants d'IA (Claude, ainsi que les Skills de ChatGPT, de Perplexity et de Mistral AI) qui **soutient la formulation clinique** de cas en psychiatrie et en psychologie clinique, avec la **CIM-11** comme référence diagnostique principale. Il reçoit un cas pseudonymisé, déjà évalué en entretien par un professionnel habilité, et renvoie une trame structurée : hypothèses argumentées, diagnostic différentiel obligatoire, lacunes d'information avec plan d'exploration, indicateurs de risque et questionnement épistémique. **Il ne pose pas de diagnostic.**

> **Auteur :** Pablo · [mindandhealth.org](https://mindandhealth.org) · [github.com/novanoticia](https://github.com/novanoticia)
> **Licence :** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr)
> **Version actuelle :** v1.7

> **Ceci est une version courte.** La documentation complète (installation pour chaque plateforme, les six modes, garde-fous, confidentialité, références et guide professionnel) est en espagnol dans le [README principal](./README.md).

## À qui s'adresse-t-il

Aux professionnels habilités en **psychiatrie** et en **psychologie clinique** qui souhaitent une aide au raisonnement après l'entretien. **Il n'est pas destiné à l'autodiagnostic, ni aux personnes sans qualification professionnelle, et ce n'est pas un dispositif médical** au sens du règlement (UE) 2017/745. Il ne remplace ni l'entretien clinique, ni le jugement clinique, ni les protocoles de votre établissement.

## Langue de la réponse

Le skill répond en **espagnol, anglais ou français**. La langue est choisie dans cet ordre : (1) une demande explicite : un code de deux ou trois lettres juste après le mode, **comme dernier mot de la première ligne**, avec le cas à la ligne suivante (`/cie11-formulacion-clinica completo fr` ; `/cie11-formulacion-clinica fr` seul équivaut au mode complet), ou une demande en langage naturel (« répondez en français ») ; (2) la langue dans laquelle vous rédigez le cas ; (3) l'espagnol. Un mot isolé dans la phrase n'est pas lu comme une langue. Si la langue n'est pas disponible (demandée, ou cas rédigé par exemple en portugais), il vous le signale, affiche l'avertissement IA dans les trois langues et poursuit dans la langue du cas si elle existe, sinon en espagnol.

**Non traduits :** le déclencheur et les noms de mode (`completo`, `diferenciales`, `lagunas`, `riesgo`, `auditoria`, `auditoria-lagunas`), les codes CIM-11 et les noms de fichiers. Les citations du cas sont conservées dans leur langue d'origine.

## Installation et utilisation

Installez-le depuis le dépôt ou depuis le paquet joint à chaque Release ; les instructions pas à pas pour chaque plateforme se trouvent dans le [README principal](./README.md#instalación). Invoquez-le ensuite avec `/cie11-formulacion-clinica [mode] [langue]` suivi du cas à la ligne suivante. La description du skill, qui décide de son activation automatique, est en espagnol : en français, utilisez la commande. Par exemple :

```
/cie11-formulacion-clinica diferenciales fr
```

**Travaillez toujours avec des cas pseudonymisés.** Ne saisissez aucune donnée identifiable de patients réels. Le texte que vous écrivez est traité par la plateforme d'IA que vous choisissez, selon ses propres conditions et sa politique de confidentialité ; ce projet ne collecte, ne conserve ni n'envoie aucune donnée.

## Limites et avertissement

Il s'agit d'un **outil méthodologique expérimental, non validé avec des cas réels par des cliniciens habilités**, et la couche linguistique **n'a pas encore été exécutée sur une plateforme réelle** (les 21 scénarios de `tests/escenarios.md` sont rédigés mais n'ont pas été exécutés). Il est calibré pour les adultes, pas pour les urgences ni pour l'évaluation du risque aigu. Sa sortie est une trame d'hypothèses que le clinicien responsable doit examiner ; tout usage réel avec des données sensibles relève de la seule responsabilité du professionnel qui l'emploie et doit respecter le cadre juridique applicable.

## Assistance de l'IA et relecture

Ce skill a été élaboré avec l'aide de **Claude (Anthropic)**, sous la direction et la responsabilité de l'auteur. **Les traductions en anglais et en français ont été rédigées par une IA et n'ont pas été relues par un locuteur natif ni par un clinicien** ; elles nécessitent une relecture humaine avant tout usage professionnel.

## Licence

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.fr). Voir [`LICENSE`](./LICENSE).
