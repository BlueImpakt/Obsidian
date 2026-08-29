---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.24 Le module Code dans N8N.txt"
---

# 3.24 Le module Code dans N8N

## Resume
- Introduction au node Code sur N8n, présenté comme essentiel mais largement sous-utilisé par les non-codeurs venus vers l'automatisation IA, l'auteur se reconnaissant lui-même dans ce profil.
- Justification du besoin de contrôle : on ne peut pas laisser l'intégralité de la fiabilité aux agents IA car ils peuvent se tromper ou ne pas respecter le formatage exact, un agent contrôleur supplémentaire consommant inutilement des ressources.
- Présentation du module Code de N8n permettant de coder en JavaScript (bientôt Python), offrant un contrôle total et constant sur le flux de données avec plus de flexibilité que les nodes standards.
- Discussion des inconvénients de faire appel systématiquement à un LLM plutôt qu'au code : latence accrue due au temps de traitement du modèle, même si les performances s'améliorent constamment.
- Encouragement à exploiter la puissance des LLM en leur fournissant un maximum de contexte en entrée, avec annonce d'un exemple pratique à venir pour illustrer ce principe.
- Démonstration à venir : construire quasiment une application entière avec un petit bout de code intégré dans un workflow N8n, illustré via une API météo marine disponible publiquement.
- Présentation de WorldWeatherOnline.com : API payante avec un quota gratuit de 100 requêtes par jour, suffisant pour tester et reproduire l'exemple, avec accès spécifique à la carte marine.
- Configuration pratique avec la latitude/longitude de la plage personnelle de l'auteur (Cape Dale, Portugal), une localisation appréciée pour le surf et le kitesurf, servant d'exemple concret.
- Illustration ludique du fonctionnement des coordonnées géographiques : montrer comment un changement de latitude déplace le point ciblé, potentiellement en pleine mer si mal calibré.
- Présentation des données riches retournées par l'API : marées (basses/hautes avec horaires) et swells (ensembles de vagues, exemple 0,7), un volume important de données brutes.
- Objectif de demander à Claude d'extraire les données vraiment importantes parmi ce volume brut, en commençant par construire l'appel API avec les paramètres de latitude/longitude configurables.
- Configuration des paramètres de l'API : format horaire (12h américain vs 24h français/européen), granularité temporelle (1h, 3h, 6h), inclusion des marées, et langue des résultats (français choisi).
- Validation de la configuration complète des paramètres (TP, langue FR) avant de présenter le flow pré-construit préparé par l'auteur pour la démonstration à venir.
- Explication du choix pédagogique délibéré d'utiliser un LLM plutôt qu'une API de géocodage (comme Google Maps) pour convertir une adresse en coordonnées, à des fins de démonstration.
- Message clé : on n'est pas obligé d'utiliser systématiquement des LLM/agents IA pour tout, mais on peut les réserver à une petite partie très peu coûteuse en ressources, comme l'extraction de coordonnées.
- Détail du prompt minimal utilisé : « extraire la latitude et la longitude de l'endroit trouvé sur le message de l'utilisateur, répondre uniquement avec le combo lat, lon et rien d'autre », illustrant la simplicité extrême possible.
- Démonstration du chat input transmettant la valeur extraite (coordonnées) directement à l'API via le paramètre Q (query) dans l'URL de la requête HTTP.
- Configuration technique de la référence dynamique avec accolades pour récupérer la valeur générée, soit via Basic LLM Chain, soit directement via json.text pour cibler le node précédent.
- Test en direct de l'appel API avec un exemple de localisation (Viana do Castelo), rencontrant un petit blocage temporaire nécessitant de relancer le processus.
- Récupération réussie de toutes les données volumineuses de l'API, avec constat qu'elles sont difficiles à lire pour un public non expert des termes marins spécialisés.
- Objectif final : utiliser le node Code pour créer un système algorithmique fixe (basé sur une structure de données stable de l'API) qui reformate intelligemment les données brutes en résultat exploitable.
- Début de rédaction du prompt destiné à générer le code JavaScript du node Code : définition d'un rôle d'expert en création de nodes code N8n en JavaScript.
- Poursuite du prompt : objectif de faciliter la lisibilité des données retournées par une API, rédigé progressivement mot par mot pour illustrer le processus de construction.
- Précision du contexte du prompt : faciliter la compréhension des données pour savoir quand aller surfer, en se basant sur les données de l'API Weather Marine Map présentée précédemment.
- Suite du prompt : demande de fournir les meilleures heures pour aller surfer dans la journée, accompagnées d'une note sur 10 pour évaluer la qualité des conditions.
- Poursuite de la construction du prompt : demande de notes sur 10 pour plusieurs critères distincts (vague, météo, courant, vent), permettant une évaluation multi-dimensionnelle des conditions de surf.
- Enrichissement du prompt avec l'ajout de smileys indiquant visuellement s'il faut aller surfer ou non, une demande d'utiliser des mots sympas et amusants pour rendre le résultat engageant.
- Objectif de rendre la donnée technique lisible et pertinente pour le plus grand nombre, avec exemple humoristique proposé : référence au film Brice de Nice quand il n'y a pas de vague.
- Finalisation de l'instruction : demander de créer un JSON de sortie lisible et exploitable, prêt à être utilisé dans un front-end d'application, clôturant la construction du prompt complet.
- Envoi du JSON d'entrée complet au modèle avec le prompt construit, laissant l'IA travailler avec le contexte fourni pour générer le code JavaScript demandé pour le node Code.
- Résultat de la génération de code par Claude, l'auteur exprimant sa préférence marquée pour Claude par rapport à ChatGPT, particulièrement pour les tâches de génération de code.
- Justification de l'intérêt du projet : rendre une application beaucoup plus agréable à utiliser, les applications de surf étant souvent difficiles à comprendre pour les débutants non familiarisés.
- Démonstration pratique d'insertion du code généré dans le node Code de N8n, avec test immédiat sur l'exemple de Viana do Castelo déjà utilisé précédemment.
- Rencontre d'un bug dans le code généré, résolu simplement en copiant le message d'erreur et en le transmettant directement à Claude pour qu'il corrige lui-même le problème identifié.
- Souligne l'accessibilité de cette approche : pas besoin de savoir coder soi-même, l'IA gère la correction, la maîtrise du code venant progressivement avec la pratique et l'usage répété.
- Suivi du raisonnement de l'IA en train de corriger le code : elle relit, vérifie sa compréhension, applique les modifications nécessaires et confirme la correction effectuée.
- Résultat final réussi et amusant : toutes les valeurs formatées avec humour (« sec comme un toit tequila », références marrantes), illustrant le succès de la transformation des données brutes en contenu ludique.
- Analyse de la structure finale obtenue : marées (tides) et prévisions (forecasts) organisées jour par jour, avec heure de surf idéale à midi pour chaque prévision détaillée.
- Confirmation du bon fonctionnement complet : le système indique chaque jour le meilleur moment pour surfer, une donnée directement réutilisable dans une véritable application front-end.
- Aperçu du potentiel : cette structure de données bien formatée pourrait constituer le cœur d'une véritable application, ne nécessitant plus que la mise en forme visuelle des données déjà propres.
- Bilan de la transformation réussie : un flux de données illisible et incompréhensible pour la majorité a été converti en informations exploitables, sans aucune intervention manuelle de codage.
- Encouragement final à expérimenter avec le node Code, à challenger l'IA sur différents cas d'usage pour en tirer pleinement profit dans ses propres automatisations.
- Conclusion sur l'absence de limitation réelle du node Code, la seule contrainte étant le temps investi à l'utiliser et à apprendre à en tirer parti efficacement.

## Concepts cles
- introduction au node Code (sous-utilisé par les non-codeurs)
- limite de fiabilité des agents IA justifiant un contrôle par code
- module Code N8n (JavaScript, bientôt Python) pour un contrôle total du flux
- inconvénient de latence lié à l'usage systématique d'un LLM
- importance de fournir un maximum de contexte aux LLM
- construction d'une application via API météo marine (WorldWeatherOnline)
- WorldWeatherOnline (100 requêtes gratuites/jour) et carte marine
- exemple concret de coordonnées géographiques (plage au Portugal)
- illustration pédagogique des coordonnées latitude/longitude
- données riches de l'API météo marine (marées, swells)
- extraction sélective des données importantes via Claude
- configuration des paramètres API (format horaire, granularité, langue)
- validation de la configuration avant présentation du flow
- choix pédagogique du LLM plutôt qu'une API de géocodage classique
- principe : réserver le LLM à des sous-tâches ciblées peu coûteuses
- exemple de prompt minimal et contraint pour extraction de coordonnées
- transmission de la valeur extraite via paramètre Q dans l'URL
- configuration de la référence dynamique (Basic LLM Chain vs json.text)
- test en direct avec Viana do Castelo (petit blocage résolu)
- récupération de données volumineuses difficiles à lire pour non-experts
- objectif : système algorithmique fixe via node Code pour reformater les données
- rédaction du prompt : rôle d'expert en code N8n JavaScript
- poursuite du prompt : objectif de lisibilité des données API
- contexte du prompt : aide à la décision pour le surf via l'API marine
- demande de note sur 10 pour évaluer les conditions de surf par créneau horaire
- notes sur 10 pour critères multiples (vague, météo, courant, vent)
- ajout de smileys et ton amusant pour rendre le résultat engageant
- objectif de lisibilité grand public avec référence humoristique (Brice de Nice)
- finalisation du prompt : JSON de sortie prêt pour un front-end
- envoi du JSON d'entrée et génération du code par l'IA
- préférence affirmée pour Claude vs ChatGPT sur le code
- justification : rendre une application de surf accessible aux débutants
- insertion pratique du code généré et test sur Viana do Castelo
- résolution de bug en transmettant simplement le message d'erreur à l'IA
- accessibilité de l'approche sans compétence de code préalable
- observation du raisonnement de l'IA lors de la correction
- résultat final humoristique et bien structuré
- structure finale organisée par jour (tides, forecasts)
- validation finale : données réutilisables dans une application
- potentiel de base pour une application complète
- bilan : transformation de données illisibles sans codage manuel
- encouragement à expérimenter et challenger l'IA avec le node Code
- conclusion : absence de limitation réelle, seul le temps d'apprentissage compte

## Outils mentionnes
- n8n
- WorldWeatherOnline
- Claude
- Google Maps
- ChatGPT

## Tips techniques
- Réserver l'usage de LLM aux sous-tâches spécifiques peu coûteuses plutôt que de tout automatiser via IA systématiquement
- Rédiger des prompts LLM minimalistes et strictement contraints (format de sortie unique) pour des sous-tâches simples et rapides
- Copier directement le message d'erreur reçu et le transmettre à l'IA pour qu'elle corrige elle-même le code buggé
- Expérimenter librement avec le node Code en challengeant l'IA sur divers cas d'usage pour en tirer le meilleur parti

## Cas d'usage reels
- [[]]
