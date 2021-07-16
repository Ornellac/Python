# GIT

# Utilitaires possibles

- FORK (https://git-fork.com/)
- Source tree
- Smart git
- Git kraken
- GIT
- WEBSTORM / PHPSTORM / VSCODE / .. IDE

# Foctionnement de FORK 

### UNSTAGED 

Les fichiers qui se sont pas encore utilisé pour le prochain commit <br />
La vaissselle qui est en dehors du lave vaisselle
Un changement DISCARD (Edition / Suppression) est annulé (DE-FAUSSER)

### STAGED

Les fichiers qui vont etre envoyé au prochain commit <br/>
La vaisselle qui est DANS le lave vaisselle
Si un changement (FICHIER / LIGNE) est unstaged => le changement est renvoyé au dessus. Il n'est pas DISCARD

### COMMIT

Les fichiers sont "sauvegardé" en l'état du STAGED par GIT <br/>
Je lance le lave-vaisselle tel qu'il est => TOUT CE QUI EST DEDANS EST DEDANS ET DONC NON MODIFIABLE POUR LE COMMIT EN COURS

Je note sur une feuille chaque fois que je lance un lave vaisselle :
- Date et heure
- Qui l'a lancé
- Message fourni
- Contenu du lave-vaisselle

Une fois le commit effectué, la place pour un nouveau est disponible.

Dans un commit :
- Le vert représente un ajout.
- Le rouge représente une suppression.

Dans un commit(FICHIER) :
- Le plus (+) représente un ajout.
-
-

### FETCH / PULL / PUSH

- Fetch => Récuperé la liste des changements. (Sans les appliqué localement et sans téléchargement, juste apercut)
- Pull => Récupere la liste des changements et les changement -> DOWNLOAD
- Push => Pousse les commints en local sur le remote (Tire la chasse) 

### MERGE / REBASE

- Merge - Commit
- Rebase ne crée pas de commit -> Modifier l'ordre des commits

### Quelle est la procedure a suivre ?

1) Je choisis les fichiers que je veux stage
2) Une fois les fichiers stages, je les commit avec un SUJET PARLANT (QUI PERMET DE COMPRENDRE CE QUE FAIT VOTRE COMMIT)
3) Si on a encore des commit a faire -> Go 2)
4) Si on a plus de commit a faire -> On peut push mais les bonnes pratiques veulent un FETCH/PULL -> PUSH
