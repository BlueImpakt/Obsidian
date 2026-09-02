# Content Feed — LinkedIn

Matière brute extraite des daily notes. Lu par n8n toutes les 48h pour générer des drafts LinkedIn. Vidé automatiquement après génération.

---

## 2026-09-01

- Cas client [[naeco-site]] : nouvelle page « Expéditions » livrée pour l'association NAECO à partir d'un brief Notion — page complète pour l'expédition 2026 « Point Zéro » (Pelagos, science/art/transmission) + rétrospective des 4 expéditions précédentes (2022-2025). Angle possible : comment on transforme un doc de préparation d'expédition en récit web immersif pour une asso environnementale, sans casser la contrainte technique existante (contenu piloté par JSONbin).

## 2026-09-02

- Cas client [[esprit-docker]] : client signale "mes clients ne reçoivent pas le mail de suivi colis". Première hypothèse (spam, compte Sendcloud gratuit) infirmée quelques heures plus tard par une investigation plus poussée : le mail que le client avait reçu venait en fait directement de Mondial Relay, pas de Sendcloud, et les Analytics du compte révèlent que **zéro** email de suivi n'est parti en 30 jours (pas un souci de délivrabilité, un souci d'envoi). Solution de repli retenue : émettre soi-même le mail "expédié" via Brevo depuis le webhook Sendcloud, sur le même verrou anti-doublon que l'email de confirmation existant. Angle possible : "le bon diagnostic n'est pas toujours le premier qu'on trouve" — comment une hypothèse plausible (et qui collait aux symptômes) s'est révélée fausse une fois qu'on a eu la bonne donnée (compteur Analytics à 0), et pourquoi ne pas dépendre des emails d'un SaaS tiers quand on ne maîtrise ni ses logs ni sa configuration.
- Cas client [[naeco-site]] : brief de refonte reçu en React/Next.js/Tailwind/Framer Motion pour une asso qui pilote son contenu via un éditeur maison (JSONbin, Ctrl+Shift+E). Migrer aurait cassé le workflow d'édition de l'équipe pour un gain cosmétique. Décision : garder le HTML statique, ajouter les animations avec Motion (vanilla JS, même API que Framer Motion, sans React). Angle possible : "dire non à la stack demandée" — pourquoi le bon choix technique n'est pas toujours celui du brief, quand une association dépend de son autonomie d'édition au quotidien.
- Cas client [[naeco-site]] : demande d'un Hero 3D (voilier qui suit la route d'expédition au scroll) écartée du périmètre de la refonte en cours — pas parce que l'idée est mauvaise (~2 semaines de travail, jamais fait chez Blue Impakt, contredit une décision déjà prise de ne pas toucher au Hero), mais en gardant une porte ouverte : un spike jetable (test technique rapide, jetable) pour mesurer la faisabilité mobile avant tout engagement sur la modélisation 3D. Angle possible : "comment arbitrer une demande de fonctionnalité ambitieuse sans juste dire non" — spike de validation avant devis, gouvernance des visuels générés par IA posée en amont plutôt qu'après coup.
