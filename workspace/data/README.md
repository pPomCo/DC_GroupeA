# workspace/data/

Mise en forme des données

## Sélection des lignes

Avec le *Makefile* on peut créer des fichiers csv correspondants aux selections :

 - sur l'ilot / les ilots
 - sur le capteur / tous les capteurs

A partir de la base allégée ('lite' : même info, 230Mo).

Il est conseillé de générer une fois la base allégée (un peu long) en tant qu'action principale (*make neocampus.lite.csv*)
pour qu'elle soit enregistrée.

Pour cela :

	# Créer la base intermédiaire et les partitions standards
	make
	
	# Créer la base allégée
	make neocampus.lite.csv
	
	# Créer une sélection sur l'ilot *ilot1* et la température
	make parts/ilot1.temp.csv
	
	# Créer une sélection sur les ilots *ouest* et *n57*, pour tous les capteurs
	make parts/ouest-n57.all.csv


---

## Regroupement des lignes par moyenne et annotation

Avec le script *preproc.py* on atteint ces buts :

 - Moyenne sur un intervalle donné (en seconde)
 - Regroupement des capteurs sur une même ligne
 - Annotation avec la fonction de confort des M2

Il est conseillé de :

 - Travailler avec la sélection la plus restreinte en entrée (accélère le temps de lecture et de moyenne)
 - Utiliser un intervalle de moyenne suffisament grand (annotation en *O(intervalle)* )


### Usage

	# Usage:
	# -d delimiter -- délimiteur du csv (optionnel, défaut = ';')
	# csvfile -- fichier csv en entrée
	# num_seconds -- intervalle pour faire les moyennes
	# sensor_types -- liste des capteurs séparés par un tiret (optionnel, défaut = 'co2-hum-lum-temp')

	python3 preproc.py [-d delimiter] csvfile num_seconds [sensor_types]


Si sensor_types est une liste de une seule valeur : on utilise la fonction ad-hoc.  
Si sensor_types est une liste de plusieurs valeurs : on utilise la fonction *annotationCapteur* en remplaçant les valeurs manquantes par des zéros.

### Exemples

	# Luminosité pour l'ilot *n57*, regroupée par jour
	csv=parts/n57.lum.csv
	make $csv
	python3 preproc.py $csv 86400 lum > output.csv
	
	# Tous les capteurs pour l'ilot *ouest*, regroupés par heure
	csv=parts/ouest.all.csv
	make $csv
	python3 preproc.py $csv 3600 > output.csv

	# Tous els capteurs pour les ilots *ilot1*, *ilot2* et *ilot3*, regroupés par semaine
	csv=parts/ilot1-ilot2-ilot3.all.csv
	make $csv
	python3 preproc.py $csv 604800 > output.csv

---


### Script *annotationUnique.py*

C'est le script fournit par les M2 (j'ai oublié leur nom...), tel quel. Il est réputé être encore en developpement, mais il fonctionne.  

On a quand même quelques problèmes avec les valeurs absentes (zéro fait baisser la note), mais est-ce de notre ressort ?

---
