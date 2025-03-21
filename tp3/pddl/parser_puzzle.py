#Parser pour convertir les fichiers .txt en fichiers .pddl des puzzles

import sys
import os
import re
import math
import random

#recuperer la taille du puzzle selon le nombre de numéro présents (0-8 -> 3x3, 0-15 -> 4x4, etc)
def get_size(puzzle):
    size = 0
    for line in puzzle:
        for number in line:
            size+=1
    return math.sqrt(size)-1

def parse_puzzle(file):
    #Lecture du fichier
    with open(file, 'r') as f:
        lines = f.readlines()
        
    print(lines)
    print(lines[0][0])

    size=int(get_size(lines))
    sizestring=size.__str__()
    
    print("Dimension puzzle:"+sizestring)

    #Ecriture du fichier .pddl dans le dossier puzzle    
    with open("puzzle/"+os.path.basename(file).replace(".txt", ".pddl"), 'w') as f:
        f.write("(define (problem puzzle)\n")
        f.write("(:domain puzzle)\n")
        f.write("(:objects\n")
        #ecritures des objets possitions et numéros
        for i in range(size*size):
            f.write("p"+str(i+1)+" - position\n")
        for i in range(size*size-1):
            f.write("n"+str(i+1)+" - numero\n")
        
        f.write(")\n")
        f.write("(:init\n")
        
        #ecriture du problem initial
        
        #ecriture position attribuée à chaque numéro (at position numero) 
        for i in range(lines.__len__()):
            #enlever les espaces dans lines[i]
            lines[i] = lines[i].replace(" ", "")
            for j in range(lines[i].__len__()):
                    if(lines[i][j] == "0"):
                        Videpos=j+1
                        f.write("(empty p"+str(j+1)+")\n")
                    else:
                        f.write("(at p"+str(j+1)+" n"+lines[i][j]+")\n")
       
        #ecriture des adjacences
        for i in range(size*size):
            # Vérifier l'adjacence horizontale uniquement si ce n'est pas la fin d'une ligne
            if((i+1) % size != 0 and i+1 < size*size):
                f.write("(adjacent p"+str(i+1)+" p"+str(i+2)+")\n")
            # Vérifier l'adjacence verticale
            if(i+size < size*size):
                f.write("(adjacent p"+str(i+1)+" p"+str(i+1+size)+")\n")
        
        #fermeture du init
        f.write(")\n")
        f.write("(:goal (and\n")
        
        #ecriture goal d'un goal faisable en echanger les positions de la case vide et d'une case adjacente
        #tirage aléatoire de la case adjacente à la case vide parmi les cases adjacentes 
        
        rdm=random.randint(1,4)
        if(rdm==1):
            if(Videpos+1<size*size):
                f.write("(at p"+str(Videpos)+" n"+str(Videpos+1)+")\n")
            else:
                f.write("(at p"+str(Videpos)+" n"+str(Videpos-1)+")\n")
        elif(rdm==2):
            if(Videpos-1>0):
                f.write("(at p"+str(Videpos)+" n"+str(Videpos-1)+")\n")
            else:
                f.write("(at p"+str(Videpos)+" n"+str(Videpos+1)+")\n")
        elif(rdm==3):
            if(Videpos+size<size*size):
                f.write("(at p"+str(Videpos)+" n"+str(Videpos+size)+")\n")
            else:
                f.write("(at p"+str(Videpos)+" n"+str(Videpos-size)+")\n")
        else:
            if(Videpos-size>0):
                f.write("(at p"+str(Videpos)+" n"+str(Videpos-size)+")\n")
            else:
                f.write("(at p"+str(Videpos)+" n"+str(Videpos+size)+")\n")
            
        
        #fermeture du goal
        f.write(")))\n")
        

            
        
def main():
   #pour chaque fichier .txt dans le dossier puzzle_txt
    for file in os.listdir("puzzle_txt"):
        if file.endswith(".txt"):
            parse_puzzle("puzzle_txt/"+file)

if __name__ == '__main__':
    main()