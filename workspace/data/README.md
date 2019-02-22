# workspace/data/group

**Work in progress**

C'est pas vraiment au point mais on peut déjà faire les moyennes journalières / horaires.

Pour les minutes, c'est très très long :-( J'y reviendrai

Pour les secondes : pas assez de valeurs, autant travailler avec les données non groupées !

Je terminerai lundi


## Makefile

Combine les valeurs des différents types de capteurs, par ilot

Note : le makefile génère aussi la base de données 'lite' (même info, 230Mo).  
Est-ce ici qu'il faut le faire ?

	# Crée tous les jeux de données regroupées et la base lite
	make

	# Crée la base lite
	make neocampus.lite.csv
	
	# Sélection de la base lite pour l'ilot <ilot> (ni moyenne, ni regroupement)
	# ilot = ilot1 | ilot2 | ilot3 | ouest | n57 | n79 | all
	make ilot.<ilot>.csv

	# Crée le jeu de données regroupées pour l'ilot <ilot> et l'intervalle <intervalle>
	# ilot = ilot1 | ilot2 | ilot3 | ouest | n57 | n79 | all
	# intervalle = day | hour | min | sec
	make group.ilot1.<ilot>.<intervalle>.csv

---

## average.py

Calcule la moyenne sur l'intervalle specifié et regroupe les valeurs co2, hum, lum, temp sur la même ligne.

Ce script est appelé par le Makefile. Il peut aussi être utilisé tel quel :

	# Usage
	python3 average.py fichier num_secs

Le format de fichier attendu en entrée est celui de la base *lite*, c'est à dire :

	<ilot>;<type>;<timestamp>;<valeur>

Le format en sortie est :

	<timestamp2>;<co2>;<hum>;<lum>;<temp>

Le traitement n'est pas efficace et sera revu.


