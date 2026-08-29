---
tags: [formation, millenium]
module: Formation Vente
section: "Lead Machine"
source_transcript: "14.03 Acheter un nom de domaine + boite mail + chauffe des emails.txt"
---

# 14.03 Acheter un nom de domaine + boite mail + chauffe des emails

## Resume
- Sommaire du module achat de domaine, boîte mail et chauffe des emails : outils pour emails, achat de domaines, comparaison des coûts, utilisation de Mailpool, génération de domaines, configuration email redirect, création d'inbox.
- Présentation des différents outils disponibles pour créer facilement des adresses email, dont l'achat direct de domaines via Waalaxy, une première option parmi plusieurs solutions à comparer.
- Comparaison de prix : Mailpool est environ deux fois moins cher (4$ contre 8$ par mois par adresse) que d'autres solutions, un écart significatif à partir de 5-10 adresses, avec démonstration de création de compte sur mailpool.ai.
- Démonstration de génération de domaines secondaires à partir d'un domaine principal (exemple : « done4u.ai » générant « getdone4u », « trydone4u »), pour diversifier l'infrastructure email sans utiliser le domaine principal.
- Démonstration pratique de sélection des adresses email générées à partir de variantes de domaine, avec recommandation de décocher celles qui ne sont pas nécessaires avant validation.
- Précision sur le formulaire d'informations d'entreprise demandé lors de l'achat de domaine : il ne sert pas à la facturation mais à la déclaration légale du propriétaire du nom de domaine.
- Exemple de coût pour trois noms de domaine (45€), avec recommandation de démarrer simplement avec un ou deux domaines seulement, tout en investissant davantage dans le nombre d'adresses email associées.
- Démonstration de configuration d'une inbox : ajout de signature par défaut et configuration du forwarding des réponses vers une adresse centrale (exemple hello@Neocell).
- Calcul de volume de prospection à l'échelle : avec 250 emails/jour par adresse multipliés par 30 adresses, le volume quotidien devient considérable, une stratégie réservée aux GTM Engineers avec budget conséquent.
- Rappel des détails à personnaliser lors de la configuration d'inbox (photo de profil, signature) avant validation de la facturation et accès aux détails d'édition de l'adresse créée.
- Démonstration de connexion d'une adresse Mailpool à Lemlist via les paramètres d'envoi d'email, une étape technique nécessaire pour relier l'infrastructure email créée à l'outil de prospection.
- Confirmation visuelle de la connexion réussie de l'adresse à Lemlist, avec vérification de l'alias de l'adresse créée dans l'interface, validant l'intégration entre les deux outils.
- Présentation de la fonctionnalité d'étiquetage des emails envoyés par Lemlist, permettant de filtrer et distinguer les envois automatisés, ainsi que la configuration du domaine de suivi personnalisé.
- Démonstration de validation de configuration DNS pour l'ensemble des boîtes mail d'une équipe sur un même domaine, avec précision que le déploiement complet peut prendre plusieurs heures.
- Introduction de ZapMail comme alternative à Mailpool, avec inconvénient principal : contrairement à Mailpool où l'achat se fait boîte par boîte, ZapMail impose des abonnements groupés d'un coup.
- Présentation d'Office 365 comme alternative pour les préférences d'écosystème, et introduction de la possibilité d'acheter des boîtes mail pré-chauffées pour éviter les cinq semaines de chauffe habituelles.
- Comparaison de tarifs entre deux options (4$ vs 3,50$ par boîte mail), avec précision que Mailpool permet l'achat à l'unité tandis que l'alternative impose un minimum de 10 boîtes mail par commande.
- Reconnaissance que le choix entre Mailpool et ZapMail relève des préférences personnelles, avec mention d'experts reconnus préférant chacune des deux options, invitant à tester selon son propre ressenti.
- Analyse d'un score de chauffe imparfait causé par une interruption d'envoi pendant une certaine période, avec constat rassurant que le taux de spam reste très faible malgré cette pause.
- Démonstration de configuration du warm-up une fois l'adresse connectée automatiquement à Lemlist : définition d'une quantité cible d'envois progressifs pour le processus de chauffe.
- Explication du fonctionnement technique du warm-up (LemWarm) : envoi d'emails vers un réseau d'adresses partenaires utilisant le même système, créant des interactions positives simulées pour construire une réputation.
- Explication du mécanisme d'ajustement dynamique du warm-up : en cas de détection de spam sur un envoi, le système redescend temporairement en volume avant de reprendre sa progression, une régulation automatique de sécurité.
- Démonstration du démarrage effectif du processus de warm-up (LemWarm) avec suivi visuel des premiers emails envoyés, invitant à laisser le processus progresser graduellement dans le temps.
- Précision qu'avec ZapMail, il est possible de contourner le processus de chauffe classique car les emails sont livrés déjà chauds, permettant de démarrer immédiatement la prospection.
- Démonstration de l'achat de boîtes mail pré-chauffées via ZapMail, avec précision importante qu'elles reposent sur des noms de domaine déjà existants, adaptés surtout à une prospection ciblant les États-Unis.
- Conclusion sur ZapMail comme équivalent globalement similaire à Mailpool (question de préférence personnelle), avec démonstration de l'ajout de mailbox supplémentaires au tarif de 3,50$.

