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
    list_time_bfs = []
    list_time_dfs = []
    list_time_astar = []
    for file in os.listdir('puzzle'):

            puzzle = load_puzzle(f'puzzle/{file}')
            #obtenir le nombre sequence max pour résoudre le puzzle présent dans le nom du fichier
            max_sequence = int(int(file.split('_len')[1].split('.')[0])/10)
            print("max_sequence",max_sequence)
            root = Node(state = puzzle, move = None)
            open = [root]
            print(f'Puzzle: {file}')
            start = time.time()
            s=solve_bfs(open)
            end = time.time()
            print(f'BFS: {end - start}')
            list_time_bfs.append([end - start, max_sequence])
            total_bfs += end - start
            if s:
                print('Valid solution:', is_solution(puzzle, s))
            else:
                print('No solution')
            start = time.time()
            open = [root]
            s=solve_dfs(open)
            end = time.time()
            list_time_dfs.append([end - start, max_sequence])
            total_dfs += end - start
            if s:
                print('Valid solution:', is_solution(puzzle, s))
            else:
                print('No solution')
            print(f'DFS: {end - start}')
            start = time.time()
            open = [root]
            s=solve_astar(open,[])
            end = time.time()
            list_time_astar.append([end - start, max_sequence])
            total_astar += end - start
            if s:
                print('Valid solution:', is_solution(puzzle, s))
            else:
                print('No solution')
            print(f'A*: {end - start}')
            print()
            
    #trie les listes de temps en fonction de la sequence max
    list_time_bfs.sort(key=lambda x: x[1])
    list_time_dfs.sort(key=lambda x: x[1])
    list_time_astar.sort(key=lambda x: x[1])
    #liste des temps pour chaque sequence max
    print("Liste des temps pour chaque sequence max")
    print("BFS",list_time_bfs)
    print("DFS",list_time_dfs)
    print("A*",list_time_astar)    
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
    
    #tracer 3 courbes pour chaque algo dans une autre fenetre
    plt.figure()
    plt.plot([x[1] for x in list_time_bfs], [x[0] for x in list_time_bfs], label='BFS')
    plt.plot([x[1] for x in list_time_dfs], [x[0] for x in list_time_dfs], label='DFS')
    plt.plot([x[1] for x in list_time_astar], [x[0] for x in list_time_astar], label='A*')
    
    # Ajouter des labels et un titre
    plt.xlabel('Sequence max')
    plt.ylabel('Temps (s)')
    plt.title('Courbe de performance des algorithmes de recherche')
    plt.legend()

    # Afficher la courbe
    plt.show()


if __name__ == '__main__':
    main()