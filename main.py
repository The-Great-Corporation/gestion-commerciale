from dataclasses import dataclass
@dataclass
class Produit:
        nom : str
        prix: float
        stock: int

tableau_info_produit = []
def info_produit():
        nom_produit = input("donner le nom du produit : ")
        prix_produit = int(input("donner le prix du produit : "))
        stock_produit = int(input("donner le stock de ce produit : "))
        produit = Produit(nom = nom_produit, prix = prix_produit, stock= stock_produit)
        tableau_info_produit.append(produit)            
        print(f"produit {nom_produit} ajouté avec succes!")
def afficher_tableau():
        print("-----tableau des produits présentes-----")
        for p in tableau_info_produit:
                print(f"nom du produit :  {p.nom} | prix du produit : {p.prix} | stock du produit : {p.stock}")
info_produit()
afficher_tableau()

        