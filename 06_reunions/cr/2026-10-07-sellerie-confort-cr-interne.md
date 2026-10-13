---
tags: [compte-rendu, sellerie-confort, cr-reunion]
created: 2026-10-07
client: sellerie-confort
---

# 2026-10-07 — Compte rendu réunion Sellerie Confort (note interne)

Réunion d'environ 2 h avec Valérie Cenizo. Préparation : [[2026-10-07-sellerie-confort]] · Projet : [[sellerie-confort-configurateur]] · Client : [[sellerie-confort]]

## En bref
- Bonne réunion. Valérie est intéressée, le besoin confirmé correspond à la fiche projet.
- **Rien n'est signé.** Contrat et date de démarrage dépendent de l'accord de son mari.
- **Nouvelle offre orale : Phase 1 à 1 400 € HT** (4 j × 350 €), toujours déduite de la Phase 2. Je me suis engagé : le prochain devis part à 1 400 €.
- Maquettes très appréciées. Elle veut que je les envoie pour les montrer à son mari.
- Phase 1 élargie, **offerte** : audit des automatisations, suivi du parcours utilisateur, perte du panier.
- Accès : elle peut me les donner. Je choisirai moi-même les modèles échantillons.
- Risque principal : VIMAWEB (voir plus bas).
- **Concurrence : une agence web les rencontre début novembre.** Je veux démarrer vite pour ne pas perdre la place (voir plus bas).

## Le besoin tel qu'elle l'a décrit
- **Matières** : l'ancien prestataire avait mis en place le système (patchs de matières sur les photos). Le prestataire actuel (VIMAWEB) ne le reproduit pas. Résultat : impossible d'ajouter une matière sans passer par lui, et il facture chaque demande. Retirer une matière passe aussi par lui.
- **Stock bloqué** : ils ont des nouvelles matières disponibles qu'ils n'ont pas pu ajouter au configurateur depuis longtemps. Source de frustration.
- **Nid d'abeille** : c'est une **broderie**, pas une matière. Il est proposé uniquement sur quelques modèles « tout préparés » (non configurables), pas dans le configurateur sur mesure. Ils veulent l'y ajouter.
- **Budget** : année difficile, très peu de commandes (une première). Elle a rappelé que 15 000 € ont déjà été investis dans le site il y a deux ans, sans être satisfaits aujourd'hui. Le prix de 1 600 € l'a freinée.
- **Plus tard** : elle a elle-même évoqué de retravailler ensemble pour refaire tout le site.

## Flux actuel d'ajout d'un nouveau modèle (≈ 1 semaine)
1. Photos de la selle sous plusieurs angles pour obtenir toutes les parties. Manuel, chez elle.
2. Travail sous Photoshop pour produire les calques. Manuel, chez elle.
3. Import des calques dans WordPress.
4. **Ajout, un par un, de chaque matière sur chaque calque.** C'est l'étape qui prend le plus de temps : WordPress ne permet pas de dire « ce calque reçoit toutes les matières du jeu ».

**Décision** : les étapes 1 et 2 restent manuelles. Elles fonctionnent bien, et la qualité et le savoir-faire de Valérie y comptent plus que dans une automatisation. On automatise l'étape 4 et le classement des matières.

## Ce qu'on fait sur les matières
- Remettre en place ce que faisait l'ancien prestataire, avec un meilleur rendu visuel.
- Refaire des photos pour les matières dont le rendu n'est pas bon (les photos restent nécessaires).
- **Reclasser les matières par famille**, pour l'expérience du client dans le configurateur et pour la gestion du catalogue côté Valérie.

## Résultat de l'audit des jeux de matières (site public, sans accès admin)
Échantillon : 44 fiches configurables (2 par marque, au hasard), fichiers de configuration publics lus et comparés. Les noms sont comparés après retrait du préfixe de couche (« Bec bleu océan » = « Assises bleu océan »).

