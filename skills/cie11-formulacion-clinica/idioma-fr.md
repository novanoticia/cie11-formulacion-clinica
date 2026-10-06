# Catálogo de frases fijas — Français

Traducción de `idioma-es.md`: mismas claves, mismos marcadores `{nombre}` y mismos textos entre comillas invertidas. Convenciones tipográficas del aviso de IA ya aprobado: espacio normal antes de «:», «;», «?» y «!», y apóstrofo recto; tratamiento de «vous». Traducción redactada por una IA, **no revisada por una persona nativa ni por un clínico**. Valídalo con `python3 scripts/validar_idiomas.py`.

## modo_no_reconocido
Mode non reconnu, j'exécute le mode complet.

## paso5_fuera_de_modo
Étape 5 activée hors du mode demandé en raison d'indicateurs de risque dans le cas.

## aviso_poblacion
Ce flux n'est pas calibré pour la population des enfants et des adolescents ; les considérations suivantes doivent être revues avec un spécialiste de ce domaine.

## aviso_notas
Le matériel fourni a la forme de notes ; certaines rubriques resteront en partie vides. Si vous disposez d'un récit plus structuré, le flux exploitera mieux l'information.

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
- *Version condensée pour le dossier clinique* (format de compte rendu : motif de consultation, antécédents, examen, impression diagnostique avec codes CIM-11, plan ; sans questionnement épistémique ni métacommentaires).
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
La langue demandée n'est pas disponible. Langues disponibles : {idiomas}.

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
numéro de Sécurité sociale (NIR), numéro de dossier médical et identifiant national de santé (INS).

## puerta1_marco_legal
RGPD (les données de santé relèvent des catégories particulières de données à caractère personnel).

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
