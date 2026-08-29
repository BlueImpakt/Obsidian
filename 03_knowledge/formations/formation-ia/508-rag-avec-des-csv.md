---
tags: [formation, millenium]
module: Formation IA
section: "Construire ses RAG"
source_transcript: "5.08 RAG avec des CSV.txt"
---

# 5.08 RAG avec des CSV

## Resume
- Introduction à un agent RAG spécialisé pour données numériques (CSV, Excel, datasets) plutôt que textuelles, un cas d'usage distinct nécessitant une approche adaptée.
- Explication de la difficulté et du risque d'erreur avec des données structurées, justifiant l'usage d'un RAG plus structuré spécifiquement adapté au traitement de données numériques.
- Présentation de Kaggle comme ressource pour trouver des datasets de test (exemple : faux CRM), une librairie utile pour construire des études de cas et exercices pratiques.
- Illustration humoristique de l'incohérence volontaire des données de test (revenus disproportionnés par rapport au nombre d'employés), un deuxième dataset scrapé étant également présenté.
- Objectif de rassembler plusieurs datasets (CSV) au sein d'un seul et même RAG pour éviter de refaire la structure d'ingestion à chaque nouveau fichier ajouté.
- Configuration d'un déclencheur Google Drive détectant les changements dans un dossier spécifique, la première brique du pipeline d'ingestion automatique de fichiers.
- Nécessité de configurer deux triggers distincts (File Created et File Updated) pour couvrir tous les cas d'ajout ou modification de fichiers dans le dossier surveillé.
- Introduction du routage par type de fichier (MIME Type) permettant de diriger chaque document reçu vers la branche de traitement appropriée selon sa nature.
- Explication du concept de MIME Type comme identifiant de la nature d'un fichier (analogie avec les fichiers MP3), utilisé pour déterminer le traitement à appliquer.
- Identification précise du MIME Type pour les fichiers Google Sheets (SpreadsheetML/Sheets) et Excel (application/vnd, format OpenXML), des identifiants techniques longs mais nécessaires.
- Confirmation des trois branches de routage établies (Sheets, CSV, Excel) avec astuce de pinner les données de test pour éviter de re-télécharger à chaque exécution du workflow.
- Bonne pratique de gestion des identifiants de fichiers via boucle (loop over items, item.json.id), avec mise en garde sur les résultats imprévisibles si mal configuré pour Google Sheets.
- Recommandation de préciser la feuille (sheet) concernée si le fichier Google Sheets contient plusieurs onglets, pour éviter des ambiguïtés lors de la modification.
- Configuration de la branche CSV : téléchargement préalable du fichier depuis Google Drive via son ID obtenu, une étape supplémentaire nécessaire par rapport aux Sheets.
- Configuration de l'option « all field except row » pour uploader les données brutes sans besoin du numéro de ligne, avec observation de la structure de sortie contenant un array de données.
- Explication de l'agrégation des trois branches de traitement (Sheets, CSV, Excel) en un flux unique, sachant qu'un item ne passe que par un seul canal à la fois.
- Illustration de l'intérêt du filtrage SQL en amont (ex : posts avec plus de 10 commentaires) pour éviter de renvoyer toutes les données à l'agent, améliorant sa réactivité.
- Utilisation de la fonction concatenate pour extraire et regrouper toutes les valeurs d'un champ de données en une seule valeur unique, une étape clé de la préparation des données.
- Configuration d'un nouveau nœud Merge (Combine, All Possible Combinations) pour associer les champs extraits (contenu, commentaire, engagement, like) entre eux.
- Explication de la restructuration de données au format texte, avant transition vers la création de deux tables dans Supabase pour organiser le stockage.
- Démonstration de configuration de table Supabase avec identifiant principal (primary) recommandé de conserver tel quel, puis ajout des champs issus de l'automatisation (titre du document).
- Explication du champ de typage (tabulaire vs mélangé/textuel) permettant de filtrer entre données à vectoriser et données structurées dans un RAG hybride.
- Récapitulatif des champs de la table principale : identifiant unique, date de création, titre, type de document, document encodé, headers (première ligne), et File ID Google Drive.
- Démonstration de liaison entre les deux tables via un identifiant de document parent (Parent File ID), établissant la relation entre la table des fichiers et celle des lignes.
- Introduction du concept de hashing (Generate Hash) dans N8n comme mécanisme pour identifier de manière fiable des séquences de données potentiellement très longues.
- Explication du principe du hashing : créer une empreinte unique et non réversible d'une donnée, permettant de comparer efficacement deux séquences sans jamais pouvoir les décoder en retour.
- Explication de l'utilité pratique du hash pour la comparaison de gros volumes : réduire 1000 posts publiés en une empreinte de 64 caractères facile à comparer pour détecter des changements.
- Démonstration de régénération et filtrage par hash (JSONHash) pour identifier les empreintes de documents déjà traités et détecter les modifications.
- Démonstration de création d'une nouvelle ligne dans Supabase (Create a Row, table Files) en configurant les colonnes File Title tout en laissant ID et Created At automatiques.
- Configuration du champ hash (empreinte de 64 caractères) dans la nouvelle ligne Supabase, en récupérant la valeur générée à l'étape crypto précédente.
- Présentation de la branche Edit pour la modification de données existantes, avec fusion des flux et ajout d'un Set Fields pour harmoniser les données entre les deux chemins.
- Précision technique sur la récupération correcte du hash généré à l'étape crypto (crypto.item.json.h) pour identifier la ligne correspondante lors d'une modification.
- Test confirmant qu'un document existant est correctement identifié et transmis, avec recommandation de pinner les données pour éviter de régénérer tout le processus à chaque test.
- Présentation de la logique conditionnelle de suppression : si le retour n'est pas vide (le document existe déjà), l'ancienne ligne est supprimée avant recréation, une logique de mise à jour propre.
- Configuration de récupération des éléments sous forme de tableau (array) pour pouvoir les faire passer correctement à l'étape suivante du workflow.
- Test en direct du traitement complet de 193 éléments sans limite, une étape de validation à grande échelle du pipeline construit, avec anticipation d'erreurs possibles.
- Confirmation de l'enregistrement réussi de toutes les données brutes liées au Parent File ID correspondant, complétant l'ingestion complète du dataset traité.
- Introduction à la structure de l'agent d'interrogation : un agent moteur gérant les demandes et un chat d'interaction, l'objectif étant d'interagir avec des fichiers CSV/Excel régulièrement mis à jour.
- Introduction pédagogique au langage SQL, comparé au JSON pour sa capacité à effectuer des requêtes précises sur des bases de données.
- Recommandation de ressources d'apprentissage SQL en ligne, proposant des exercices interactifs pour comprendre les différentes fonctions couramment utilisées.
- Démonstration d'utilisation de l'IA pour générer un exemple de requête SQL structurée (post, contenu, likes, commentaires), une méthode pratique d'apprentissage accéléré.
- Explication basique de la structure d'une requête SQL, permettant de retourner des valeurs précises d'une base de données selon des critères définis.
- Présentation de la structure en trois parties de l'outil d'interrogation : sélection du Supabase Tool (distinct du Vector Store) avec l'action Get Many Rows.
- Configuration d'un appel direct à la base de données Postgres déjà connectée précédemment, réutilisant la même méthode de connexion établie dans les vidéos antérieures.
- Récapitulatif détaillé du schéma de la table Files : ID, CreatedAt, FileTitle, Type (tabulaire ou vecteur), Hash (empreinte), headers (schéma des colonnes CSV).
- Explication de la relation entre la table Files et File Rows (chaque ligne de CSV liée par Parent File ID), une architecture relationnelle claire pour organiser les données.
- Rédaction d'un contexte exhaustif pour l'agent expliquant la structure des deux tables (Files et File Rows), un maximum d'information fournie pour guider précisément son comportement.
- Description du processus en étapes de l'agent : récupération des métadonnées, analyse de la demande (colonnes/filtres), création d'une requête SQL dynamique adaptée.
- Règle importante précisée dans le prompt de l'agent : les données sont stockées au format JSON dans la colonne content, une précision cruciale pour la construction correcte des requêtes.
- Instruction de syntaxe PostgreSQL spécifique pour requêtes JSON, avec règle systématique de filtrage par Parent File ID pour cibler le bon fichier et limiter les résultats retournés.
- Explication de la construction de la requête SQL exemple : sélection des colonnes pertinentes (nom, âge, prix) puis clause FROM indiquant la source des données.
- Règles de sécurité imposées à l'agent : autoriser uniquement les requêtes SELECT (lecture seule), éviter les requêtes sans limite sur les grandes tables, valider l'échappement des paramètres.
- Test réel de l'agent avec une requête complexe (10 meilleurs posts de Julien Song sur 2025), démontrant l'exécution complète du pipeline requête/récupération/réponse.
- Résultat concret retourné par l'agent : détails d'engagement d'un post spécifique (3383 engagements, 2074 likes, 273 commentaires, 221 partages) sur un sujet précis.
- Analyse de la requête SQL générée dans les logs : sélection du contenu et de la date, avec tri par engagement (order by) pour obtenir les posts les plus viraux.
- Observation que l'agent a dû effectuer plusieurs requêtes car la date du jour n'était pas transmise dans le contexte initial, un point d'amélioration identifié.
- Correction apportée : ajout de la date du jour dynamique (formule $now) dans le contexte du prompt de l'agent, pour éviter les requêtes redondantes.
- Conclusion du build RAG CSV avec test final réussi retournant les trois meilleurs posts du mois en cours, validant l'ensemble du pipeline construit.

