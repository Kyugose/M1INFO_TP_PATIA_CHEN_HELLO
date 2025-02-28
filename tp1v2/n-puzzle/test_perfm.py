from solve_npuzzle import (load_puzzle,
                           solve_astar,
                           solve_bfs,
                           solve_dfs,
                           is_solution,
                     )
from node import Node
import time
import os

#lance dfs bfs et astar sur tout les fichiers du dossier puzzles et compare les performances
def main():
    print('Start')
    total_dfs = 0
    total_bfs = 0
    total_astar = 0
    for file in os.listdir('puzzle'):

            puzzle = load_puzzle(f'puzzle/{file}')
            root = Node(state = puzzle, move = None)
            open = [root]
            print(f'Puzzle: {file}')
            start = time.time()
            s=solve_bfs(open)
            end = time.time()
            print(f'BFS: {end - start}')
            total_bfs += end - start
            if s:
                print('Valid solution:', is_solution(puzzle, s))
            else:
                print('No solution')
            start = time.time()
            s=solve_dfs(open)
            end = time.time()
            total_dfs += end - start
            if s:
                print('Valid solution:', is_solution(puzzle, s))
            else:
                print('No solution')
            print(f'DFS: {end - start}')
            start = time.time()
            s=solve_astar(open,[])
            end = time.time()
            total_astar += end - start
            if s:
                print('Valid solution:', is_solution(puzzle, s))
            else:
                print('No solution')
            print(f'A*: {end - start}')
            print()
    #temps total pour chaque algo
    print(f'Total BFS: {total_bfs}')
    print(f'Total DFS: {total_dfs}')
    print(f'Total A*: {total_astar}')
    
    #afficer en courbe les temps d'execution
    import matplotlib.pyplot as plt

    # Données de performance (exemple)
    algorithms = ['BFS', 'DFS', 'A*']
    performance = [total_bfs, total_dfs, total_astar]

    # Tracer la courbe de performance plusieur courbe en fonction des algorithmes
    plt.plot(algorithms, performance)

    # Ajouter des labels et un titre
    plt.xlabel('Algorithmes')
    plt.ylabel('Temps total (s)')
    plt.title('Courbe de performance des algorithmes de recherche')

    # Afficher la courbe
    plt.show()

if __name__ == '__main__':
    main()