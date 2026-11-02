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
| **Code sur mesure (auteurs à confirmer, voir §3 bis)** | **Moyenne** | Déjà lu en partie en Phase 1 : `woo-payline-caution`, `product-manufacturing-label`, `sc-order-note`, modèles WCPDF dans Divi Child. À documenter à la reprise |
| **Paiements** (Payline, Alma, Cofidis) et DPD | **Moyenne, risque élevé** | Une panne coûte des ventes : commande test après chaque mise à jour |
| **Incident de sécurité** (extension compromise) | **Élevée si avérée** | Seul vrai manque d'expérience |

Constats déjà connus, à reprendre dans l'état des lieux : extension compromise **WP Logo Showcase Responsive Slider** active en prod ([[pre-phase-1]], alerte du 14/10) ; HPOS bloqué (Shipping Method Description) ; réglages Complianz perdus et WP Consent API ajouté (mail de VIMAWEB du 29/10) ; GA4 dépose des cookies malgré le refus ([[phase-1]] §12) ; page de sauvegarde Divi indexée (audit SEO du 27/10).

## 3 bis. Constats du 02/11 (Santé du site, facture VIMAWEB, licences)

Sources : export Outils → Santé du site → Info (02/11, 10:41), photo de la facture VIMAWEB, vérifications dans l'admin. Rien n'a été modifié sur le site.

### Facture VIMAWEB : « Maintenance – Formule Premium »
- **120 € HT/mois** (144 € TTC), prélèvement bancaire. Il y a donc bien une relation commerciale avec VIMAWEB : **devis ou conditions d'origine à demander à Valérie** (durée d'engagement, reconduction, préavis). Valérie dit ne pas avoir de contrat écrit ni avec VIMAWEB ni avec ARTEO : à confirmer.
- Inclus : hébergement et nom de domaine, réinstallation, sauvegardes quotidienne + mensuelle (autre datacenter), mises à jour WordPress et extensions, licences, Google Analytics, assistance 30 min/mois, **6 h/an de modifications et de contenu**, demandes sous 48 h.
- **Comparaison avec l'offre (175 € HT/mois)** : l'offre n'inclut ni hébergement, ni licences, ni les 6 h/an. L'écart réel est plus grand que 55 €. À chiffrer avant la visio : coût annuel de l'hébergement o2switch et des licences.
- **Incohérences** : la facture cite Elementor Pro, Astra, WP Forms, WP Rocket et Cleantalk. **Elementor Pro, Astra et WP Rocket sont absents du site** (cache = LiteSpeed Cache gratuit, thème = Divi). « Nom de domaine inclus » : le domaine est chez OVH, au nom de Valérie. À clarifier par écrit, sans accuser.
- Illisible sur la photo : date d'émission, numéro, période, durée d'engagement, taux des pénalités. Échéance lue : 18/11/2026, à confirmer.

### Licences et titulaires
| Élément | Constat | Titulaire |
|---|---|---|
| Divi 4.27.8 | Nom d'utilisateur et clé masqués dans Divi → Options → Mises à jour | Inconnu |
| SEOPress PRO 10.3 | Clé active | Inconnu |
| WPForms 2.0.3.1 | Licence **Elite** valide (la plus chère) pour **1 formulaire**, 2 278 entrées enregistrées | Inconnu |
| CleanTalk 6.90 | Abonnement actif, compteur 27 466 spams bloqués | **VIMAWEB** (confirmé) |
| WP Umbrella (extension + mu-plugin), Patchstack (mu-plugin) | Monitoring/sécurité, accès distants probables | Probablement VIMAWEB, à confirmer |

Le titulaire n'est visible nulle part dans WordPress : reçus dans les mails de Valérie (cherche « elegant themes », « seopress », « wpforms », « cleantalk ») ou demande écrite à VIMAWEB via Valérie (compte, date de renouvellement, coût annuel). Le titulaire doit être connu pour chaque licence avant la reprise.

