---
tags: [formation, millenium]
module: Formation IA
section: "Agents Vocaux"
source_transcript: "10.02 Créer son 1er Agent IA vocal.txt"
---

# 10.02 Créer son 1er Agent IA vocal

## Resume
- Introduction pratique à la création d'un premier agent vocal via une plateforme modulaire, avec plan annonçant le choix de plateforme, comparaison de solutions, création de compte et de l'agent, puis personnalisation.
- Présentation de SynthFlow comme solution no-code adaptée à un démarrage rapide, avec limite inhérente aux plateformes no-code : les intégrations natives fonctionnent bien mais peuvent manquer de flexibilité pour des besoins spécifiques.
- Présentation de Retell AI comme bon compromis entre simplicité (dashboard intuitif) et puissance (API robuste), permettant une personnalisation profonde tout en restant accessible pour débuter.
- Démonstration de la création de compte et navigation initiale sur la plateforme : choix entre créer un agent chat ou vocal, avec possibilité d'importer depuis des fichiers existants.
- Recommandation de démarrer avec un Single Agent Prompt pour un cas simple (agent de réception), avec accès à des templates de référence pour s'inspirer avant de personnaliser.
- Présentation du premier choix de personnalisation majeur : le modèle LLM sous-jacent, qui détermine directement l'intelligence de l'agent vocal, un paramètre modulaire central.
- Recommandation de dimensionner le modèle selon la complexité de l'agent : GPT-4.1 peut être surdimensionné pour un agent simple, GPT-4.1 mini ou le fast tier étant recommandés pour réduire la latence de réponse.
- Présentation de l'option Voice Clone : possibilité de cloner une voix, avec avertissement légal important sur la nécessité d'obtenir les droits/permissions de la personne dont la voix est utilisée.
- Rappel de l'importance du module cerveau (modèle LLM) affectant à la fois l'intelligence et la vitesse de réponse de l'agent, le délai étant présenté comme l'un des éléments les plus critiques.
- Constat que les voix natives de la plateforme n'offrent que des accents américains, anglais ou mexicains, nécessitant de passer par une voix clonée pour obtenir un accent français adapté.
- Présentation des différents fournisseurs de voix disponibles (Minimax, Fish Audio, Eleven Labs, Cartesia, OpenAI), avec recommandation personnelle d'Eleven Labs, considéré comme leader de la génération vocale.
- Configuration pratique en français avec accent parisien, avec recommandation importante de choisir une voix conversationnelle plutôt que narrative pour un rendu plus naturel en dialogue.
- Finalisation du choix de voix (« Mylène ») avec présentation des options de modèle Eleven Labs disponibles selon le fournisseur, certaines version « turbo » anglophones étant plus coûteuses.
- Observation chiffrée importante : le simple choix du français augmente le délai de réponse d'environ 200 millisecondes, car cette langue est moins bien entraînée que l'anglais dans les modèles de transcription/TTS.
- Test pratique final de l'agent créé (exemple « Clinique Martin ») : validation d'un agent fonctionnel en français avec réponse rapide, tout en recommandant de surveiller le coût pour rester dans le budget.
- Présentation des variables dynamiques disponibles : variables de test créables par l'utilisateur et variables par défaut (état de l'agent pour les configurations multi-états, heure actuelle, etc.).
- Présentation des deux méthodes d'ajout de numéro de téléphone, avec précision importante : Retell ne fournit nativement que des numéros canadiens ou américains, pas de numéros français directs.
- Démonstration d'achat de numéro via « Buy a Number » : les numéros américains sont peu coûteux et généralement bien équipés en services, une option à considérer selon le besoin.
- Explication de la réglementation spécifique pour obtenir un numéro français : nécessité de fournir un ensemble de documents réglementaires approuvés, contrairement aux numéros américains moins régulés.
- Précision sur la déclaration d'usage du numéro dans le cas d'un usage revendeur : nécessité d'informer les clients finaux qu'ils doivent fournir des informations sur leur entreprise pour que le système fonctionne.
- Remplissage du formulaire réglementaire : informations d'entreprise (ou personne seule), immatriculation SIRET, et site web éventuel, des données nécessaires pour valider la demande de numéro français.
- Délai d'attente variable pour obtenir le numéro (3 jours à une semaine selon les cas), puis nécessité de le configurer dans Retell via connexion SIP Trunking une fois acquis.
- Configuration des options essentielles de sécurité SIP : Secure Trunking (connexion chiffrée), Call Transfer, options PSTN et Symmetric RTP, avant de passer à la configuration de terminaison.
- Configuration du contrôle d'IP en copiant-collant les paramètres fournis par Retell, une étape optionnelle selon l'usage (test ou production), avant de finaliser via Origination.
- Liaison finale du numéro configuré avec Retell via le Termination URI précédemment défini, avec avertissement pratique : bien vérifier l'absence d'espace parasite dans la valeur copiée.
- Finalisation de l'assignation de l'agent (Sophie) au numéro de téléphone configuré, avec choix de la version d'agent et restriction géographique des appels acceptés (France uniquement dans cet exemple).

## Concepts cles
- introduction pratique à la création d'un premier agent vocal
- SynthFlow pour démarrage rapide no-code (avec limites de flexibilité)
- Retell AI comme compromis simplicité/puissance (dashboard + API)
- navigation initiale et choix agent chat vs vocal
- recommandation Single Agent Prompt pour un cas simple
- choix du modèle LLM comme premier paramètre de personnalisation
- dimensionnement du modèle selon complexité (4.1 mini pour réduire la latence)
- option Voice Clone avec avertissement légal sur les droits de voix
- délai de réponse comme élément critique de l'agent vocal
- limite des voix natives (accents anglophones uniquement) nécessitant clonage
- comparaison des fournisseurs de voix (recommandation Eleven Labs)
- configuration en français avec accent parisien et voix conversationnelle
- finalisation du choix de voix et variantes de modèle Eleven Labs
- surcoût de latence de ~200ms lié au choix du français (moins entraîné)
- test final de validation de l'agent (fonctionnalité et budget)
- variables dynamiques (test et par défaut)
- limite : Retell fournit uniquement des numéros canadiens/américains nativement
- achat de numéro américain (peu coûteux, bien équipé)
- réglementation stricte pour numéro français (documents requis)
- déclaration d'usage revendeur nécessitant informations client final
- remplissage du formulaire réglementaire (SIRET, site web)
- délai d'attente pour numéro français (3 jours à 1 semaine)
- connexion via SIP Trunking
- configuration sécurité SIP (Secure Trunking, PSTN, Symmetric RTP)
- configuration du contrôle d'IP fourni par Retell
- liaison finale du numéro via Termination URI (attention aux espaces)
- assignation finale de l'agent au numéro avec restriction géographique

## Outils mentionnes
- SynthFlow
- Retell AI
- GPT-4.1
- Eleven Labs
- Fish Audio
- Cartesia

## Tips techniques
- Démarrer avec un Single Agent Prompt pour un agent vocal simple (réception) plutôt qu'une architecture complexe
- Utiliser un modèle allégé (ex: GPT-4.1 mini) ou le fast tier pour un agent vocal simple, afin de réduire la latence de réponse
- Ne jamais cloner une voix sans avoir obtenu au préalable la permission explicite de la personne concernée
- Privilégier Eleven Labs pour la génération vocale, reconnu comme leader du secteur
- Choisir une voix conversationnelle plutôt que narrative pour un agent vocal dialoguant naturellement avec l'utilisateur
- Toujours vérifier l'absence d'espace parasite lors du copier-coller d'une valeur technique comme le Termination URI

## Cas d'usage reels
- [[]]
