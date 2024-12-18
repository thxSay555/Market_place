import csv
import tkinter as tk


users=[{"id":0,"nom":"admin","prénom":None,"password":"admin","e-mail":"tkt"}
]
list_product=[
    {"nom_du_produit": "ananas", "prix": 10.5, "quantité": 5, "id_marchand":0},
    {"nom_du_produit": "bannanes", "prix": 7.2, "quantité": 8, "id_marchand":3},
    {"nom_du_produit": "pommes", "prix": 15.0, "quantité": 2, "id_marchand":5},
    {"nom_du_produit": "what the heck", "prix": 3.8, "quantité": 10, "id_marchand":0},
]




def tri_users_product():
    produits_tries={}
    for user in users:
        if nom == user["nom"]:
            for product in user["produits"]:
                sorted(product["prix"])
    return produits_tries


def recherche():
    nom_produit=input("Que recherchez vous ?(le nom exact)\n")
    for prod in list_product:
        if prod["nom_du_produit"]==nom_produit:
            print(prod)
            return prod
    print("Ce nom de produit n'est pas dans notre base de données")
    return 


def nouvel_utilisateur():
    new_id=users[-1]["id"]+1
    users.append({"id":new_id,"password":input("password \n"),"nom":input("nom \n"),"prénom":input("prénom \n"),"e-mail":input("e-mail")})
    return

def ajouter_produits():
    id=input("id, s'il vous plait \n")
    nom_prod=str(input("Comment s'appel le produits? \n"))
    prix=float(input("prix ? \n"))
    quantité=int(input("Quelle est la quantité? \n"))
    prod={"nom_du_produit":nom_prod,"prix":prix, "quantité":quantité, "id_marchand":id}
    for user in users:
        if user["id"]==id:
            list_product.append(prod)
    ajouter_encore=input("Voulez vous ajouter un autre produit? \n Oui:1\n Non:0\n")
    if ajouter_encore ==1:
        ajouter_produits()
    elif ajouter_encore==0:
        print("See u!!!")
    return

def tri_produits(id,produits):
    return

def supprimer_utilisateur(nom):
    for dic in users:
        for key in dic.keys():
            if key["nom"]==nom:
                dic.clear()
    return

def login(nom,prénom):
    for dic in users:
        for key in dic.keys():
            if key["nom"]==nom and key["prénom"]==prénom:
                pwd=input("veuillez donner votre mot de passe")
                if pwd==key("password"):
                    print("vous êtes connecté(e)")
                    return 
            else:
                print("Je sais pas qui t'es!!!")
    return




def main():
    while True:
        print("Vous avez 5 options:\n1:ajouter un produits\n2:supprimer un utilisateur\n3:ajouter un utilisateur\n4:rechercher un produit\n5:sortir du menu\n")
        choix=int(input("Il faut entrer un choix entre 1-5 \n "))
        if choix==1:
            ajouter_produits()
        elif choix==2:
            supprimer_utilisateur()
        elif choix==3:
            nouvel_utilisateur()
        elif choix==4:
            recherche()

        elif choix==5:
            print("See u!!!")
            break
            
        else:
            print("Choix invalide")


if __name__ == "__main__":
    main()


#Exportation du fichier csv:
field=["id","nom","prénom","password","e-mail"]

# Ouvrir le fichier CSV et écrire les lignes à partir des dictionnaires
with open('essai.csv', 'w', newline='') as file:
    commerçant = csv.DictWriter(file, fieldnames=field)
    commerçant.writeheader()
    commerçant.writerows(users)


