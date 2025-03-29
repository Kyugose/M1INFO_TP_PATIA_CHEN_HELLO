import sys

def affiche_lignes(fichier):
    try:
        with open(fichier, 'r') as f:
            for ligne in f:
                print(ligne, end='')
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier}' n'existe pas.")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python afficheSeq.py <nom_du_fichier>")
    else:
        affiche_lignes(sys.argv[1])