## Concepts cles
- introduction à l'agent RAG spécialisé pour données numériques (CSV, Excel)
- justification d'un RAG structuré adapté aux données numériques (limiter les erreurs)
- présentation de Kaggle comme source de datasets de test
- illustration de l'incohérence volontaire des données de test factices
- objectif de rassembler plusieurs datasets au sein d'un seul RAG (structure réutilisable)
- configuration du déclencheur Google Drive pour changements dans un dossier
- nécessité de deux triggers distincts (File Created et File Updated)
- introduction du routage par type de fichier (MIME Type) vers la branche adaptée
- explication du concept de MIME Type comme identifiant de nature de fichier
- identification précise des MIME Types pour Google Sheets et Excel
- confirmation des trois branches de routage et astuce de pin des données de test
- bonne pratique de gestion des identifiants via boucle pour Google Sheets
- recommandation de préciser la feuille concernée en cas de multiples onglets Google Sheets
- configuration de la branche CSV avec téléchargement préalable du fichier via ID
- configuration pour uploader les données brutes sans numéro de ligne
- explication de l'agrégation des trois branches de traitement en un flux unique
- illustration de l'intérêt du filtrage SQL en amont pour la réactivité de l'agent
- utilisation de la fonction concatenate pour regrouper les valeurs d'un champ
- configuration d'un nœud Merge pour associer les champs extraits (contenu, engagement)
- explication de la restructuration de données et transition vers Supabase (deux tables)
- démonstration de configuration de table Supabase avec identifiant principal
- explication du champ de typage pour filtrer données tabulaires vs textuelles
- récapitulatif complet des champs de la table principale de métadonnées
- démonstration de liaison entre tables via identifiant de document parent
- introduction du concept de hashing pour identifier des données longues
- principe du hashing comme empreinte unique non réversible pour comparaison
- utilité pratique du hash pour comparer efficacement de gros volumes (64 caractères)
- démonstration de filtrage par hash pour détecter les modifications de documents
- démonstration de création de ligne Supabase avec configuration des colonnes
- configuration du champ hash récupéré depuis l'étape crypto
- présentation de la branche Edit avec fusion des flux via Set Fields
- précision technique sur la récupération correcte du hash pour identifier une ligne
- test de confirmation d'identification de document existant (recommandation de pin)
- logique conditionnelle de suppression pour mise à jour propre des documents existants
- configuration de récupération des éléments sous forme de tableau (array)
- test en direct du traitement à grande échelle (193 éléments sans limite)
- confirmation de l'enregistrement réussi de toutes les données liées au Parent File ID
- introduction à la structure de l'agent d'interrogation de fichiers mis à jour
- introduction pédagogique au langage SQL (comparaison avec le JSON)
- recommandation de ressources d'apprentissage SQL interactives en ligne
- démonstration d'utilisation de l'IA pour générer un exemple de requête SQL
- explication basique de la structure d'une requête SQL de retour de valeurs
- présentation de la structure de l'outil Supabase Tool (distinct du Vector Store)
- configuration d'un appel direct à la base Postgres déjà connectée
- récapitulatif détaillé du schéma complet de la table Files
- explication de la relation entre Files et File Rows via Parent File ID
- rédaction d'un contexte exhaustif de structure de données pour guider l'agent
- description du processus en étapes de l'agent (analyse, requête SQL dynamique)
- règle cruciale : données stockées en JSON dans la colonne content
- instruction de syntaxe PostgreSQL pour JSON et filtrage systématique par Parent File ID
- explication de la construction d'une requête SQL exemple (SELECT, FROM)
- règles de sécurité de l'agent : SELECT uniquement, limites, échappement des paramètres
- test réel de l'agent sur une requête complexe filtrée par personne et année
- résultat concret d'engagement retourné par l'agent (chiffres détaillés)
- analyse de la requête SQL générée dans les logs (tri par engagement)
- observation : requêtes multiples dues à l'absence de la date du jour en contexte
- correction : ajout de la date du jour dynamique ($now) dans le contexte
- conclusion du build RAG CSV avec test final validant le pipeline complet

