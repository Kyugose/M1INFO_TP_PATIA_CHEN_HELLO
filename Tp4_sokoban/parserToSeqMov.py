import subprocess
import sys

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
        
        actions = result.stdout.split("found plan as follows:")[1].split("time spent")[0].strip().split("\n")
        
        #convertir les actions en une liste d'acions U-D-R-L
        mouvement=""
        
        for action in actions:
            if action.strip() != "":
                act=action.strip().split("(")[1].split(")")[0]
                #print(act.strip())
                if(act.strip().startswith("moveup")):
                    mouvement += "U"
                elif(act.strip().startswith("movedown")):
                    mouvement += "D"
                elif(act.strip().startswith("moveright")):
                    mouvement += "R"
                elif(act.strip().startswith("moveleft")):
                    mouvement += "L"
                elif(act.strip().startswith("pushup")):
                    mouvement += "U"
                elif(act.strip().startswith("pushdown")):
                    mouvement += "D"
                elif(act.strip().startswith("pushright")):
                    mouvement += "R"
                elif(act.strip().startswith("pushleft")):
                    mouvement += "L"
        print(mouvement)
        
        
                
                
        

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python parserResultPddl.py <domain_file> <problem_file> <timeout>")
    else:
        domain_file = sys.argv[1]
        problem_file = sys.argv[2]
        timeout = sys.argv[3]
        run_pddl4(domain_file, problem_file, timeout)