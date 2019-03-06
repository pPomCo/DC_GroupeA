# Moyenne sur un intervalle de temps + regroupement co2-hum-lum-temp + confort
#
# usage: python3 $0 [-d delimiter] csv_file num_seconds [stypes]
#
# -d delimiter -- délimiteur du csv (défaut ';') -- optionnel
# csv_file -- fichier csv en entrée (input)
# num_seconds -- durée de l'intervalle
# stypes -- types de capteurs (default 'co2-hum-lum-temp') -- optionnel
#
# Input :
#   - Une ligne de header
#   - Délimiteur ';' ou donné avec -d
#   - lignes au format <ilot>;<type>;<timestamp>;<value>
#   - type parmi co2|hum|lum|temp
#
# Output :
#   - Une ligne de header
#   - Délimiteur identique à l'input
#   - lignes au format <timestamp>;<stype0>;<stype1>;...;<stypen>;<confort>
#   - Valeurs manquantes notées "" (chaine vide)
#
#
# Confort est donné par le module annotationUnique des M2.
#
# Si stypes est une liste de 1 élément ('co2' ou 'hum' ou 'lum' ou 'temp')
# confort est calculé avec la fonction ad-hoc
#
# Si stypes contient plusieurs éléments, confort est calculé avec
# annotationUnique.annotationCapteur, les valeurs manquantes étant mises à 0
#

import pandas
import numpy as np
import sys
import time

import annotationUnique as anno


def usage():
    """Usage error"""
    print("usage: python3 {} [-d delimiter] csvfile num_seconds [stypes]".format(sys.argv[0]), file=sys.stderr)
    exit(1)



class Timer(object):
    """Mesure le temps d'exécution"""
    def __init__(self, file=sys.stderr):
        self.t = time.clock()
        self.file = file

    def start(self, msg="Timed execution"):
        """Start timer"""
        print(msg, end="... ", flush=True, file=self.file)
        self.t = time.clock()

    def stop(self):
        """Stop timer"""
        print(round(time.clock()-self.t, 3), "sec", file=self.file)
        




def annotate(row):
    """Annotation avec la valeur de confort des M2

     - Un seul type de capteur -> fonction ad-hoc
     - Plusieurs types -> fonction annotationCapteur avec 0 pour les valeurs manquantes
    """
    
    # Si un seul type dans l'index (+confort -> len==2)
    if len(row.index) == 2:
        if (row.index[0] == 'co2'):
            row['confort'] = anno.co2(row['co2'])
        elif (row.index[0] == 'hum'):
            row['confort'] = anno.humidite(row['hum'])
        elif (row.index[0] == 'lum'):
            row['confort'] = anno.luminosite(row['lum'])
        elif (row.index[0] == 'temp'):
            row['confort'] = anno.temperature(row['temp'])
        else:
            print("index '{}' not recognized".format(row.index[0]),
                  file=sys.stderr)

            
    # Si plusieurs types : annotationCapteur avec 0 pour valeurs manquantes
    else:
        getvalue = lambda t: row[t] if t in row.index else 0
        row['confort'] = anno.annotationCapteur(getvalue('temp'),
                                                getvalue('lum'),
                                                getvalue('co2'),
                                                getvalue('hum'))
    return row



def main(csvfile, num_seconds, stypes = ['co2', 'hum', 'lum', 'temp'],
         delimiter=';'):
    """Fonction 'main'

    csvfile -- fichier csv à traiter
    num_seconds -- durée de l'intervalle sur lequel on moyenne
    stypes -- liste ordonnée des types des capteurs (sensor types)
    delimiter -- séparateur du fichier csv (in et out)
    """


    # Mesure le temps d'exécution
    timer = Timer()
 


    # Lecture
    timer.start("Read csv")
    data = pandas.read_csv(csvfile, sep=delimiter)
    timer.stop()




    timer.start("Average")

    # Regrouper toutes les valeurs de la tranche horaire sous un même timestamp
    data['timestamp'] = data['timestamp'] // num_seconds

    # Moyenne
    avg = data.groupby(['timestamp', 'type']).mean()

    timer.stop()


    
##    output = avg.unstock().apply(annotate, axis=1)




    timer.start("Prepare output")

    # Stocker l'output
    output = pandas.DataFrame(index=np.unique(data['timestamp']),
                              columns=stypes+["confort"])

    
    # Recopier les valeurs. Un peu long...
    for (ts,stype), row in avg.iterrows():
        if stype in stypes:
            output.at[ts,stype] = row[0]

    timer.stop()
    timer.start("Annotations")

    # Annotations
    output = output.apply(annotate, axis=1)

    timer.stop()

    # Ecriture résultat
    print(output.to_csv(sep=delimiter))

    exit(0)
    
 
    





if __name__ == "__main__":

    # usage: python3 $0 [-d delimiter] csv_file num_seconds [stypes]
    

    delim = ';'
    stypes = ['co2', 'hum', 'lum', 'temp']

    argv = sys.argv[1:]
    if len(argv) < 2:
        usage()

    if argv[0] == '-d':
        delim = argv[1]
        argv = argv[2:]

    if len(argv) < 2:
        usage()

    if len(argv) > 2:
        stypes = argv[2].split('-')
    

    main(csvfile=argv[0],
        num_seconds=int(argv[1]),
        stypes=stypes,
        delimiter=delim)
