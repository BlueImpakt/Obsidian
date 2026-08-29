---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.07 Les Merge, Filtres, IF, Switch nodes dans N8N.txt"
---

# 3.07 Les Merge, Filtres, IF, Switch nodes dans N8N

## Resume
- Introduction aux nodes IF, FILTER et SWITCH sur N8n, avec un schéma pédagogique préalable illustrant une liste de 5 personnes récupérée de Google Sheets pour poser les bases conceptuelles avant la pratique.
- Explication de la logique du node IF : il fonctionne comme une combinaison de conditions, pouvant être simple (une seule condition, ex: prénom égal à X) ou plus complexe selon le besoin.
- Différence clé entre IF et Filter : contrairement à IF qui laisse continuer tous les éléments avec deux branches possibles, Filter agit comme un bloqueur pur, stoppant purement et simplement ceux qui ne remplissent pas le critère.
- Exemple concret d'usage à grande échelle : un processus de création de contenu différent pour quatre plateformes (TikTok, YouTube, Instagram, etc.), chacune nécessitant une branche de traitement distincte.
- Introduction du node Merge, permettant de combiner différentes branches et d'unifier les réponses en un seul flux, essentiel après avoir divisé un scénario en plusieurs voies parallèles.
- Conclusion de l'introduction schématique, transition vers la pratique du node IF en premier, suivi du Filter, puis des autres nodes de manipulation de données dans N8n.
- Présentation de 4 profils fictifs issus d'un CRM de démonstration (Marguerite Didier chez Hermès, Jean-Pascal Dumont chez Pasquier, etc.) servant d'exemple concret pour illustrer les nodes de filtrage suivants.
- Rappel de la règle d'indexation en programmation : le chiffre 0 correspond au premier élément d'une liste, illustré par la sélection et l'exécution récupérant Jean Dupont, 55 ans, CEO d'Anon.
- Présentation du fonctionnement du module IF : il produit deux résultats possibles (deux branches) selon qu'une condition est vraie ou fausse, différent du concept de filtre équivalent sur Make.
- Démonstration pratique : les quatre lignes de Google Sheets sont retournées sans filtrage préalable, puis l'objectif devient de filtrer entre les cas « s'appelle Jean Dupont » et « ne s'appelle pas Jean Dupont ».
- Présentation rapide des opérateurs de string du node IF : existence de valeur, non-existence, valeur vide, avec les branches vrai/faux correspondantes pour chaque cas de test.
- Présentation des opérateurs contains/does not contain, commence par/ne commence pas par, termine par/ne termine pas par, ainsi que le support des expressions régulières (regex).
- Présentation des opérateurs numériques (plus grand/petit que, plus grand/petit ou égal) et des opérateurs de date (après/avant), une gamme complète pour toutes les comparaisons possibles.
- Présentation des opérateurs pour les listes (nombre d'entrées supérieur/inférieur à X) et pour les objets (existence, vide/non-vide), complétant le panorama des types de comparaison disponibles.
- Filtrage concret pour identifier les positions exécutives (CEO Jean Dupont chez Danone, directeur marketing Michel Robert chez ETAM), en excluant les deux autres profils non pertinents pour déclencher des actions ciblées.
- Construction d'un prompt IA personnalisé ciblant et flattant la position exécutive du destinataire, avec connexion d'un modèle (démonstration de connexion credential Anthropic sur N8n).
- Démonstration pratique de connexion API Anthropic à N8n : création d'une clé API nommée explicitement pour traçabilité, copie et intégration dans l'interface, finalisant la connexion entre les deux plateformes.
- Sélection du modèle Claude Sonnet 4 pour la chain configurée, avec anticipation de la duplication de cette structure pour créer une nouvelle instruction personnalisée pour le second profil exécutif.
- Résultat des deux messages personnalisés générés pour les CEO de Danone et ETAM, jugés relativement bien construits, avec une petite retouche à faire sur un exemple générique non désiré.
- Intervention du module Merge pour rassembler les deux canaux de traitement parallèles (les deux messages générés) en un flux unifié, avec démonstration visuelle des deux inputs distincts fusionnés.
- Démonstration du node Filter avec l'exemple « is not equal to Jean-Pascal » : sélection du prénom comme critère, filtrant pour exclure ce profil spécifique et ne laisser passer que les autres.
- Introduction du node Switch pour aller plus loin que le simple vrai/faux : il permet une granularité supérieure en routant les éléments vers plusieurs voies distinctes selon différentes valeurs possibles.
- Présentation de l'option Fallback Output du Switch : permet d'ajouter une voie de sortie séparée pour capturer les éléments correspondant à une condition spécifique (exemple : ceux allant vers Danone).
- Démonstration concrète du Switch avec trois voies distinctes (Pasquier, Danone, Hermès) permettant de dispatcher les personnes selon leur réponse à une question, une puissance bien supérieure au simple IF à deux voies.
- Présentation de l'option d'envoi vers tous les Matching Outputs : utile si un élément correspond à plusieurs critères simultanément (exemple : appartenance à deux entreprises), pour éviter qu'il ne soit envoyé qu'à un seul.
- Débogage en direct d'une condition Switch mal configurée (entreprise égale à Pasquier), illustrant le processus itératif de correction d'erreur de configuration d'un critère de routage.
- Démonstration de création d'un fallback pour le Switch : dupliquer le node et y définir la valeur restante (ni Danone ni Hermès), capturant tous les cas non explicitement couverts par les branches définies.
- Justification de la présentation condensée de ces nodes : ils seront revus régulièrement dans des applications concrètes tout au long de la formation, évitant une vidéo trop longue sur chacun individuellement.

## Concepts cles
- introduction pédagogique aux nodes IF/FILTER/SWITCH
- logique du node IF (combinaison de conditions simples ou complexes)
- différence clé IF (deux branches) vs Filter (bloqueur pur)
- exemple d'usage à grande échelle : branches par plateforme de contenu
- node Merge pour combiner et unifier plusieurs branches
- annonce du plan pratique (IF puis Filter puis autres)
- présentation de profils fictifs du CRM de démonstration
- rappel de l'indexation à partir de 0 (règle de programmation)
- fonctionnement du module IF (deux résultats possibles)
- comparaison avec le filtre Make
- exemple pratique de filtrage sur un critère nominal (Jean Dupont)
- opérateurs de string du node IF (existence, vide)
- opérateurs contains, commence par, termine par, regex
- opérateurs numériques et de date pour le node IF
- opérateurs pour listes (nombre d'entrées) et objets (existence)
- filtrage concret par position exécutive (CEO, directeur)
- prompt personnalisé ciblant les exécutifs + connexion credential Anthropic
- connexion pratique API Anthropic à N8n (nommage explicite de la clé)
- sélection de Claude Sonnet 4 et anticipation de duplication de structure
- résultat de messages personnalisés générés pour deux profils exécutifs
- utilisation pratique du module Merge pour unifier deux flux parallèles
- démonstration Filter avec opérateur 'is not equal to'
- introduction du Switch pour un routage à granularité fine (au-delà du vrai/faux)
- option Fallback Output du Switch
- démonstration Switch à trois voies (vs IF limité à deux)
- option Matching Outputs multiples pour éviter les blocages sur critères ambigus
- débogage en direct d'une condition Switch mal configurée
- création pratique d'un fallback par duplication de node
- justification pédagogique d'une présentation condensée

## Outils mentionnes
- n8n
- Google Sheets
- Make
- Anthropic
- Claude

## Tips techniques
- Nommer explicitement chaque clé API créée pour en faciliter la gestion et suppression future

## Cas d'usage reels
- [[]]
