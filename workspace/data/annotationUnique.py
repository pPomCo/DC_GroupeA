# -*- coding: utf-8 -*-
"""
Annotation des données selon un seuil défini par les spécifications du Google doc suivant :
https://docs.google.com/document/d/1vtwxloreLhoaFz1Pv8dX8Ovy9aDcBi80iWPXRxZvmLY/edit

"""

# Annotation d'une valeur de température selon les seuils définis
def temperature(valeur):
    if(valeur < 23.2 and valeur > 20.8):
        return 5
    elif(valeur < 24.5 and valeur > 19.5):
        return 4
    elif(valeur < 26 and valeur > 18):
        return 3
    elif(valeur < 27 and valeur > 17):
        return 2
    elif(valeur < 28 and valeur > 16):
        return 1
    else:
        return 0

# Annotation d'une valeur de luminosité selon les seuils définis
def luminosite(valeur):
    if(valeur > 600 and valeur < 900):
        return 5
    elif(valeur > 550 and valeur < 950):
        return 4
    elif(valeur > 500 and valeur < 1000):
        return 3
    elif(valeur > 400 and valeur < 1100):
        return 2
    elif(valeur > 200 and valeur < 1300):
        return 1
    else:
        return 0

# Annotation d'une valeur de co2 selon les seuils définis
def co2(valeur):
    if(valeur<400):
        return 5
    elif(valeur<600):
        return 4
    elif(valeur<800):
        return 3
    elif(valeur<1000):
        return 2
    elif(valeur<1200):
        return 1
    else:
        return 0

# Annotation d'une valeur d'humidité selon les seuils définis
def humidite(valeur):
    if(valeur < 55 and valeur > 45):
        return 5
    elif(valeur < 58 and valeur > 42):
        return 4
    elif(valeur < 63 and valeur > 37):
        return 3
    elif(valeur < 70 and valeur > 30):
        return 2
    elif(valeur < 80 and valeur > 20):
        return 1
    else:
        return 0

# Annotation d'une situation globale pour un capteur, en regroupant les valeurs trouvées durant des périodes de deux minutes, pour les différentes mesures.
def annotationCapteur(valeurTemperature, valeurLuminosite, valeurCo2, valeurHumidite):
    annotationRetour = 0
    # Définition de poids, selon l'importance d'un critère pour l'humain
    # Poids définis ici après un vote entre les membres du groupe
    poidsTemperature = 0.3
    poidsLuminosite = 0.2
    poidsCo2 = 0.4
    poidsHumidite = 0.1
    annotationRetour += poidsTemperature * temperature(valeurTemperature)
    annotationRetour += poidsLuminosite * luminosite(valeurLuminosite)
    annotationRetour += poidsCo2 * co2(valeurCo2)
    annotationRetour += poidsHumidite * humidite(valeurHumidite)

    return str(annotationRetour);
