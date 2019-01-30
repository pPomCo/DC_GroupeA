# Données

Préparation des données pour le développement, l'entraînement et les tests.


### Partition des données

 - Dev : 10 %
 - Train : 70 %
 - Test : 20 %

La partition est faite sur la milliseconde modulo 10.
	
	# Partition du fichier ./neocampus.csv
	make
	
	# Partition du fichier <nom>.csv
	make <nom>_dev.csv <nom>_train.csv <nom>_test.csv
	
	# Et bien sur, pour n'avoir que la partition dev...
	make <nom>_dev.csv
	
	
