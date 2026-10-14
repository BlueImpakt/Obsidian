---
tags: [prepa-reunion, sellerie-confort]
created: 2026-10-14
client: sellerie-confort
---

# 2026-10-14-sellerie-confort-hebergement-acces

## Objectif de la réunion
- Savoir **qui héberge quoi** et **qui détient quels accès**, avant de demander quoi que ce soit à Valérie (elle part en congés le 17/10)
- Choisir comment obtenir la copie du site pour l'audit (production ou dev), dans le cadre du contrat signé le 13/10
- Pas une réunion au sens strict : base du mail à Valérie et d'un éventuel appel rapide avant le 17/10

## En 30 secondes
- Le site en vente tourne sur **o2switch**. Le compte o2switch appartient à **VIMAWEB** (confirmé par Valérie le 14/10).
- **OVH** : Valérie y détient le **domaine**, la **zone DNS** et un **ancien hébergement de 2013** (ancien site + boîtes mail). Il ne sert plus le site actuel.
- Pour la Phase 1, **on n'a pas besoin de l'hébergement** : l'admin WordPress suffit, comme le prévoit le contrat (art. 2).
- Pour la Phase 2 (staging, import en masse, mise en production), il faudra **VIMAWEB** ou un transfert du compte o2switch au nom de Valérie.

## Contexte / passif
- Projet : [[sellerie-confort-configurateur]] · Client : [[sellerie-confort]]
- Contrat et devis Phase 1 signés le 13/10/2026 (1 400 € HT, acompte 700 € versé, accès admin WordPress reçus). Délai : 4 jours de travail sur 10 jours calendaires à compter de l'accès effectif, soit vers le 23-24/10
- Les 10 jours courent : dates à tracer par écrit
- VIMAWEB n'est pas encore informé de notre collaboration (voir [[2026-10-07-sellerie-confort-cr-interne]], section « Risque VIMAWEB »)

## Qui détient quoi

| Élément | Où | Titulaire | Comment je le sais |
|---|---|---|---|
| Domaines `sellerieconfort.com`, `.fr`, `sellerie-confort.com` | OVH | Valérie (compte « SELLERIE CONFORT ») | Console OVH, capture du 14/10 |
| Zone DNS (le « panneau » qui dit où est le site) | OVH | Valérie | Serveurs de noms `ns200` / `dns200.anycast.me` |
| Site WordPress en vente | o2switch (`109.234.165.168`) | **VIMAWEB** | En-tête serveur `o2switch-PowerBoost-v3`, reverse DNS, déclaration de Valérie |
| `dev.sellerieconfort.com` | o2switch (`109.234.165.38`) | Probablement VIMAWEB (même hébergeur, à confirmer) | En-tête serveur |
| Ancien hébergement (créé le 17/06/2013, 69 Go sur 250, PHP 7.2) | OVH | Valérie | Console OVH |
| Hébergement performance « sellerz » | OVH | Valérie | Console OVH ; rôle inconnu |
| Boîtes mail (`mail.`, `smtp.`) | OVH | Valérie | DNS public + « Adresses e-mails : Actif » |
| Réception mail (MX) | Google Workspace | À confirmer | DNS public |
| Licences des plugins (`mkl_pc`, `wapf`, Divi) | — | **VIMAWEB** | CR du 07/10 |

## Expliqué simplement
- Le **domaine** est l'adresse postale de la boutique. Le **DNS** est le panneau qui indique à quelle adresse physique se trouve le local. L'**hébergeur** est le local lui-même.
- Valérie possède l'adresse et le panneau, chez OVH. Le panneau envoie les visiteurs vers un local loué chez o2switch, au nom de VIMAWEB.
- L'ancien local, chez OVH, existe toujours et contient l'ancien site. Plus personne n'y est envoyé par le panneau, mais il est encore payé et allumé.
- **Pourquoi OVH semble tout héberger** : la console OVH liste le domaine sur l'hébergement OVH, parce qu'il y est *configuré*. Ça ne dit pas où vont les visiteurs. Ce qui décide, c'est l'enregistrement DNS (type A), qui pointe vers o2switch.

### Chronologie probable (hypothèse, à faire valider)
1. **2013** : domaine et hébergement OVH créés le même jour ; site sur mesure signé Sam-Web.
2. **2022 environ** : un WordPress est préparé sur l'hébergement OVH (`dev2022`, page « Site en construction »).
3. **Plus tard** : le WordPress en vente est installé sur o2switch (par VIMAWEB), le DNS est repointé.
4. L'ancien hébergement OVH reste actif, avec les boîtes mail.

## Ce que j'ai vérifié (lecture publique, sans modifier quoi que ce soit)

| Test | Résultat |
|---|---|
| En-tête HTTP de `www.sellerieconfort.com` | `Server: o2switch-PowerBoost-v3` |
| Reverse DNS de l'IP du site | `salvador.o2switch.net`, propriétaire O2SWITCH |
| NS du domaine | OVH (`anycast.me`) |
| `dev.sellerieconfort.com` | WordPress, `noindex`, **sans mot de passe**, sur o2switch |
| Contenu `dev` | Pages inchangées depuis mars 2025, produits au plus tard juin 2026 : copie ancienne, jamais resynchronisée |
| OVH, `www.sellerieconfort.com` interrogé par IP | Ancien site Sam-Web (PHP 7.2), bandeau « nouveau site » |
| OVH, `dev2022` interrogé par IP | WordPress « Site en construction », `wp-login` et `wp-json` répondent |

