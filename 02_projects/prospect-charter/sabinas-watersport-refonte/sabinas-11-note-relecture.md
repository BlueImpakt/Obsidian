---
tags: [sabinas-watersport, prospection]
created: 2026-10-31
projet: sabinas-watersport-refonte
---

# sabinas-11-note-relecture

Projet : [[sabinas-watersport-refonte]] · Client : [[sabinas-watersport]] · Source : repo `sabina-watersport-refonte`, `docs/note-relecture.md` · Annexes : `attachments/` (DESIGN.md, décisions, hypothèses, faits, écart au skill, étude de réservation)


31/10/2026. Pour Melvin. Ce qui a changé depuis la v1 du 21/10, ce qui a été décidé à ta place et ce qu'il te reste à regarder. Écart au skill : `docs/11-ecart-au-skill.md` (tout est fait).

## Deux propositions en ligne

| | Adresse | État |
|---|---|---|
| **v1** (21/10, citée dans l'accroche) | https://sabinas-concept-x7k2m9.vercel.app/ | **intacte**, projet Vercel `sabinas-concept-x7k2m9`, rien redéployé |
| **v2** (cette passe) | https://sabinas-xuygcn.vercel.app/ · page privée https://sabinas-xuygcn.vercel.app/p/ | nouveau projet Vercel `sabinas-xuygcn` ; la maquette renvoie vers `/p/` 7 jours après J0 (J0 par défaut : mardi 3/11) |

Rien n'est envoyé. `PITCH_CONTACT` est vide. Dossier d'envoi : `sortie/envoi/` (hors git), note dans le vault `sabinas-12-dossier-envoi`.

**Messages à relire avant envoi** (`sortie/envoi/messages/`, en anglais) :
- le J0 est le modèle d'un premier contact (« I'm Melvin… »), alors que tu as déjà écrit à Sabina pour la v1 (`docs/08`, « we spoke last week ») : à présenter comme une seconde proposition, avec les deux liens ;
- le J+8 n'a pas de détail d'avis vérifié : à écrire à la main ou à sauter. Sa deuxième phrase, qui décrit la maquette, est maintenant propre à Sabina : la demande arrive complète et chiffrée, et se confirme en deux gestes.

Aperçu local : `npx --yes http-server@14.1.1 maquette -p 4186 -c-1` dans le dépôt, puis http://127.0.0.1:4186/.

## Ce qui se voit à la première lecture

