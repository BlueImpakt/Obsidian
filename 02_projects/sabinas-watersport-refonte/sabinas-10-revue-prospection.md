# Revue finale : la maquette est-elle solide pour la prospection ?

Date : 21/10/2026. Relecture faite sans sous-agent (skills `ux-copy`, `design-critique`, passage persona), sur la version `?v=68`.

## Grille (0 à 5), avant puis après le tour 1

| Critère | Avant | Après | Note |
|---|---|---|---|
| Offre claire en 5 secondes (hero) | 4,5 | 4,5 | Titre, note Google/Tripadvisor, vidéo, WhatsApp |
| Preuve (avis, chiffres) | 4 | 4 | Avis résumés, pas de vrais verbatims |
| Cadrage problème / gain pour Sabina | 4 | 4 | Page concept : 3 → 1, avant/après |
| Valeur démontrée (démo prix, flux auto) | 4,5 | 4,5 | |
| Réduction du risque | 3 | 4 | Ajout « Sans risque, sans pression » : anciens sites en ligne jusqu'à la bascule |
| Prochain pas clair | 2,5 | 4 | Bouton « Voir le nouveau site » + 3 étapes. **Dépend de `PITCH_CONTACT`** |
| Crédibilité de l'expéditeur | 2 | 3 | Ligne « sites web et automatisation ». Pas de référence client |
| Exactitude / zéro invention | 3,5 | 3,5 | Voir « À reconfirmer » |
| Personnalisation | 4 | 4 | |
| Finition mobile | 4 | 4 | |

Moyenne : environ 3,8 avant, 4,0 après.

## Corrigé au tour 1
- Page concept : bouton doré « Voir le nouveau site » dans l'en-tête.
- Page concept : bloc « Sans risque, sans pression » (réponse, appel de 15 min, offre claire, sites actuels conservés).
- Signature : « sites web et automatisation ».
- Copie FR : « Notre choix pour les familles », « Journée en voilier » (cohérence), « La suite ».

## Bloquant avant envoi
1. `PITCH_CONTACT` (app.js, ligne 14) est vide : sans lui, la page concept n'a aucun bouton de réponse.
2. Héberger `maquette/` en privé et remplacer `[LINK]` dans `docs/08`.
3. Passer les fichiers à `?v=69` après avoir rempli le contact.

## À reconfirmer le jour de l'envoi
- 479 avis Google, 443 Tripadvisor, prix Viator ≈ 1 250 €.
- L'appel de 15 minutes : c'est une proposition à confirmer par Melvin.
- Conditions marquées « Exemple » (acompte 30 %, météo, annulation 7 jours) : à valider avec Sabina.
- Légende vidéo : plus de mention WDR dans la maquette.

## Pas encore couvert
- Prix de la prestation (décision en attente côté fork).
- Une référence client ou une capture d'un site déjà livré.
- Promesse de délai de réponse (inconnue).
- Âges minimum et horaires des sports nautiques.
- Position des spots Cave Island, Blue Lagoon, Grand Canyon, Rockwall Caves (carte).
