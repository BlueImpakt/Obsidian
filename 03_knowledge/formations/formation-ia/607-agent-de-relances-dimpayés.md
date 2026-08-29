---
tags: [formation, millenium]
module: Formation IA
section: "Agents de Productivité"
source_transcript: "6.07 Agent de relances d’impayés.txt"
---

# 6.07 Agent de relances d’impayés

## Resume
- Introduction à la construction d'un agent de recouvrement de créances impayées, destiné à automatiser un travail fastidieux à faible valeur ajoutée humaine.
- Constat de marché sur les retards de paiement (environ 60% des entreprises françaises concernées), un problème fréquent que peu de structures traitent efficacement en interne.
- Exemple concret de use case pour cet agent : cartes bancaires bloquées ou expirées, un problème fréquent dans les ventes en ligne, les programmes d'accompagnement et le freelancing.
- Comparaison chiffrée des coûts de recouvrement : perte de 10-15% via une agence court terme ou email, contre 25-50% des sommes recouvertes pour un cabinet de recouvrement à long terme.
- Réflexion sur le positionnement tarifaire paradoxal de cet agent : générer beaucoup de valeur financière tout en restant difficile à vendre cher, le prix dépendant de la somme à recouvrer.
- Stratégie de vente identifiée : cibler des entreprises peu réceptives à l'IA en général mais intéressées par la simple récupération de sommes dues, une porte d'entrée commerciale alternative.
- Configuration d'un rappel quotidien parcourant un Google Sheet (ou un CRM), une flexibilité qui permet d'adapter la source de données selon l'outil déjà utilisé par l'entreprise.
- Argument différenciant de la valeur humaine simulée : aller au-delà des simples rappels automatiques de logiciels, en filtrant d'abord les transactions ayant échoué.
- Explication du branchement conditionnel : les transactions déjà résolues passent directement, tandis que celles en échec sont transmises à l'agent qui lit les conversations précédentes pour contexte.
- Importance cruciale de vérifier le contexte des échanges précédents avant de relancer : si la personne a déjà donné une date de paiement précise, il ne faut pas la relancer inutilement.
- Présentation de la structure de l'agent : récupération de l'historique des interactions, envoi via Gmail Send, et génération d'un lien de paiement pour faciliter le règlement.
- Explication du choix pédagogique d'utiliser Google Sheets plutôt que Stripe directement pour les données de démonstration, avec annonce de la création d'un lien de paiement Stripe à venir.
- Transition vers la construction pratique du workflow, en commençant par l'analyse de la structure du Google Sheet pour comprendre la logique de déclenchement de l'agent.
- Description des colonnes du Google Sheet de suivi : statut de paiement, numéro de commande, produit, email acheteur, type d'abonnement ou paiement unique.
- Présentation des Agent Logs enregistrant chaque action réalisée par jour, un maximum de contexte pour l'agent avant introduction de l'API Stripe.
- Choix pédagogique de traiter un cas simple applicable aux factures comme aux paiements récurrents d'autres outils, plutôt que la complexité complète de l'API Stripe.
- Reconnaissance de la complexité de l'API Stripe, avec focalisation volontaire sur les liens de paiement pour simplifier, en identifiant d'abord le client lié à la donnée.
- Démonstration de récupération d'une facture Stripe par ID (Retrieve an invoice) pour obtenir toutes les données nécessaires que l'agent utilisera pour évaluer le statut.
- Configuration de récupération des transactions via Get Rows in Sheets, l'action principale pour accéder au système de suivi de paiement dans Google Sheets.
- Configuration du filtrage des transactions à traiter selon la colonne statut (vide) et le type, une étape clé pour cibler uniquement les paiements nécessitant une action.
- Limite de Google Sheets par rapport à Airtable pour le filtrage avancé (pas de formules type 'contains'), nécessitant de travailler avec des cases entières et des critères fixes.
- Recommandation de bonne pratique de test : utiliser un alias email (technique du « plus » sur Gmail) pour rediriger les emails de test vers soi-même plutôt que de vrais destinataires.
- Observation d'un problème de données doublonnées dans les résultats (une facture apparaissant deux fois car déjà payée), nécessitant un filtrage supplémentaire pour l'éviter.
- Recommandation de sécurité en phase de test : éviter les boucles infinies en laissant le workflow aller dans le vide, ou utiliser l'option Execute Once pour limiter les répétitions.
- Configuration d'une condition IF vérifiant si l'objet retourné par GetRowsInSheets n'est pas vide, une logique de branchement essentielle pour la suite du traitement.
- Configuration de la branche de modification via Update Row in Sheet en cas de résultat non vide, pour mettre à jour le statut de la transaction concernée.
- Filtrage par Transaction ID et Transaction Status, avec discussion sur les options en cas de résultats multiples : utiliser un ID différent ou un timestamp pour départager.
- Confirmation de la mise à jour réussie du statut dans le Google Sheet, validant que le workflow peut désormais poursuivre correctement dans sa boucle de traitement.
- Transition vers la présentation des différents outils connectés à l'agent, avec introduction de leur configuration avant explication détaillée du rôle de chacun.
- Configuration du premier outil (logs) permettant à l'agent d'accéder à l'historique des actions passées, filtré précisément par Transaction ID.
- Configuration alternative de recherche d'emails via opérateurs de recherche Gmail (from:adresse) pour ceux préférant cette méthode aux filtres classiques.
- Utilisation d'un outil personnel nommé « Perfect AI Agent Prompt Builder » pour générer le prompt de l'agent de relance avec quatre emails selon des délais et niveaux d'urgence définis.
- Présentation des trois outils de l'agent dans le prompt généré : Log (filtrage par Transaction ID), Read Email (lecture des conversations), Lien Paiement (création de lien de paiement).
- Identification d'une lacune dans le prompt généré (paramètres manquants pour certains outils), avec correction prévue avant application au workflow N8n.
- Configuration de la date actuelle en mode expression ($now) dans le prompt, avec précision que le nom de l'entreprise sera défini ailleurs dans le workflow.
- Correction et clarification du SOP de l'agent en quatre étapes ordonnées : vérifier les logs, lire les emails, obtenir le lien de paiement si nécessaire, puis agir en conséquence.
- Précision de l'usage de la variable FromAI pour préciser le sender lors de la vérification des emails, avec confirmation que le lien de paiement n'est obtenu que si nécessaire.
- Configuration détaillée du paramètre d'identifiant de transaction (sans format spécifique) et de l'adresse email client comme sender pour l'outil Read Email.
- Construction manuelle d'un JSON structuré incluant un timestamp au format ISO et un champ log contenant le contenu des actions effectuées, pour une meilleure fiabilité.
- Principe important : préférer une valeur dynamique fixe plutôt que de laisser l'agent réfléchir sur une information qui ne change pas, réduisant les risques d'erreur.
- Débogage en direct d'un problème de branchement conditionnel persistant en faux, illustrant les difficultés fréquentes de logique conditionnelle lors des tests.
- Utilisation de l'option Always Output Data comme technique de filtrage pour progresser étape par étape dans le débogage du workflow.
- Présentation des environnements Stripe (test, live, et sandboxes multiples) permettant de créer plusieurs environnements de test distincts plutôt qu'un seul.
- Démonstration d'ajout d'un produit Stripe et récupération du Price ID associé, un identifiant crucial pour la suite de la configuration du lien de paiement.
- Vérification et re-import de la clé API sandbox Stripe (légèrement différente de celle initialement utilisée) via import curl pour s'assurer de la bonne configuration.
- Finalisation de la configuration avec le bon Price ID importé, avant lancement d'un premier test de l'agent avec ajout d'une étape de log pour vérifier la sortie.
- Observation du raisonnement de l'agent (Gemini) lors du premier test : vérification des logs vides, puis constat que la transaction n'a pas encore atteint le seuil de relance (J+7).
- Identification d'un problème de calcul de date par l'agent, ne comprenant pas correctement quelle est la date de référence pour déterminer si le délai est atteint.
- Relance complète du flow après ajustement, confirmant que l'agent fonctionne correctement en recherchant dans les logs puis en poursuivant sa logique de traitement.
- Exemple concret de message de relance généré par l'agent (facture 1617, 699€, produit NoCodePro), avec observation qu'un élément attendu (lien) n'a pas été correctement récupéré.
- Diagnostic de l'anomalie : l'agent considère à tort avoir déjà envoyé l'email à cause de la mémoire persistante, nécessitant un reset de mémoire pour retirer ce contexte erroné.
- Confirmation du bon fonctionnement complet après reset de mémoire : recherche log, lecture email, obtention du lien de paiement, envoi de l'email, mise à jour de la Google Sheet.
- Suite du flux réussi : récupération effective du lien de paiement Stripe et envoi de l'email contenant ce lien au destinataire de test configuré.
- Suggestion d'amélioration future : utiliser un Output Parser structuré pour mieux définir le format de réponse de l'agent, plutôt que de parser après coup.
- Finalisation de la configuration du Structured Output Parser (generateFromJSONExample) et confirmation que l'email a bien été envoyé et reçu dans la boîte mail de test.
- Test d'exécution du workflow sans les logs disponibles : l'agent obtient le lien de paiement mais n'a pas lu les emails avant d'envoyer, illustrant l'importance du log pour éviter les doublons.
- Nouveau test avec les logs activés, permettant de vérifier si l'agent évite correctement de renvoyer un email déjà envoyé précédemment.
- Confirmation du bon comportement de l'agent : il détecte qu'un email de rappel a déjà été envoyé à J8 et n'entreprend aucune action supplémentaire, évitant le spam.
- Conclusion du build avec recommandation d'ajouter une mémoire pour tracer les échanges de l'agent, confirmée par la vérification de l'email réellement reçu avec le lien de paiement Stripe.

