tableau_info_produit = []
def info_produit():
        nom_produit = input("donner le nom du produit : ")
        prix_produit = int(input("donner le prix du produit : "))
        stock_produit = int(input("donner le stock de ce produit : "))
        produit = {
            "nom": nom_produit,
            "prix": prix_produit,
            "stock": stock_produit
        }
        tableau_info_produit.append(produit)            
        print(f"produit {nom_produit} ajouté avec succes!")
def afficher_tableau():
        print("-----tableau des produits présentes-----")
        for i in tableau_info_produit:
                print(f"produit {i["nom"]}: prix : {i["prix"]}, stock {i["stock"]}")
info_produit()
afficher_tableau()

        