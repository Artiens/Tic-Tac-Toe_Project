import csv
def lire_csv_et_compter(nom_fichier,recherche):
    comptage= []
    with open(nom_fichier, 'r', newline='', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv, delimiter=';')
        temp_1=0
        temp_2=0
        temp_3=0
        total=0
        
        for ligne in lecteur_csv:
            if ligne[0]==recherche:
                total+=1
                
            if ligne[0]==recherche and ligne[9]=="win" :
                temp_1+=1

            if ligne[0]==recherche and ligne[9]=="draw" :
                temp_2+=1

            if ligne[0]==recherche and ligne[9]=="loss" :
                temp_3+=1
        comptage.append(round(temp_1/total,3))
        comptage.append(round(temp_2/total,3))
        comptage.append(round(temp_3/total,3))
    return comptage

if __name__ == "__main__":
    nom_fichier="uvic/projet data/tictactoe_claire.csv"
    recherche=[(0, 0),(1, 0),(2, 0),(0, 1),(1, 1),(2, 1),(0, 2),(1, 2),(2, 2)]
    for i in range (0,9):
        comptage=lire_csv_et_compter(nom_fichier,str(recherche[i]))
        print(comptage)
    