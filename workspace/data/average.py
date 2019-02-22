# Moyenne sur un intervalle de temps + regroupement co2-hum-lum-temp
#
# usage: python3 $0 csv_file num_seconds
#
# csv_file -- fichier csv en entrée (input)
# num_seconds -- durée de l'intervalle
#
# Input :
#   - Une ligne de header
#   - Séparateur ';'
#   - lignes au format <ilot>;<type>;<seconds>;<value>
#   - type parmi co2|hum|lum|temp
#
# Output :
#   - Une ligne de header
#   - Séparateur identique à l'input
#   - lignes au format <timestamp>;<co2>;<hum>;<lum>;<temp>
#   - Valeurs manquantes notées "" (chaine vide)



import pandas
import numpy as np
import sys


def usage():
    """Usage error"""
    print("usage: python3 {} csvfile num_seconds".format(sys.argv[0]), file=sys.stderr)
    exit(1)





def main(csvfile, num_seconds, delimiter=';'):
    """Fonction 'main'

    csvfile -- fichier csv à traiter
    num_seconds -- durée de l'intervalle sur lequel on moyenne
    delimiter -- séparateur du fichier csv (in et out)
    """



    # Lecture
    data = pandas.read_csv(csvfile, sep=delimiter)

    # Regrouper toutes les valeurs de la tranche horaire sous un même timestamp
    data['timestamp'] = data['timestamp'] // num_seconds

    # Moyenne
    avg = data.groupby(['timestamp', 'type']).mean()

    

    # Aplatir le timestamp et le type en une dimension
    avg = avg.groupby(level=0)


    # En-tete du csv
    print("timestamp;co2;hum;lum;temp", flush=True)

    # Itération TRES lente -> à revoir !
    buffer = []
    for i, (timestamp, subdf) in enumerate(avg):
        values = {
            'co2': '',
            'hum': '',
            'lum': '',
            'temp': ''
            }
        for row in subdf.iterrows():
            values[str(row[0][1])] = float(row[1])
            
        # Ecriture
        print("{t}{d}{co2}{d}{hum}{d}{lum}{d}{temp}".format(
            d = delimiter,
            t = timestamp,
            co2 = values['co2'],
            hum = values['hum'],
            lum = values['lum'],
            temp = values['temp']
            ))

    





if __name__ == "__main__":

    # usage: python3 $0 csv_file num_seconds
    
    if len(sys.argv) != 3:
        usage()

    main(csvfile=sys.argv[1], num_seconds=int(sys.argv[2]))
