# Comptes-rendus des réunions client

## Lundi 14/01 : Découverte du projet

Contact : 09/01
Horaires : 9:00-9:45

Pierre est arrivé avec 30 minutes de retard (bouchons).

### Objectif du projet :

- prédiction des valeurs futures des capteurs
- prédiction d'une éventuelle fonction de confort
- prédiction d'annotation concernant la performance du système
- minimiser la taille du modèle
- explorer les possibilités du jeu de données

### Gestion du projet :

- contexte :
  - client ne sait (pour l'instant) rien des données : à nous de proposer des solutions/initiatives
  - enseignant référent (même personne, rôle différent) capable de nous orienter sur les points techniques
- livrables : notebook Jupyter contenant code & rapport
- exigences : le mieux possible
- contact : mail, 2 réunions restantes (prochaine 28/01)

### Métier :

- outils : python (obligatoire), keras (recommandé) et scikit
- modèles : régression, réseau de neurones
  - entrée : fenêtres, jours semaine avant dernière couche cachée
  - entraînement : train sur une semaine, dev lundi, test mardi, google collab
  - sortie : observations ultérieures, fenêtres une heure (ou plus), jour (non-)ouvré ou heure du jour
- données :
  - transformations possibles : encodage one-hot
  - simplification des dates : précision secondes, médiane sur fenêtre, supprimer complètement
  - synchronisation des capteurs : régression multivariée
  - ajout : données météorologiques, planning des salles...
- ressources :
  - [http://karpathy.github.io/2015/05/21/rnn-effectiveness/](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
  - [http://colah.github.io/posts/2015-08-Understanding-LSTMs/](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)


---

## Lundi 11/02 : RDV (IRIT)

Contact : 11/02
Horaires : 10h-10h20

Rendez-vous impromptu

### Confirmation / redéfinition des exigences

 - Prédire la fonction de confort :
    - Par régression (scikit-learn)
    - Avec RNN (keras)
 - Rapport :
    - Modèles
    - Résultats
    - Limites
    - Erreurs

La prédiction de la consommation est abandonnée (pas de données).

### Conseils

 - Prendre en main keras :
    - Faire tourner des exemples du net (mots-clés : régression multivarié RNN m-list)
    - Comprendre comment formater les données (avant tout apprentissage)
 - Essayer aussi la classification (discrétiser par intervalles)
 - Post-processing (conversion régression/classification)
 - Identifier les valeurs de la fonction de confort :
    - discret/continu
    - domaine de valeurs (à priori entre 0 et 5)
    - **-> Envoyer le nombre de valeur par mél, pour conseils supplémentaires**

### Divers

M. Pellegrini n'étant que peu disponible, il a nommé un AMOA :

	M. Léo CANCES
	leo.cances@irit.fr

Nous enverrons les courriels aux deux adresses (MOA et AMOA)

---

## Lundi 21/03 : Revue du livrable n°1

Contact : 12/03
Horaires : 9:00-9:45

Liste des présents : Jérémie HUTEAU, Quentin MARTY

### Revue du rapport
  - Etre précis sur les termes : modèles similaires -> prédictions similaires
  - Expliciter le processus afin de permettre la réplication du travail : train/test split
  - Présenter les informations pertinentes : nombre d'exemples, historiques d'apprentissage
  - Conclure sur nos résultats : performances du modèle avec les paramètres choisis 
  - Objectivité des commentaires : métrique "élevée" ou "faible" est arbitraire
  - Lister les outils et librairies utilisées
  - Citer les références utilisés (articles scientifiques, techniques)

### Revue du modèle
Le client est satisfait du travail réalisé.
Le référent propose les pistes d'améliorations suivantes :
  - Ajouter le mois (encodage one-hot) dans le vecteur d'input
  - Prédire une série temporelle plutôt qu'une seule valeur : TimeDistributed(Dense) ou LSTM(..., return_sequences = True)

