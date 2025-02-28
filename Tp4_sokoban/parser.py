import json

def parse_test_in(test_in):
    lines = test_in.strip().split('\n')
    objects = []
    init = []
    goal = []
    positions = {}
    pos_counter = 1

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            pos_name = f"p{pos_counter}"
            positions[(x, y)] = pos_name
            objects.append(pos_name)
            if char == '@':
                init.append(f"(player-at {pos_name})")
            elif char == '#':
                init.append(f"(wall-at {pos_name})")
            elif char == '.':
                goal.append(f"(goal-at {pos_name})")
            elif char == '$':
                init.append(f"(box-at {pos_name})")
            elif char == '*':
                init.append(f"(box-at {pos_name})")
                goal.append(f"(goal-at {pos_name})")
            pos_counter += 1

    return objects, init, goal

def generate_pddl_problem(title, objects, init, goal):
    pddl_problem = f"(define (problem {title.replace(' ', '-')})\n"
    pddl_problem += "  (:domain sokoban)\n"
    pddl_problem += "  (:objects\n"
    pddl_problem += "    player - player\n"
    pddl_problem += "    box - box\n"
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
    with open('/home/chene/sokoban/config/test21.json') as f:
        data = json.load(f)
    
    title = data['title']['2']
    test_in = data['testIn']
    
    objects, init, goal = parse_test_in(test_in)
    pddl_problem = generate_pddl_problem(title, objects, init, goal)
    
    with open('problem.pddl', 'w') as f:
        f.write(pddl_problem)

if __name__ == "__main__":
    main()