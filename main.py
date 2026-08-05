from  models.produit import Produit

tableau_info_produit = []
def info_produit():
        nom_produit = input("donner le nom du produit : ")
        while True:
                try:
                        prix_produit = int(input("donner le prix du produit : "))
                        break
                except ValueError:
                        print("Reesayer: Vous avez tapez un texte au lieu d'un nombre!")
        while True:
                try:
                        stock_produit = int(input("donner le stock de ce produit : "))
                        break
                except ValueError:
                        print("Reesayer: Vous avez tapez du texte au lieu d'un nombre!")
        produit = Produit(nom = nom_produit, prix = prix_produit, stock= stock_produit)
        tableau_info_produit.append(produit)            
        print(f"produit {nom_produit} ajouté avec succes!")
def afficher_tableau():
        print("-----tableau des produits présentes-----")
        for p in tableau_info_produit:
                print(f"nom du produit :  {p.nom} | prix du produit : {p.prix} | stock du produit : {p.stock}")
if __name__ == "__main__":
        info_produit()
        afficher_tableau()


        