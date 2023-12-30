import csv

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
    

# Exemple d'utilisation
chemin_entree_csv = "tictactoe/tictactoe.csv"
chemin_sortie_csv = "tictactoe/win_tictactoe.csv"
extraire_victoires(chemin_entree_csv, chemin_sortie_csv)
