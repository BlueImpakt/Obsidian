---
tags: [knowledge]
---

# Troubleshooting

Bugs résolus et leur solution. Une section par bug, avec contexte + fix.

## Hook d'ingestion `/clear` ne se déclenchait jamais (Claude Code 2.1.199 / Windows)

**Contexte** : la chaîne `/clear` → agent headless `good-night` (ingestion continue du vault, voir `[[ajouter-lecon-au-rag-millenium]]` pour le pipeline voisin) semblait fonctionner (logs présents le 2026-08-29) mais plus rien après 22h40. Les 3 logs initiaux se sont révélés être des lancements **manuels** du script pour le tester, pas de vrais déclenchements automatiques — donc en réalité le hook n'avait jamais tourné tout seul.

**Root cause** (trouvée par test matriciel, 4 combinaisons event/matcher instrumentées en parallèle) : sur ce build (Claude Code 2.1.199, Windows), `/clear` déclenche bien `SessionStart` **et** `SessionEnd`, mais le `source`/`reason` transmis n'est **pas** la chaîne littérale `"clear"` — la doc officielle est fausse pour cette version. Résultat : tout hook avec `"matcher": "clear"` exact est mort-né, seuls les matchers en **alternation** (`startup|resume|clear|compact|fork`) firent. En plus, les hooks `SessionStart` reçoivent un **stdin vide** sur ce build — un script qui fait `INPUT="$(cat)"` puis filtre sur `source` en JSON échoue systématiquement, même si l'event se déclenche.

**Fix** :
1. `~/.claude/settings.json` : hook basculé de `SessionStart` vers **`SessionEnd`**, avec un matcher en alternation `"clear|logout|prompt_input_exit|other"` (jamais `"clear"` seul).
2. `~/.claude/skills/good-night/ingest_on_clear.sh` : suppression du bloc lecture stdin + garde applicatif sur `source` (redondant avec le matcher `settings.json`, et mortel quand stdin est vide) — le script se fie désormais uniquement au matcher.

**Comment vérifier que ça tourne** : `~/.claude/skills/good-night/state/logs/hook-trace.log` doit contenir une ligne `FIRED` puis `LAUNCHED` à chaque `/clear`.

**À retenir** : ne jamais faire confiance à la doc Claude Code sur la valeur exacte de `source`/`reason` pour un event donné sans l'avoir vérifiée par une sonde catch-all sur ce build précis — instrumenter (log inconditionnel en tête de script + matcher large) avant de committer un matcher strict.

### Suite : boucle d'emballement une fois le hook actif

**Symptôme** : hook enfin fonctionnel → ~33 agents `claude -p` déclenchés en 3 min, en accélération.

**Root cause** : deux effets cumulés. (1) `SessionEnd` fire **~2× par `/clear`** sur ce build. (2) surtout : l'agent d'ingestion lance lui-même `claude -p`, dont la fin re-déclenche `SessionEnd` → nouvel agent → récursion. Les agents se reconnaissent comme « méta » et n'écrivent rien dans le vault (donc pas de corruption), mais le *spawn* continue.

**Fix** — deux gardes en tête de `ingest_on_clear.sh` :
1. **Anti-récursion** : le lancement fait `nohup env GOODNIGHT_INGEST=1 bash -c "... claude -p ..."`. Le hook sort immédiatement si `$GOODNIGHT_INGEST = 1` (le marqueur est bien hérité par le hook `SessionEnd` de la session headless — vérifié).
2. **Rate-limit** : sentinelle `state/.last-ingest` (`touch` avant lancement) ; le hook sort si elle a moins de 180 s. Absorbe le double-fire et plafonne à une ingestion / 3 min.

