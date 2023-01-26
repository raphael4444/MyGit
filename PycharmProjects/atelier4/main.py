# # Exercice 1
#     # Partie 1
# i = 10
#
# while i != 0:
#     i -= 1
#     print("J'aime programmer avec Python !")
#
#     # Partie 2
# liste_animaux = ["baleine","chien","chat","brebis","loup"]
# for element in liste_animaux:
#         print(element)
#
# # Exercice 2
#
# x = 0
# while x <= 10:
#     x += 1
#     print(x)
#
# input_x = int(input("Entrez un nombre svp : "))
# while input_x is not 10:
#     input_x = input("Entrez un nombre svp : ")
#     # break
#
# print("C'est gagné !")
#
# # Exercice 3
# le_nombre = 57
# nombre_input = None
# while nombre_input != le_nombre:
#     nombre_input = input("Entrez un nombre entre 0 et 100 : ")
#     if int(nombre_input) < int(le_nombre):
#         print("Le nombre est plus grand")
#     elif int(nombre_input) > int(le_nombre):
#         print("Le nombre est plus petit")
#     elif int(nombre_input) == int(le_nombre):
#         print("c'est gagné")
#         break

# Exercice 4

# longueur = int(input("Entrez une longueur : "))
# hauteur = int(input("Entrez une hauteur : "))
# symbole = str(input("Entrez le symbole : "))
#
# while hauteur != 0:
#     hauteur -= 1
#     print(symbole*longueur)

# Exercice 5

hauteur = int(input("Entrez une hauteur : "))

longueur = 1
blanc = " "

for la_hauteur in range(hauteur):
    if la_hauteur == 1:
        print("^")
    elif la_hauteur > 1:
        longueur += 2
        print("^" * longueur)





