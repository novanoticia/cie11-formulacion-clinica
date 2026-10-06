# Catálogo de frases fijas — Français

Traducción de `idioma-es.md`: mismas claves, mismos marcadores `{nombre}` y mismos textos entre comillas invertidas. Convenciones tipográficas del aviso de IA ya aprobado: espacio normal antes de «:», «;», «?» y «!», y apóstrofo recto; tratamiento de «vous». Traducción redactada por una IA, **no revisada por una persona nativa ni por un clínico**. Los nombres de `categorias` son los oficiales de la OMS (CIE-11 MMS, versión 2024-01, «Simple Tabulation» en español, inglés y francés), copiados sin retocar. Valídalo con `python3 scripts/validar_idiomas.py`.

## modo_no_reconocido
Mode non reconnu, j'exécute le mode complet.

## paso5_fuera_de_modo
Étape 5 activée hors du mode demandé en raison d'indicateurs de risque dans le cas.

## aviso_poblacion
Cette démarche n'est pas calibrée pour la population des enfants et des adolescents ; les considérations suivantes doivent être revues avec un spécialiste de ce domaine.

## aviso_notas
Le matériel fourni a la forme de notes ; certaines rubriques resteront en partie vides. Si vous disposez d'un récit plus structuré, la démarche exploitera mieux l'information.

## cabecera_comorbilidad
⚠ *Couche de comorbidité systémique activée — condition détectée : {condicion}.*
*Les considérations spécifiques s'appliquent tout au long des étapes suivantes.*

## no_documentado
[non documenté dans le cas]

## nota_final
Ce document est une trame de formulation, non un diagnostic. La décision clinique revient au professionnel responsable du cas. Texte généré avec l'aide de l'IA ; il requiert une relecture humaine avant tout usage clinique.

## aviso_ia
**Avertissement :** cette réponse est élaborée avec l'aide de l'IA. Elle constitue un soutien pour le professionnel responsable du cas et doit être relue par un professionnel qualifié avant toute décision clinique.

## versiones_alternativas
*Si vous le souhaitez, je peux également générer :*
- *Version condensée pour le dossier patient* (format de compte rendu : motif de consultation, antécédents, examen psychique, orientation diagnostique avec codes CIM-11, plan ; sans questionnement épistémique ni métacommentaires).
- *Version synthétique pour la supervision* (5-10 lignes avec les hypothèses principales, les lacunes critiques et les indicateurs de risque, pour une discussion rapide).

## auditoria_solida
La formulation est solide dans ses grandes lignes ; les considérations suivantes sont des nuances, non des objections de fond.

## sugerencia_auditoria
Pour une analyse des erreurs spécifiques de la formulation, invoquez `/cie11-formulacion-clinica auditoria`.

## sugerencia_auditoria_lagunas
Pour une analyse centrée sur ce qui manque, invoquez `/cie11-formulacion-clinica auditoria-lagunas`.

## sospecha_desarrollada
Soupçon développé en H1 ; ici il est seulement consigné comme élément nécessitant une coordination avec l'équipe prescriptrice

## no_explorado_ideacion
idéation suicidaire non explorée lors de cet entretien

## idioma_no_disponible
Cette langue n'est pas disponible. Langues disponibles : {idiomas}.

## enc_1
Cas structuré

## enc_2
Hypothèses diagnostiques à considérer

## enc_2a
Hypothèses principales (avec spécificateurs le cas échéant)

## enc_2b
Hypothèses à surveiller (le cas échéant)

## enc_3
Diagnostic différentiel obligatoire

## enc_4
Lacunes d'information et plan d'exploration

## enc_4a
Lacunes identifiées

## enc_4b
Plan d'exploration priorisé

## enc_5
Indicateurs de risque

## enc_6
Questionnement épistémique

## enc_A
Détection d'erreurs spécifiques

## enc_B
Lacunes critiques pour soutenir la formulation auditée

## enc_nota_final
Note finale

## puerta1_identificadores
Par exemple, numéro de Sécurité sociale (NIR), numéro de dossier médical et identifiant national de santé (INS), ou les identifiants équivalents de la juridiction du clinicien.

## puerta1_marco_legal
Par exemple, le RGPD, ou la réglementation applicable en matière de protection des données (les données de santé relèvent des catégories particulières de données à caractère personnel).

## lbl_3_organicas
Causes organiques

## lbl_3_sustancias
Substances et médicaments

## lbl_3_psiquiatricos
Autres troubles psychiatriques primaires

## lbl_3_reaccion
Réaction aux circonstances de vie

## lbl_4b_consulta
Pour la prochaine consultation (entretien clinique)

## lbl_4b_pruebas
Examens complémentaires et exploration objective

## lbl_4b_fuentes
Informations issues de sources externes

## urg_necesaria
nécessaire avant de clore la formulation

## urg_util
utile dans les semaines à venir

## urg_opcional
facultatif si le doute persiste

## lbl_5_explicitas
Indicateurs explicites

## lbl_5_implicitas
Indicateurs implicites ou infraliminaires

## lbl_5_protectores
Facteurs protecteurs

## recordatorio_riesgo
Rappel : si le cas décrit un risque aigu ou imminent, cette démarche ne remplace ni les protocoles d'évaluation du risque de l'établissement ni l'évaluation clinique directe.

## especificadores_por_determinar
spécificateurs à déterminer après élargissement de l'exploration

## sin_datos_documentados
aucune donnée documentée dans le cas

## categorias
- 6A60 | Trouble bipolaire de type I
- 6A61 | Trouble bipolaire de type II
- 6A70 | Épisode dépressif unique
- 6A71 | Trouble dépressif récurrent
- 6A72 | Dysthymie
- 6A73 | Trouble anxieux et dépressif mixte
- 6B00 | Trouble d'anxiété généralisée
- 6B04 | Trouble d'anxiété sociale
- 6B40 | Trouble de stress posttraumatique
- 6B43 | Trouble d'adaptation
- 6C40 | Troubles dus à la consommation d'alcool
- 6C40.1 | Mode de consommation nocif d'alcool
- 6E60 | Syndrome neurodéveloppemental secondaire
- 6E61 | Syndrome psychotique secondaire
- 6E62 | Trouble de l'humeur secondaire
- 6E63 | Syndrome d'anxiété secondaire

## glosario
- trame de formulation
- clinicien responsable du cas
- hypothèses principales
- hypothèses à surveiller
- diagnostic différentiel
- lacunes d'information
- plan d'exploration
- indicateurs de risque
- questionnement épistémique
- pseudonymisation
- identifiants directs et indirects
- non documenté dans le cas
- non exploré
- couche de comorbidité systémique
- CIM-11
- porte d'entrée
- médiation clinique
