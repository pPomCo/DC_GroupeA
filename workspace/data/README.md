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
	
	
Remarque : 5 lignes parmi les 10 587 536 n'ont pas ce format de date (pas de microsecondes) :
 
	939107:luminosity;u4/campusfab/luminosity/57;0;2017-10-10T20:41:34;lux;57
	4349946:humidity;u4/302/humidity/ilot3;31;2018-03-07T13:56:31;%r.H.;ilot3
	4973373:temperature;u4/302/temperature/ilot2;17.62;2018-03-24T22:53:24;celsius;ilot2
	6801212:luminosity;u4/302/luminosity/ilot1;7;2018-05-15T03:25:29;lux;ilot1
	7701240:temperature;u4/302/temperature/ouest;16.57;2018-06-13T00:42:30;celsius;ouest