**Contrepartie assumée** : un vrai `/clear` avec du travail neuf dans les 180 s suivant une ingestion est différé — mais le `/clear` qualifiant suivant ré-scanne **toutes** les sessions non ingérées (rien n'est perdu), et `/good-night` balaie le soir.

**Vérif OK** = trace avec **1 seul** `LAUNCHED` puis des `SKIP (... < 180s)` / `SKIP (session issue de l ingestion)`, sans cascade.

## [[naeco-carte]] — tracés d'expédition qui reviennent à leur position initiale en cours d'édition

**Symptôme** : en mode éditeur, un tracé déplacé revient parfois tout seul à sa position d'avant, sans intervention.

**Root cause** : race condition au chargement de la page. Le `fetch` JSONbin `/latest` (asynchrone, 2-10 s de latence typique sur l'offre gratuite) répond parfois **après** que l'utilisateur soit entré en mode édition et ait déjà modifié un tracé. Le `.then()` du fetch remplaçait alors `expeditions` **sans aucune condition**, écrasant la modif en cours à l'écran et dans le localStorage — indépendamment de toute action de l'utilisateur.

**Fix** : flag `localDirty` passé à `true` dans l'intercepteur d'écriture locale (`ls_set`, `index.html:545-547`) ; garde ajoutée dans le `.then()` du chargement distant (`index.html:2620-2627`) qui ignore la réponse JSONbin si `localDirty` ou mode édition actif. Une fois qu'une modif locale a eu lieu, le chargement distant est volontairement sauté pour le reste de la session — recharger la page pour repartir de l'état JSONbin le plus récent.

**À retenir** : tout site avec le pattern [[jsonbin-source-de-verite]] (fetch distant au chargement + édition en direct possible immédiatement) doit gérer explicitement le cas où le fetch répond en retard sur une action utilisateur déjà en cours — sinon la version distante écrase silencieusement la version locale.

## [[naeco-site]] — vidéos Cloudinary tronquées à quelques secondes via URL de transformation à la volée

**Symptôme** : un film de 23 min uploadé sur Cloudinary était livré à 4,5 secondes via une URL de transformation à la volée ; des vidéos d'ambiance de 8-12s ressortaient à moins d'1 seconde.

**Root cause** : les URLs Cloudinary avec transformation à la volée (`f_auto,q_auto,w_...`) tronquent la durée de la vidéo livrée sur ce compte — comportement pas documenté nulle part côté projet, découvert en comparant la durée réelle du fichier source à la durée jouée en prod.

**Fix** : ne plus utiliser de transformation à la volée pour les vidéos. Pré-encoder localement (ffmpeg) 2 résolutions (desktop/mobile), uploader les fichiers déjà à la bonne taille/bitrate tels quels sur Cloudinary, et les référencer sans paramètre de transformation dans l'URL.

**À retenir** : sur Cloudinary, les transformations à la volée sont fiables pour les images mais pas garanties pour la durée d'une vidéo — pour tout fond vidéo responsive (voir aussi le pattern voile-vers-marine plus bas), pré-encoder et uploader les variantes desktop/mobile directement plutôt que de compter sur `w_`/`q_auto` à la livraison.

## [[naeco-site]] — bande de vidéo brute visible entre deux sections à fond vidéo

**Symptôme** : sur les sections courtes (à peine plus hautes qu'un écran — Mission, Constat, Piliers), une fine bande de vidéo non teintée apparaissait à la jonction avec la section suivante.

**Root cause** : le calque vidéo était en `position: sticky`, ce qui le garde collé à l'écran même une fois la fin réelle (courte) de la section dépassée au scroll, alors que le voile de couleur qui doit le recouvrir (« voile-vers-marine ») s'arrête pile à la fin de la section — désalignement entre les deux bords.

**Fix** : sur les sections dont la hauteur ne dépasse pas beaucoup un écran (Mission, Constat, Piliers), calque vidéo repassé en `position: absolute` calé exactement sur le voile. `sticky` réservé aux sections nettement plus hautes qu'un écran (ex. Expédition, gonflée par le scroll horizontal pinné du Carnet de bord), où le calque doit rester visible tout le temps du défilement interne.

**À retenir** : un fond vidéo `sticky` + un voile de recouvrement séparé doivent partager exactement le même système de positionnement/bornage — sinon toute section dont la hauteur réelle est proche de 100vh peut laisser dépasser le calque `sticky` après la fin du voile.

## [[naeco-site]] — `overflow: hidden` empêche un enfant `position: sticky` de s'accrocher

**Symptôme** : un calque vidéo en `position: sticky` à l'intérieur d'une section ne se figeait jamais au scroll — il défilait normalement, juste rogné aux bords de son conteneur.

**Root cause** : `overflow: hidden` sur le conteneur parent en fait un **conteneur de défilement** (scroll container) au sens CSS. `position: sticky` se cale par rapport à l'ancêtre défilant le plus proche — or ce conteneur-là ne défile jamais lui-même (il grandit avec la page), donc l'enfant sticky ne s'accroche à rien.

**Fix** : remplacer `overflow: hidden` par `overflow: clip` sur le conteneur. `clip` découpe le débordement visuel exactement comme `hidden`, mais ne crée **pas** de conteneur de défilement — le `position: sticky` de l'enfant redevient fonctionnel tout en restant borné à la boîte du conteneur (effet de bord utile : quand la section sort de l'écran, le sticky colle le bas du média au bas de la section, donc plus de "trou" en fin de section et plus de débordement possible sur la section suivante).

**À retenir** : chaque fois qu'un `position: sticky` enfant ne s'accroche pas alors que le CSS a l'air correct, vérifier si un ancêtre a `overflow: hidden`/`auto`/`scroll` — et préférer `overflow: clip` dès qu'on veut à la fois clipper *et* garder un sticky interne fonctionnel.

## [[naeco-carte]] — flash visuel intermittent (légende puis carte) causé par une animation CSS morte forçant un repaint GPU continu

**Symptôme** : un flash intermittent et non reproductible à volonté — d'abord vu sur la légende (bloc collapsé une frame sur ~5), puis, après un premier fix partiel, sur la carte elle-même (bande de tuiles pâles, sans le fill/les traces attendus, ~23% des frames).

**Root cause** : une keyframe `dash-flow` animait `stroke-dashoffset` en continu sur un élément qui n'était **pas** un tracé SVG (une `<div>` de légende dessinée via `background-image`) — `stroke-dashoffset` n'a aucun effet sur une `<div>` mais **n'a pas de fast-path compositeur** : Chromium doit re-peindre et re-rastériser **toute la couche** à chaque frame, en continu, même si le rendu visuel ne change jamais. Les tuiles/calques qui ratent la deadline de composition sont présentés à leurs bornes périmées (état précédent, ex. panneau "vide" ou tuile sans son fill semi-transparent) → flash. Sur la carte, le même piège touchait un vrai tracé SVG (`.exp-dash`) qui partageait son unique `<svg>` avec un gros polygone (fill semi-transparent) — l'animation du tracé forçait donc aussi le re-rasterisage permanent du polygone voisin, alors qu'ils n'ont aucun lien logique.

**Fix** : (1) supprimer les animations mortes qui n'ont plus d'effet sur l'élément qu'elles ciblent (identifiables via `getKeyframes()` dans les devtools — si les props animées ne s'appliquent pas au type d'élément, l'animation ne sert à rien mais coûte quand même) ; (2) pour l'animation réellement utile (le tracé pointillé), passer l'`easing` de `linear` à `steps(8)` — le rendu reste fluide à l'œil mais le nombre de repaints/s chute drastiquement (~60/s → ~5,7/s dans ce cas), suffisant pour ne plus rater les deadlines de composition.

**Méthode de diagnostic qui a marché** : mesurer la coupe/le défaut sur plusieurs frames d'une vidéo (position en x/y constante ou variable ?) pour distinguer un vrai bug de layout (bordures/coins qui bougent) d'un artefact de composition GPU (coupe nette, sans bordure, toujours au même endroit) — puis chercher ce qui force un repaint permanent au repos plutôt que ce qui se déclenche une fois.

**À retenir** : `stroke-dashoffset`, `filter`, `box-shadow` animés et quelques autres propriétés n'ont pas de fast-path compositeur — animées en `linear` et en continu, elles peuvent forcer un re-rasterisage permanent de toute la couche qui les contient, y compris des éléments visuellement indépendants qui partagent la même couche (ex. plusieurs formes dans un seul `<svg>`). Une animation qui semble inoffensive (elle ne fait "rien" à l'œil, ou anime un élément mineur) peut donc dégrader silencieusement le rendu d'éléments voisins sans lien apparent.

## [[naeco-carte]] — mot de passe éditeur et clé API en clair dans un fichier HTML statique côté client

**Contexte** : architecture "tout côté client, pas de backend" (HTML unique + JSONbin comme base de données) — le mot de passe qui protège le mode éditeur et la clé JSONbin (lecture **et** écriture complètes sur les données de production) sont tous deux écrits en clair dans le code source, visibles via "Afficher le code source" sans même avoir besoin des devtools.

**Risque** : le mot de passe éditeur ne protège que l'UI — n'importe qui peut soit le lire et l'utiliser normalement, soit l'ignorer complètement et appeler l'API JSONbin directement avec la clé trouvée dans le code, en contournant le site entier.

**Fix retenu (pas encore déployé)** : séparer la clé de **lecture** (restreinte en lecture seule côté JSONbin, sans danger si elle fuite) de la clé d'**écriture** (déplacée côté serveur, dans un petit proxy Cloudflare Worker qui vérifie une autorisation avant d'écrire). Le site public ne charge plus que la clé lecture-seule ; le bouton "Enregistrer" de l'éditeur appelle le Worker au lieu de JSONbin directement. Aucun changement pour l'utilisateur (même mot de passe, même UI).

**À retenir** : pour tout site "HTML statique + BaaS" (JSONbin, Firebase, Supabase avec RLS mal configuré, etc.) sans étape de build/serveur, vérifier systématiquement si la clé embarquée dans le code source a des droits d'écriture — c'est un pattern qui revient dès qu'un site no-backend a besoin d'un mode édition en ligne, voir aussi [[jsonbin-source-de-verite]].

## [[naeco-site]] — filet de lumière d'1px au raccord de deux dégradés CSS voisins

**Symptôme** : une fine ligne claire persistait à la jonction entre deux sections censées se raccorder sans couture, même après avoir renforcé le voile d'assombrissement de la première section.

**Root cause** : ce n'était pas un problème d'opacité de voile, mais un problème de **rastérisation** : les deux sections utilisaient chacune un dégradé CSS qui "arrive"/"repart" de la même couleur pile à la frontière. À un DPR non-entier (ex. 1,5), le bord de chaque calque est arrondi indépendamment au pixel physique le plus proche — les deux arrondis ne tombent pas exactement au même endroit, laissant un filet d'1px non couvert par aucun des deux dégradés.

**Fix** : ne pas compter sur deux dégradés qui se rejoignent pile à la frontière. Poser un aplat de couleur opaque en `::before`/`::after` sur l'une des deux sections, qui **déborde volontairement de quelques px** (2-3px) par-dessus la frontière avant de fondre dans le dégradé — un seul calque continu recouvre alors le bord des deux rendus, au lieu de deux bords indépendants qui doivent coïncider au pixel près.

**À retenir** : à la jonction de deux dégradés voisins, ne jamais faire confiance à une coïncidence de couleur pile sur la ligne de partage — un pattern d'aplat qui déborde légèrement (déjà utilisé ailleurs sur ce site pour les jonctions vidéo, voir plus haut) est plus robuste qu'un alignement pixel-perfect entre deux calques rastérisés séparément.
