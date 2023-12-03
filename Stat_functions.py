import os
import pandas as pd

def winrate_first(data):
    data = data.iloc[:, [0, -1]]
    stock = []
    for i in range(1,10):
        cntw = 0
        cntl = 0
        cntd = 0
        for index, ligne in data.iterrows():
            if ligne['RESULT'] == 'win' and ligne['MOVE1']==i:
                cntw = cntw + 1
            if ligne['RESULT'] == 'loss' and ligne['MOVE1']==i:
                cntl = cntl + 1
            if ligne['RESULT'] == 'draw' and ligne['MOVE1']==i:
                cntd = cntd + 1
        stock.append((round(cntw/(cntw+cntl+cntd),3),round(cntl/(cntw+cntl+cntd),3),round(cntd/(cntw+cntl+cntd),3)))
    return stock
                


def winrate(data):
    win = 0
    loss = 0
    draw = 0
    for index, row in data.iloc[1:].iterrows():
        win = win + list(row).count('win')
        loss = loss + list(row).count('loss')
        draw = draw + list(row).count('draw')
    return (win/data.shape[0], loss/data.shape[0], draw/data.shape[0])


def finish(data, move):
    number_move = 0
    for index, row in data.iloc[1:].iterrows():
        
        question = list(row).count(0)
        if question == 9-move:
            number_move = number_move + 1
    return number_move/data.shape[0]

if __name__ == "__main__":
    # Define the name of the file
    nom_fichier_csv = "tictactoe.csv"
    # Obtenez le chemin complet du fichier CSV en utilisant os.path.join pour concaténer le dossier actuel avec le nom du fichier
    chemin_fichier_csv = os.path.join(os.path.dirname(__file__), nom_fichier_csv)
    with open(chemin_fichier_csv, "r", newline="") as file:
        data = pd.read_csv(chemin_fichier_csv, delimiter=';', encoding='utf-8', header=0)
        position_mapping = {
            "?" : 0,
            "(0, 0)": 1,
            "(0, 1)": 2,
            "(0, 2)": 3,
            "(1, 0)": 4,
            "(1, 1)": 5,
            "(1, 2)": 6,
            "(2, 0)": 7,
            "(2, 1)": 8,
            "(2, 2)": 9,
        }

        # Transformation des coordonnées en valeurs numériques
        for col in data.keys():
            if col != 'RESULT':
                data[col] = [position_mapping[m] if m in position_mapping else position_mapping['?'] for m in data[col]]
        # Calculate the winrate.
        win, loss, draw = winrate(data)
        print(f"The probability of winning as the first player is {win}\nThe probability of losing as the first player is {loss}\nThe probability of a draw is {draw}\n")       
        
        # Calculate the probability of a game finishing in a certain number of move.
        for n in range(5,10):
            number_move = finish(data,n)
            print(f"The probability that a game finish in {n} moves is {number_move}.\n")
        
        # Calculate the winrate of a first move.
        stock = winrate_first(data)
        print(f"{stock}")

