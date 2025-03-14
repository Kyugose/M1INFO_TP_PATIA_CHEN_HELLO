
from npuzzle import (Solution,
                     State,
                     Move,
                     UP, 
                     DOWN, 
                     LEFT, 
                     RIGHT,
                     get_children,
                     is_goal,
                     is_solution,
                     load_puzzle,
                     create_goal,
                     make_move,
                     to_string)
from node import Node
from typing import Literal, List
import argparse
import math
import time

BFS = 'bfs'
DFS = 'dfs'
ASTAR = 'astar'

Algorithm = Literal['bfs', 'dfs', 'astar']

def solve_bfs(open : List[Node]) -> Solution:
    '''Solve the puzzle using the BFS algorithm'''
    start_time = time.time()
    dimension = int(math.sqrt(len(open[0].get_state())))
    moves = [UP, DOWN, LEFT, RIGHT]
    while open:
        current_time= time.time()
        #arreter si la solution est trop longue
        if current_time - start_time > 5:
            return []
        node = open.pop(0)
        if is_goal(node.get_state()):
            return node.get_path()
        puzzle = node.get_state()
        k = node.cost
        #print('k = ', k)
        children = get_children(puzzle, moves, dimension)
        for child in children:
            n = Node(state = child[0], move = child[1], parent = node, cost = k + 1)
            open.append(n)
            
    return []

#DFS iteratif 10 profondeur puis largeur
def solve_dfs(open: List[Node]) -> Solution:
    '''Solve the puzzle using the DFS algorithm'''
    start_time = time.time()
    dimension = int(math.sqrt(len(open[0].get_state())))
    noeud_traiter = []
    
    current_cap=10
    
    while open:
        current_time= time.time()
        #arreter si la solution est trop longue
        if current_time - start_time > 5:
            return []
        node = open.pop(0)
        if is_goal(node.get_state()):
            return node.get_path()
        noeud_traiter.append(node)
        puzzle = node.get_state()
        k = node.cost
        children = get_children(puzzle, [UP, DOWN, LEFT, RIGHT], dimension)
        for child in children:
            n = Node(state=child[0], move=child[1], parent=node, cost=k + 1)
            #afficher le puzzle
            if n not in noeud_traiter and k < current_cap:
                open.insert(0,n)
            else:
                open.append(n)
    return []

def solve_astar(open : List[Node], close : List[Node]) -> Solution:
    '''Solve the puzzle using the A* algorithm'''
    start_time = time.time()
    dimension = int(math.sqrt(len(open[0].get_state())))
    moves = [UP, DOWN, LEFT, RIGHT]
    while open:
        current_time= time.time()
        #arreter si la solution est trop longue
        if current_time - start_time > 5:
            return []
        node = open.pop(0)
        if is_goal(node.get_state()):
            return node.get_path()
        puzzle = node.get_state()
        k = node.cost
        children = get_children(puzzle, moves, dimension)
        for child in children:
            n = Node(state = child[0], move = child[1], parent = node, cost = k + 1)
            if n not in close:
                open.append(n)
        open.sort(key = lambda x: heuristic(x) + x.cost)
            
    return []

def heuristic(node : Node) -> int:
    '''Calculate the heuristic value of the puzzle'''
    #distance de manhattan entre chaque case et sa position finale
    puzzle = node.get_state()
    dimension = int(math.sqrt(len(puzzle)))
    goal = create_goal(dimension)
    h = 0
    for i in range(0, len(puzzle)):
        if puzzle[i] != goal[i]:
            #position actuelle
            x = i // dimension
            y = i % dimension
            #position finale
            x_goal = goal.index(puzzle[i]) // dimension
            y_goal = goal.index(puzzle[i]) % dimension
            #distance de manhattan
            h += abs(x - x_goal) + abs(y - y_goal)
    return h

def main():
    parser = argparse.ArgumentParser(description='Load an n-puzzle and solve it.')
    parser.add_argument('filename', type=str, help='File name of the puzzle')
    parser.add_argument('-a', '--algo', type=str, choices=['bfs', 'dfs', 'astar'], required=True, help='Algorithm to solve the puzzle')
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
    
    args = parser.parse_args()
    
    puzzle = load_puzzle(args.filename)
    
    if args.verbose:
        print('Puzzle:\n')
        print(to_string(puzzle))
    
    if not is_goal(puzzle):   
         
        root = Node(state = puzzle, move = None)
        open = [root]
        
        if args.algo == BFS:
            print('BFS\n')
            start_time = time.time()
            solution = solve_bfs(open)
            duration = time.time() - start_time
            if solution:
                print('Valid solution:', is_solution(puzzle, solution))
                print('Duration:', duration)
                #execution de la solution
                for move in solution:
                    puzzle = make_move(puzzle, move, int(math.sqrt(len(puzzle))))
                    print(to_string(puzzle))
                print('Solution:', solution)
            else:
                print('No solution')
        elif args.algo == DFS:
            print('DFS')
            start_time = time.time()
            solution = solve_dfs(open)
            #arreter si la solution est trop longue
            if len(solution) > 10:
                print('No solution')
            duration = time.time() - start_time
            if solution:
                print('Valid solution:', is_solution(puzzle, solution))
                print('Duration:', duration)
                #execution de la solution
                for move in solution:
                    puzzle = make_move(puzzle, move, int(math.sqrt(len(puzzle))))
                    print(to_string(puzzle))
                print('Solution:', solution)
                
            else:
                print('No solution')
        elif args.algo == ASTAR:
            print('A*')
            start_time = time.time()
            solution = solve_astar(open,[])
            duration = time.time() - start_time
            if solution:
                print('Valid solution:', is_solution(puzzle, solution))
                print('Duration:', duration)
                #execution de la solution
                for move in solution:
                    puzzle = make_move(puzzle, move, int(math.sqrt(len(puzzle))))
                    print(to_string(puzzle))
                print('Solution:', solution)
                    
            else:
                print('No solution')
    else:
        print('Puzzle is already solved')
    
if __name__ == '__main__':
    main()