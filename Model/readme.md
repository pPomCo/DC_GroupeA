# Comment on s'en sert ?

- dans un premier temps mettez dans Formatage/parts : les outputs du script de
pr�traitement des donnees sous la forme "ilot"."feature".csv

- lancer le script traning.py qui prend trois arguments : l'ilot, la feature et la taille
d'un vecteur, ce qui enregistrera les models dans le dossier "models" (attention c'est long)
et �a vous affichera de beaux graphiques pour voir si votre mod�le predit bien

- puis pour predire la valeur de confort c'est pas encore fait, y'a un script pour tester
(test_val_conf.py) mais j'ai mis des valeurs un peu nazes m�me si le r�sultat est coh�rent
il faut que je rajoute l'ajout de vraies donn�es

Je ne saurais trop vous conseiller d'aller voir les notebooks c'est beaucoup plus parlant
(m�me si beaucoup se ressemblent parce que y'a pas de sys.argv sur jupyterlab, en tous cas j'ai pas trouv�)