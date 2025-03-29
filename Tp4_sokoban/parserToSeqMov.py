import subprocess
import sys
import os

def run_pddl4(domain_file, problem_file, timeout, heuristic="FAST_FORWARD"):
        # Commande Java pour exécuter le solveur PDDL4J avec FAST_FORWARD
        command = [
            "java", "-cp", "./pddl4j-4.0.0.jar", "-server", "-Xms2048m", "-Xmx2048m",
            "fr.uga.pddl4j.planners.statespace.HSP",
            domain_file, problem_file, "-t", timeout, "-e", heuristic
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
    
        #print(result.stdout)
        
        #affiche que ce qui se trouve après "Found plan"   
        #print(result.stdout.split("found plan as follows:")[1].split("time spent")[0])
        
        #si trouve la solution
        
        if "found plan as follows:" in result.stdout:
            actions = result.stdout.split("found plan as follows:")[1].split("time spent")[0].strip().split("\n")
            
            #convertir les actions en une liste d'acions U-D-R-L
            mouvement=""
            
            for action in actions:
                if action.strip() != "":
                    act=action.strip().split("(")[1].split(")")[0]
                    #print(act.strip())
                    if(act.strip().startswith("moveup")):
                        mouvement += "U\n"
                    elif(act.strip().startswith("movedown")):
                        mouvement += "D\n"
                    elif(act.strip().startswith("moveright")):
                        mouvement += "R\n"
                    elif(act.strip().startswith("moveleft")):
                        mouvement += "L\n"
                    elif(act.strip().startswith("pushup")):
                        mouvement += "U\n"
                    elif(act.strip().startswith("pushdown")):
                        mouvement += "D\n"
                    elif(act.strip().startswith("pushright")):
                        mouvement += "R\n"
                    elif(act.strip().startswith("pushleft")):
                        mouvement += "L\n"
            print(mouvement)
        else:
            print("")

        problem_file_base = problem_file.rsplit("/", 1)[-1].rsplit(".pddl", 1)[0]
        output_dir = "SeqMov/"
        
        # Create the directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        with open(os.path.join(output_dir, problem_file_base), "w") as file:
            file.write(mouvement)
        
        
                
                
        

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python parserToSeqMov.py <domain_file> <problem_file> <timeout>")
    else:
        domain_file = sys.argv[1]
        problem_file = sys.argv[2]
        timeout = sys.argv[3]
        run_pddl4(domain_file, problem_file, timeout)