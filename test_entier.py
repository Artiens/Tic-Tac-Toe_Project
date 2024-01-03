import random
import csv
import os
import json
import matplotlib.pyplot as plt
from tqdm import tqdm
import torch 
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score, log_loss
import os


class TicTacToeNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(TicTacToeNN, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        
        return x

# Paramètres du réseau
input_size = 9  # Taille de la grille de morpion (3x3)
hidden_size = 16  # Vous pouvez ajuster la taille selon vos besoins
output_size = 9  # Probabilités de jouer dans chaque case

# Instancier le réseau
net = TicTacToeNN(input_size, hidden_size, output_size)

# Définir la fonction de perte et l'optimiseur
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

input_data_test=[[0, 1, 1, 1, -1, 0, 1, -1, -1],[0, 1, 1, -1, -1, 0, 1, 0, -1],[1, 1, -1, -1, 0, 1, -1, 1, -1],[0, -1, 0, 1, 0, 1, -1, 1, -1],[1, 0, 1, -1, 0, 0, -1, 0, 0]]
float_data = [[0 for _ in range(9)] for _ in range(5)]

for i in range (5):
    for j in range (9):
        float_data[i][j]=float(input_data_test[i][j])
        
test_data=torch.tensor(float_data)

chemin_entree = "win_tictactoe.csv"
with open(chemin_entree, newline='') as fichier_entree:
    lecteur_csv = csv.reader(fichier_entree,delimiter=';')
    # Parcourir les lignes du fichier CSV
    next(lecteur_csv)
    i=0
    for ligne in lecteur_csv:
        i=i+1
        if i%362==0:
            for j in range (10):
                if j%2==0:
                    if ligne[j]!='?':    
                        bite=json.loads(ligne[j])

input_ttt=[]
output_ttt=[]

nom_fichier_csv = "win_tictactoe.csv"
chemin_entree = os.path.join(os.path.dirname(__file__), nom_fichier_csv)
with open(chemin_entree, newline='') as fichier_entree:
    lecteur_csv = csv.reader(fichier_entree,delimiter=';')
    # Parcourir les lignes du fichier CSV
    next(lecteur_csv)

    for ligne in lecteur_csv:
        for i in range (10):
            if i%2==0:
                input_ttt.append(ligne[i])
            else:
                output_ttt.append(ligne[i])

compteur=0
for i in range (len(input_ttt)):
    if input_ttt[i]!='?':
        compteur=compteur+1
ttt_input_float= [[0 for _ in range(9)] for _ in range(compteur+1)]
ttt_output_float= [[0 for _ in range(9)] for _ in range(compteur+1)]
i=0
for k in range (len(input_ttt)):
    if input_ttt[k]!='?':
        
        temp1=json.loads(input_ttt[k])
        temp2=json.loads(output_ttt[k])
        for j in range(9):
            ttt_input_float[i][j]=float(temp1[j])
            ttt_output_float[i][j]=float(temp2[j])
        i=i+1

ttt_input_tensor=torch.tensor(ttt_input_float)
ttt_output_tensor=torch.tensor(ttt_output_float)


training_history=[0 for _ in range(20)]
for epoch in tqdm(range(500)):
    # Passer les données à travers le réseau
    output = net(ttt_input_tensor)
    loss = criterion(output, ttt_output_tensor)
    # Rétropropagation et mise à jour des poids
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

X_test=torch.tensor([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
net.eval()
with torch.no_grad():
    test_outp = net(X_test)
    
rfff=torch.relu(test_outp)
ch = torch.argmax(rfff)
print(ch)

def IA_jeu(grille,symbole):
    
    gril = [element for row in grille for element in row]

    for i in range(len(gril)):        
        gril[i]=float(gril[i])
    
    grille_tensor=torch.tensor(gril)


    net.eval()
    with torch.no_grad():
        test_output = net(grille_tensor)
    ffff=torch.relu(test_output)


    
    for i in range (len(ffff)):
        if ffff[i]!=0.0 and gril[i]!=0.:
            ffff[i]=0.0
            
    ligne,colonne=999,999

    if torch.all(ffff == 0.0):
        # print("aléatoire")
        while ligne == 999 and colonne==999:
            li, col = random.randint(0, 2), random.randint(0, 2)
            if grille[li][col] == 0.0:
                ligne,colonne=li,col
    else:
        chif = torch.argmax(ffff)
        chiffre=chif.item()
        ligne = chiffre // 3
        colonne = chiffre % 3

    
    grille[ligne] [colonne]=symbole    
    sortie = [[0.0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            sortie[i][j] = grille[i][j]
    return sortie

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
    return all(cell != 0.0 for ligne in grille for cell in ligne)


# Turn of the bot
def tour_ordinateur(grille, symbole):
    while True:
        ligne, colonne = random.randint(0, 2), random.randint(0, 2)
        if grille[ligne][colonne] == 0.0:
            grille[ligne][colonne] = symbole
            sortie = [[0.0 for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    sortie[i][j] = grille[i][j]
            return sortie


# Save the game in a CSV file
def enregistrer_partie(coups, resultat):
    nom_fichier_csv = 'random_against_IA.csv'
    chemin_entree = os.path.join(os.path.dirname(__file__), nom_fichier_csv)
    with open(chemin_entree, "a", newline="") as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow(coups + [resultat])   

def jeu_ordinateur_vs_ordinateur():
    grille = [[0.0 for _ in range(3)] for _ in range(3)]  # Créer une grille vide de 3x3
    ordinateur1 = 1.0
    ordinateur2 = -1.0
    coups = []

    # print("Début du jeu entre deux ordinateurs :")
    # afficher_grille(grille)
    while True:
        

        ###PREMIER JOUEUR###
        grille_coup= IA_jeu(grille, ordinateur1)
        coups.append(grille_coup)
        # print(grille_coup1)

        if verifier_victoire(grille, ordinateur1):
            #print(f"L'ordinateur X ({ordinateur1}) a gagné !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "win")
            break
        elif verifier_match_nul(grille):
            #print("Match nul !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "draw")
            break




        ### DEUXIEME JOUEUR ###
        grille_coup = tour_ordinateur(grille, ordinateur2)
        coups.append(grille_coup)
        # print(grille_coup2)

        if verifier_victoire(grille, ordinateur2):
            #print(f"L'ordinateur O ({ordinateur2}) a gagné !")
            while(len(coups) < 9):
                coups.append("?")
            enregistrer_partie(coups, "loss")
            break
        elif verifier_match_nul(grille):
            #print("Match nul !")
            while(len(coups) <= 9):
                coups.append("?")
            enregistrer_partie(coups, "draw")
            break


# Define the name of the file
nom_fichier_csv = "random_against_IA.csv"
chemin_entree = os.path.join(os.path.dirname(__file__), nom_fichier_csv)

# Verify if the file already exists, otherwise create it
if not os.path.isfile(nom_fichier_csv):
    with open(nom_fichier_csv, "w", newline="") as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow(["MOVE1","MOVE2","MOVE3","MOVE4","MOVE5","MOVE6","MOVE7","MOVE8","MOVE9","RESULT"])

for i in range(1000):
    jeu_ordinateur_vs_ordinateur()