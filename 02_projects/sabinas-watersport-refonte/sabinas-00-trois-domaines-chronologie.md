---
tags: [project-doc, sabinas-watersport]
created: 2026-10-21
projet: sabinas-watersport-refonte
source: GitHub/sabina-watersport-refonte/docs/00-trois-domaines-chronologie.md
---

↩ [[sabinas-watersport-refonte]]

# Pourquoi 3 domaines, et dernière mise à jour de chacun

Relevé du 21/10/2026 : RDAP Verisign, archives Wayback, horodatages des images Jimdo, texte des sites.

## Chronologie

| Domaine | Créé | Renouvelé | Expire | Hébergement | Ce que c'est |
|---|---|---|---|---|---|
| sabinas-watersport.com | **13/02/2007** | 13/02/2026 | 13/02/2027 | Jimdo Creator | Le centre nautique d'origine, ouvert en 2007 |
| catamaran-yachtsailing-rhodos.com | **19/05/2017** | 20/05/2026 | 19/05/2027 | Jimdo Creator | Site mono-produit catamaran/voilier, lancé avec le bateau |
| dolphin-tours-rhodos.com | **01/12/2022** | 02/12/2025 | **01/12/2026** | Jimdo Dolphin | Site de la société de croisières « Dolphin Tours Rhodos », créée en 2023 |

Les 3 domaines sont chez le même registrar allemand (InterNetX, revendeur de Jimdo) et sur les mêmes serveurs DNS Jimdo, donc tout est géré depuis un même compte ou une même personne.

## Pourquoi 3 sites (faits + hypothèses)

1. **Fait : deux entités.** Page About de dolphin-tours : « With our cruise company Dolphin Tours Rhodos we started new in 2023 and cooperate well with our Watersports company "Sabinas Watersport Rhodos" where the boat trips start. » Les croisières sont donc portées par une société distincte depuis 2023.
   - *Hypothèse à vérifier avec Sabina* : séparation juridique, fiscale ou d'assurance. En Grèce, le transport de passagers en excursion (licence de bateau professionnel ou de tourisme) n'a pas le même cadre qu'une concession de sports nautiques sur la plage.
2. **Fait : couches successives.** Un site a été ajouté à chaque nouvelle activité (2007 sports nautiques → 2017 catamaran → 2022/23 société de croisières), sans jamais refondre l'existant.
3. **Hypothèse : tactique SEO des années 2010.** `catamaran-yachtsailing-rhodos.com` est un domaine qui reprend mot pour mot la requête visée (exact-match domain), et son premier titre en 2018 le confirme : « catamaran yachtsailing rhodes charter… ». La tactique vaut beaucoup moins depuis la mise à jour Google « EMD » de 2012, et elle disperse l'autorité sur 3 domaines.
4. **Résultat aujourd'hui.** Les 3 sites vendent les mêmes bateaux, au même point de départ, avec les mêmes contacts. Le catamaran apparaît sur les 3 sites, le voilier et le speedboat sur 2. L'acheteur change de domaine en cliquant sur un prix, et Google voit 3 sites concurrents du même propriétaire.

## Dernière mise à jour de chaque site

| Site | Dernière mise à jour datable | Preuve |
|---|---|---|
| sabinas-watersport.com | **26/02/2026** | Dernière image envoyée (horodatage `/version/1772101639`) sur la page DE catamaran. Autres envois les 2, 18 et 30/01/2026. En oct. 2025 le site affichait encore « 2025 » ; aujourd'hui uniquement « 2026 ». |
| catamaran-yachtsailing-rhodos.com | **25/02/2026** | Dernière image (`1772005451`) sur la page DE prix 2026 + sunset ; favicon changé le 19/01/2026. Prix relevés entre oct. 2025 et aujourd'hui : privé **850 → 950 €**, semi-privé **150 → 160 €/pers**. |
| dolphin-tours-rhodos.com | **saison 2026, date exacte illisible** | Jimdo Dolphin n'expose pas d'horodatage et les archives Wayback sont des coquilles JS vides. Les contenus sont marqués « Welcome 2026 » et « Prices 2026 ». |

Lecture : Sabina met à jour **une fois par an, en janvier-février avant la saison** (prix, années, quelques photos), sur les 3 sites à la main. Le site est maintenu, mais par une personne qui recopie la même info en 3 endroits et en 3 langues, d'où les incohérences.

## Points d'attention pour la proposition

- **dolphin-tours-rhodos.com expire le 01/12/2026.** C'est le bon moment pour décider de la consolidation (renouveler pour garder la redirection 301).
- **Argument commercial principal** : « une seule mise à jour par an au lieu de trois ». Les prix sont saisis une fois et s'affichent partout, dans toutes les langues.
- La migration doit conserver les 3 domaines en redirection 301 page à page, pour ne perdre ni le SEO ni les liens existants (OTA, TripAdvisor, Google Business).