## Points à aborder
1. **Faire voir la zone DNS à Valérie** : OVH → Noms de domaine → `sellerieconfort.com` → onglet Zone DNS → ligne **A**, cible `109.234.165.168`. Sa propre console règle le débat « c'est chez OVH ».
2. **Titulaire du compte o2switch : VIMAWEB.** Conséquence : ni Valérie ni moi ne pouvons créer un staging ou toucher au serveur sans eux.
3. **Copie du site pour l'audit** : voir la section suivante. Je propose la production via le plugin d'export prévu au contrat, avec son accord écrit.
4. **Information de VIMAWEB** : elle est d'accord pour les prévenir. À faire avant que mon activité ne devienne visible (accès, plugin d'export).
5. **Que faire de l'ancien hébergement OVH** : rien pour l'instant. Constat dans le rapport, décision plus tard avec elle.

## Copie du site : production ou dev ?

| | Export depuis la production | Export depuis dev |
|---|---|---|
| Accord écrit | Oui, de Valérie (art. 2, un mail suffit) | Accès admin sur dev, probablement via VIMAWEB |
| Dépend de VIMAWEB | Non | **Oui, probablement** : dev est sur leur compte |
| Fraîcheur | Données du jour | Figé vers juin 2026 |
| Risque pour la boutique | Faible (plugin d'export, à faire hors heures de pointe) | Aucun |
| Données clients | À filtrer à l'export (obligatoire) | **Présentes** : 1 071 utilisateurs, 151 entrées de formulaire |

**Décision (14/10)** : exporter **depuis la production**, avec filtre de tables et accord écrit de Valérie. Dev est écarté : le relevé Site Health montre **1 071 utilisateurs et 151 entrées de formulaire** (données personnelles, interdites dans le clone par l'art. 2) et des versions plus anciennes que la prod (Product Configurator 1.5.13 contre 1.7.5). Dev reste utile comme référence de lecture seule. C'est une préproduction créée avec l'outil WP Tiger d'o2switch, dans un compte cPanel nommé `sellerieconfort`.

## Quand l'accès o2switch deviendra nécessaire

| Cas | Phase | Indispensable ? |
|---|---|---|
| Export trop lourd (17,87 Go au total dont 15,06 Go d'uploads, base 1,47 Go) | 1 | Seulement si le plugin échoue |
| Staging propre pour développer et tester | 2 | Oui |
| Import en masse des images (~83 000) | 2 | Très utile (SSH ou FTP) |
| Scripts WP-CLI, tâches planifiées, réglages PHP | 2 | Utile |
| Sauvegardes et restauration avant intervention | 2 | Oui |
| Mise en production, purge du cache serveur | 2 | Oui |
| Logs d'erreurs pour le panier perdu | 1 (offert) ou 2 | Non bloquant |

**À retenir** : en Phase 1 on s'en passe. À poser en prérequis de la Phase 2, avec la justification de chaque besoin, et deux issues possibles : VIMAWEB conserve le compte et intervient à la demande, ou Valérie reprend le compte à son nom.

## Questions à poser
- Peux-tu envoyer une capture de la **zone DNS** OVH (ligne A de `sellerieconfort.com` et `www`) ?
- Qui a créé `dev.sellerieconfort.com`, quand, et est-il utilisé en ce moment ? (des fichiers y ont été régénérés les 5 et 17 septembre)
- Es-tu d'accord pour que j'exporte le site depuis la production avec le plugin prévu au contrat (accord écrit par mail) ?
- Accord pour que je prévienne VIMAWEB, ou préfères-tu le faire toi-même ?
- L'ancien hébergement OVH (créé en 2013, 69 Go) et l'offre « sellerz » : les utilises-tu pour autre chose que le mail ?
- Qui reçoit la facture du compte o2switch (toi ou VIMAWEB), et combien paies-tu VIMAWEB aujourd'hui pour l'hébergement ?
- Le domaine expire le **17/06/2027** : le renouvellement automatique est-il actif chez OVH ?

## Constats à mettre dans le rapport (sans y toucher en Phase 1)
- PHP 7.2 sur l'hébergement OVH actif (fin de support depuis longtemps), avec l'ancien site (« Mon compte », panier) toujours joignable en interrogeant le serveur directement
- 69 Go non inventoriés sur un plan de 2013 : sources d'origine (photos haute résolution), WordPress de 2022, sauvegardes ? Ne rien supprimer sans inventaire
- Deux offres OVH actives, dont une dédiée : dépense à vérifier. **Les boîtes mail sont sur ce plan** : résilier sans migrer les coupe
- `dev.sellerieconfort.com` accessible publiquement sans mot de passe, copie ancienne de la boutique
- Échéances : renouvellement du plan OVH en **avril 2027**, expiration du domaine le **17 juin 2027**
- Domaine `sellerie-confort.com` (avec tiret) et `.fr` : redirections à auditer (SEO)

## Prochaines actions
- [ ] Envoyer le mail à Valérie : capture de la zone DNS, accord écrit pour l'export en production, accord pour informer VIMAWEB, questions ci-dessus
- [ ] Noter par écrit la date d'accès effectif (départ du délai de 10 jours)
- [ ] Obtenir l'accord écrit **avant le 17/10**, puis faire l'export et le clone local
- [ ] Choisir l'outil d'export (filtre de tables pour exclure clients, commandes, comptes, formulaires)
- [ ] Ne rien modifier ni supprimer sur OVH ou o2switch

## Liens
- Client : [[sellerie-confort]]
- Projet : [[sellerie-confort-configurateur]]
- Réunion précédente : [[2026-10-07-sellerie-confort]] (prépa) · [[2026-10-07-sellerie-confort-cr-interne]] (CR)
