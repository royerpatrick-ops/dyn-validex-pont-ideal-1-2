# DYN-VALIDEX — pont idéal déterministe sur [1,2]

Archive scientifique associée au DOI [10.5281/zenodo.23188815](https://doi.org/10.5281/zenodo.23188815).

Auteur humain et responsable de la publication : **Patrick Royer**, chercheur indépendant sans affiliation institutionnelle.

## Portée scientifique exacte

Ce dépôt présente un résultat mathématique **conditionnel au modèle idéal continu explicitement défini** dans le rapport. Une partition exacte y réduit les configurations admissibles à neuf cellules du plan auxiliaire, puis la moyenne de phase et le conditionnement ramènent l’intégrale locale `I_[1,2]` à une partie exacte et une intégrale lisse sur un rectangle.

Deux implémentations utilisant l’arithmétique rationnelle, des bornes dirigées de racines carrées et un reste de Simpson tensoriel justifié fournissent l’encadrement affiché vers l’extérieur :

```text
0.234689097597 <= I_[1,2] <= 0.234689433430
```

La portée est **locale, idéale et non normalisée**. Aucun facteur `6/pi^2`, raccord `C_mod`, coefficient asymptotique, transfert de loi P2 ou constante globale n’est établi. Les sept composantes gelées restent `UNKNOWN/null`. Les contrôles finis accompagnent les arguments universels ; ils ne les remplacent pas.

## Contenu principal

- [`01_PONT_IDEAL_1_2_DOI_23188815_v0_2.pdf`](01_PONT_IDEAL_1_2_DOI_23188815_v0_2.pdf) — rapport principal ;
- [`02_SUPPLEMENTS_PONT_IDEAL_1_2_v0_2.zip`](02_SUPPLEMENTS_PONT_IDEAL_1_2_v0_2.zip) — archive originale des compléments ;
- [`supplements/`](supplements/) — même complément extrait pour consultation directe des sources, preuves, certificats et pièces de relecture ;
- [`03_LICENCE_DEL.pdf`](03_LICENCE_DEL.pdf) — texte original de la licence DEL ;
- [`METADONNEES_ZENODO_v0_2.txt`](METADONNEES_ZENODO_v0_2.txt) — description détaillée, périmètre, assistance IA et statut de relecture.

## Assistance par intelligence artificielle

L’assistance de ChatGPT/Codex est substantielle : dérivations mathématiques, rédaction, génération de code, vérifications exactes, contrelectures IA et intégration finale du dossier. Patrick Royer demeure l’auteur humain et responsable du contenu. Les versions de modèles non consignées ne sont pas déduites.

La revue contradictoire Codex jointe est une **revue par IA**, pas une revue humaine extérieure. Les certificats fournis documentent les vérifications indiquées dans leur périmètre ; ils ne constituent pas une formalisation par assistant de preuve ni une évaluation par les pairs.

## Statut de la relecture

**Aucune vérification personnelle de chaque démonstration par un mathématicien humain extérieur n’est attestée.** Une revue mathématique humaine indépendante est sollicitée et n’a pas encore été effectuée. Voir [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md) et le dossier historique [`supplements/dossier_revue_humaine_historique/`](supplements/dossier_revue_humaine_historique/).

## Intégrité de la publication

La préparation de ce dépôt GitHub n’a exécuté aucun nouveau calcul de quadrature, programme de partition, flux RNG scientifique ni run P2. Le rapport, l’archive de compléments, la licence DEL, les certificats et les pièces gelées ont été copiés sans modification. Le supplément a uniquement été extrait pour rendre les sources et certificats directement consultables.

## Licence

Les contenus couverts sont publiés sous la **Licence Dynagénèse Éthique (DEL)** personnalisée fournie dans [`03_LICENCE_DEL.pdf`](03_LICENCE_DEL.pdf). Les éléments tiers et faits mathématiques restent soumis à leurs régimes propres.
