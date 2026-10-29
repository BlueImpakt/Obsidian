---
tags: [sellerie-confort, maintenance, reprise]
created: 2026-10-29
client: sellerie-confort
projet: sellerie-confort-configurateur
statut: proposée (mail à Valérie du 29/10), non signée
---

# Reprise de la maintenance du site

Reprise de la maintenance de sellerieconfort.com, aujourd'hui assurée par VIMAWEB, en parallèle de la Phase 2. Contexte : [[pre-phase-1]] (hébergement, rôle de VIMAWEB, constats), [[phase-1]] (code sur mesure lu, alerte sécurité), [[prepa-phase-2]] (hébergement, licences, RGPD).

Projet : [[sellerie-confort-configurateur]] · Client : [[sellerie-confort]]

> **Rôle de Claude sur ce dossier : assistant et garde-fou.** Melvin n'a jamais repris la maintenance d'un site marchand. Claude l'accompagne à chaque étape, vérifie avant chaque action sur la prod, et l'arrête (en le disant clairement) dès qu'un point de la section 6 est en jeu.

## 1. Contexte (29/10)

- Valérie a répondu à l'audit : **Phase 2 acceptée, Phase 3 pas pour l'instant** (coût). Elle voulait d'abord garder la maintenance chez VIMAWEB.
- David (VIMAWEB) lui a envoyé un mail hostile à Melvin (profil « pas développeur », IA, « 7 k€ juste pour le configurateur », accompagnement impossible, exigences : post_meta, garantie 6 mois, interventions facturées à l'heure, SEO). Ça a agacé la cliente.
- Conclusion commune : collaborer avec VIMAWEB sur le configurateur sera compliqué. **Valérie propose à Melvin de reprendre la maintenance tout de suite**, sans la refonte complète.
- Décision de Melvin : **aucun échange direct avec VIMAWEB** (risque de pièges). Tout passe par écrit, par Valérie.

## 2. Offre envoyée

| Élément | Montant | Contenu |
|---|---|---|
| Reprise du site en l'état | **700 € HT**, une fois (2 j, en partie mutualisés avec le lot « Environnements » de la Phase 2 ; marge possible à 875 € HT, 2,5 j) | Transfert hébergement et licences au nom de Sellerie Confort (licences à sa charge) ; inventaire extensions et code sur mesure ; sécurisation (extension compromise, fichiers, mots de passe, comptes admin) ; sauvegardes externes, surveillance, préprod permanente ; **état des lieux écrit et daté** |
| Maintenance | **175 € HT/mois**, engagement 12 mois, jours ouvrés | Mises à jour mensuelles testées en préprod, sauvegardes quotidiennes, surveillance sécurité et disponibilité, correction des incidents causés par une mise à jour, support courant (~30 min/mois) |
| Hors forfait | taux horaire | Évolutions (pages, fonctions, design) ; interventions sur le code sur mesure de VIMAWEB (caution Payline, notes de commande, export factures…) ; nettoyage d'une compromission avérée |
| Pendant Phase 2 (puis 3) | 0 € en plus | Aucune intervention de maintenance facturée en supplément jusqu'à la mise en production de la phase. Limites gardées en tête : date de fin = mise en prod ; évolutions hors refonte à part ; un vrai bug dans le code VIMAWEB inclus = geste commercial |

- 175 €/mois maintenu car c'était le point de friction (la cliente ne paiera pas plus). La rentabilité tient par la reprise facturée et le périmètre borné.
- Calendrier annoncé : reprise au démarrage, livraison Phase 2 **mi-décembre**, mise en ligne choisie hors période de forte activité (probablement début janvier).
- Garantie Phase 2 : 6 mois après mise en prod (clause dans la réponse à Valérie : défauts reproductibles du code livré, signalés par écrit, prise en charge 2 j ouvrés, exclusions mises à jour / hébergement / tiers / évolutions, diagnostic facturé si le défaut ne vient pas du code, compte admin nominatif + journal des modifications).

## 3. Ce que fait VIMAWEB aujourd'hui, et la difficulté

| Tâche | Difficulté | Pour Melvin |
|---|---|---|
| Mises à jour WordPress, WooCommerce, extensions | Faible, si testées en préprod d'abord | Méthode déjà en place : copie, test, retour arrière |
| Sauvegardes | Faible | o2switch (JetBackup) + une sauvegarde externe en plus |
| Hébergement o2switch, cPanel, PHP | Faible à moyenne | Rapport système déjà lu ; support o2switch réactif |
| Cookies (Complianz), courriels (WP Mail SMTP), DNS chez OVH | Faible à moyenne | Réglages, pas de code |
| **Code sur mesure VIMAWEB** | **Moyenne** | Déjà lu en partie en Phase 1 : `woo-payline-caution`, `product-manufacturing-label`, `sc-order-note`, modèles WCPDF dans Divi Child. À documenter à la reprise |
| **Paiements** (Payline, Alma, Cofidis) et DPD | **Moyenne, risque élevé** | Une panne coûte des ventes : commande test après chaque mise à jour |
| **Incident de sécurité** (extension compromise) | **Élevée si avérée** | Seul vrai manque d'expérience |

Constats déjà connus, à reprendre dans l'état des lieux : extension compromise **WP Logo Showcase Responsive Slider** active en prod ([[pre-phase-1]], alerte du 14/10) ; HPOS bloqué (Shipping Method Description) ; réglages Complianz perdus et WP Consent API ajouté (mail de VIMAWEB du 29/10) ; GA4 dépose des cookies malgré le refus ([[phase-1]] §12) ; page de sauvegarde Divi indexée (audit SEO du 27/10).

## 4. Les trois points à préparer

1. **Sécurité** : à la reprise, retrait de l'extension et contrôle des fichiers (porte dérobée `wp-comments-posts.php`, injection dans `wp-config.php`). **Si la compromission est avérée : ne pas nettoyer soi-même**, faire appel à un service spécialisé (Sucuri, Wordfence ou équivalent, quelques centaines d'euros, à la charge de la cliente).
2. **Paiements** : un test automatique du tunnel de commande sur la préprod (une commande par moyen de paiement en mode test), lancé après chaque mise à jour.
3. **Urgences** : procédure écrite de retour arrière (restauration) ; jours ouvrés seulement ; un développeur WordPress de confiance identifié en renfort. Vérifier que la **RC pro** couvre la maintenance d'un site marchand.

