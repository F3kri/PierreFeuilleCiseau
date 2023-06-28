import random

a = input("citez 'pierre', 'feuille' ou 'ciseau' : ")
bot = random.randint(1, 3)

if bot == 1:
    print("l'adversaire a joué pierre !") 
elif bot == 2:
    print("l'adversaire a joué feuille !")
elif bot == 3:
    print("l'adversaire a joué ciseau !")

if a == "pierre" and bot == 1:
    print("Egalité !")
elif a == "pierre" and bot == 2:
    print("Vous avez perdu !")
elif a == "pierre" and bot == 3:
    print("Vous avez gagné !")

if a == "feuille" and bot == 1:
    print("Vous avez gagné !")
elif a == "feuille" and bot == 2:
    print("Egalité !")
elif a == "feuille" and bot == 3:
    print("Vous avez perdu !")

if a == "ciseau" and bot == 1:
    print("Vous avez perdu !")
elif a == "ciseau" and bot == 2:
    print("Vous avez gagné !")
elif a == "ciseau" and bot == 3:
    print("Egalité !")