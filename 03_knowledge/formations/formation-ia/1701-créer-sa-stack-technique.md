---
tags: [formation, millenium]
module: Formation IA
section: "Claude Code"
source_transcript: "17.01 Créer sa stack technique.txt"
---

# 17.01 Créer sa stack technique

## Resume
- Sommaire du module créer sa stack technique avec Claude Code : introduction, importance de la planification, éviter le piège de la solution, les 5 questions essentielles, identifier un problème douloureux, stratégie B2B vs B2C.
- Rassurance introductive pour les non-développeurs : les concepts techniques à venir seront dédiabolisés et abordés progressivement pour éviter toute intimidation face à la stack technique.
- Critique du piège classique du fondateur SaaS focalisé sur la solution technique plutôt que sur la validation de la douleur réelle du problème, un phénomène amplifié par la ruée générale vers le SaaS.
- Exemple personnel de résolution de problème authentique : en résolvant son propre problème lié au TDAH, l'auteur résout naturellement celui d'autres personnes partageant la même condition, avec une compréhension plus fine que quiconque.
- Positionnement des besoins ciblés dans la pyramide de Maslow : viser les besoins primaires humains (se nourrir, se reposer) plutôt que des besoins secondaires, un facteur de robustesse du marché ciblé.
- Argument en faveur du B2B sur le B2C : une entreprise perçoit une dépense comme un investissement, contrairement à un particulier, facilitant la conversion si le problème ciblé est suffisamment large et pertinent pour elle.
- Anecdote personnelle sur une application dans le top 5 de l'App Store en 2020 (pendant le Covid), un jeu de soirée, illustrant un succès produit antérieur de l'auteur peu connu de son audience.
- Principe d'alignement entre prix et intensité de la douleur résolue : même un problème mineur (non vital) reste un vrai problème, à condition que le prix du service soit calibré à son niveau réel de douleur.
- Explication de l'impact supérieur d'un outil remplaçant un logiciel métier réglementaire coûteux, comparé à un simple outil d'organisation comme Notion facturé 10€, en raison du coût élevé de l'alternative.
- Constat de l'évolution du marché avec l'IA : le rythme d'implémentation continue a réduit l'importance perçue des tests utilisateurs classiques, une tendance notable même si l'auteur en recommande encore l'usage.
- Recommandation de clarté dans le développement produit pour ne pas noyer les utilisateurs dès le premier jour avec trop de fonctionnalités, illustrée par le succès de l'application « KLEI » citée en exemple de checklist parfaite.
- Exemple de valeur positive du partage : les personnes qui partagent leurs dashboards Notion parfaitement conçus s'organisent et créent leurs propres mini-applications dans un écosystème fermé et protégé.
- Constat que peu de créateurs d'applications pensent à la monétisation malgré une volonté de payer réelle des utilisateurs ; recommandations : abonnement mensuel et essai gratuit pour maximiser l'adoption.
- Stratégie de capitalisation sur l'engagement immédiat : encourager un abonnement de longue durée au moment où l'acheteur est le plus motivé (« craquage »), sécurisant la trésorerie indépendamment de l'usage réel ultérieur.
- Recommandation stratégique d'éviter de remplacer un outil existant (résistance du DSI et des décideurs) mais plutôt de venir en complément de la myriade d'outils déjà utilisés, une adoption bien plus facile.
- Illustration de la réutilisabilité d'un outil s'interfaçant avec un logiciel métier déjà maîtrisé (exemple : Cegid pour la comptabilité), permettant de dupliquer l'application sans devoir la refaire à chaque fois.
- Introduction de React comme framework basé sur JavaScript, divisant l'application en composants uniques et réutilisables pour gagner en efficacité de développement.
- Présentation d'entreprises majeures utilisant React (Netflix, Airbnb, Discord), expliquant pourquoi l'IA maîtrise si bien ce framework : un entraînement massif sur des milliers de projets React existants.
- Explication du fonctionnement des composants React (header, card, button) et de la mise à jour partielle de page sans rechargement complet, garantissant fluidité et réactivité de l'application.
- Présentation de Next.js, développé par Vercel, comme framework React optimisé par défaut (streaming HTML, composants serveurs, rendu client/serveur, gestion CSS intégrée).
- Liste d'entreprises utilisant Next.js (Dice, Notion, Nike, Sonos, Audible), confirmant la robustesse de la technologie, avec métaphore automobile introduisant les composants complémentaires à venir.
- Introduction de Tailwind CSS comme framework CSS alternatif à l'écriture de CSS personnalisé dans des fichiers séparés, simplifiant le style visuel des applications pour les débutants en développement.
- Transition vers les librairies design pour organiser facilement les composants UI, avant présentation du back-end comme deuxième grande brique de la stack technique (bases de données et actions serveurs).
- Distinction claire entre base de données (stockage des données) et back-end (exécution des actions côté serveur), les deux éléments permettant à une application d'être dynamique et interactive.
- Présentation des fonctionnalités back-end courantes : déclenchement d'actions programmées (déjà vu dans N8n), stockage de fichiers, mise en cache automatique, mises à jour temps réel, intégrations frameworks.
- Distinction technique importante entre database storage (données structurées, lignes de base de données) et file storage (fichiers, vidéos, images), deux notions à ne pas confondre dans une stack.
- Présentation de Neon comme base de données Postgres, l'une des trois approches différentes de base de données évoquées (aux côtés de Convex), sans entrer dans un détail technique excessif.
- Présentation de Supabase comme solution tout-en-un intégrant base de données, stockage, Edge Functions et fonctionnement temps réel, avec structure tarifaire équivalente à d'autres solutions comparées.
- Présentation de Clerk comme solution d'authentification simplifiée avec support SSO pour de nombreuses applications tierces (comme Linear), avec tarif de 20$/mois pour 50 000 utilisateurs mensuels actifs.
- Transition vers BetterAuth, présenté comme alternative préférée par l'auteur à Clerk, proposant une authentification tout aussi simplifiée à intégrer dans une application.
- Détail des avantages de BetterAuth : 40 fournisseurs sociaux d'authentification supportés, compatibilité avec toutes les stacks techniques, gestion automatique des credentials, installation facile.
- Présentation des tarifs de paiement en ligne pour l'Europe et le Royaume-Uni (1,5%+0,25€ vs 2,5%+0,25%), une comparaison fondamentale pour choisir son outil de réception de paiements.
- Recommandation de Polar.sh plutôt que Stripe pour simplifier la gestion des paiements et éviter la complexité des déclarations fiscales multi-pays, avec un tarif de 4% + 40 centimes.
- Récapitulatif de la configuration d'une stack technique complète, avec présentation du pipeline de build en étapes : planification, setup de Claude Code, premier prompt réel, vérification de conformité.
- Introduction de Git comme outil de stockage de code en ligne collaboratif : téléchargement, édition, création de branches, et fusion (merge) vers la version live une fois validées collectivement.

