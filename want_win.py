import csv
import os
import pandas as pd

def extraire_victoires(chemin_entree, chemin_sortie):
    lignes_victoires = []

    with open(chemin_entree, newline='') as fichier_entree:
        lecteur_csv = csv.reader(fichier_entree,delimiter=';')
        
        # Lire l'en-tête du fichier CSV
        entete = next(lecteur_csv)

        # Trouver l'index de la colonne "RESULT"
        index_result = 9

        # Parcourir les lignes du fichier CSV
        for ligne in lecteur_csv:
            # Vérifier si la colonne "RESULT" contient "win"

            if "win" in ligne[index_result]:

                lignes_victoires.append(ligne)

    # Écrire les lignes de victoire dans un nouveau fichier CSV
    with open(chemin_sortie, mode='w', newline='') as fichier_sortie:
        ecrivain_csv = csv.writer(fichier_sortie,delimiter=';')
        
        # Écrire l'en-tête
        ecrivain_csv.writerow(entete)

        # Écrire les lignes de victoire
        ecrivain_csv.writerows(lignes_victoires)
    
def ajouter_colonne_move0(chemin_entree, chemin_sortie):
    # Charger le fichier CSV dans un DataFrame
    dataframe = pd.read_csv(chemin_entree, delimiter=';')

    # Ajouter une nouvelle colonne "MOVE 0" avec la valeur [0, 0, 0, 0, 0, 0, 0, 0, 0]
    dataframe.insert(0, "MOVE 0", '[0, 0, 0, 0, 0, 0, 0, 0, 0]')

    # Sauvegarder le DataFrame modifié dans un nouveau fichier CSV
    dataframe.to_csv(chemin_sortie, index=False, sep=';')

# Exemple d'utilisation
repertoire_courant = os.path.dirname(__file__)
nom_fichier_csv = "tictactoe.csv"
chemin_entree_csv = os.path.join(repertoire_courant, nom_fichier_csv)

nom_sortie_csv = "win_tictactoe.csv"
chemin_sortie_csv = os.path.join(repertoire_courant, nom_sortie_csv)

extraire_victoires(chemin_entree_csv, chemin_sortie_csv)
ajouter_colonne_move0(chemin_sortie_csv,chemin_sortie_csv)