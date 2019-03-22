# Prétraitement des données : sélection sur l'ilot et le type de capteur
#
# Produit les partitions neo.<ilots>.<capteurs>.csv et neocampus.lite.csv
#   ilot -- identifiants d'ilot séparés par des '-'
#   capteurs -- type de capteur ou 'all'
# 
# et aussi...
#
# Produit des corpus annotés avec la commande 'make samples' : 
# output/<ilots>.<capteurs>.<intervalle>.csv
#   ilot -- ilot1 | all
#   capteurs -- all | co2 | hum | lum | temp
#   intervalle -- 300 | 900 | 1800 | 3600 | 21600 | 86400
# 


# Base originale
BASE_DATASET = All-All-2017-09-01_2018-09-01.csv

# Base allégée
LITE = neocampus.lite.csv

# Dossier des partitions
PDIR = parts
ODIR = output

# Fichiers de sortie
SENSORS = co2 hum lum temp
ILOTS = ilot1 ilot2 ilot3 ouest n57 n79
PARTS = $(foreach t, $(SENSORS) all, $(foreach i, $(ILOTS) all, $(PDIR)/$(i).$(t).csv))
SAMPLES = $(foreach t, $(SENSORS) all, $(foreach i, ilot1 all, $(foreach s, 300 1200 3600 21600 86400, $(ODIR)/$(i).$(t).$(s).csv)))





# Enregistre la base allégée et les fichiers de sortie
all: $(LITE) $(PARTS) $(SAMPLES)


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
	awk -F ';' '{print $$6 ";" $$1 ";" $$4 ";" $$3;}' |\
	sed 's/erature//' | sed 's/idity//' | sed 's/inosity//' |\
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
	grep '^\($(subst -,\|,$*)\)' $^ >> $@


$(PDIR)/%.co2.csv: ilot.%.csv | $(PDIR)
	head -n 1 $^ > $@
	grep 'co2' $^ >> $@ || echo "Pas de co2 dans $*" >&2

$(PDIR)/%.hum.csv: ilot.%.csv | $(PDIR)
	head -n 1 $^ > $@
	grep 'hum' $^ >> $@ || echo "Pas de hum dans $*" >&2

$(PDIR)/%.lum.csv: ilot.%.csv | $(PDIR)
	head -n 1 $^ > $@
	grep 'lum' $^ >> $@ || echo "Pas de lum dans $*" >&2

$(PDIR)/%.temp.csv: ilot.%.csv | $(PDIR)
	head -n 1 $^ > $@
	grep 'temp' $^ >> $@ || echo "Pas de temp dans $*" >&2

$(PDIR)/%.all.csv: ilot.%.csv | $(PDIR)
	cp $^ $@







# Créer les exemples de training-set
samples: $(SAMPLES)

$(ODIR)/%.csv: | $(PARTS) $(ODIR)
	$(eval ilot = $(word 1, $(subst ., ,$*)))
	$(eval capt = $(word 2, $(subst ., ,$*)))
	$(eval intv = $(word 3, $(subst ., ,$*)))
	echo -n "timestamp" > $@
	python3 preproc.py $(PDIR)/$(ilot).$(capt).csv $(intv) $(if $(filter-out all, $(capt)), $(capt)) | grep -v ';;' >> $@
	


# Dossiers
$(ODIR) $(PDIR):
	mkdir -p $@






clean:
	rm -fr ilot.*.csv $(PDIR)

clean_base:
	rm -f $(LITE)

maxclean: clean clean_base

.PHONY: all samples clean maxclean clean_base
