import json
import sys
import os

def parse_test_in(test_in):
    lines = test_in.strip().split('\n')
    objects = []
    init = []
    goal = []
    pos_counter = 0
    tablepos = []
    
    
    print(lines)

    #parcourir le terrain et ajouter dans le init les positions des boites, joueurs, case vide et goal
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            pos_name = f"p{pos_counter}"
            if char == ' ':
                init.append(f"(clear p{pos_counter})")
                tablepos.append([x, y,pos_counter])
                objects.append(pos_name)
                pos_counter += 1
            if char == '@':
                init.append(f"(player-at p{pos_counter})")
                tablepos.append([x, y,pos_counter])
                objects.append(pos_name)
                pos_counter += 1
            elif char == '.':
                goal.append(f"(box-at p{pos_counter})")
                init.append(f"(clear p{pos_counter})")
                tablepos.append([x, y,pos_counter])
                objects.append(pos_name)
                pos_counter += 1
            elif char == '$':
                init.append(f"(box-at p{pos_counter})")
                tablepos.append([x, y,pos_counter])
                objects.append(pos_name)
                pos_counter += 1
            elif char == '*':
                init.append(f"(box-at p{pos_counter})")
                goal.append(f"(box-at p{pos_counter})")
                tablepos.append([x, y,pos_counter])
                objects.append(pos_name)
                pos_counter += 1
            elif char == '+':
                goal.append(f"(box-at p{pos_counter})")
                init.append(f"(player-at p{pos_counter})")
                tablepos.append([x, y,pos_counter])
                objects.append(pos_name)
                pos_counter += 1
                    
    print(tablepos)
    #table avec que x y
    tableposxy = [[x,y] for x,y,p in tablepos]
    #print(tableposxy)
    #ajouter les adjacents haut bas gauche droite
    for case in tablepos:
        if case == 0:
            continue
        else:
           x,y,p=case
           #print(x,y,p)
           if [x+1,y] in tableposxy:
               p2 = tableposxy.index([x+1,y])
               init.append(f"(adjacentdroit p{p} p{p2})")
           if [x-1,y] in tableposxy:
               p2 = tableposxy.index([x-1,y])
               init.append(f"(adjacentgauche p{p} p{p2})")
           if [x,y+1] in tableposxy:
               p2 = tableposxy.index([x,y+1])
               init.append(f"(adjacenthaut p{p} p{p2})")
           if [x,y-1] in tableposxy:
               p2 = tableposxy.index([x,y-1])
               init.append(f"(adjacentbas p{p} p{p2})")
    #print(init)

    return objects, init, goal

def generate_pddl_problem(title, objects, init, goal):
    pddl_problem = f"(define (problem {title.replace(' ', '-')})\n"
    pddl_problem += "  (:domain sokoban)\n"
    pddl_problem += "  (:objects\n"
    pddl_problem += "    " + " ".join(objects) + " - position\n"
    pddl_problem += "  )\n"
    pddl_problem += "  (:init\n"
    pddl_problem += "    " + "\n    ".join(init) + "\n"
    pddl_problem += "  )\n"
    pddl_problem += "  (:goal\n"
    pddl_problem += "    (and\n"
    pddl_problem += "      " + "\n      ".join(goal) + "\n"
    pddl_problem += "    )\n"
    pddl_problem += "  )\n"
    pddl_problem += ")"
    return pddl_problem

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 parserToPddl.py <path_to_testX.json>")
        sys.exit(1)
        
    json_file = sys.argv[1]
    with open(json_file) as f:
            data = json.load(f)
            
    
    title = data['title']['2']
    test_in = data['testIn']
    
    #afficher le terrain
    print(test_in)
    
    objects, init, goal = parse_test_in(test_in)
    pddl_problem = generate_pddl_problem(title, objects, init, goal)
    
    #store le fichier pddl en testX.pddl avec le testX de l'argument
    
    nom=json_file.split(".")[0].split("/")[-1]
    
    # écrire le fichier pddl dans le répertoire "problems"
    output_dir = "problemPDDL/"
    output_path = output_dir + nom + ".pddl"
    
    # créer le répertoire s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)
    
    # écrire le fichier PDDL
    with open(output_path, 'w') as f:
        f.write(pddl_problem)
    
    print(f"PDDL problem file written to: {output_path}")

if __name__ == "__main__":
    main()