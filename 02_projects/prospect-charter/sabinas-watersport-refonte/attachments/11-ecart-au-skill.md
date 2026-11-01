# 11 · Écart entre la maquette Sabina et le skill `maquette-prospect`

31/10/2026. Sabina a été faite les 21 et 22/10, avant le skill. Ce document compare la maquette `maquette/` (v1, celle déployée en privé et citée dans l'accroche) au skill tel qu'il est après RM Croisières, Ty Domino et Lab'oratoire.

**Quelle maquette ?** `maquette/` et non `maquette-3d/`. La v1 est celle que Melvin a itérée (hero drone HD, galeries, vidéos, carte OSM), déployée et citée dans le message. `maquette-3d/` est restée au point de contrôle B, avec un Finish-Gate KO. Si c'était le mauvais choix : les corrections décrites ici se reportent sur `maquette-3d/` en 1 à 2 jours, les faits et la porte servent tels quels.

Coût : **S** < 30 min · **M** 30 min à 2 h · **L** plus de 2 h. Statut après correction en fin de ligne (✅ fait, ⏳ partiel, ✗ non fait, avec la raison).

## 1. Ce qui se voit à la première lecture (priorité)

| Exigence du skill | Sabina v1 | Correction | Coût | Statut |
|---|---|---|---|---|
| **Hero** : photo sur tout le premier écran, titre posé dessus, deux boutons, numéro du bureau en signature (filet, Didone italique), pas de légende ni de pastille sur la photo, zoom lent, texte en cascade | Photo en encart à côté du texte ; 3 pastilles sur la photo (« Rhodes east coast », « 5.0 · 479 Google reviews », « 4.9 · Tripadvisor #1 ») ; bouton lecture vidéo sur la photo | Hero plein écran sur la vue drone HD (photo choisie par Melvin pour la v1, 2 400 px), titre et accroche dessus, boutons « Voir les sorties » et « Sports nautiques », numéro +30 697 259 3276 en signature. Pastilles et bouton vidéo retirés (la vidéo reste dans « Qui sommes-nous »). Zoom de 10 s borné à la taille du fichier | M | ✅ |
| **Accroches percutantes**, un fait propre au client plutôt qu'un superlatif | « Exclusive boat trips… First-class service… absolute privacy » ; « Choose your day at sea » ; « What guests mention most » | Titres réécrits sur les faits : itinéraire réel, 8 personnes au plus, 2007, Lavezzi 40. Superlatifs retirés (« first-class », « absolute », « exclusive » en titre). 3 titres de hero proposés dans la note de relecture | M | ✅ |
| **Photos jamais agrandies** (mesurées) | Pas mesuré ; vignettes en `-sm` (500 à 800 px) dans des cadres qui peuvent les dépasser à 1 440 px ; webp qualité ~72 | Pipeline reproductible depuis les originaux (`research/photos.py`) : 1 200 et 900 px en qualité 95, grande version jusqu'à 2 400 px, vignettes en 78 ; `srcset` partout ; la porte mesure chaque `<img>` à 4 largeurs | M | ✅ |
| **Sources non citées dans les pages** | « Platform price: Viator listing… October 2026 », « From Sabina's YouTube channel », « Summary of public reviews… as of October 2026 », « Dufour 30 Classic: Click&Boat listing », lien LinkedIn de recherche | Retirés des pages ; sources dans `docs/faits.md` et `docs/hypotheses.md`. Reste en page : badges « Exemple » / « À confirmer », et la mention © OpenStreetMap (licence de la carte, pas une source) | S | ✅ |
| **Avis : nombre masqué sous 50** | 479 et 443 avis (au-dessus de 50) | Règle sans effet ici. Chiffres revérifiés le 31/10 sur Wanderlog : Google 5,0 / **510** (la v1 disait 479), Tripadvisor 4,9 / 443. Affichés seulement dans la section avis et la fiche, plus sur la photo | S | ✅ |
| **Prix à un seul endroit** (« Prix et conditions », tableau groupé) | Prix complets répétés : cartes, fiche, calculateur, pages détail, grille des sports nautiques dans une fiche | Section « Prix et conditions » sur l'accueil : un tableau par famille (catamaran, voilier, speedboat, sports nautiques), conditions dessous. Les cartes gardent un seul « dès … » (invariant luxe : prix sur la carte), les fiches calculent le total pour le nombre de personnes choisi et renvoient au tableau | M | ✅ |
| **Demande WhatsApp pré-rédigée** (sortie, date, personnes, total, options), depuis la fiche et le tunnel | Lien `wa.me` avec « Hello Sabina, I'm interested in a boat trip » | Message construit à partir du choix : sortie, date, personnes, total, langue ; depuis la fiche, chaque étape du tunnel et l'écran de fin. Numéro publié par Sabina (+49 176 31707126) : pas de badge « exemple » | S | ✅ |
| **En-tête** : accroche du client entre logo et menu en Didone italique, menu dans l'ordre des sections, bouton « Request », fond translucide, langue dans l'en-tête | Bandeau « Concept by Blue Impakt… draft, not live » au-dessus ; menu à 2 entrées ; pas d'accroche | Bandeau retiré (lien « Concept » en pied de page). Accroche du client « Your holiday highlight » (texte de catamaran-yachtsailing-rhodos.com) en GFS Didot italique ; menu Sorties · Sports nautiques · Prix et conditions · Qui sommes-nous ; bouton « Demander » ; blanc 70 % + flou ; menu mobile en panneau | M | ✅ |
| **Téléphone d'abord** (390 px, puis 1 440 / 1 920) | Conçu mobile, mais premier écran non mesuré aux 6 tailles | Premier écran mesuré à 390 × 664 et aux tailles d'ordinateur du protocole ; barre d'action du bas conservée | S | ✅ |
| **Langues DE et IT, relues** (agent natif avec `ux-copy`) | EN, FR, DE ; pas d'italien ; DE jamais relu par un natif simulé | Italien ajouté (accueil, fiches, tunnel, concept) ; relecture DE et IT par deux agents « client natif » ; la note de relecture dit qu'aucun natif humain ne les a lues | L | ✅ |

## 2. Étapes du skill

| Étape | Sabina v1 | Manque | Correction | Coût | Statut |
|---|---|---|---|---|---|
| 1. Relevé et faits sourcés | Audit `docs/01` très complet (crawl, 47 images vérifiées), inventaire photos, `docs/09` | Pas d'extraction outillée, pas de `docs/faits.md` valeur par valeur, pas de test qui compare la maquette aux faits | `extraire.py` sur les 3 domaines → `research/extraction/` ; `docs/faits.md` ; `gate-faits.json` vérifié par la porte | M | ✅ |
| 1. Étude de réservation | Contenue dans `docs/01 §4`, `02 §4`, `04` | Pas de fichier dédié | `docs/etudes/2026-10-31-sabinas-reservation.md` (synthèse sourcée des docs existants) | S | ✅ |
| 1. Tunnels concurrents de la zone | `docs/02 §2` : 9 concurrents du sud-est de Rhodes, outils relevés (Booknetic, Rezdy, OTA) | Pas de rejeu de tunnel écran par écran comme pour la Martinique | Non refait : la conclusion de `02 §2.2` (personne n'a de calendrier ni d'acompte en ligne pour du privé) suffit à fixer le principe. Si elle est fausse : le tunnel « demande » pourrait sembler en retard face à un concurrent en réservation immédiate ; refaire l'étude = 1 agent, ~1 h | L | ✅ refait le 31/10 (2e passe) : `docs/etudes/2026-10-31-rhodes-tunnels-concurrents.md`, 15 opérateurs rejoués |
| 1. Jours et saison réels | Calendrier de démo mai-octobre 2027 | Saison réelle par produit (sunset fin mai à mi-septembre, voilier jusqu'au 25/09) non appliquée au calendrier | Calendrier borné par produit d'après les faits ; jours complets marqués « Exemple » | S | ✅ |
| 2. Références premium + invariants | `docs/02 §3` (5 opérateurs nautiques) | Pas de maisons de luxe hors secteur, pas de captures | Invariants appliqués (`invariants-luxe.md`) ; pas de nouveau relevé. Coût si faux : la comparaison à l'aveugle n'a pas de références propres à Rhodes | L | ✅ `docs/revues/references-premium.md` : 11 sites, captures 390/1 440 |
| 3. Idée propre au client + `DESIGN.md` | Idée « la journée en 4 escales » (route Stafilia → Cave Island → Lindos → Blue Lagoon) déjà là ; système dans l'en-tête de `styles.css` | Pas de `DESIGN.md` | `DESIGN.md` écrit (jetons réels, règles du hero, ce qui reste libre justifié par Sabina) ; l'idée passe dans le hero comme légende-programme | S | ✅ |
| 4. Planche validée par Melvin | Melvin a validé la v1 en direct pendant la construction | — | Sans objet (maquette existante) | — | — |
| 5. Construire, langues, animations des textes | Motion (CDN) : entrées, compteurs, cartes | Pas de garde `navigator.webdriver` (captures de la porte) ni `?anim` | Classe `js-anim` posée dans le `<head>` (garde webdriver, `?anim`, mouvement réduit) ; texte du hero et titres qui montent | S | ✅ |
| 6. Porte qualité | Jamais lancée | `gate.json`, `gate-faits.json`, tests du projet | Écrits ; porte n° 6 PASS sur les 8 contrôles bloquants (LCP téléphone 3,8 s, à remesurer avant envoi) | M | ✅ |
| 6. Batterie de revues (Finish-Gate, personas, a11y, code, aveugle, couverture) | Finish-Gate, a11y, ux-copy faits le 21/10 sur une version antérieure | Pas de comparaison à l'aveugle, pas d'audit de couverture outillé, pas de parcours concierge | Non relancés dans cette passe (priorité au visible) ; listés dans la note comme prochaine étape | L | ✅ Finish-Gate (HOLD puis contre-revue), impeccable + guidelines, accessibilité, textes, personas, code, motion, couverture, 2 juges à l'aveugle (`docs/revues/*-v2*.md`) |
| 7. Dossier d'envoi (`envoi.py`) | Accroche WhatsApp DE/EN et e-mail EN écrits à la main | Pas de vidéo, pas d'avant/après outillé, pas de page privée `/p/` | Hors périmètre (ni envoi ni déploiement) | L | ✅ `envoi/envoi.json`, dossier dans `sortie/envoi` et dans le vault (`sabinas-12-dossier-envoi`) |

## 3. Exigences du tunnel

| Exigence | Sabina v1 | Correction | Statut |
|---|---|---|---|
| Prix total visible avant les coordonnées | Oui (« Estimated price » en pied de feuille dès l'étape 1) | Gardé ; total recalculé en direct | ✅ |
| Date et personnes en premier | Oui | Gardé ; calendrier borné à la saison du produit | ✅ |
| ≤ 3 étapes, < 10 gestes | 3 étapes ; 10 à 11 gestes (e-mail obligatoire, case à cocher) | E-mail facultatif si WhatsApp donné ; case à cocher remplacée par les conditions affichées au-dessus du bouton d'envoi : 7 gestes | ✅ |
| Annulation et météo visibles avant l'envoi, au plus près des CGV | Case « I have read the booking conditions » ; conditions inventées (30 %, J-7) | Sabina n'a pas de CGV : on affiche ce qui est réel (acompte fixe de 150 € par PayPal ou carte) et, marqués « À confirmer », une règle météo et une règle d'annulation proposées | ✅ |
| Alternative humaine à chaque étape | Seulement la barre du site, masquée par la feuille | Lien WhatsApp pré-rédigé et appel dans chaque étape et à la fin | ✅ |
| Écran de fin avec délai chiffré | « Sabina will get back to you on WhatsApp shortly » | « Réponse sous 24 h » marquée « Exemple » (Sabina ne publie aucun délai) | ✅ |
| Côté gérant | Page concept : flux « confirmer d'un tap », rappel, alerte vent, avis | Vue `#bureau` (2e passe) : demandes complètes, confirmer en 2 gestes, planning qui suit les décisions, alerte vent, messages automatiques | ✅ |
| Mode intermédiaire (concierge, agence) | Absent | Ajouté (2e passe), badge « À confirmer » : case « I'm booking for a guest », lien d'acompte au client ou à l'hôtel, entrée en pied de page ; 9 gestes, 3 étapes | ✅ (à confirmer par Sabina) |

## 4. Préférences de Melvin

| Préférence | Sabina v1 | Après |
|---|---|---|
| Photo principale = celle mise en avant par le client | Choix faits à la main le 21/10 (inventaire) | Recoupé avec la photo mise en avant de l'extraction ; écarts listés dans `docs/faits.md` ✅ |
| Cartes pleines | Vignette dans une ligne de liste | Photo qui remplit son cadre ✅ |
| Une seule forme de fiche | Une forme (galerie défilante, choix de Melvin sur Sabina : 5 éléments, vidéo au centre) | Gardée : c'est la décision propre au projet, pas la mosaïque 1 + 2 ✅ |
| Jamais agrandir | Non mesuré | Mesuré par la porte ✅ |
| Webp 95, versions 1 200 et 900 px, vignettes 78 | ~72, tailles variables | Pipeline refait ✅ |
| Langue dans l'en-tête | Oui | 4 langues : EN, DE, IT, FR ✅ |
| Pas de source citée dans les pages | 5 mentions | Retirées ✅ |
| Durée proposée dans le tunnel venue du site | Durées du site (6 h, 3 h, 4 h, 2,5 h) | Gardées ✅ |
| Nombre d'avis seulement à partir de 50 | 479 / 443 | 510 / 443 (revérifié) ✅ |
| Titres percutants | Plusieurs titres génériques | Réécrits ✅ |
| Textes animés, jamais en mouvement réduit ni sous `navigator.webdriver` | Animations sans garde webdriver | Garde ajoutée ✅ |
| Pas de bouton pause sur le hero | Sans objet (photo fixe) | Photo fixe avec zoom lent ✅ |
| Menu dans l'ordre des sections | 2 entrées | 4 entrées dans l'ordre ✅ |
| Aucun avis, chiffre ou coordonnée inventés | Thèmes d'avis résumés présentés comme tels ; « English & Deutsch » non sourcé ; acompte de 30 % inventé ; « dès 640 € » faux sur la carte speedboat | Thèmes gardés (synthèse sourcée, sans citation, liens vers les avis) ; langues à bord retirées (remplacées par « Skipper RYA Offshore », sourcé) ; acompte réel de 150 € ; « dès 400 € » ✅ |
| Pas de déploiement | `.vercel/` présent, déployé le 22/10 | Rien redéployé ; la version en ligne reste l'ancienne ✅ |
| Prix à un seul endroit | Non | Section « Prix et conditions » ✅ |
| WhatsApp pré-rédigé | Non | Oui ✅ |
| PITCH_CONTACT vide | Vide | Vide ✅ |

## 5. Pièges techniques du skill

| Piège | Sabina v1 | Correction | Statut |
|---|---|---|---|
| HTML identique au dictionnaire | L'anglais est lu dans le HTML (pas de doublon) ; FR/DE/IT dans `i18n.js` | Test de parité des clés dans les 4 langues | ✅ |
| Diaporama et photos sous le premier écran chargées trop tôt | Galeries en `loading=lazy` | Gardé | ✅ |
| Pas de mesure JS pour la mise en page | Hero en CSS | Hero plein écran en `svh`/`dvh` CSS | ✅ |
| Polices Google bloquantes | Feuille Google Fonts bloquante dans le `<head>` | Chargées à l'événement `load` de la fenêtre (`window.addEventListener`), repli Didot / Bodoni 72 / Georgia | ✅ |
| `[hidden]` contre `display:grid` | Déjà `[hidden]{display:none!important}` | — | ✅ |
| Grilles en `minmax(0,1fr)` | Partiel | Cartes et tableaux de prix | ✅ |
| `sizes` qui compte le recadrage | Non | `sizes` des cartes et du hero calculés avec le ratio | ✅ |
| Classe d'animation posée dans le `<head>` | Animations posées par le script en fin de page | Classe `js-anim` posée en ligne dans le `<head>` | ✅ |
| `favicon.ico` absent | Absent (bonnes pratiques) | Ajouté | ✅ |
| Lighthouse simulé + vrai bridage | Jamais mesuré | Les deux, via la porte | ✅ |

### Pièges nouveaux rencontrés dans cette passe (à reporter dans le skill)

| Piège | Constat | Remède |
|---|---|---|
| Dictionnaire anglais de la v1 plus fort que le HTML | Le menu affichait encore « Exclusive boat trips » après la réécriture du HTML | `t()` lit d'abord l'anglais du HTML ; le dictionnaire EN ne sert qu'aux textes écrits en JS |
| Listes de jours codées par langue | Exception en italien à l'ouverture du calendrier (tunnel IT en échec) | Jours tirés d'`Intl.DateTimeFormat` |
| En-tête à 4 langues | Débordement de 82 à 153 px à 1 440 px en IT et FR | Bouton court (« Request »), accroche seulement dès 1 400 px, en-tête plus large que le contenu |
| Zoom du hero en images-clés avec `var()` | 2,1 s de « Style & Layout » sur téléphone bridé, LCP 6,4 s | Web Animations API avec une valeur calculée (compositeur) : LCP 3,8 s |
| Hero q95 en 2 400 px choisi par les téléphones DPR 3 | 1,6 Mo pour une seule photo | `<picture>` : 900 px si densité ≤ 2,6, 1 200 px au-delà ; 2 400 px seulement sur ordinateur |
| Vignettes 900 px q95 dans les cartes | 329 Ko pour une carte | Vignette 720 px en qualité 78 (cartes sur téléphone Android) |
| Fourchette « up to 4 » + « 950 € » dans un tableau | La porte lit « 4 950 » | Faits visés sur `.tarif td.amt` (piège déjà connu du skill, retrouvé ici) |
| Bouton de la barre sur la fiche catamaran | Ouvrait la demande sans présélection (bug hérité de la v1) | `data-book="cat-private"` sur la fiche |
