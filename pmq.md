### ------------
le PMQ selon Dr. Migeon : https://app.elaastic.com/player/index.html#/play/FredoMigeon/584a6effe4b07a30b65a6499/html?toc=1#584a378be4b07a30b65a6459

Objectif : Veiller à ce que les exigences du projet, notamment les exigences du produit, soient respectées et validées.
### ------------

# PM Qualité

## 1.1) Identification des exigences qualité
comment ?
- en extrayant les exigences directement des PP via des entretiens, le cahier des charges
ou simplement une liste d'exigence décrétée par les PP.
- en se fixant nous-même, entre les membres du projet, des exigences qualités afin d'améliorer le travail en groupe 
ou la lisibilité du code.

Exigences qualités d'origine externe (via les PP) : 
- 11 : Utilisation de Python avec Scikit ou Keras (exigence de Dr. TP)
- 12 : Aucune autre pour l'instant, ça ne saurait tarder

Exigences qualités d'origine interne (via réunions et bonnes pratiques qui font consensus dans le milieu informatique) : 
[X] 21 : Les produits, consituant des livrables, devront être partagé et developpé par plusieurs membres de l'équipe avec facilité
[ ] 22 : Pour s'assurer que tous les membres du groupe ont comprit une tâche -> faire modélisation besoin ? faire precondition/postcondition ?
[ ] 23 : Pour s'assurer que tous les SP fonctionnent bien

## 1.2) Solutions qualité
- 11 : Exigence simple à satisfaire : developper avec python
- 21 : Convention de code :
a) Variables de la forme : nbrDeFeatures;
b) 1 commentaire par boucle au minimum
- 31 : (en parralèle au code) Programme de tests aux limites simple (qui regroupera les tests aux limites de tous les SP)

## 1.3) Contrôle qualité
L'application de toutes les exigences doit être validée par {unanimité/ au moins 51% du groupe} pour être considérée
conforme et fonctionnelle {ou alors on utilise le framework UnitTest de python3 ce serait probablement plus pro
et dans ce cas il faut revoir les solutions qualité qui seront toutes plus ou moins intégrées à ça}