### Auteurs du code sur mesure (en-têtes)
| Élément | Auteur déclaré |
|---|---|
| Notes de commande 1.1.0 | Vimaweb |
| SC - Export PDF Factures 1.0.0 | Vimaweb |
| Woo Payline Caution 1.0 | Vimaweb |
| mu-plugin « Active Plugins » 1.0 | ARTEO Digital (à lire : un mu-plugin ne se désactive pas depuis l'admin) |
| SC Notice Carbone 1.0.0 | « Sellerie Confort » |
| Divi Child 1.0.0 | « Anonyme » |
| Product Manufacturing Labels 1.0, `fix-wapf-preview.php`, `_patchstack.php` | Non renseigné |
| Purge + Tag « Configurable » 1.2.0 | « Vous » |

Un en-tête n'est pas une preuve de propriété. Pour les droits (cession écrite), il faut les devis et factures de chaque module, ou une réponse écrite de VIMAWEB et d'ARTEO via Valérie.

### Autres constats techniques
- **Extension compromise toujours active** : WP Logo Showcase Responsive Slider (Essential Plugin) 3.8.7.1. Priorité de sécurité n° 1 de la reprise (voir §4).
- **Configurateur** : prod en 1.7.6, **2.0.1 disponible** (testé : 2.0.0). Relire le journal des modifications et relancer les tests avant la mise en production.
- **Mises à jour** : désactivées partout sauf WPForms ; une douzaine d'extensions en retard (écarts mineurs) et Divi 4.27.8 → 4.27.9. SEOPress 10.4 / SEOPress PRO 10.3 : versions décalées.
- **Poids** : 17,9 Go (dont 15 Go d'images, base 1,47 Go) : impact sur sauvegardes externes et migration.
- **Hébergement** : PHP 8.3.36, LiteSpeed, MariaDB 11.4.13, WordPress 7.1.4, 2 856 utilisateurs.
- **À nettoyer plus tard (avec sauvegarde)** : DPD France 5.3.3, APF Pro et Product Manufacturing Labels inactifs ou en doublon.
- **WpTiger (o2switch)** actif en production.

## 4. Les trois points à préparer

1. **Sécurité** : à la reprise, retrait de l'extension et contrôle des fichiers (porte dérobée `wp-comments-posts.php`, injection dans `wp-config.php`). **Si la compromission est avérée : ne pas nettoyer soi-même**, faire appel à un service spécialisé (Sucuri, Wordfence ou équivalent, quelques centaines d'euros, à la charge de la cliente).
2. **Paiements** : un test automatique du tunnel de commande sur la préprod (une commande par moyen de paiement en mode test), lancé après chaque mise à jour.
3. **Urgences** : procédure écrite de retour arrière (restauration) ; jours ouvrés seulement ; un développeur WordPress de confiance identifié en renfort. Vérifier que la **RC pro** couvre la maintenance d'un site marchand.

## 5. Déroulé de la reprise (checklist)

### Avant de signer
- [ ] Réponse de Valérie : devis ou conditions d'origine de la facture VIMAWEB (engagement, reconduction, préavis éventuels ; pas de contrat écrit annoncé avec VIMAWEB ni ARTEO), titulaire du compte o2switch et des licences (Divi, SEOPress Pro, WPForms Elite, CleanTalk = VIMAWEB, WP Umbrella, Patchstack), auteur et droits de chaque module sur mesure (§3 bis)
- [ ] Chiffrer l'offre à périmètre égal avec la facture VIMAWEB (120 € HT, hébergement, licences, 6 h/an) avant d'en discuter avec Valérie
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

- ~~Combien la cliente paie VIMAWEB aujourd'hui~~ → 120 € HT/mois, voir §3 bis. Reste : période d'engagement et ce que la facture inclut réellement (licences citées absentes du site)
- Le site est-il dans un compte o2switch dédié ou dans un compte d'agence de VIMAWEB
- Titulaire de chaque licence (Divi, SEOPress Pro, WPForms Elite, WP Umbrella, Patchstack) et accès distants VIMAWEB à retirer à la reprise
- Qui a écrit chaque module sur mesure et dans quel cadre (devis, factures) ; contenu du mu-plugin « Active Plugins » (ARTEO)
- Réaction de VIMAWEB à la fin du contrat (délais de transfert, rétention des accès) : prévoir que Valérie fixe une date ferme par écrit
