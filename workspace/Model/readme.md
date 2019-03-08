# Comment on s'en sert ?

- dans un premier temps mettez dans Formatage/parts : les outputs du script de
prétraitement des donnees sous la forme "ilot"."feature".csv

- lancer le script traning.py qui prend trois arguments **(ceci a été modifié)** : l'ilot, la feature et la taille
d'un vecteur, ce qui enregistrera les models dans le dossier "models" (attention c'est long)
et ça vous affichera de beaux graphiques pour voir si votre modèle predit bien

- puis pour predire la valeur de confort lancez le script test_val_conf.py, les valeurs actuelles 
devront être dans le dossier "current_values", de la forme val1;val2;...;valN avec N = 90 pour 
la luminosité et N = 30 pour les autres (parce que l'intervalle de temps sur l'entrainement n'est 
pas le même pour la luminosité, je changerais ça plus tard)



## jupyterlab pas encore à jour
Je ne saurais trop vous conseiller d'aller voir les notebooks c'est beaucoup plus parlant
(même si beaucoup se ressemblent parce que y'a pas de sys.argv sur jupyterlab, en tous cas j'ai pas trouvé
## jupyterlab pas encore à jour