## Concepts cles
- introduction à l'agent de recouvrement de créances impayées
- constat de marché : ~60% des entreprises françaises concernées par des retards de paiement
- exemple concret de use case : cartes bancaires bloquées ou expirées
- comparaison chiffrée des coûts de recouvrement (10-15% vs 25-50%)
- réflexion sur le positionnement tarifaire paradoxal de l'agent de recouvrement
- stratégie de vente : cibler des entreprises peu réceptives à l'IA via le recouvrement
- configuration d'un rappel quotidien parcourant un Google Sheet (ou CRM alternatif)
- argument différenciant : simuler une valeur humaine au-delà des rappels automatiques standards
- explication du branchement conditionnel selon le statut de transaction
- importance de vérifier le contexte avant relance (éviter les relances inutiles)
- présentation de la structure de l'agent (historique, Gmail Send, lien de paiement)
- choix pédagogique d'utiliser Google Sheets plutôt que Stripe pour la démo
- transition vers la construction pratique via la structure du Google Sheet
- description des colonnes du Google Sheet de suivi des paiements
- présentation des Agent Logs pour maximiser le contexte de l'agent
- choix pédagogique d'un cas simple applicable à divers outils de paiement
- focalisation volontaire sur les liens de paiement Stripe (complexité de l'API)
- démonstration de récupération de facture Stripe par ID
- configuration de récupération des transactions via Get Rows in Sheets
- configuration du filtrage par statut vide pour cibler les paiements à traiter
- limite de Google Sheets vs Airtable pour le filtrage avancé (pas de 'contains')
- recommandation de test : utiliser un alias Gmail (technique du 'plus') pour rediriger les emails de test
- observation d'un problème de données doublonnées nécessitant un filtrage supplémentaire
- recommandation de sécurité en test : éviter les boucles infinies (option Execute Once)
- configuration d'une condition IF vérifiant la non-vacuité de l'objet retourné
- configuration de la branche de modification via Update Row in Sheet
- discussion sur les options de départage en cas de résultats multiples (ID vs timestamp)
- confirmation de la mise à jour réussie validant la poursuite de la boucle
- transition vers la présentation des outils connectés à l'agent
- configuration du premier outil de logs filtré par Transaction ID
- configuration alternative de recherche via opérateurs Gmail (from:)
- utilisation d'un Prompt Builder personnel pour générer un prompt d'agent structuré
- présentation des trois outils de l'agent (Log, Read Email, Lien Paiement)
- identification et correction d'une lacune du prompt généré (paramètres manquants)
- configuration de la date actuelle en mode expression ($now) dans le prompt
- correction et clarification du SOP en quatre étapes ordonnées
- précision d'usage de la variable FromAI pour le sender lors de la vérification
- configuration détaillée des paramètres de transaction et sender pour Read Email
- construction manuelle d'un JSON structuré avec timestamp ISO et champ log
- principe : préférer une valeur dynamique fixe pour une information stable (réduire les erreurs)
- débogage en direct d'un problème de branchement conditionnel persistant
- utilisation de l'option Always Output Data comme technique de filtrage de débogage
- présentation des environnements Stripe multiples (test, live, sandboxes)
- démonstration d'ajout de produit Stripe et récupération du Price ID
- vérification et re-import de la clé API sandbox Stripe
- finalisation de configuration et lancement du premier test avec log de vérification
- observation du raisonnement de l'agent Gemini lors du premier test (seuil J+7)
- identification d'un problème de calcul de date par l'agent
- relance complète du flow confirmant le bon fonctionnement après ajustement
- exemple concret de message de relance généré (facture 699€) avec anomalie de lien manquant
- diagnostic : mémoire persistante causant un faux positif d'envoi déjà effectué
- confirmation du fonctionnement complet après reset de mémoire
- suite du flux réussi avec envoi effectif du lien de paiement Stripe
- suggestion d'amélioration future : Output Parser structuré pour le format de réponse
- finalisation du Structured Output Parser et confirmation de réception d'email
- test sans logs disponibles illustrant le risque de doublons d'envoi
- nouveau test avec logs activés vérifiant l'évitement de doublon d'envoi
- confirmation du bon comportement évitant le renvoi (email déjà envoyé à J8)
- conclusion du build avec recommandation de mémoire pour traçabilité

## Outils mentionnes
- n8n
- Google Sheets
- Gmail
- Stripe
- Airtable
- Gemini

## Tips techniques
- Utiliser un cas d'usage concret et non technique (recouvrement de créances) comme porte d'entrée commerciale vers des entreprises peu réceptives à l'IA
- Toujours vérifier le contexte des échanges précédents avant d'envoyer une relance automatique, pour éviter de relancer une personne ayant déjà donné une date de paiement
- Enregistrer systématiquement les actions réalisées par l'agent dans un journal de logs, pour fournir un contexte historique complet lors des relances suivantes
- Utiliser un alias email via la technique du '+' sur Gmail pour rediriger tous les emails de test vers soi-même sans affecter de vrais destinataires
- Utiliser l'option Execute Once en phase de test pour éviter les boucles infinies lors de déclenchements répétés du workflow
- Utiliser un outil de génération de prompt dédié (Prompt Builder) pour structurer efficacement des prompts d'agents complexes
- Définir dynamiquement mais de façon fixe une information qui ne change pas, plutôt que de laisser l'agent la déduire lui-même, pour réduire les risques d'erreur
- Utiliser l'option Always Output Data comme technique de filtrage lors d'un débogage étape par étape complexe
- Créer plusieurs sandboxes Stripe distinctes pour isoler différents scénarios de test plutôt que de tout mélanger dans un seul environnement
- Réinitialiser la mémoire d'un agent lors des tests répétés pour éviter qu'un contexte résiduel ne fausse son comportement (croire une action déjà effectuée)
- Utiliser un Output Parser structuré dès la conception pour définir précisément le format de réponse attendu de l'agent, plutôt que de parser après coup

## Cas d'usage reels
- [[]]
