import os
import csv
import matplotlib.pyplot as plt
import ast

repertoire_courant = os.path.dirname(__file__)
nom_fichier_csv = "tictactoe.csv"
chemin_entree_csv = os.path.join(repertoire_courant, nom_fichier_csv)
nb_win = 0
ligne_win = []
nb_loss= 0
ligne_loss = []
nb_draw= 0
ligne_draw = []
first_move = []

with open(chemin_entree_csv, newline='') as fichier_entree:
        lecteur_csv = csv.reader(fichier_entree,delimiter=';')
       
        entete = next(lecteur_csv)
        index_result = 9
        # Parcourir les lignes du fichier CSV
        for ligne in lecteur_csv:
            # Vérifier si la colonne "RESULT" contient "win"

            if "win" in ligne[index_result]:
                nb_win += 1
                ligne_win.append(ligne)
            if "loss" in ligne[index_result]:
                nb_loss += 1
                ligne_loss.append(ligne)
            if "draw" in ligne[index_result]:
                nb_draw += 1
                ligne_draw.append(ligne)
            first_move.append(ligne[0])

etiquettes = ['win', 'loss', 'draw']
valeurs1 = [nb_win, nb_loss, nb_draw]

nom_fichier_csv = "random_against_IA.csv"
chemin_entree_csv = os.path.join(repertoire_courant, nom_fichier_csv)

nb_win_IA = 0
ligne_win_IA = []
nb_loss_IA= 0
ligne_loss_IA = []
nb_draw_IA= 0
ligne_draw_IA = []
first_move_IA = []
with open(chemin_entree_csv, newline='') as fichier_entree:
        lecteur_csv = csv.reader(fichier_entree,delimiter=';')
        print(lecteur_csv)
        index_result = 9
        # Parcourir les lignes du fichier CSV
        for ligne in lecteur_csv:
            # Vérifier si la colonne "RESULT" contient "win"

            if "win" in ligne[index_result]:
                nb_win_IA += 1
                ligne_win_IA.append(ligne)
            if "loss" in ligne[index_result]:
                nb_loss_IA += 1
                ligne_loss_IA.append(ligne)
            if "draw" in ligne[index_result]:
                nb_draw_IA += 1
                ligne_draw_IA.append(ligne)
            first_move_IA.append(ligne[0])

etiquettes = ['win', 'loss', 'draw']
valeurs2 = [nb_win_IA, nb_loss_IA, nb_draw_IA]

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Premier graphe camembert
axs[0].pie(valeurs1, labels=etiquettes, autopct='%1.1f%%', startangle=140)
axs[0].set_title('WinRate without IA')

# Deuxième graphe camembert
axs[1].pie(valeurs2, labels=etiquettes, autopct='%1.1f%%', startangle=140)
axs[1].set_title('WinRate with IA')

# Affichage des graphes
plt.tight_layout()
plt.show()
valeurs1 = [0]*9
valeurs2 = [0]*9

categories = ["0","1","2","3","4","5","6","7","8"]
for i in first_move:
    valeurs1[ast.literal_eval(i).index(1)] += 1

for i in first_move_IA:
    valeurs2[[element for sous_liste in ast.literal_eval(i) for element in sous_liste].index(1.0)] += 1
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].bar(categories, valeurs1)
axs[1].bar(categories, valeurs2)
plt.xlabel('coordinate of the move')
plt.ylabel('quantity of first move')
axs[0].set_title('partition of the first move without IA')
axs[1].set_title('partition of the first move with IA')
plt.tight_layout()
plt.show()
