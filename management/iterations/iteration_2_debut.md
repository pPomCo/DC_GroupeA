# Début d'itération n°1 : 18/02-03/03

Jeudi 21/02

Les vacances tombent la seconde semaine de l'itération

### Etat actuel | contexte du projet

#### Gestion de projet

 - Contact client ré-établi
 - Attribution d'un AMOA 
 
#### Métier

 - Exigences recueillies.
 - Aucun travail concret réalisé
 
### Objectifs

 - Débuter le travail concret
 - Mettre en place le "pipeline de production" :
    1. Prétraitement des données
    2. Exploration des données
    3. Modèle avec keras
    4. Évaluation du modèle
    5. Rapport

### Taches

Les taches sont clairement définies !

1. Prétraitement
  - Regroupement des valeurs co2,hum,lum,temp
    - Par seconde / minute / heure
    - Avec nan pour les valeurs absentes
    - Avec pandas ou Makefile si c'est plus pratique
    - Etiqueter avec la valeur de confort
2. Exploration des données
  - Corrélations entre capteurs et/ou avec la valeur de confort
  - Représenter histogrammes / courbes
  - Statistiques (moyenne, min, max, variance/ecrat type)
3. Modèle avec keras
  - Regression linéaire
  - Prédire confort actuel et/ou futur
4. Evaluer
  - Définir les métriques
  - Définir validation (croisée ?) / partition données
5. Rapport
  - Structure du rapport
  - Chacun rédige ce qu'il a fait
  - Évaluation de l'évaluation
  - Synthèse


Répartition :

| Travail          | Auteur   | Effort | Date butoir |
| ----- ---------- | -------- | ------ | ----------- |
| 1. Prétraitement | Pierre   | 8      | mardi 26    |
| 2. Exploration   | Jérémie  | 5      | mercredi 27 |
| 3. Modèle        | Quentin  | 5 à 20 | jeudi 28    |
| 4. Evaluation    | Jérémie  | 5      | vendredi 29 |
| 5. Rapport       | Tous     | 4      | samedi 30   |


### Livrables

Le rapport sera livré le ...
Le rendez-vous sera pris pendant les vacances.
 

