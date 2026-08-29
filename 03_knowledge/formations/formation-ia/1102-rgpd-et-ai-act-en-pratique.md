---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un expert de n8n"
source_transcript: "11.02 RGPD et AI Act en pratique.txt"
---

# 11.02 RGPD et AI Act en pratique

## Resume
- Sommaire de la vidéo pratique sur RGPD et AI Act : cadre légal, responsabilités et rôles, principes de conservation, droits des utilisateurs, EU AI Act, directive NIS2, automatisation du nettoyage de données, gestion du consentement.
- Chiffre clé cité en exemple d'application réelle du RGPD : en 2023, Meta a dû payer 1,2 milliard d'euros pour transfert incorrect des données de ses utilisateurs vers les États-Unis, une sanction jugée quasi négligeable au regard des budgets de Facebook.
- Définition du rôle de responsable du traitement : celui qui utilise directement les données et détermine leur stockage et leur traitement, avec obligation de déclaration et de réponse aux droits des personnes selon le RGPD.
- Présentation de la première base légale de traitement des données, la plus générale : le consentement explicite de l'utilisateur informé de la rétention de ses données et de la raison, même banale.
- Présentation de deux autres bases légales : le besoin de service (nécessité déclarée mais sans consentement explicite requis) et l'exécution contractuelle, lorsque les données sont nécessaires à l'accomplissement d'un contrat.
- Présentation de deux bases légales marginales pour le contexte du cours : l'intérêt légitime (exemple non traité en détail) et la sauvegarde des intérêts vitaux, applicable uniquement lorsque la vie d'une personne est en danger.
- Transition vers les droits des utilisateurs à intégrer dans les workflows : droit d'accès, droit de rectification, droit à l'effacement, des droits fondamentaux à prendre systématiquement en compte.
- Recommandation pratique pour les chatbots : toujours prévoir un contact humain ou une bascule vers l'IA, un point de réclamation avec révision humaine manuelle, et le droit à la notification, avant transition vers l'EU AI Act.
- Présentation du niveau de risque élevé de l'EU AI Act, qui concerne souvent directement l'automatisation avec IA/LLM effectuée dans le cours : scoring de CV, qualification de crédit, IA médicale sont cités comme cas typiques concernés.
- Introduction du dernier cadre légal à considérer, la directive NIS2 (Network Information and Security Directive 2), aux règles très similaires aux précédentes mais centrées sur les modalités de notification en cas d'incident.
- Détail sur la NIS2 : obligation de transparence en cas de faille ou fuite de données (plan de réponse, responsable désigné), avec un délai réglementaire à respecter pour répondre à l'ANSSI ou l'autorité équivalente.
- Transition vers la pratique : appliquer le principe de minimisation vu plus tôt en éliminant automatiquement les données non nécessaires, via un exemple de workflow N8n dédié à ce nettoyage automatisé.
- Démonstration du workflow de nettoyage automatique : déclenchement horaire simple, puis récupération des exécutions via le node natif N8n permettant d'agir sur la plateforme elle-même.
- Configuration de la credential nécessaire pour accéder aux exécutions N8n : création d'une nouvelle credential avec compte N8N et clé API générée via le menu N8N API.
- Bonne pratique de sécurité rappelée : renouveler périodiquement les clés API malgré la contrainte que cela représente ; démonstration de création, copie et collage de la clé ainsi que récupération de la base URL nécessaire.
- Présentation des options de filtrage du workflow de nettoyage : possibilité de cibler un workflow ID spécifique ou de filtrer par statut d'exécution (réussi, erreur, en attente), avec recommandation de ne pas utiliser ces filtres par défaut.
- Exemple pratique de suppression automatique dans une Data Table N8n : élimination des lignes créées ou actualisées il y a plus de 335 heures, une méthode automatisée couvrant une partie de la conformité minimisation.
- Nuance sur l'élimination automatique périodique des données : dans la plupart des cas réels, certaines informations doivent être conservées pour que les workflows continuent de fonctionner correctement.
- Présentation du node de hashing/crypto pour les cas où l'information (email, données d'inscription) ne doit pas être conservée en clair : le node crypto permet d'appliquer cette transformation avant stockage.
- Explication de l'usage du hash comme identifiant de traçabilité : au lieu de conserver l'email en clair, on conserve uniquement son hash, permettant de retrouver et journaliser une élimination de données sans exposer l'information d'origine.
- Conclusion sur l'approche du nettoyage automatique comme un cadre Lego réutilisable à personnaliser selon chaque cas spécifique, l'auteur recommandant de partir de cette base théorique et pratique plutôt que de tout réinventer.

## Concepts cles
- plan de la vidéo pratique RGPD/AI Act
- amende de 1,2 milliard d'euros infligée à Meta en 2023 (transfert de données)
- définition du responsable du traitement (obligations)
- base légale du consentement explicite et informé
- bases légales : nécessité de service et exécution contractuelle
- bases légales marginales : intérêt légitime et intérêts vitaux
- droits des utilisateurs à intégrer dans les workflows (accès, rectification, effacement)
- recommandation : contact humain et révision manuelle dans les chatbots
- transition vers l'EU AI Act
- niveau de risque élevé de l'AI Act (scoring CV, crédit, IA médicale)
- directive NIS2 (notification en cas d'incident)
- obligation de transparence et délai de notification NIS2
- introduction du workflow N8n de nettoyage automatique des données
- déclenchement horaire et récupération des exécutions via node N8n natif
- création de credential N8N API pour accéder aux exécutions
- renouvellement périodique des clés API comme bonne pratique de sécurité
- options de filtrage du nettoyage (workflow ID, statut d'exécution)
- suppression automatique par ancienneté dans une Data Table N8n (seuil 335h)
- nuance : conservation nécessaire de certaines données pour le fonctionnement des workflows
- node crypto N8n pour hasher les données sensibles avant stockage
- usage du hash comme identifiant de traçabilité sans exposition des données
- approche Lego réutilisable pour personnaliser le nettoyage automatique selon les cas

## Outils mentionnes
- n8n

## Tips techniques
- Toujours prévoir dans un chatbot un point de contact humain accessible et une possibilité de révision manuelle en cas de réclamation
- Renouveler périodiquement les clés API par mesure de sécurité, malgré la contrainte opérationnelle que cela représente
- Ne pas appliquer de filtre par workflow ID ou statut par défaut sur le nettoyage automatique, pour couvrir l'ensemble des exécutions
- Utiliser un node crypto pour hasher les données personnelles (email) avant stockage lorsqu'elles n'ont pas besoin d'être conservées en clair

## Cas d'usage reels
- [[]]
