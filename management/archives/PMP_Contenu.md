

## PM Contenu

*S'assurer que tous le travail requis, et seulement le travail requis, est réalisé.*

Plusieurs aspects, plusieurs produits :

1. Documents de TD (=SJQ)
2. Comptes-rendus M. Pellegrini
3. Diaporama de soutenance
4. Fiches d'avancement Interpromo

*ordonné selon le barème de notation*

### Définition du contenu

TD :

1. Les produits sont identifiés et listés en séance
2. Cette liste est validée par Mme Oliveira avant la fin de la séance
3. Le contenu est défini

Compte-rendus M. Pellegrini :

1. Les produits sont identifiés en RDV
2. Ils sont listés dans le compte-rendu de RDV (chapitre à part)
3. Le compte-rendu est envoyé par mél à M. Pellegrini
4. M. Pellegrini confirme
5. Le contenu est défini

Diaporama de soutenance :

- **Le protocole n'est pas élabli**

Fiches d'avancement Interpromo

- **Le protocole n'est pas élabli**



### Réalisation du contenu

Pour chaque produit liste (TD, compte-rendu de rendez-vous) :

1. Les taches sont estimées en *points d'effort*
2. L'ordonnancment est décidé pour la réalisation de ces produits (voir PM délais : ordonnancement + échéance)
3. On attribue à chaque tache un *réalisateur* selon les *points d'effort* attribués
4. On attribue à chaque tache un *référent* différent du *réalisateur*. Il aide et contrôle.
5. Une branche dédiée est créée sur le dépôt git. La liste des produits (1.) y est déposée
6. Les produits y sont déposés au fur et à mesure de leure réalisation
7. Après validation, la branche est fusionnée avec *master* afin d'en faciliter l'accès à Mme Oliveira

## Validation du contenu :

1. L'auteur/l'un des auteurs crée une carte sur le *Trello* (colonne *Validation*)
2. Le *référent* compare le produit à celui identifié et listé en TD (protocole 1.)
3. Les remarques / réserves / objections / suggestions sont ajoutées en commentaire à la carte sur le *Trello*. Si besoin, une réunion peut être organisée.
4. La validation est actée. La carte reste sur le *Trello* jusqu'à ce que la branche ait été fusionnée



### Recueil des exigences

TD / SJQ

1. Les livrables sont déposés sur un dépôt *git* ou *Google drive* dont l'accès est partagé avec Mme Oliveira
2. Les échéances sont respectées, **la date du dépôt faisant foi**.
3. D'après le barème incomplet ([Organisation 2018-2019, pages 22 à 27](../documentation/UEprojet/Organisation_2018_2018.pdf))
   - Compte-rendu pour chaque RDV, communiqué suffisament à l'avance pour être corrigé à la réunion suivante
   - Livrables conformes aux attentes
   - Support / diaporama lors de la recette (*apporte une réelle plus-value*)
   - Aucun livrable ne manque

M. Pellegrini

- Langage *python*
- Bibliothèques *keras* (recommandée) et *scikit*
- Les comptes-rendus sont au format notebook/jupyter

Diaporama de soutenance

- Première page : 
   - Nom et composition de l'équipe
   - Nom du client
   - Organisme du client
   - Titre du projet
   - Date
   - Logos si utiles
 - Adapté à 12-15 minutes
 - Une diapositive donne le plan, les suivantes permettent de suivre l'avancement dans ce plan
 - Pas de fautes d'orthographes
 - Transparent avec points positifs et négatifs
 - Sujet du diaporama : guidé par le barème [Organisation 2018-2019, pages 26](../documentation/UEprojet/Organisation_2018_2018.pdf)
 
Fiches d'avancement Interpromo

- Toutes les semaines
- Document sur *Google Drive* de l'UE **lien ?**
- Par le *chef de projet*


Format :

- Les documents sont rédigés en *MarkDown*
- Les images sont placées dans un dossier *images/*



### Stockage du contenu

| Produit                       | Workspace | Final        | Sauvegarde |
| :---------------------------- | :---------| :----------- | :--------- |
| Livrables TD                  | Dépôt git | Dépôt git    |            |
| Livrables M. Pellegrini       | Dépôt git | *aucun*      |            |
| Diaporama de soutenance       | Dépôt git | *aucun*      |            |
| Fiche d'avancement Interpromo | *aucun*   | Google Drive |            |





### SDP

http://yuml.me/edit/b0351123

![Image SDP](http://yuml.me/b0351123.png)

Le sous-découpage et l'évaluation des tâches en points d'effort sera effectuée
lors des réunions d'ouverture d'itération.

"Code" pour yuml :

	%2F%2F SDJ, 
	, 
	[Projet]-[UE], 
	, 
		[UE]-[PAQL], 
		[UE]-[PMP], 
		[UE]-[Comptes-rendus],
			[Comptes-rendus]-[CR iteration],
			[Comptes-rendus]-[CR RDV client],
		[UE]-[Cahier de recette],
		[UE]-[Bilan],
		[UE]-[Soutenance],
			[Soutenance]-[Diaporama],
			[Soutenance]-[Script],
	[Projet]-[InterPromo], 
		[InterPromo]-[Recherche],
			[Recherche]-[RNN],
			[Recherche]-[CRNN],
			[Recherche]-[Reduction en dimension],
			[Recherche]-[Regression],
		[Interpromo]-[Analyse comparative]


### Matrice RACI pour la gestion du contenu

| Tâche		| MOE   | MOA   | Réfs  | SJQ   | M1/M2 |
| :-----------: | :---: | :---: | :---: | :---: | :---: |
| Recueil exig.	| R,A	| C,I	| C	| C,I	| C ?	|
| SDJ		| R,A	| C,I	| C ? 	| I	|	|
| Recette	| R,A	| C,I	| C,I ? | 	|	|
| Soutenance	| R,A	| 	|  	| I 	|	|
| Fiches av. IP	| R,A	| 	| I  	|  	|	|
| Maîtrise ctn	| R,A,C |	|	|	|	|



