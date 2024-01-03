import random
import csv
import os


# Verify if a player win
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

# Verify draw
def verifier_match_nul(grille):
    return all(cell != 0 for ligne in grille for cell in ligne)


# Turn of the bot
def tour_ordinateur(grille, symbole):
    while True:
        tableau=[]
        ligne, colonne = random.randint(0, 2), random.randint(0, 2)
        if grille[ligne][colonne] == 0:
            grille[ligne][colonne] = symbole
            #convertion 
            for i in range(3):
                for j in range(3):
                    tableau.append(grille[i][j])
            return tableau


def jeu_ordinateur_vs_ordinateur():
    grille = [[0 for _ in range(3)] for _ in range(3)]  # Créer une grille vide de 3x3
    ordinateur1 = 1
    ordinateur2 = -1
    coups = []

    # print("Début du jeu entre deux ordinateurs :")
    # afficher_grille(grille)
    while True:
        

        ###PREMIER JOUEUR###
        grille_coup1= tour_ordinateur(grille, ordinateur1)   
        coups.append(grille_coup1)
        # print (coups)

        # afficher_grille(grille)

        if verifier_victoire(grille, ordinateur1):
            # print(f"L'ordinateur X ({ordinateur1}) a gagné !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "win")
            break
        elif verifier_match_nul(grille):
            # print("Match nul !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "draw")
            break




        ### DEUXIEME JOUEUR ###
        grille_coup2 = tour_ordinateur(grille, ordinateur2)
        coups.append(grille_coup2)
        # print(coups)

        # afficher_grille(grille)

        if verifier_victoire(grille, ordinateur2):
            # print(f"L'ordinateur O ({ordinateur2}) a gagné !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "loss")
            break
        elif verifier_match_nul(grille):
            # print("Match nul !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "draw")
            break

    # print("Fin du jeu.")

# Save the game in a CSV file
def enregistrer_partie(coups, resultat):
    with open(chemin_fichier_csv, "a", newline="") as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow(coups + [resultat])


if __name__ == "__main__":
    # Define the name of the file
    nom_fichier_csv = "tictactoe.csv"
    # Obtenez le chemin complet du fichier CSV en utilisant os.path.join pour concaténer le dossier actuel avec le nom du fichier
    chemin_fichier_csv = os.path.join(os.path.dirname(__file__), nom_fichier_csv)

    # Verify if the file already exists, otherwise create it
    if not os.path.isfile(chemin_fichier_csv):
        with open(chemin_fichier_csv, "w", newline="") as file:
            writer = csv.writer(file,delimiter=";")
            writer.writerow(["MOVE1","MOVE2","MOVE3","MOVE4","MOVE5","MOVE6","MOVE7","MOVE8","MOVE9","RESULT"])

    for i in range(1000):
        jeu_ordinateur_vs_ordinateur()
    
