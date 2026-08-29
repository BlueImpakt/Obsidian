---
tags: [formation, millenium]
module: Formation IA
section: "Découvrir tous les Outils IA"
source_transcript: "0.7 Sora.txt"
---

# 0.7 Sora

## Resume
- Sommaire de la vidéo sur Sora : pourquoi ne pas utiliser Sora directement, utilisation d'un wrapper alternatif, découverte de X-Field, ses avantages, comparaison avec ChatGPT, et panorama des modèles disponibles dans X-Field.
- L'auteur explique pourquoi il déconseille d'utiliser Sora directement via son interface native, l'un des rares cas où il recommande de ne pas utiliser un outil IA brut, une position similaire à celle qu'il défend pour NanoBanana.
- Justification de cette recommandation : sans compétence artistique poussée, on obtient toujours de moins bons résultats en essayant de définir soi-même des styles, comparé aux styles préétablis créés par des artistes ayant collaboré directement avec ces marques/entreprises.
- Avantage d'utiliser un wrapper (interface intermédiaire) plutôt que l'outil directement : rester à jour sur les derniers modèles sans devoir réinventer son workflow à chaque fois, la vidéo étant le seul domaine où l'auteur recommande spécifiquement cette approche, faute de valeur ajoutée à utiliser l'outil natif directement.
- Présentation des Lens et mouvements de caméra pré-programmés disponibles dans l'outil, offrant un rendu plus cinématographique et vivant, particulièrement utile pour les débutants en réalisation photo/vidéo.
- Explication technique des mécanismes d'attention : ils permettent de calculer en permanence les relations entre les mots d'une phrase, déterminant quels mots ont le plus de probabilité d'avoir une relation significative et impactante entre eux.
- Retour historique : les premières architectures étaient destinées à la recherche interne, avant un déploiement progressif. L'auteur évoque que Google avait l'opportunité de sortir un produit équivalent à ChatGPT avant même ChatGPT, mais cette opportunité est restée non exploitée en interne.
- Présentation du deuxième pilier de la course à l'IA : les investissements massifs dans le compute, nécessaires pour effectuer les calculs extrêmement énergivores requis, ce qui implique des infrastructures dédiées considérables.
- Explication du RLHF (Reinforcement Learning with Human Feedback) : les utilisateurs donnaient un feedback explicite sur les réponses au début de ChatGPT (validation ou invalidation de la qualité de la réponse), un mécanisme aujourd'hui moins visible mais toujours présent.
- Récit du départ de Dario Amodei d'OpenAI, ne se retrouvant pas dans la vision stratégique de l'entreprise, menant à la création de sa propre société, Anthropic, un moment clé de l'histoire du secteur.
- L'auteur situe une rupture majeure à partir de 2017, marquée par l'injection massive de capitaux dans le secteur. Il introduit une innovation clé venue, une fois de plus, de la Navy américaine, comme point de départ historique du récit technique.
- Illustration du fonctionnement des premiers réseaux de neurones artificiels via un exemple simple de classification d'image (chat ou chien), puis introduction des réseaux de neurones récurrents, capables en plus d'analyser de créer une boucle de traitement.
- Analogie avec les débuts très limités de ChatGPT (avant même son nom actuel) : une capacité à formuler certaines phrases correctement, mais un effondrement de cohérence dès que trop d'informations étaient fournies, un syndrome similaire observé dans les premiers réseaux récurrents.
- Introduction du GRU (2014), architecture créée par Joshua Bengio, un des pères fondateurs de l'IA, conçue pour simplifier l'architecture LSTM jugée trop complexe, tout en conservant l'essentiel de sa capacité de gestion de la mémoire.
- Explication de la rupture conceptuelle apportée par l'architecture Transformer : abandonner la lecture séquentielle mot par mot au profit d'un traitement simultané de toute l'information, une idée fondatrice qui a tout changé.
- Récit de la prudence initiale de Google face au risque de dérapages (contenus incorrects, usages illégaux potentiels), qui les a conduits à s'abstenir de sortir publiquement leur technologie, contrairement à d'autres acteurs plus audacieux.
- Anecdote caricaturée sur le décalage de perception entre équipes internes enthousiastes annonçant une révolution majeure et une direction Google plus sceptique, poussant certains acteurs frustrés à partir créer leur propre structure indépendante.
- Présentation du papier fondateur « Attention is All You Need », publié par l'équipe de recherche Google, qui remplace toutes les approches précédentes en permettant une parallélisation massive du traitement, dépassant les limites des réseaux de neurones antérieurs.
- Explication de la stratégie initiale d'OpenAI : développer l'IA générative via un pré-entraînement massif ingérant énormément de données disponibles sur Internet, suivi d'une phase de fine-tuning pour améliorer progressivement la qualité des réponses.
- L'auteur qualifie les tout premiers modèles de « nuls de chez nuls » comparé aux standards actuels, bien qu'extraordinaires pour l'époque. C'est la démocratisation grand public de ChatGPT en décembre 2022 qui a véritablement transformé OpenAI en l'entreprise qu'elle est aujourd'hui.
- Anecdote sur la frustration persistante d'Elon Musk, ayant investi financièrement dans OpenAI avec une vision open source et philanthropique, se sentant floué par le virage commercial pris par Sam Altman, radicalement opposé à sa vision initiale.
- Détail des trois étapes fondamentales ayant permis de rendre GPT-3.5 accessible au grand public : Supervised Fine Tuning, Reward Model Training, et Optimisation PPO, chacune contribuant à maximiser la qualité perçue des réponses par les utilisateurs.
- Retour sur Google comme architecte technique fondamental (origine de l'architecture Transformer), suivi de la sortie de BERT en 2018, décrit comme une première ébauche de ce que pourrait devenir un LLM moderne, avant l'arrivée de LaMDA et PaLM.
- L'auteur souligne que Google maîtrise l'intégralité de sa chaîne de valeur (puces, infrastructure, modèles) et n'a donc pas besoin de dépendre d'un fournisseur externe, contrairement à NVIDIA et OpenAI qui sont mutuellement dépendants l'un de l'autre pour la puissance de calcul.
- Rappel du lien entre l'architecture Transformer et le Deep Learning, et présentation de l'évolution continue des GPU vers toujours plus de puissance, plaçant les architectures développées à la pointe technologique mondiale.
- Constat d'une pénurie permanente de GPU liée à une demande extrêmement forte de la part de tous les acteurs voulant s'équiper de la meilleure technologie. Introduction de Meta comme acteur clé ayant misé sur l'IA très tôt.
- Constat que Meta, malgré une recherche IA et des talents de très haut niveau, a pris du retard commercial. Face à cet enjeu majeur, Mark Zuckerberg a lancé une chasse aux talents à coups de millions pour rattraper ce retard.
- L'auteur exprime sa préférence personnelle pour Claude, jugé offrir la meilleure expérience globale sur les LLM à ce jour (tout en reconnaissant que ce jugement peut évoluer rapidement). Introduction du Constitutional AI d'Anthropic, une approche différente du RLHF classique basé sur le feedback humain.
- Chronologie de l'évolution de Claude : lancement en mars 2023 (quatre mois après ChatGPT), avancée notable en juillet 2023, puis un véritable coup d'accélérateur à partir de mars 2024.
- Explication de la course aux investissements motivée par la peur de rater le train technologique, Google ressentant également un léger retard et investissant massivement en réponse. Introduction d'un autre acteur, actuellement dépendant d'OpenAI mais en cours de déploiement autonome progressif.
- Présentation de deux découvertes majeures ayant suivi l'architecture Transformer, avec des avancées continues chez OpenAI et chez DeepMind (Google), illustrant que l'innovation technologique ne s'arrête jamais et s'auto-alimente.
- Description d'une boucle d'accélération exponentielle : chaque avancée de recherche déclenche davantage d'investissements, qui à leur tour permettent de nouvelles avancées encore plus rapides, créant une dynamique de croissance auto-entretenue dans le secteur.
- Retour aux fondamentaux de l'IA : historiquement centrée sur la sémantique (traitement du langage), même si les premières applications concernaient plutôt les images. L'auteur souligne que pour atteindre l'ambition de l'IA générale, cette dimension sémantique reste essentielle.
- Présentation de Hugging Face, décrit comme le « GitHub de l'IA » : une plateforme communautaire mondiale hébergeant plus d'un million de modèles, jouant un rôle central de partage et de collaboration dans l'écosystème IA.
- Présentation de Cohere, acteur important spécialisé notamment dans les automatisations et agents (utilisé dans N8N) pour effectuer du re-ranking sur les systèmes RAG, une technique visant à améliorer la pertinence des résultats de recherche.
- Introduction de l'enjeu de la qualité des données : certains experts anticipent un plateau qualitatif à mesure que le contenu généré par IA se multiplie, dégradant potentiellement la qualité générale du contenu disponible en ligne (phénomène déjà observable).
- Conclusion sur l'incertitude inhérente à l'évolution future de l'IA : même les meilleurs chercheurs ne peuvent tout prédire avec certitude concernant le déploiement et la trajectoire du secteur, l'auteur restant néanmoins optimiste sur l'époque exceptionnelle que nous vivons.

## Concepts cles
- plan de présentation sur Sora et alternatives (wrapper, X-Field)
- recommandation de ne pas utiliser Sora directement (cas rare)
- styles préétablis par des artistes vs tentative personnelle de style
- avantage d'un wrapper pour rester à jour sans réinventer son workflow
- Lens et mouvements de caméra pré-programmés
- accessibilité pour débutants en réalisation
- mécanismes d'attention et calcul des relations entre mots
- opportunité manquée par Google de sortir un ChatGPT avant l'heure
- investissements massifs dans le compute comme pilier de la course IA
- RLHF illustré par les débuts de ChatGPT (feedback explicite utilisateur)
- départ de Dario Amodei d'OpenAI et création d'Anthropic
- rupture financière de 2017 dans le secteur IA
- origine militaire (Navy) d'une innovation clé
- réseaux de neurones artificiels (classification simple)
- réseaux de neurones récurrents (avec boucle)
- analogie avec les limites des tout premiers modèles conversationnels
- GRU (2014) par Joshua Bengio
- simplification du LSTM tout en gardant sa capacité mémoire
- rupture conceptuelle du Transformer (traitement simultané vs séquentiel)
- prudence de Google face aux risques (abstention de sortie publique)
- décalage de perception interne chez Google (caricature)
- papier fondateur 'Attention is All You Need' (Google Research)
- stratégie OpenAI : pré-entraînement massif puis fine-tuning
- démocratisation de ChatGPT en décembre 2022 comme tournant majeur
- frustration d'Elon Musk face au virage commercial d'OpenAI
- trois étapes clés de GPT-3.5 (Supervised Fine Tuning, Reward Model, PPO)
- Google comme architecte fondamental (Transformer, BERT 2018, LaMDA, PaLM)
- maîtrise complète de la chaîne de valeur par Google
- interdépendance NVIDIA/OpenAI
- évolution continue de la puissance des GPU
- pénurie permanente de GPU
- Meta comme acteur précoce sur l'IA
- retard commercial de Meta malgré ses talents de recherche
- chasse aux talents massive orchestrée par Zuckerberg
- préférence personnelle pour Claude
- Constitutional AI comme alternative au RLHF classique
- chronologie de Claude (mars 2023 → juillet 2023 → mars 2024)
- investissements massifs motivés par la peur de rater le virage IA
- avancées continues post-Transformer (OpenAI, DeepMind)
- boucle d'accélération exponentielle recherche/investissement
- fondements sémantiques historiques de l'IA
- Hugging Face comme 'GitHub de l'IA' (plus d'un million de modèles hébergés)
- Cohere spécialisé dans le re-ranking pour les systèmes RAG
- risque de dégradation de la qualité du contenu par saturation IA
- incertitude fondamentale sur l'avenir de l'IA malgré l'expertise

## Outils mentionnes
- Sora
- NanoBanana
- ChatGPT
- Google
- OpenAI
- Anthropic
- GPT-3.5
- BERT
- NVIDIA
- Meta
- Claude
- DeepMind
- Hugging Face
- GitHub
- Cohere
- n8n

## Tips techniques
- Utiliser un wrapper plutôt qu'un outil de génération vidéo natif pour rester à jour sans reconstruire son workflow à chaque nouveau modèle

## Cas d'usage reels
- [[]]
