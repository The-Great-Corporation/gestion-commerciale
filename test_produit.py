from models.produit import Produit
def test_creation_produit():
    p = Produit(nom = "sucre", prix= 550.0, stock= 10)
    # verification avec assert
    assert p.nom == "sucre"
    assert p.prix == 550.0
    assert p.stock == 10
    
