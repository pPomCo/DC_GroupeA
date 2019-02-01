# Projet DC Groupe A
*Projet master DC inter-promo -- tache 2.3*

	
## Livrables TD -> Mme Oliveira

Le **PMP Initial** se trouve : [/management/PMP.md](management/PMP.md)


## Équipe

 - Jérémie HUTEAU
 - Quentin MARTY
 - Pierre POMERET-COQUOT

## Version actuelle

La dernière version stable est **Itération 0 (organisation)**  
La version en cours est **Itération 1 (exécution)** (débutée le 4 février sur la [branche execution1](https://github.com/pPomCo/DC_GroupeA/tree/execution1))


## Liens annexes

 - [Drive](https://drive.google.com/drive/folders/1fA0EA_270pQEeYymY6j-n2p_zJQ6i1UI?usp=sharing)
 - [Tableau Trello](https://trello.com/b/HIFU6ivc/ue-projet)
 - [Slack](https://projetinterpr-pok6126.slack.com/)




---

# Git

Quelques rappels rapides :

	# Cloner le dépôt (enregistrer en local le dépôt distant)
	git clone git@github.com:pPomCo/DC_GroupeA.git
	
	# Actualiser le dossier local avec le contenu du dépôt distant
	git pull
	
	# Changer de branche
	git checkout <branche>
	
	# Créer une branche (ne se déplace pas)
	git branch <branche>

	# Voir l'état actuel
	git status

	# Définir les fichiers ou dossiers participant au commit
	git add <fichier1> [<fichier2> ...]

	# Définir que tous les fichiers et (sous-)dossiers du répertoire courant participeront au commit
	git add .

	# Commit (enregistre l'état actuel sur la branche courante)
	git commit -m "<message>"
	
	# Actualiser le dépôt distant avec le contenu du dossier local
	git push

On travaille sur la branche phaseN (ex: execution2), qui sera fusionnée avec master en fin d'itération.  
Normalement tout se passe bien.

Si vous voulez utiliser *merge*, *--amend*, *reset head* ou encore *-f*, merci de le faire
sur une sous-branche dont vous êtes responsable.  
Sinon, demandez au responsable de la branche :-)


	
