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

