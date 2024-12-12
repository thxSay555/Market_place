def tri_fusion_produits(produits, cle):
    
    if len(produits) <= 1:
        return produits

  
    milieu = len(produits) // 2
    moitié_gauche = produits[:milieu]
    moitié_droite = produits[milieu:]

 
    gauche_triée = tri_fusion_produits(moitié_gauche, cle)
    droite_triée = tri_fusion_produits(moitié_droite, cle)

 
    return fusion(gauche_triée, droite_triée, cle)

def fusion(gauche, droite, cle):
    liste_triée = []
    i = j = 0

    while i < len(gauche) and j < len(droite):
        if gauche[i][cle] <= droite[j][cle]:
            liste_triée.append(gauche[i])
            i += 1
        else:
            liste_triée.append(droite[j])
            j += 1


    liste_triée.extend(gauche[i:])
    liste_triée.extend(droite[j:])

    return liste_triée


produits = [
    {"nom_du_produit": "A", "prix": 10.5, "quantité": 5},
    {"nom_du_produit": "B", "prix": 7.2, "quantité": 8},
    {"nom_du_produit": "C", "prix": 15.0, "quantité": 2},
    {"nom_du_produit": "D", "prix": 3.8, "quantité": 10}
]

produits_tries_par_prix = tri_fusion_produits(produits, "prix")
produits_tries_par_quantite = tri_fusion_produits(produits, "quantité")

print("Trié par prix :", produits_tries_par_prix)
print("Trié par quantité :", produits_tries_par_quantite)
