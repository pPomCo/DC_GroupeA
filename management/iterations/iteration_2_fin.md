# Fin d'itération n°2 : 3 mars 2019

## Revue

### Réalisation des taches / objectifs

1. Prétraitement
  - Regroupement des valeurs co2,hum,lum,temp : OK
  - Par seconde / minute / heure : OK
  - Avec nan pour les valeurs absentes : OK
  - Avec pandas ou Makefile si c'est plus pratique : OK
  - Etiqueter avec la valeur de confort : OK
2. Exploration des données
  - Corrélations entre capteurs et/ou avec la valeur de confort : OK
  - Représenter histogrammes / courbes : OK 
  - Statistiques (moyenne, min, max, variance/ecrat type) : NON
3. Modèle avec keras
  - Regression linéaire : NON mais RNN
  - Prédire confort actuel et/ou futur : presque
4. Evaluer
  - Définir les métriques : NON
  - Définir validation (croisée ?) / partition données : 50%
5. Rapport
  - Structure du rapport : NON
  - Chacun rédige ce qu'il a fait : 30%
  - Évaluation de l'évaluation : NON
  - Synthèse : NON



  
  
## Rétrospective

 - C'est positif d'avoir commencé le travail concret
 - Sous-estimation des points d'efforts de chaque tache -> pas terminées
    - Doubler les points d'efforts après estimation
 - Encore du retard -> ne pas arrêter les efforts
 - Attribution du référent : plutôt positif
 - Difficulté de communication Q/J -> plus de diplomatie
 - Déviation par rapport aux tâches définies (régression est devenue RNN)


## Revue

 - Prétraitement des données : Nan dans le csv -> c'est un problème
 - Validation -> méthode à établir et/ou confirmer
 - Exploration -> établir la saisonnalité
 - Modèle : mauvaises données en entrée, revoir fenêtrage / mieux documenter
 


