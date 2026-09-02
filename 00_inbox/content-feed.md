# Content Feed — LinkedIn

Matière brute extraite des daily notes. Lu par n8n toutes les 48h pour générer des drafts LinkedIn. Vidé automatiquement après génération.

---

## 2026-09-01

- Cas client [[naeco-site]] : nouvelle page « Expéditions » livrée pour l'association NAECO à partir d'un brief Notion — page complète pour l'expédition 2026 « Point Zéro » (Pelagos, science/art/transmission) + rétrospective des 4 expéditions précédentes (2022-2025). Angle possible : comment on transforme un doc de préparation d'expédition en récit web immersif pour une asso environnementale, sans casser la contrainte technique existante (contenu piloté par JSONbin).

## 2026-09-02

- Cas client [[esprit-docker]] : client signale "mes clients ne reçoivent pas le mail de suivi colis". Le code était irréprochable — la vraie cause était une config Sendcloud à trois verrous en cascade (toggle compte, toggle intégration, couverture pays des templates) et au final : compte gratuit Sendcloud = expéditeur générique non personnalisable, mails avec réputation moyenne qui finissent en spam. Angle possible : "un bug côté client n'est pas toujours un bug de code" — méthode de diagnostic en cascade sur un SaaS tiers (Sendcloud) quand on ne maîtrise ni les logs ni les identifiants du panel.