| Jeu | Matières | Couches concernées | Fiches identiques |
|---|---|---|---|
| A, matières | 37 | Bec, Bandeaux, Assises, Assises avant/arrière, Bandes et dosseret, Bandes latérales, Dosseret | 43/44 pour Bec et Bandeaux, 100 % pour les autres types |
| B, surpiqûres | 26 | Surpiqûres | 43/44 |
| C, liserés | 44 | Liserés | 43/43 |

- **Fiche atypique : CFMOTO 800 NK.** Noms de couches propres, jeux de 44 à 46 matières, orthographes différentes (« bleu egyptien », « bordeau »). Demande un nettoyage.
- **Faute de frappe** « gris tonnerrre » (3 r) dans 57 couches de type Assises : signe de copier-coller entre fiches. Le reste du jeu de 37 est identique partout.
- **5 gabarits de noms de couches** pour les mêmes zones : Assises / Bandes et dosseret (24 fiches) ; Assises avant / Assises arrière / Dosseret / Bandes latérales (10) ; « Assises et comme assise » (4) ; « Assises & Comme assises » / Bandes (2) ; Avant assise arrière (2). Les noms ne suivent pas le contenu.

**Conclusion** : on peut remplacer la saisie matière par matière par **3 jeux réutilisables (37, 26 et 44)**, rattachés à chaque couche selon son type. Seule la fiche CFMOTO 800 NK échappe à la règle. C'est l'argument chiffré pour la Phase 2.

## Broderies
- Priorité basse pour Valérie, haute pour moi (vrai plus pour le configurateur).
- Il faut des tests pour savoir si c'est faisable. **Le test du nid d'abeille est inclus dans les tests broderies**, eux-mêmes inclus dans l'audit de la Phase 1.
- Elle a été convaincue par la qualité des rendus présentés. Pas besoin de détailler les méthodes (calcul, génération) : elle juge le résultat.

## Ergonomie
Principe confirmé : **tout sur une seule page** (matières, broderies, options, informations client), sans navigation entre plusieurs pages. On le garde.

## Phase 1 élargie (offert, sans surcoût)
En plus du configurateur et des tests matières/broderies :
1. **Automatisations** : elle fait beaucoup de choses à la main (rappels, emailing, bons de commande…). Auditer ce qui peut être automatisé, avec temps et coût pour le faire.
2. **Suivi statistique** : comprendre ce qui existe aujourd'hui, et proposer un outil de suivi du parcours utilisateur pour voir où les visiteurs s'arrêtent.
3. **Panier perdu** : il n'y a pas de cookies sur le site, donc un client qui perd son panier doit tout recommencer. Vérifier pourquoi, et envisager un mail de relance sur abandon de panier (exemple qui relie les points 1 et 2).

## Accès, démarrage, cadre
- Elle peut me donner les accès WordPress. **VIMAWEB a aujourd'hui les mêmes accès WordPress que Valérie**, et elle peut m'ajouter en administrateur sans rien lui demander : pas de risque de blocage côté accès.
- Je choisis moi-même les modèles échantillons (accès à tout le catalogue).
- Date de démarrage et signature : suspendues à l'accord de son mari.
- Toutes les données multimédias sont dans WordPress, donc faciles à récupérer avec un export.
- **Licences des plugins : c'est VIMAWEB qui les détient aujourd'hui.** Elle est d'accord pour les racheter ou les reprendre à son nom si besoin, pour être plus indépendante. Je lui ai écrit que j'avais vérifié que c'est possible.