## Concepts cles
- plan de présentation du module de création de stack technique
- rassurance introductive pour les non-développeurs face aux concepts techniques
- critique du piège de la focalisation sur la solution plutôt que sur la douleur validée
- exemple personnel : résoudre son propre problème (TDAH) pour mieux servir une audience similaire
- positionnement des besoins ciblés selon la pyramide de Maslow (besoins primaires)
- argument B2B vs B2C : l'entreprise investit, le particulier dépense
- anecdote personnelle : application dans le top 5 App Store en 2020 (jeu de soirée)
- principe d'alignement entre prix du service et intensité réelle de la douleur résolue
- impact supérieur d'un outil remplaçant un logiciel métier réglementaire coûteux (vs Notion)
- constat de la réduction des tests utilisateurs classiques face au rythme d'implémentation IA
- recommandation de clarté et simplicité initiale (exemple de l'application KLEI)
- exemple de valeur du partage de dashboards Notion dans un écosystème protégé
- constat du manque de focus sur la monétisation, recommandation abonnement + essai gratuit
- stratégie de capitalisation sur l'engagement immédiat (abonnement longue durée)
- stratégie de complémentarité plutôt que de remplacement d'outil existant (éviter le DSI)
- illustration de réutilisabilité d'un outil interfacé avec un logiciel métier connu (Cegid)
- introduction de React (composants réutilisables basés sur JavaScript)
- exemples d'entreprises utilisant React (Netflix, Airbnb, Discord) et maîtrise de l'IA sur ce framework
- fonctionnement des composants React et mise à jour partielle sans rechargement
- présentation de Next.js (par Vercel) et ses optimisations par défaut
- exemples d'entreprises utilisant Next.js (Notion, Nike, Sonos, Audible)
- introduction de Tailwind CSS comme alternative simplifiée au CSS personnalisé
- librairies design UI et introduction du back-end (bases de données, actions serveurs)
- distinction claire entre base de données (stockage) et back-end (actions serveur)
- fonctionnalités back-end courantes (actions programmées, cache, temps réel)
- distinction technique entre database storage et file storage
- présentation de Neon comme base de données Postgres (une des trois approches)
- présentation de Supabase comme solution tout-en-un (base de données, stockage, temps réel)
- présentation de Clerk (authentification, SSO, 20$/mois pour 50 000 utilisateurs)
- présentation de BetterAuth comme alternative préférée à Clerk
- avantages de BetterAuth (40 fournisseurs sociaux, gestion automatique des credentials)
- comparaison des tarifs de paiement en ligne Europe vs Royaume-Uni
- recommandation de Polar.sh plutôt que Stripe (simplicité fiscale, 4%+0,40€)
- récapitulatif de la configuration de stack et pipeline de build en étapes
- introduction de Git (branches, merge, collaboration sur le code)

## Outils mentionnes
- Claude Code
- Notion
- Cegid
- React
- JavaScript
- Netflix
- Airbnb
- Discord
- Next.js
- Vercel
- Nike
- Sonos
- Audible
- Tailwind CSS
- n8n
- Neon
- Convex
- Supabase
- Clerk
- Linear
- BetterAuth
- Polar.sh
- Stripe
- Git

## Tips techniques
- Toujours valider en priorité que le problème est réellement douloureux avant de se focaliser sur la solution technique, contrairement au réflexe classique
- Résoudre en priorité un problème personnel authentique que l'on connaît intimement, pour développer une solution plus pertinente qu'un problème externe non vécu
- Privilégier le B2B au B2C quand c'est possible : les entreprises perçoivent une dépense comme un investissement, facilitant la conversion
- Aligner systématiquement le prix d'un service au niveau réel d'intensité de la douleur résolue, même pour un problème mineur
- Limiter volontairement le nombre de fonctionnalités présentées dès le premier jour pour ne pas noyer les nouveaux utilisateurs
- Proposer systématiquement un essai gratuit avant abonnement mensuel pour maximiser l'adoption et la conversion d'une application
- Encourager un engagement d'abonnement de longue durée au moment de motivation maximale de l'acheteur, pour sécuriser la trésorerie
- Positionner un nouvel outil comme complémentaire plutôt que remplaçant d'un outil existant, pour éviter la résistance du DSI et des décideurs
- Privilégier Polar.sh plutôt que Stripe pour simplifier la gestion des déclarations fiscales multi-pays, malgré un taux légèrement plus élevé

## Cas d'usage reels
- [[]]
