# TP3 pddl

### Dans le folder tower , il y a un fichier domain.pddl qui représente le tower et un problem.pddl : 4 disk sur la table de taille 1,2,3,4 on veut avoir 1 sur, 2 sur 3,3 sur 4.

### Dans le folder puzzle ,il y a un fichier domain.pddl qui représente le npuzzle et un problem.pddl 

### Nous avons fait le choix de représenter le puzzle avec des possition 1-9 et numéro 1-8 , chaque case est représenté par une possition avec un numéro si la case n'est pas empty. Pour symboliser l'action move on instaurer un prédicat d'ajacent .

### Nous avons un parser qui permet de transformer les nzpuzzle générer dans le tp précédent en un problem .pddl 

### command pour lancer le parser : python3 parser_puzzle.py 
il convertit les fichiers .txt présent dans puzzle_txt en un problem.pddl

### Pour tester, on lance le pddl4j.sh fournit sur domain.pddl et problem.pddl présent dans les fodler tower et puzzle
