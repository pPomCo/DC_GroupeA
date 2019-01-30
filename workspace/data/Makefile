


# Fichier à partitionner par défaut
FILENAME = neocampus.csv
DATA = $(subst .csv,,$(FILENAME))


# Action par défaut : partition 'dev' de neocampus.csv
dev: $(DATA)_dev.csv $(DATA)_train.csv $(DATA)_test.csv



# Converstion du format YYYY-MM-DDTHH:MM:SS.uuuuuu en timestamp unix
%_ts.csv: %.csv
	cat $^ \
     | sed 's/-/ /g' \
     | sed 's/T/ /' \
     | sed 's/:/ /g' \
     | sed 's/\.......;/;/' \
     | awk -F ';' '{print $$1 ";" $$2 ";" $$3 ";" mktime($$4) ";" $$5 ";" $$6}' > $@



# Partition dev : millisecondes mod 10 == 0
%_dev.csv: partition.0.%.csv
	cat $^ > $@

# Partition train : millisecondes mod 10 in [1..7]
%_train.csv: $(foreach i, 1 2 3 4 5 6 7, partition.$(i).%.csv)
	cat $^ > $@

# Partition test : millisecondes mod 10 in [8;9]
%_test.csv: partition.8.%.csv partition.9.%.csv
	cat $^ > $@
	
	
partition.%.csv: 
	grep '\......'$(subst .,';' ,$*).csv > $@

clean: 
	rm -fr *_dev.csv *_train.csv *_test.csv *ts.csv

.PHONY: all dev train test clean

