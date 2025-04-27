# TP3 PDDL

## Contenu des dossiers

### Dossier `tower`
- Contient un fichier `domain.pddl` qui représente le problème de la tour.
- Contient un fichier `problem.pddl` décrivant une configuration initiale avec 4 disques de tailles 1, 2, 3, et 4 sur la table. L'objectif est d'obtenir une pile où le disque 1 est sur le disque 2, le disque 2 sur le disque 3, et le disque 3 sur le disque 4.

### Dossier `puzzle`
- Contient un fichier `domain.pddl` qui représente le problème du puzzle.
- Contient les problem du taquin parser avec le parser `parser_puzzle.py`

Nous avons choisi de représenter le puzzle avec des positions numérotées de 1 à 9 et des numéros de tuiles de 1 à 8. Chaque case est représentée par une position et un numéro, sauf si la case est vide. Pour symboliser l'action de déplacement (`move`), nous avons introduit un prédicat `adjacent`.

## Parser pour le puzzle
- Un parser est fourni pour transformer les puzzles générés dans le TP précédent en un fichier `problem.pddl`.
- Commande pour exécuter le parser :  
    ```bash
    python3 parser_puzzle.py
    ```
    Ce script convertit les fichiers `.txt` présents dans le dossier `puzzle_txt` en un fichier `problem.pddl`.

## Test des fichiers PDDL
Pour tester, il faut utiliser le script `pddl4j.sh` fourni sur les fichiers `domain.pddl` et `problem.pddl` présents dans les dossiers `tower` et `puzzle`.