## Concepts cles
- plan de présentation du module achat de domaine et chauffe des emails
- présentation des outils d'achat de domaine (Waalaxy en première option)
- comparaison de prix Mailpool (2x moins cher, ~4$/mois) vs alternatives
- démonstration de génération de domaines secondaires variés à partir d'un domaine principal
- démonstration de sélection des adresses email générées (décocher les inutiles)
- précision : formulaire d'informations d'entreprise sert à la déclaration légale, pas à la facturation
- exemple de coût (45€ pour 3 domaines) et recommandation de démarrer avec 1-2 domaines
- démonstration de configuration d'inbox (signature, forwarding vers adresse centrale)
- calcul de volume à l'échelle (250 emails/jour x 30 adresses)
- rappel des détails de personnalisation d'inbox (photo, signature) avant facturation
- démonstration de connexion d'une adresse Mailpool à Lemlist
- confirmation de connexion réussie entre l'adresse email et Lemlist
- fonctionnalité d'étiquetage des emails envoyés et domaine de suivi personnalisé
- démonstration de validation DNS pour toutes les boîtes mail d'un domaine (délai de déploiement)
- introduction de ZapMail : inconvénient de l'achat groupé par abonnement (vs Mailpool à l'unité)
- Office 365 comme alternative et option de boîtes mail pré-chauffées (5 semaines économisées)
- comparaison tarifaire (4$ vs 3,50$/boîte) et minimum de 10 boîtes pour l'alternative
- reconnaissance : choix Mailpool vs ZapMail selon préférence personnelle
- analyse d'un score de chauffe dégradé par une interruption d'envoi
- démonstration de configuration du warm-up avec quantité cible progressive
- fonctionnement technique du warm-up via réseau d'adresses partenaires
- mécanisme d'ajustement dynamique du warm-up en cas de spam détecté
- démonstration du démarrage du warm-up avec suivi visuel progressif
- précision : ZapMail permet de démarrer immédiatement sans chauffe (emails déjà chauds)
- démonstration d'achat de boîtes pré-chauffées ZapMail (adaptées aux USA, domaines existants)
- conclusion ZapMail comme équivalent de Mailpool et démonstration d'ajout de mailbox

## Outils mentionnes
- Mailpool
- Waalaxy
- Lemlist
- ZapMail
- Office 365
- LemWarm

## Tips techniques
- Comparer les tarifs des fournisseurs d'adresses email (Mailpool étant environ deux fois moins cher) avant de choisir, l'écart devenant significatif à volume
- Générer plusieurs domaines secondaires variés à partir du domaine principal pour diversifier l'infrastructure email sans exposer le domaine principal
- Démarrer avec seulement un ou deux noms de domaine, sans complexifier inutilement, en concentrant plutôt l'effort sur le nombre d'adresses email
- Acheter des boîtes mail pré-chauffées pour éviter les 5 semaines habituelles de chauffe manuelle, moyennant un coût supplémentaire

## Cas d'usage reels
- [[]]
