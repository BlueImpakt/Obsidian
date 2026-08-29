---
tags: [dashboard]
---

# Dashboard Blue Impakt

> Vue vivante générée par Dataview/Tasks. Rien n'est écrit à la main ici — tout est recalculé à l'ouverture. Nécessite les plugins **Dataview** et **Tasks** (voir CLAUDE.md).

## Clients P1 actifs
```dataview
TABLE statut, secteur, localisation
FROM "01_clients"
WHERE contains(tags, "p1")
```

## Clients par statut
```dataview
TABLE statut
FROM "01_clients"
GROUP BY statut
```

## Projets en cours / bloqués
```dataview
TABLE statut, client
FROM "02_projects"
WHERE statut = "encours" OR statut = "bloqué"
```

## Patterns validés récents
```dataview
TABLE type, created
FROM "03_knowledge/patterns"
SORT created DESC
LIMIT 10
```

## Réunions récentes
```dataview
TABLE client, created
FROM "06_reunions"
SORT created DESC
LIMIT 10
```

## Toutes les actions ouvertes
```tasks
not done
path includes 01_clients OR path includes 02_projects OR path includes 00_inbox
```
