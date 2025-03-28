import json

def parse_test_in(test_in):
    lines = test_in.strip().split('\n')
    objects = []
    init = []
    goal = []
    pos_counter = 1

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            pos_name = f"p{pos_counter}"
            objects.append(pos_name)
            if char == '@':
                init.append(f"(player-at p{pos_counter})")
            elif char == '#':
                init.append(f"(wall-at p{pos_counter})")
            elif char == '.':
                goal.append(f"(box-at p{pos_counter})")
            elif char == '$':
                init.append(f"(box-at p{pos_counter})")
            elif char == '*':
                init.append(f"(box-at p{pos_counter})")
                goal.append(f"(box-at p{pos_counter})")
            pos_counter += 1

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
    with open('config/test21.json') as f:
        data = json.load(f)
    
    title = data['title']['2']
    test_in = data['testIn']
    
    #afficher le terrain
    print(test_in)
    
    objects, init, goal = parse_test_in(test_in)
    pddl_problem = generate_pddl_problem(title, objects, init, goal)
    
    with open('test.pddl', 'w') as f:
        f.write(pddl_problem)

if __name__ == "__main__":
    main()