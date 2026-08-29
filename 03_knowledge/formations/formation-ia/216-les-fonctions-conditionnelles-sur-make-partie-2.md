---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.16 Les fonctions conditionnelles sur Make • Partie 2.txt"
---

# 2.16 Les fonctions conditionnelles sur Make • Partie 2

## Resume
- Introduction aux opérateurs AND et OR non encore vus, complétant les opérateurs égal et différent (point d'exclamation égal, signifiant « n'est pas égal ») déjà présentés précédemment.
- Démonstration de l'opérateur différent (!=) : 1 n'est pas égal à 2 donne faux (car ce n'est pas l'inégalité recherchée), mais combiné avec 3 égal à 3, le résultat global devient vrai, illustrant la logique combinée AND.
- Généralisation de l'usage des opérateurs AND/OR à d'autres types de fonctions (texte, etc.), l'auteur invitant à explorer ces possibilités créativement dans de futures automatisations pratiques.
- Explication des valeurs booléennes (vrai/faux) appliquées à un cas concret : une condition IF avec « contains » (fonction de manipulation de texte détaillée plus tard) illustre l'usage pratique de ces booléens.
- Démonstration du résultat d'un routeur : la voie 1 est sélectionnée car c'est la première à valider l'opération (le texte « Ousmane » est bien contenu dans la valeur testée), avec précision sur la nuance entre opérateur égal et vérification de vérité.
- Explication de la détection automatique de type par Make : « True » écrit avec des guillemets est interprété comme une string (texte), tandis que sans guillemets, il est reconnu comme une véritable valeur booléenne, une distinction subtile mais importante.
- Démonstration de la logique de routage selon une condition « égal à faux » : la donnée testée étant vraie, elle emprunte la voie 2 (et non la voie 1 qui cherche spécifiquement le cas faux), illustrant la précision nécessaire dans la définition des conditions.
- L'auteur teste avec honnêteté une valeur peu connue (« Erase »britannique) sans être certain de son usage exact, illustrant une approche pédagogique transparente face aux fonctionnalités moins courantes de l'outil.

## Concepts cles
- introduction des opérateurs AND et OR (complément à égal/différent)
- démonstration pratique de l'opérateur différent combiné avec AND
- généralisation des opérateurs AND/OR à divers types de fonctions
- exemple de booléen appliqué à une condition 'contains'
- exemple de sélection de voie 1 dans un routeur via 'contains'
- distinction entre string 'True' (texte) et booléen True (valeur)
- exemple de routage selon condition 'égal à faux'
- transparence pédagogique face à une fonctionnalité peu utilisée (Erase)

## Outils mentionnes
- Make

## Tips techniques
- Attention à la distinction entre écrire 'True' comme texte (avec guillemets) et comme valeur booléenne réelle dans Make

## Cas d'usage reels
- [[]]