## Hébergement et DNS (constat du 13/10, lecture publique, sans accès)
- **Hébergeur : o2switch** (France), serveur LiteSpeed avec cache actif. Confirmé par l'en-tête serveur et l'IP enregistrée au nom d'O2SWITCH.
- **DNS : OVH** (`ns200.anycast.me`, `dns200.anycast.me`), donc pas chez l'hébergeur.
- **Email : Google Workspace** (MX `smtp.google.com`).
- **Domaine** enregistré le 17/06/2013, expire le **17/06/2027**. Registrar non identifié, probablement OVH (hypothèse).
- **Qui détient quoi : inconnu.** Titulaire du compte o2switch (VIMAWEB ou Valérie ?), du compte OVH, administrateur Google. Il en dépend si je peux créer un staging et basculer sans passer par VIMAWEB, au même titre que les licences.
- **Staging** : probablement faisable chez o2switch (à vérifier selon l'offre), le DNS se règle chez OVH.

## Risque VIMAWEB
- VIMAWEB veut refaire tout le site hors WordPress. Valérie ne veut pas travailler avec eux : ça s'est mal passé jusqu'ici. Elle préfère travailler avec moi.
- Leur intérêt : vendre un nouveau site plutôt que d'améliorer l'existant (ça rapporte plus et donne plus de liberté sur l'ajout des matières). Ils refusent aujourd'hui d'améliorer l'existant, peut-être pour pousser vers la refonte (hypothèse, formulée avec « peut-être » dans la note client).
- Risque réel : les **licences** des plugins, qu'ils détiennent. Pas les accès WordPress (Valérie les a).
- **VIMAWEB n'est pas encore informé.** Valérie est d'accord pour qu'on l'informe. Réaction inconnue. Mieux vaut qu'ils l'apprennent d'elle que dans les logs d'accès : sinon un prestataire qui travaille sans eux peut braquer la relation, alors qu'elle en a encore besoin pour d'autres choses.
- **Il faut lui exposer le risque avant qu'il arrive**, par écrit, pour qu'elle ait un argument face à son mari si VIMAWEB freine. Fait dans la note client.
- Angles à clarifier : contrat de maintenance avec VIMAWEB (clause d'exclusivité, intervention d'un tiers ?), et le fait que Valérie portera seule l'argument face à son mari.

## Le plugin du configurateur peut nous limiter
Le plugin actuel (`mkl_pc`) n'a sans doute pas de notion de famille ni de jeu de matières partagé : chaque matière y est une image par calque. Il peut donc limiter les familles de matières, les broderies et l'ensemble de la refonte. À trancher dans l'audit de la Phase 1. Options :
1. **Étendre sans toucher au cœur** : API ou hooks du plugin, idéal si possible.
2. **Couche à côté** qui gère les familles et génère les données que `mkl_pc` attend, sans modifier le plugin.
3. **Forker le plugin** : copie modifiée à ma main. Lourd, je deviens responsable des mises à jour et de la sécurité.
4. **Abandonner le plugin** et construire un configurateur maison branché sur WooCommerce : liberté totale, mais plus long et plus cher (affichage des couches, clics, calcul du prix à refaire). Option de repli seulement.

Dans la note client : une phrase simple (vérification du plugin, rapport avec solutions, avantages et inconvénients). Pas le détail des options 3 et 4.

## WordPress : ce qu'on retient (réflexion du 13/10, hypothèses à confirmer par l'audit)
- **WordPress n'est pas le facteur limitant.** Ce qui limite Valérie : le plugin `mkl_pc` et la façon dont c'est monté (matières saisies une par une, aucune structure, la médiathèque comme seul outil). Mon discours « WordPress très limitant » devant le client est à nuancer : limite du plugin actuel, pas de WordPress.
- **Tout peut se refaire en restant sur WordPress** : configurateur (plugin maison + bloc JS), thème sur mesure à la place de Divi, back-office. WooCommerce reste le moteur (panier, paiement, commandes). URLs, SEO et historique intacts. Remplacer `mkl_pc` par un configurateur maison ne fait pas sortir de WordPress.
- **Repli si `mkl_pc` bloque** : configurateur maison en plugin (option 4 ci-dessus), pas un site hors WordPress.
- **Données** : ~107 matières distinctes (37 + 26 + 44) à classer en familles, structure par jeux rattachés au type de couche. Famille à définir avec Valérie (couleur, type de matière, finition). Table dédiée pour les ~83 000 images de combinaison, sauf si le rendu masque + texture est retenu (tests Phase 1).
- **Back-office cible** : écran « Ajouter un modèle » (calques déposés en lot, type par couche, matières rattachées seules, aperçu, publication) + écran « Matières » (familles, ajout ou désactivation répercutés partout). Étape 4 du flux supprimée, étapes 1 et 2 inchangées.
- **Déploiement** : staging obligatoire, les deux configurateurs coexistent, bascule modèle par modèle, `mkl_pc` désactivé à la fin.
- **Ordres de grandeur (estimations, non validées)** : Phase 2 ≈ 16 à 18 j ; thème et pages sur WordPress +10 à 14 j ; site complet hors WordPress 35 à 50 j. Le ~5 000 € de la Phase 3 tient sur WordPress, pas hors WordPress.
- **Risques** : plugins tiers (licences), sécurité du code PHP, mises à jour WooCommerce, je suis seul à maintenir. Parade : peu de plugins tiers, tests automatisés, dépôt et documentation au nom du client.
- **Ne pas affirmer avant l'audit** : que `mkl_pc` permette tout, le rendu des broderies, l'hébergement.

## Phase 3 évoquée (pas dans la note client)
Idée d'un nouveau site l'an prochain, détaché de WordPress, codé de zéro par moi. Simple piste, rien d'engagé. À reconsidérer : une refonte sur WordPress est moins chère et moins risquée (voir section précédente).

## Concurrence : une agence web début novembre
- Une agence web les rencontre début novembre pour leur proposer un nouveau site. Ils ne sont pas prêts à refaire tout le site, mais ont dit « on va l'écouter ». Je ne suis pas le seul positionné.
- Une agence coûte plus cher. Mon avantage : prix et réactivité.
- **Stratégie : jouer la disponibilité, sans pression.** Ne pas citer l'agence dans la note client. J'ai de la place en octobre : si on signe vite et que j'ai les accès avant leur départ, je livre la Phase 1 pendant leurs congés, ils lisent le rapport et étudient la Phase 2 pendant leurs congés, et la décision est prête à leur retour. La Phase 1 n'engage pas la Phase 2 et elle est déduite : c'est déjà dit dans la note.
- **Départ en congés : le 17 octobre (confirmé).** Le rapport ne sera pas livré avant : il faut le contrat signé et les accès avant leur départ, puis livraison pendant les congés. Ne pas promettre un délai que je ne peux pas tenir.

## Stratégie tarifaire (hypothèses de travail, à affiner après l'audit)
Réfléchi à l'oral après la réunion. **Rien de tout ça n'est à dire à Valérie avant que la Phase 1 soit livrée et appréciée.**

| Étape | Montant | Remarque |
|---|---|---|
| Phase 1 | 1 400 € HT (4 j × 350 €) | −12,5 % par rapport à 1 600 €. Déduite de la Phase 2 |
| Phase 2 (configurateur) | **cible révisée : 5 500 € avant déduction** (6 000 à 6 500 € puis 7 500 € envisagés plus tôt) | Soit environ 4 100 € restant à payer après les 1 400 €. Avec 350 €/j : environ 16 jours |
| Phase 3 (refonte du site sur WordPress : thème et pages) | environ 5 000 € | Soit environ 14 jours à 350 €, à vérifier : court pour un site complet |
| **Total visé** | **environ 10 500 €** (5 500 + 5 000) | Proche de l'objectif de départ de 10 000 € |

- **Fourchette annoncée à Valérie (dans la note client, en réponse à son message du 07/10 au soir) : 4 000 à 7 000 € HT pour le configurateur, Phase 1 incluse.** Ma cible réelle est 5 500 €, donc au milieu de la fourchette. Elle est présentée comme volontairement large, à resserrer par l'audit. Risque d'ancrage sur 4 000 € : justifier plus tard par ce que révèle le plugin.
- **Automatisations et suivi** : l'**audit est offert**, la **mise en place est payante, en options** chiffrées à part après l'audit. Pas dans la fourchette. Dit dans la note client (« chiffrée à part, en option »).
- **Plafond de prix** : pas d'engagement ferme pris. Si je m'engage un jour sur un plafond, c'est légal mais j'absorbe tout dépassement. Prévoir une clause : le plafond vaut pour le périmètre identifié par l'audit, et un changement majeur (plugin à forker, configurateur maison) rouvre la discussion.
- Contexte : ils ont déjà dépensé 15 000 € dans le site il y a deux ans, sans être satisfaits. Un total proche de 10 000 € se défend bien.
- **Maintenance et hébergement** : VIMAWEB leur facture aujourd'hui 140 €/mois. Si je reprends tout (code, hébergement, maintenance), je vise un **forfait de 450 €/mois** (fourchette envisagée : 400 à 500 €). Repères de marché évoqués à l'oral, non sourcés : forfaits WordPress freelance d'environ 50 à 170 €/mois, agences jusqu'à 300 à 500 €.
- **Ce que couvre le forfait** : hébergement, sécurité, sauvegardes, surveillance, ajustements et petites améliorations **sans refacturer à chaque demande** (contraste voulu avec VIMAWEB, qui facture chaque modification).
- **Ce qui sort du forfait** : nouvelle fonctionnalité, nouveau module, ou plus d'une journée de travail, sur devis. À écrire noir sur blanc pour ne pas finir à travailler gratuitement. Réviser le montant après quelques mois.
- Une fois hors WordPress, je serais seul à pouvoir maintenir le code : prévoir la documentation et le transfert possible, pour que le client ne se sente pas piégé.

## Actions
- [ ] Envoyer la note client + les maquettes à Valérie, avec le devis à 1 400 € HT
- [ ] **Proposer une date de prochaine réunion directement dans le message**
- [ ] Mettre à jour le contrat Phase 1 et le devis I-26-08-1 : 1 400 €, nouveaux volets offerts dans le livrable, dates en blanc
- [ ] Mettre à jour la fiche [[sellerie-confort-configurateur]] : Next actions, Blocages, prix
- [ ] Licences des plugins : préparer avec Valérie la reprise à son nom si VIMAWEB bloque
- [ ] Valérie informe VIMAWEB de notre collaboration rapidement, si elle donne suite
- [ ] Dans l'audit : vérifier ce que permet `mkl_pc` (options ci-dessus)
- [ ] Obtenir le contrat signé et l'accès WordPress avant le 17 octobre, pour livrer le rapport pendant les congés
- [ ] Demander à Valérie qui est titulaire des comptes o2switch, OVH et Google Workspace (avant de contacter VIMAWEB)
- [ ] Après l'audit : chiffrer la Phase 2 en jours réels, viser 5 500 € dans la fourchette annoncée (4 000 à 7 000 €)
- [ ] Préparer le devis à 1 400 € et le contrat Phase 1 pour une signature rapide (les anciens documents disent encore 1 600 € et des dates en blanc)

## À vérifier
- **Ce qui a été montré à Valérie sur la qualité des rendus.** La fiche projet dit « rien testé » sur le compositing. Noter précisément ce qui a été présenté, pour ne pas sur-promettre.
- **Le tarif de 350 €/jour s'applique-t-il aussi à la Phase 2 ?** Le contrat actuel dit « même taux de 400 €/jour ».
- **Le périmètre de l'audit offert** doit tenir dans les 4 jours : le cadrer comme un audit léger avec estimation, pas comme une mise en place.
- **Licences** : détenues par VIMAWEB. Confirmer la procédure de reprise à son nom pour chaque plugin (`mkl_pc`, `wapf`, Divi) : transfert par l'éditeur ou rachat.
- **Panier perdu** : cause à trouver (session WooCommerce, cache LiteSpeed ?), hypothèse seulement.
- **Marques** : l'audit parle de 28 marques, la fiche dit 27 (Hyosung en trop). Aligner.
- **Couche « Bandeaux »** : dans la maquette R6, elle a 44 choix, alors que l'audit la classe dans le jeu A (37). À recouper (nommage différent sur la R6 ?).
- **Titulaires des comptes** o2switch (hébergement), OVH (DNS, domaine) et Google Workspace : à demander à Valérie (qui reçoit les factures ?). Ressources du serveur, version de PHP, accès serveur et possibilité d'un staging : non vérifiables depuis le site public.
- **Stockage de `mkl_pc`** : où il garde les identifiants de médias (import des données). Compter aussi les médias orphelins et les doublons (empreinte de fichier).
