# Ce qui n'est pas un fait dans la maquette

État au 28/10/2026. À relire avant l'envoi, puis à valider avec RM Croisières avant toute mise en ligne.

## 1. Inventé, marqué « exemple » dans la maquette

| Élément | Où | Réalité aujourd'hui |
|---|---|---|
| Délai de réponse « sous 24 h, du lundi au samedi » | écran de fin de la demande | Aucun délai publié ; horaires du bureau 9 h-17 h, lundi-samedi (site) |
| Lien WhatsApp (`wa.me/596696722544`) | barre mobile, fiche, tunnel | Aucun WhatsApp publié ; le numéro est le mobile du site |
| Trois demandes (Famille Exemple, Agence Exemple, Groupe Test), adresses example.com | vue bureau | Fictives |
| Messages automatiques et leur calendrier, choix « automatique / je relis » | vue bureau | Le système proposé, pas l'existant |
| Email de confirmation et lien « Payer l'acompte » | vue bureau | Le lien dépend de la banque de RM (inconnue) |

## 2. Vrai, mais tiré d'une autre source que rmcroisieres.com (à reconfirmer)

| Élément | Source |
|---|---|
| Frais de fin de séjour 680 € (260 + 300 + 120), 2 330 € pour Liberta | 12knots, conditions de RM, 28/10/2026 |
| Semaines du samedi au samedi | Grille de RM chez 12knots |
| Semaines complètes de Manureva, Le Dumbea, Estella | 12knots, 28/10/2026 (flux Booking Manager) |
| Note Google 4,3 sur 20 avis | Relevé de l'agent prospect-charter, 23/10/2026 |
| Nom « Liberta » du Sunreef 50 | Visite 3D et ancienne page du site |

## 3. Déduit ou choisi par nous

- **Année des grilles** : la seconde grille de chaque fiche est lue comme 2027 (confirmé par 12knots pour Manureva, Le Dumbea).
- **Prorata des nuits** pour une semaine à cheval sur deux saisons : règle retrouvée sur les prix de 12knots.
- **Skipper et hôtesse comptés 7 jours** par semaine (le site dit « par jour »).
- **« CB » = cabines.**
- **Port de départ** : le client choisit Le Marin ou Blue Lagoon ; on ignore quels bateaux partent de Saint-Vincent.
- **Contradictions du site laissées visibles** sur les fiches : Manureva (Lagoon 46 / adresse 42), La Gloria (Lagoon 42 / adresse 46), Rev'anou (13,92 m), Aquila 28 (13,61 m), caution de Liberta (2 000 €).
- **Légendes** : « Face au rocher du Diamant » (reconnaissable, page Croisières Nord de RM) ; « La marina de Blue Lagoon, baie de Calliaqua » (nom du fichier et page Blue Lagoon).

## 4. Ton commercial écrit par nous

« Choisissez la route, puis le bateau. », « Deux ports d'attache », « Vingt-deux bateaux, chacun son nom », « Ce que coûte une semaine », textes de la page concept. Les itinéraires sont ceux de RM, noms de lieux corrigés en anglais (« Mosquito » → Mustique).

## 5. Engagements de Melvin

Aucun prix ni délai promis par Blue Impakt. La page concept propose quinze minutes d'échange. `PITCH_CONTACT` (email et téléphone de Melvin) est vide dans `maquette/concept.js` : à remplir par Melvin avant l'envoi.

## 6. Photos

Toutes viennent de rmcroisieres.com (`research/flotte.json` : URL d'origine de chaque photo). Plusieurs fiches réutilisent des photos de chantier (Lagoon, Bénéteau) ou partagées entre bateaux du même modèle (Sol et Estella, Pantagonia, Affligem et Rev'anou, Manureva et Lily, Le Dumbea et Kayo) : c'est l'état du site actuel. La photo de Pantagonia, Affligem et Rev'anou porte le filigrane d'un autre site (« www.car… ») : à remplacer par une photo de RM.
