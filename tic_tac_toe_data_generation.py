import random
import csv
import os




    

# Fonction pour afficher la grille du jeu
def afficher_grille(grille):
    print("\n")
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(grille, symbole):
    for ligne in grille:
        if all(cell == symbole for cell in ligne):
            return True
    for colonne in range(3):
        if all(grille[i][colonne] == symbole for i in range(3)):
            return True
    if all(grille[i][i] == symbole for i in range(3)) or all(grille[i][2 - i] == symbole for i in range(3)):
        return True
    return False

# Fonction pour vérifier si la grille est pleine (match nul)
def verifier_match_nul(grille):
    return all(cell != " " for ligne in grille for cell in ligne)

# Fonction pour le tour de jeu de l'ordinateur
def tour_ordinateur(grille, symbole):
    while True:
        ligne, colonne = random.randint(0, 2), random.randint(0, 2)
        if grille[ligne][colonne] == " ":
            grille[ligne][colonne] = symbole
            return ligne,colonne

# Fonction principale du jeu
def jeu_ordinateur_vs_ordinateur():
    grille = [[" " for _ in range(3)] for _ in range(3)]  # Créer une grille vide de 3x3
    ordinateur1 = "X"
    ordinateur2 = "O"

    coups = []

    print("Début du jeu entre deux ordinateurs :")
    #afficher_grille(grille)

    while True:
        ligne, colonne = tour_ordinateur(grille, ordinateur1)
        coordonnees = (ligne,colonne)
        coups.append(coordonnees[:])

        #afficher_grille(grille)

        if verifier_victoire(grille, ordinateur1):
            print(f"L'ordinateur X ({ordinateur1}) a gagné !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "win")
            break
        elif verifier_match_nul(grille):
            print("Match nul !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "draw")
            break

        ligne, colonne = tour_ordinateur(grille, ordinateur2)
        coordonnees = (ligne,colonne)
        coups.append(coordonnees[:])

        #afficher_grille(grille)

        if verifier_victoire(grille, ordinateur2):
            print(f"L'ordinateur O ({ordinateur2}) a gagné !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "loss")
            break
        elif verifier_match_nul(grille):
            print("Match nul !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "draw")
            break

    print("Fin du jeu.")

# Fonction pour enregistrer la partie dans un fichier CSV
def enregistrer_partie(coups, resultat):
    with open(chemin_fichier_csv, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(coups + [resultat])

if __name__ == "__main__":
    # Définissez le nom du fichier CSV que vous souhaitez créer
    nom_fichier_csv = "tictactoe.csv"
    # Obtenez le chemin complet du fichier CSV en utilisant os.path.join pour concaténer le dossier actuel avec le nom du fichier
    chemin_fichier_csv = os.path.join(os.path.dirname(__file__), nom_fichier_csv)

    # Vérifiez si le fichier CSV existe, sinon créez-le
    if not os.path.isfile(chemin_fichier_csv):
        with open(chemin_fichier_csv, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["MOVE1","MOVE2","MOVE3","MOVE4","MOVE5","MOVE6","MOVE7","MOVE8","MOVE9","RESULT"])

    for i in range(10000):
        jeu_ordinateur_vs_ordinateur()