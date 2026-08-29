---
tags: [formation, millenium]
module: Formation IA
section: "Agents Vocaux"
source_transcript: "10.03 Sécuriser vos agents vocaux.txt"
---

# 10.03 Sécuriser vos agents vocaux

## Resume
- Sommaire du module sécurisation des agents vocaux : sécurité RGPD, extraction de données post-appel, paramètres de rétention, guardrails de sécurité, Agent Handbook, connexion d'outils externes.
- Reprise du travail précédent : l'agent dispose déjà d'un prompt fonctionnel et est joignable dans la langue voulue, avec annonce d'approfondissement du prompt pour plus de complexité et d'informations.
- Détail des éléments d'humanisation du prompt : personnalité de représentant professionnel définissant le langage, et mots de remplissage naturels (« alors oui, laissez-moi vous montrer ») pour un rendu plus humain.
- Présentation de l'alphabet phonétique (aide à l'épellation) et de la normalisation de la parole, essentielle pour que les dates soient dictées correctement plutôt qu'au format numérique brut.
- Transition vers les sections de personnalisation avancée : paramètres vocaux, paramètres de transcription en temps réel, et paramètres d'appel, à explorer successivement.
- Présentation du son de fond (background sound) ajoutant du réalisme à la conversation : préférence personnelle pour l'ambiance « coffee shop », jugée plus crédible que le call center ou le bruit statique.
- Explication du réglage de temporisation de réponse après silence détecté : accorder un délai supplémentaire pour vérifier si l'utilisateur reprend la parole, un compromis entre réactivité et latence perçue.
- Présentation de l'extrême opposé du réglage : sensibilité élevée entraînant une interruption immédiate au moindre bruit, à ajuster selon l'environnement sonore réel (réduire en environnement bruyant).
- Présentation du paramètre de prononciation personnalisée, particulièrement utile pour les domaines techniques avec vocabulaire spécifique nécessitant une prononciation précise et correcte.
- Exemple d'usage du paramètre de prononciation dans un contexte médical (clinique de cardiologie) : mots comme « cœur » ou « artères » nécessitant une transcription précise et prioritaire.
- Présentation du système de détection des menus IVR robotiques automatiques, permettant à l'agent de raccrocher intelligemment, ainsi que des options de détection de messagerie vocale (raccrocher ou laisser un message).
- Recommandation forte de limiter la durée d'appel maximale à 3 minutes : au-delà, il vaut mieux rappeler plus tard plutôt que de prolonger un appel qui traîne, une bonne pratique de gestion des cas limites.
- Confirmation du réalisme apporté par le bruit de fond (conversations perceptibles) et des options d'interruption, concluant la configuration de l'agent désormais opérationnel et correctement paramétré.
- Transition vers la sécurisation RGPD et l'ajout d'outils à l'agent, avec sensibilité particulière soulignée en Europe pour les données médicales et vocales, considérées comme des informations personnelles sensibles.
- Présentation du Data Storage Settings : trois options de conservation des données d'appel par Retell, chacune associée à une durée de rétention différente, consultables dans l'historique des appels du dashboard.
- Précision importante : les deux options de rétention les plus complètes conservent aussi l'enregistrement audio de l'appel ; pour ne garder que les transcripts sans audio, il faut utiliser l'OptinSecureURL.
- Présentation de l'option la plus restrictive : ne conserver aucun attribut de contenu, seulement des métadonnées basiques sur la plateforme (type d'appel), sans aucun enregistrement de l'appel lui-même.
- Conclusion du volet sécurité et conformité RGPD (éviter les infractions), avant transition vers une nouvelle section touchant aux données clients : le Post Call Data Retrieval qui récupère des informations après l'appel via un modèle d'IA analysant le transcript.
- Exemple d'extraction de données post-appel : possibilité de récupérer des informations comme l'âge du client ou un résumé automatique de l'appel, avec des champs par défaut déjà actifs car nécessaires au fonctionnement de Retell.
- Présentation du besoin d'être notifié ou de recevoir des actualisations une fois un appel terminé, via la création d'un webhook sur N8N, en privilégiant le webhook de production pour éviter de rester en mode test.
- Présentation des trois moments déclencheurs possibles du webhook (début, fin, et analyse de l'appel), avec préférence personnelle pour l'événement « appel analysé » qui regroupe les informations issues du Post Call Extraction.
- Test en direct du webhook : après un appel terminé, réception dans N8N d'une nouvelle exécution contenant l'agent concerné, son nom, et les variables dynamiques renseignées durant l'appel, visibles via les headers.

## Concepts cles
- plan de présentation de la sécurisation des agents vocaux
- reprise et annonce d'approfondissement du prompt existant
- éléments d'humanisation : personnalité professionnelle et mots de remplissage
- alphabet phonétique et normalisation de la parole (dates)
- transition vers paramètres vocaux/transcription/appel
- son de fond pour crédibilité (préférence coffee shop)
- réglage de temporisation après détection de silence (compromis latence)
- ajustement de sensibilité d'interruption selon l'environnement sonore
- paramètre de prononciation personnalisée pour vocabulaire technique
- exemple médical de prononciation prioritaire (cardiologie)
- détection IVR robotique et gestion de la messagerie vocale
- recommandation de limite de durée d'appel (3 minutes maximum)
- validation finale du réalisme et de la configuration de l'agent
- sensibilité RGPD des données médicales et vocales en Europe
- Data Storage Settings (trois options de rétention)
- OptinSecureURL pour conserver les transcripts sans l'enregistrement audio
- option de conservation minimale (métadonnées seules, aucun enregistrement)
- Post Call Data Retrieval (extraction post-appel via LLM)
- exemples d'extraction post-appel (âge, résumé automatique)
- notification post-appel via webhook N8N (mode production)
- trois déclencheurs de webhook (début/fin/analysé), préférence pour 'appel analysé'
- test en direct du webhook (contenu reçu : agent, nom, variables dynamiques)

## Outils mentionnes
- Retell AI
- n8n

## Tips techniques
- Ajouter des mots de remplissage naturels dans le prompt d'un agent vocal pour le rendre plus humain et moins mécanique
- Utiliser un son de fond type 'coffee shop' pour rendre un agent vocal plus crédible et naturel
- Réduire la sensibilité d'interruption d'un agent vocal dans un environnement bruyant pour éviter les faux déclenchements
- Limiter la durée maximale d'un appel automatisé à 3 minutes : au-delà, préférer rappeler plus tard
- Utiliser l'OptinSecureURL pour ne pas conserver l'enregistrement audio tout en gardant les transcripts, dans une logique de minimisation RGPD
- Utiliser le webhook de production plutôt que le webhook de test pour recevoir les notifications post-appel de façon fiable

## Cas d'usage reels
- [[]]
