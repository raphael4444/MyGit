# Exercice 1
#     1)
#
#
# class Voiture:
#     def __init__(self,modele,marque,prix):
#         self.modele = modele
#         self.marque = marque
#         self.prix = prix
#
#
# voiture1 = Voiture("classic","kia",15000)
#
# print(voiture1.prix)

# 2)
#
#
# class Avion:
#     def __init__(self,modele,marque,nbr_siege,distance):
#         self.modele = modele
#         self.marque = marque
#         self.nbr_siege = nbr_siege
#         self.distance = distance
#
#
# avion1 = Avion("Airbus","Boeing","3",99000)
# #
# #
# print(avion1.nbr_siege)

# Exercice 2
# class Humain:
#     def __init__(self, age, nom, prenom):
#         self.age = age
#         self.nom = nom
#         self.prenom = prenom
#
#     def modifier_prenom(self, prenom):
#         self.prenom = prenom
#
#     def grandir(self, age_en_plus):
#         self.age += age_en_plus
#
#
# moi = Humain(23, "lui", "toi")
# quelqu1 = Humain(999, "vieux", "tresvieux")
#
# print(moi.age)
# moi.modifier_prenom("raphael")
# print(moi.prenom)
# moi.grandir(6)
# print(moi.age)

# Exercice 3
# class CompteBancaire:
#     def __init__(self, numeroCompte, nom, solde):
#         self.numeroCompte = numeroCompte
#         self.nom = nom
#         self.solde = solde
#
#
#     def versement(self,montant_versement):
#         self.solde += montant_versement
#
#
#     def retrait(self,montant_retrait):
#         self.solde -= montant_retrait
#
#
#     def afficher(self):
#         print(self.solde)
#
#
# mon_compte = CompteBancaire(1560,"raphael",10000)
#
# mon_compte.afficher()
# mon_compte.versement(15000)
# mon_compte.afficher()
# mon_compte.retrait(25000)
# mon_compte.afficher()

# Exercice 4 - TODO: A faire

class Personne:
    def __init__(self,taille,poids, age):
        self.taille = taille
        self.poids = poids
        self.age = age

    def imc(self):


    def interpretation(self):

# Exercice 5