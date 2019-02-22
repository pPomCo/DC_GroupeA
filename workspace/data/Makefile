# Prétraitement des données
#
# Produit les fichiers grouped.<ilot>.<intervalle>.csv
# ilot -- identifiant d'ilot
# intervalle -- intervalle pour la moyenne, en secondes
#
# Enregistre la base allégée



# Base originale
BASE_DATASET = All-All-2017-09-01_2018-09-01.csv

# Base allégée
LITE = neocampus.lite.csv

# Fichiers de sortie
# Actuellement, c'est déraisonnable d'espérer utiliser average.py 
# sur les intervalles 'min' et 'sec'
INTERVALS = day hour
ILOTS = ilot1 ilot2 ilot3 ouest n57 n79
OUTPUT = $(foreach t, $(INTERVALS), $(foreach i, $(ILOTS), group.$(i).$(t).csv))



# Moyenniseur
EXE_AVG = python3 average.py





# Enregistre la base allégée et les fichiers de sortie
all: $(LITE) $(OUTPUT)


# Base allégée 
#   - types co2|hum|lum|temp
#   - projection ilot;type;timestamp;value
#   - ilots fablab rennomés 
#   - Conversion timestamp unix
$(LITE): $(BASE_DATASET) 
	# Header
	echo "ilot;type;timestamp;value" > $@
	
	# Filtre, raccourcit et convertit les dates en timestamp 
	# (cela peut prendre quelques minutes)
	cat $^ |\
	sed 's/erature//' | sed 's/idity//' | sed 's/inosity//' |\
	awk -F ';' '{print $$6 ";" $$1 ";" $$4 ";" $$3;}' |\
	sed 's/^57;/n57;/' | sed 's/^79;/n79;/' |\
	sed 's/\.......;/;/' |\
	sed 's/-/ /g' | sed 's/:/ /g' | sed 's/T/ /' |\
	awk -F ';' '{ print $$1 ";" $$2 ";" mktime($$3) ";" $$4; }' >> $@


# Copie de la base lite (temporaire)
ilot.all.csv: $(LITE)
	cp $^ $@

# Séléction sur l'ilot (temporaire)
ilot.%.csv: $(LITE)
	head -n 1 $^ > $@
	grep '^$*' $^ >> $@

# Moyenne par seconde
group.%.sec.csv: ilot.%.csv
	$(EXE_AVG) $^ 1 #> $@

# Moyenne par minute
group.%.min.csv: ilot.%.csv
	$(EXE_AVG) $^ 60 > $@

# Moyenne par heure
group.%.hour.csv: ilot.%.csv
	$(EXE_AVG) $^ 3600 > $@

# Moyenne par jour
group.%.day.csv: ilot.%.csv
	$(EXE_AVG) $^ 86400 > $@



clean:
	rm -f ilot.*.csv group.*.csv

clean_base:
	rm -f $(LITE)

maxclean: clean clean_base

.PHONY: all clean maxclean clean_base
