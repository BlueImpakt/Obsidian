---
tags: [client, actif, p2, environnement, france]
created: 2026-08-29
statut: actif
priorite: p2
secteur: environnement
localisation: france
---

# naeco

## Relationnel
- **Association** : NAECO — "Mobiliser l'art et la science pour l'océan"
- **Activité** : expéditions à la voile, créations artistiques, sensibilisation ; documentation de la biodiversité marine (ex. expédition 2022 "The Pelagos Sanctuary", collaboration STARESO)

## Historique des échanges
-

## Décisions prises
-

## Besoins identifiés
- Site vitrine de l'association
- Carte interactive des expéditions/observations/données scientifiques (Pelagos, escales, sites d'étude)

## Devis / propositions
-

## Next actions
- [ ]

## Journal
- 2026-09-10 (suite) : Sur [[naeco-carte]] — logo NAECO posé sur le splash de chargement (fond ivoire), 2 sites d'étude ADNe ajoutés et positionnés dans le tracé Point Zéro pré-tracker. Bug "trace disparaît à l'ouverture de l'éditeur" signalé de nouveau non résolu après un premier fix poussé — reste ouvert. Détails dans la fiche projet.
- 2026-09-10/11 (suite) : Sur [[naeco-carte]] — bug éditeur reclassé faux positif de cache navigateur (fix confirmé fonctionnel). Décision : plus de tracé pour STARECORSICA (campagne sans navigation propre), retiré de la carte en gardant l'entrée en légende. Image de partage (og-image) et écran de chargement peaufinés (Corse + "EXPÉDITIONS"). Deux bugs réels trouvés et corrigés : flash/saccade à l'ouverture (repaint GPU de la légende, diagnostiqué depuis une vidéo client) et header mobile qui débordait à 320-375px (boutons de recentrage/présentation inatteignables) — les deux corrigés mais pas encore poussés. Nouveau bug signalé en fin de session : création de site d'étude cassée. Détails dans la fiche projet.
- 2026-09-11 : Sur [[naeco-carte]] — bug "création de site d'étude cassée" (signalé en fin de session précédente) corrigé, ainsi qu'un bug photo d'escale invisible (lien Google Drive mal interprété). Nouveau site d'étude Point Zéro ajouté (Galéria). Détails dans la fiche projet.
- 2026-09-11 (suite) : Sur [[naeco-carte]] — faille de sécurité (mot de passe éditeur + clé JSONbin en clair dans le code) corrigée et vérifiée en prod via un proxy Cloudflare Worker (lecture et écriture). Flash visuel intermittent (légende puis carte) diagnostiqué et corrigé en plusieurs essais, jusqu'à isoler la trace animée sur son propre calque SVG. Vignette des popups "sites d'étude" retirée, onglet de filtre "Photos" retiré du header. Nouvelle escale "Point Zéro" créée pour Ota (11/09, projection MARE NOSTRUM + ateliers de sensibilisation). Détails dans la fiche projet.
- 2026-09-12 : Sur [[naeco-carte]] — bug de tracé live invisible dans le navigateur intégré Instagram corrigé (CORS ouvert sur les endpoints de lecture publique du tracker, déploiement manuel du Worker restant). Deux nouveaux sites d'étude Point Zéro ajoutés sur le tracé (Plongée scientifique 30M, Prélèvement ADNe sub-surface Calcatoggio). Détails dans la fiche projet.
- 2026-09-12 (suite) : Sur [[naeco-site]] — bandeau « Site en chantier » du header finalisé en « 🚧 Site en travaux » et déployé (`a18c6a0`), après avoir été implémenté deux fois sans être commité. Détails dans la fiche projet.
- 2026-09-13 : Sur [[naeco-carte]] — légende mobile rendue repliable (fix chevauchement avec les popups), 343 points de tracking parasites nettoyés (nuit du 12 au 13/09, GPS en dérive au mouillage). Détails dans la fiche projet.
- 2026-09-13 (suite) : Sur [[naeco-carte]] — 343 points GPS parasites nettoyés + garde-fou serveur anti-dérive déployé sur le tracker ; styling carte (transparences, fond marine, onglets header) ajusté sur plusieurs itérations et déployé. Détails dans la fiche projet.
- 2026-09-15 : Contexte d'article de presse rédigé pour l'expédition Point Zéro 2026 (chapeau, contexte, fiche technique), mis en page dans un document Word (`expedition-point-zero-2026-contexte.docx`). Ton retravaillé sur retour (formulations superlatives "révolution"/"inédit" retirées), paragraphe ajouté sur la diversité des 5 méthodes d'observation croisées sur un même territoire/saison. Incorporation du contenu "Bilan de mi-expédition" (premiers prélèvements ADNe/filet Manta) démarrée, pas confirmée terminée dans la session.
- 2026-09-15 (suite) : Article de presse — bilan mi-expédition incorporé : paragraphe mégafaune remplacé par les observations au large (>30 milles, 2 nuits à la dérive) : dauphins bleu et blanc (groupes 5-30), 6 rorquals communs, ~40 globicéphales venus au bateau (18h-3h), 2 tortues caouannes de nuit, raies mobula (4 individus filmés au drone), poissons volants exocets. Paragraphe de contexte sur la mission retravaillé sur plusieurs itérations avec Melvin (retrait de l'affirmation erronée d'un "état de référence" existant, ajout puis retrait/réajout d'une transition, formulation finale : dresser un état des lieux de la santé écologique du milieu marin autour de l'île, étape essentielle dans la structuration d'un réseau de surveillance à l'échelle régionale).
- 2026-09-16 : Article de presse Point Zéro finalisé — doublons supprimés du Contexte (constat/protocoles/soutiens répétés), logique reséquencée (historique NAECO → itinéraire → STARECORSICA → constat écologique → protocoles → volet créatif). Bilan mi-expédition condensé (5 blocs → 3 paragraphes) puis rééquilibré sur retour client (trop condensé) pour un ton grand public (vulgarisation ADNe/filet Manta/caméras appâtées, sans jargon de rapport). Complété avec l'escale à Porto (ateliers scolaires d'Ota, visite du bateau, projection *Mare Nostrum*, expo photo).
- 2026-09-16 (suite) : Sur [[naeco-site]] — bloc carte interactive fusionné dans la bande dégradée entre Expédition 2026 et Partenaires. Détails dans la fiche projet.
- 2026-09-16 (suite) : Sur [[naeco-carte]] — régression `validateFix` corrigée (rejetait les fixes stationnaires légitimes au mouillage), déployé ; 157 points GPS parasites de Porto supprimés, 14 points supplémentaires (dérive à pied) identifiés en attente de suppression. Détails dans la fiche projet.
- 2026-09-16 (suite) : Sur [[naeco-site]] — logo partenaire STARESO récupéré (Drive), recadré, intégré (Cloudinary) et vérifié en live ; rien commité. Liste des 5 prochains partenaires à intégrer transmise par le client (Agence de l'Eau, Le Fonds Vert, FDVA, Fonds HLD, La MAIF Ajaccio). Détails dans la fiche projet.
- 2026-09-17 : Sur [[naeco-carte]] — migration des 43 images Drive vers Cloudinary lancée (risque de perte d'accès au Drive), 42/43 migrées, 1 lien cassé encore à trancher avant de patcher la carte. Détails dans la fiche projet.

## Liens
- Projets : [[naeco-site]], [[naeco-carte]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
