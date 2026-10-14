---
tags: [project, encours, sellerie-confort, phase-1]
created: 2026-10-14
client: sellerie-confort
projet: sellerie-confort-configurateur
---

# Discussion Claude : Phase 1

Journal des discussions menées avec Claude **en dehors de Claude Code** (échanges vocaux et conversation), pas des notes de réunion client. Contient les points tranchés ou clarifiés le 14/10/2026. Complète [[pre-phase-1]] et [[2026-10-14-sellerie-confort-hebergement-acces]]. Projet : [[sellerie-confort-configurateur]] · Client : [[sellerie-confort]]

## 1. OVH vs o2switch, en deux phrases pour Valérie

> Votre nom de domaine et vos adresses mail sont chez OVH, mais votre site, lui, est hébergé ailleurs, chez o2switch, via votre prestataire de maintenance. OVH, c'est l'adresse postale et la boîte aux lettres ; o2switch, c'est la maison où vit le site ; le DNS est le panneau qui indique le chemin de l'une à l'autre.

| | OVH | o2switch |
|---|---|---|
| Rôle ici | Registraire des domaines, zone DNS, boîtes mail, ancien hébergement | Hébergement du site actif (prod, et dev) |
| Titulaire | Valérie | VIMAWEB |
| Mon accès | Aucun (hors contrat) | Aucun (non nécessaire en Phase 1) |

Très courant d'avoir deux prestataires séparés : rien d'anormal. **Valérie ne sait pas que le site est chez o2switch.** Décision : **pas de mail dédié ni d'annonce maintenant** (aucun impact sur la mission). À mentionner comme constat factuel dans le **rapport de fin de Phase 1**.

## 2. Pourquoi l'absence d'accès o2switch compte (pour la suite)

- **Phase 1 : aucun blocage.** Tout passe par l'admin WordPress (extension d'export, lecture des fiches).
- **Après** : pas d'accès aux fichiers serveur, à la config PHP, aux clés de sécurité. Les licences des plugins sont chez VIMAWEB. S'ils coupent l'accès admin ou refusent de maintenir ce qu'ils n'ont pas fait, on perd la main.
- **Risque de maintenance** : VIMAWEB peut refuser de maintenir un configurateur modifié par un tiers.
- **Atténuation** : privilégier une **couche séparée** (petit plugin sur les crochets de `mkl_pc`) plutôt que toucher au cœur du plugin, avec documentation. Responsabilités claires : eux gardent le plugin d'origine, nous notre couche. À présenter à Valérie en ce sens. Si la 2.0.0 s'avère la bonne voie, la mise à jour est un vrai chantier (migration de données) : à tester sur la copie d'abord.
- Rappel : l'avis de sécurité sur le plugin Essential Plugin reste **hors périmètre** (décision du 14/10), voir [[pre-phase-1]] §8.

## 3. Pourquoi pas `dev` comme copie de travail

- **Données personnelles** : 1 071 utilisateurs et 151 entrées de formulaire (art. 2 du contrat).
- **Trop ancien** : WordPress 6.9.1, WooCommerce 10.5.2, configurateur 1.5.13, contre 7.1.3, 11.2.1 et 1.7.6 en prod.
- **Territoire de VIMAWEB** : préproduction créée avec WP Tiger (o2switch), où ils ont prototypé le plugin « templates par tag modèle ». On risquerait de perturber leur travail sans qu'ils le sachent.
- Hypothèse : ils ont essayé d'améliorer le configurateur puis laissé tomber (ou mis en pause). À vérifier en lisant leur plugin avant tout chiffrage.
- WP Tiger n'est utilisable qu'avec un accès cPanel o2switch : hors contrat, donc non.

## 4. Copie de travail : l'approche retenue

- **Clone filtré de la prod** (WordPress à jour, préfixe `SC_`), sans clients, commandes, comptes ni formulaires. Même admin, mêmes produits, mêmes images, même configuration du configurateur.
- **Héberger** : en local (Local ou DevKinsta) pour la Phase 1, gratuit. Un VPS (Hetzner, DigitalOcean) seulement si besoin de montrer la copie à Valérie. Le même plugin sert à l'export et à l'import, local ou en ligne.
- **Outil d'export** : piste **WPvivid** (gratuit, sélection de contenu). Alternatives : Migrate Guru (sans limite de taille, mais peu de contrôle sur l'exclusion), WP Migrate payant (exclusion fine), ou export SQL à la main. **À vérifier à l'écran** : que l'outil exclut bien `shop_order` et leurs `postmeta`. Les commandes sont dans `SC_posts` (HPOS désactivé), donc un filtre par table ne suffit pas. Contrôle final : chercher `_billing_` et `_shipping_` dans l'export.
- **Nom de l'outil non cité** dans le mail à Valérie (on garde la liberté d'en changer).
- Exclure les données personnelles alors que j'ai déjà accès à l'admin : ce n'est pas la même chose de consulter ponctuellement que de conserver une copie durable de milliers de comptes clients chez moi. Responsabilité en cas de fuite (art. 2).
- Effet de l'exclusion : pages « mes commandes » et statistiques de ventes vides, sans impact sur le configurateur ni les fiches produits. Ajuster l'exclusion au cas par cas si un plugin plante.

## 5. Accord écrit de Valérie pour l'extension d'export

Le contrat prévoit un accord écrit préalable (un mail suffit) : trace datée du feu vert au moment où l'action est faite. **À obtenir avant le 17/10.** L'extension reste installée **pendant la Phase 1** (pas seulement le temps de l'export) et est **désinstallée à la fin de la mission**.

Version finale du mail :

> **Objet : Export technique du site, autorisation**
>
> Bonjour Valérie,
>
> Conformément à notre contrat, j'ai besoin d'installer temporairement une extension WordPress sur le site de production, pour en faire une copie technique sans données personnelles, ni commandes, ni comptes clients, que je teste ensuite en local. Elle restera installée pendant la Phase 1 et sera désinstallée à la fin de la mission. Rien d'autre ne sera modifié sur le site.
>
> Pouvez-vous me confirmer votre accord par retour de mail ?
>
> Merci,
> Melvin

## Next actions
- [ ] Envoyer le mail d'accord à Valérie (avant le 17/10) et archiver sa réponse
- [ ] Confirmer par mail la date de départ du délai de 10 jours
- [ ] Choisir et tester l'outil d'export (exclusion `shop_order` et `postmeta` à vérifier)
- [ ] Lire le plugin « SC - Sync MKL Product Configurator » de VIMAWEB sur dev avant de chiffrer
- [ ] Mentionner l'hébergement o2switch dans le rapport de fin de Phase 1