## 5. Déroulé de la reprise (checklist)

### Avant de signer
- [ ] Réponse de Valérie : préavis du contrat VIMAWEB, titulaire du compte o2switch et des licences (Divi, SEOPress Pro, autres), droits sur le code sur mesure (utilisation et modification par un autre prestataire)
- [ ] RC pro : couverture maintenance d'un site marchand
- [ ] Contrat : reprise + maintenance + clause garantie Phase 2 + exclusions + jours ouvrés + nettoyage de compromission hors forfait + cession du code Phase 2 au paiement complet
- [ ] Renfort WordPress identifié

### Transfert (demandes faites par Valérie à VIMAWEB, Melvin lui dit quoi demander)
- [ ] Compte o2switch au nom de Sellerie Confort (ou migration vers un compte à elle, voir [[prepa-phase-2]] §2)
- [ ] Licences des extensions payantes transférées ou rachetées
- [ ] Accès : compte admin WordPress nominatif pour Melvin, SFTP/SSH, cPanel
- [ ] Code sur mesure et éventuelle documentation remis

### Jour J de la reprise
- [ ] **Sauvegarde complète avant toute action**, conservée hors du serveur
- [ ] **État des lieux écrit et daté**, envoyé à Valérie avant toute modification : versions (WP, PHP, WooCommerce, extensions), extensions actives, comptes admin, constats de la section 3, captures
- [ ] Contrôle de la compromission ; si avérée → service spécialisé, arrêt
- [ ] Mots de passe changés, comptes admin revus
- [ ] Sauvegardes externes, surveillance de disponibilité, journal des modifications (Simple History ou WP Activity Log)
- [ ] Préprod permanente
- [ ] Test du tunnel de commande en préprod
- [ ] Procédure de retour arrière écrite

### Ensuite, chaque mois
- [ ] Mises à jour en préprod → tests (tunnel de commande, configurateur) → prod → contrôle
- [ ] Vérification des sauvegardes (une restauration test par trimestre)
- [ ] Note mensuelle courte à Valérie (ce qui a été fait, temps passé)

## 6. Garde-fous (Claude arrête Melvin si…)

- une action touche la prod **sans sauvegarde récente** ou sans passage par la préprod ;
- une mise à jour en prod n'est pas suivie d'une **commande test** ;
- Melvin s'apprête à **nettoyer lui-même** une compromission avérée ;
- un engagement écrit dépasse le périmètre (gratuité sans date de fin, correction gratuite du code VIMAWEB, astreinte le week-end, délai intenable) ;
- un échange part **directement vers VIMAWEB** au lieu de passer par Valérie, ou répond aux attaques personnelles ;
- une modification est faite avant que l'état des lieux soit envoyé ;
- des données clients sortent du serveur sans le cadre RGPD prévu ([[prepa-phase-2]]) ;
- le temps passé dépasse durablement ce que couvrent 175 €/mois (environ 3,5 h à 50 €/h) : le signaler pour renégocier le périmètre.

## 7. Questions ouvertes

- Combien la cliente paie VIMAWEB aujourd'hui, et pour quoi (point de comparaison)
- Le site est-il dans un compte o2switch dédié ou dans un compte d'agence de VIMAWEB
- Réaction de VIMAWEB à la fin du contrat (délais de transfert, rétention des accès) : prévoir que Valérie fixe une date ferme par écrit
