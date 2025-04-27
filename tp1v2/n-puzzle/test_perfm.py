from solve_npuzzle import (
    load_puzzle,
    solve_astar,
    solve_bfs,
    solve_dfs,
    is_solution,
)
from node import Node
import time
import os
import numpy as np
import matplotlib.pyplot as plt

def main():
    print('Start')
    total_dfs = 0.0
    total_bfs = 0.0
    total_astar = 0.0

    list_time_bfs = []
    list_time_dfs = []
    list_time_astar = []

    # Parcours des fichiers de puzzle
    for file in os.listdir('puzzle'):
        if not file.endswith('.txt'):
            continue

        puzzle = load_puzzle(f'puzzle/{file}')
        max_sequence = int(int(file.split('_len')[1].split('.')[0]) / 10)
        d = int(len(puzzle) ** 0.5)

        print(f'Puzzle: {file} (dimension {d}x{d}, max_sequence {max_sequence})')

        root = Node(state=puzzle, move=None)

        # BFS
        start = time.time()
        sol_bfs = solve_bfs([root])
        duration = time.time() - start
        total_bfs += duration
        list_time_bfs.append((max_sequence, d, total_bfs))
        print(f'  BFS: {duration:.4f}s, valid: {is_solution(puzzle, sol_bfs) if sol_bfs else False}')

        # DFS
        start = time.time()
        sol_dfs = solve_dfs([root])
        duration = time.time() - start
        total_dfs += duration
        list_time_dfs.append((max_sequence, d, total_dfs))
        print(f'  DFS: {duration:.4f}s, valid: {is_solution(puzzle, sol_dfs) if sol_dfs else False}')

        # A*
        start = time.time()
        sol_astar = solve_astar([root], [])
        duration = time.time() - start
        total_astar += duration
        list_time_astar.append((max_sequence, d, total_astar))
        print(f'  A*:  {duration:.4f}s, valid: {is_solution(puzzle, sol_astar) if sol_astar else False}')

        print()

    # Affichage des totaux
    print(f'Total BFS:  {total_bfs:.4f}s')
    print(f'Total DFS:  {total_dfs:.4f}s')
    print(f'Total A*:   {total_astar:.4f}s')

    list_time_bfs.sort(key=lambda x: (x[0], x[1]))
    list_time_dfs.sort(key=lambda x: (x[0], x[1]))
    list_time_astar.sort(key=lambda x: (x[0], x[1]))

    difficulty_bfs   = [(seq * dim) // 100 * 100 for seq, dim, _ in list_time_bfs]
    difficulty_dfs   = [(seq * dim) // 100 * 100 for seq, dim, _ in list_time_dfs]
    difficulty_astar = [(seq * dim) // 100 * 100 for seq, dim, _ in list_time_astar]

    times_bfs   = [t for _, _, t in list_time_bfs]
    times_dfs   = [t for _, _, t in list_time_dfs]
    times_astar = [t for _, _, t in list_time_astar]

    cumul_bfs   = np.cumsum(times_bfs)
    cumul_dfs   = np.cumsum(times_dfs)
    cumul_astar = np.cumsum(times_astar)

    plt.figure(figsize=(10, 6))
    plt.plot(difficulty_bfs,   cumul_bfs,   label='BFS ', color='red', marker='^')
    plt.plot(difficulty_dfs,   cumul_dfs,   label='DFS ', color='blue', marker='s')
    plt.plot(difficulty_astar, cumul_astar, label='A*', color='green', marker='o')

    plt.xlabel('Difficulté (max_sequence × dimension)')
    plt.ylabel('Temps total cumulé (secondes)')
    plt.title('Courbes de temps total cumulé par algorithme')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
