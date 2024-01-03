import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
chemin_fichier = os.path.join(chemin_actuel, 'generative_with_the_plate.py')
chemin_fichier2 = os.path.join(chemin_actuel, 'want_win.py')
chemin_fichier3 = os.path.join(chemin_actuel, 'test_entier.py')
chemin_fichier4 = os.path.join(chemin_actuel, 'results.py')

# Appel à un fichier Python
print("Generate the dataset")
exec(open(chemin_fichier).read())
print("Getting all the win")
exec(open(chemin_fichier2).read())
print("Training the IA")
exec(open(chemin_fichier3).read())
print("Showing results")
exec(open(chemin_fichier4).read())