- **Hero plein écran** : vue drone HD du catamaran, titre posé dessus (à droite sur ordinateur, pour ne pas couvrir le bateau), deux boutons, l'itinéraire en légende et le numéro en signature.
- **En-tête** : « Your holiday highlight », menu Boat trips · Watersports · Prices & terms · Who we are, bouton « Request », 4 langues (EN, DE, IT, FR).
- **Cartes** : grille régulière de 6 cartes. **Prix et conditions** : chaque tarif une seule fois, puis les conditions.
- **Demande en 3 étapes** (sortie et date, coordonnées, envoi), message WhatsApp déjà rédigé vers le numéro publié par Sabina.
- **Nouveau en passe 2** :
  - **Vue bureau** (`#bureau`, lien depuis l'écran de fin) : la demande qu'on vient d'envoyer arrive en tête ; lire puis confirmer et envoyer le lien d'acompte en 2 gestes ; proposer une autre date ; alerte vent du jeudi (garder ou déplacer) ; planning de la semaine ; messages automatiques. Données d'exemple, badge « Exemple ».
  - **Mode intermédiaire** : case « I'm booking for a guest » à l'étape 2 (réception d'hôtel, agence), qui paie l'acompte, lien « Hotels and agencies » en pied de page. Badge « À confirmer ».
  - Fiche catamaran : « On board » (4 points), galerie réordonnée ; voilier sans modèle de bateau, 3 étapes ; FAQ « pas de sortie dauphins » ; histoire de l'équipe complétée ; sports nautiques « dès 15 € ».
  - Calendrier : aujourd'hui et demain signalés, mois passés retirés ; disponibilités alignées sur le planning du bureau.

## Sourcé, supposé, manquant

- **Sourcé** (`docs/faits.md`, 49 faits vérifiés par la porte dans les 4 langues) : prix 2026, horaires, capacités, acompte de 150 €, téléphone, WhatsApp, saisons, équipe, avis Google 5,0 / 510. Prix plateforme désormais sourcé : Booking.com 1 250 €, Pelago 1 277,70 € (relevés le 31/10).
- **Retiré en passe 2** (audit de couverture, `docs/revues/couverture-site.md`) : le modèle du voilier (« Dufour 30 Classic » sur Click&Boat, mais la coque de la photo porte « Gib'Sea 302 »), le « retour sous voiles » du catamaran (lu sur une photo, écrit nulle part). La porte interdit désormais ces mots.
- **Supposé** (`docs/hypotheses.md`, badges) : règle météo, annulation à 7 jours, solde le jour de la sortie, réponse sous 24 h, jours complets, mode intermédiaire, toutes les données du bureau, coucher de soleil à la voile.
- **Manque** : photos HD du jet-ski et des vidéos ; tes coordonnées (`PITCH_CONTACT`) ; les réponses de Sabina aux questions de `docs/etudes/2026-10-31-sabinas-reservation.md`.

## Décisions prises à ta place (détail et coût : `docs/decisions.md`, n° 1 à 21)

1. v1 mise à niveau (pas `maquette-3d/`) ; titre « Lindos from the sea. The Blue Lagoon, for your group alone. »
2. Vue bureau dans la même page ; données de démo sur la semaine du lundi 7 juin 2027 (n° 12, 13).
3. Mode intermédiaire ajouté sans preuve que Sabina travaille avec les réceptions : à retirer en 15 min si non (n° 14).
4. Nouveau projet Vercel pour la v2, lien valable 7 jours après J0 (n° 15, 16). Messages d'envoi en anglais (n° 17).
5. **À trancher par toi** :
   - pas de recadrage portrait du hero sur téléphone : plus net, mais le LCP (3,9 s pour 4,0 s) sauterait (n° 19) ;
   - bouton principal en deux apparences, or plein et encre-or (n° 20) ;
   - titre à droite et chapeau à gauche du hero sur ordinateur ;
   - adresse mail affichée : info@dolphin-tours-rhodos.com, la seule publiée ;
   - note Google sur le hero, suggérée par les personas : non faite, contraire à ta préférence d'un hero sans pastille.
6. **À demander à Sabina** : le modèle du voilier ; le rôle de Roland et le nom « Dolphin Tours ».

## Revues de la passe 2 (`docs/revues/`)

- **Comparaison à l'aveugle** avec Sunset Oia, Edmiston, Burgess (relevé `references-premium.md`), 2 juges, 6 écrans, 390 et 1 440 px. Passage 1 : 1re ex aequo avec Edmiston (7,2). Après corrections, passage 2 : **1re**, 7,8 contre 7,5, 1re sur 4 écrans sur 6 (`aveugle-v2-passage2.md`).
- **Finish-Gate** : HOLD avec 3 bloquants, corrigés. La contre-revue a donné HOLD avec 3 majeurs (lien WhatsApp du bureau, feuille trop basse en paysage, galerie trop haute), corrigés, **non revus une 3e fois**.
- Accessibilité, personas, textes 4 langues, code, motion, guidelines : corrigés ou consignés dans `decisions.md`.
- **Tunnels des concurrents à Rhodes** (`docs/etudes/2026-10-31-rhodes-tunnels-concurrents.md`) : la réservation instantanée d'un bateau privé n'existe que sur les plateformes, où Sabina vend elle-même. En direct, personne ne la propose : le tunnel par demande est au niveau du marché.

## Mesures (porte qualité n° 10, 31/10/2026 : **PASS**)

Rapport : `sortie/porte-10/rapport.md` (hors git). Médiane de 3 passages, indice machine 1 282 à 1 688.

| | Téléphone, vrai bridage | Téléphone, simulé | Ordinateur |
|---|---|---|---|
| Accueil : LCP / poids | 3,9 s / 997 Ko | 4,2 s / 1 033 Ko | 0,8 à 2,3 s / 2,3 Mo |
| Fiche catamaran : LCP / poids | 3,9 s / 1,3 Mo | 7,0 s / 1,4 Mo | 0,8 à 2,4 s / 2,6 Mo |
| Accessibilité / bonnes pratiques | 100 / 100 partout | | |
| CLS | 0,034 au plus | | |

- 144 vues sans débordement (4 langues, 360 à 1 920 px). 768 images, aucune agrandie. 40 états ouverts sans échec. 0 erreur console. 49 faits OK.
- Tunnel : 7 gestes et 3 étapes (client, téléphone et ordinateur), 9 gestes et 3 étapes (réception d'hôtel).
- Les LCP à 3,9 s frôlent le seuil : à remesurer machine libre si tu touches au hero.
- 11 photos moins nettes que l'écran d'un iPhone (vidéos YouTube, jet-ski de 306 px) : à demander en HD.

## Ce que la porte ne remplace pas : 10 minutes sur ton iPhone

Safari, sur https://sabinas-xuygcn.vercel.app/, en portrait puis en paysage :

1. Accueil, carte « Private Catamaran Day », fiche, galerie avec les flèches.
2. « Choose a date », une date, nom et WhatsApp, envoi, jusqu'à l'écran de fin.
3. Ouvre le lien WhatsApp pour voir le message rédigé, **sans l'envoyer** : il part chez Sabina.
4. Écran de fin, « See Sabina's side » : la demande en tête du bureau ; Review puis Confirm ; alerte vent (Keep / Move) ; planning.
5. Recommence en cochant « I'm booking for a guest » : nom du client, réception, qui paie ; vérifie le résumé et le bureau.
6. Pied de page « Hotels and agencies ».
7. VoiceOver sur l'accueil et la demande. Langues IT et DE dans le menu.