## Outils mentionnes
- n8n
- Kaggle
- Google Drive
- Google Sheets
- Supabase
- Postgres

## Tips techniques
- Utiliser un RAG spécifiquement structuré pour les données numériques, un traitement classique étant risqué en termes d'erreurs sur ce type de données
- Utiliser Kaggle pour trouver des datasets de test réalistes lorsqu'on a besoin de données factices pour des démonstrations ou exercices
- Concevoir un RAG capable d'ingérer automatiquement plusieurs datasets similaires sans devoir refaire la structure à chaque nouveau fichier
- Configurer systématiquement deux triggers (création ET mise à jour) pour un dossier Google Drive surveillé, afin de ne manquer aucun cas
- Pinner (figer) les données de test dans N8n pour éviter de re-télécharger inutilement les mêmes fichiers à chaque itération de test
- Utiliser une boucle explicite sur les identifiants de fichiers plutôt qu'une configuration par défaut, pour éviter des résultats imprévisibles avec Google Sheets
- Toujours préciser la feuille (sheet) spécifique concernée quand un fichier Google Sheets contient plusieurs onglets, pour éviter toute ambiguïté
- Filtrer les données via requête SQL en amont plutôt que de renvoyer l'intégralité des données à l'agent, pour améliorer sa réactivité
- Toujours conserver l'identifiant principal (primary) par défaut d'une table Supabase, ne pas le modifier sans raison spécifique
- Vérifier précisément le chemin de récupération du hash généré (crypto.item.json.h) pour identifier correctement la ligne à modifier
- Pinner les données à chaque étape de test complexe pour éviter de régénérer inutilement tout le processus en amont
- Utiliser des ressources d'apprentissage SQL interactives en ligne pour se familiariser avec les fonctions courantes avant de les appliquer dans un agent
- Demander à une IA de générer des exemples de requêtes SQL structurées pour accélérer l'apprentissage pratique du langage
- Fournir un contexte exhaustif et précis de la structure des tables de données à l'agent, pour maximiser la fiabilité de ses requêtes
- Toujours préciser explicitement dans le prompt de l'agent le format de stockage des données (JSON dans une colonne) pour des requêtes correctes
- Toujours filtrer systématiquement par Parent File ID dans les requêtes pour cibler le bon fichier et éviter de charger des données non pertinentes
- Restreindre systématiquement un agent SQL aux requêtes SELECT en lecture seule, avec limites obligatoires sur les grandes tables et validation d'échappement
- Toujours inclure la date du jour dynamique ($now) dans le contexte d'un agent manipulant des données temporelles, pour éviter des requêtes redondantes

## Cas d'usage reels
- [[]]
