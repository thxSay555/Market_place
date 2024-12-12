import csv


users=[{"id":0,"nom":"admin","prénom":None,"password":"admin","produits":None}]
list_product=[{}]




def tri_users_product(nom):
    produits_tries={}
    for user in users:
        if nom == user["nom"]:
            for product in user["produits"]:
                sorted(product["prix"])
    return produits_tries


def recherche(*elmt):

    return


def nouvel_utilisateur(nom,prénom,password,produits):
    new_id=users[-1]["id"]+1
    users.append({"id":new_id,"password":password,"nom":nom,"prénom":prénom,"produits":produits})
    return

def ajouter_produits(id,*produits):
    for user in users:
        if user["id"]==id:
            list_product.append(produits)
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

print(users[0]["nom"])

nouvel_utilisateur("ABOU HARB","Elias","test123","Pommes, Orange, Mango")
nouvel_utilisateur("FERAH","Jassym","Sgueg","Skibidi")



def main():
    while True:
        choix=int(input("Il faut entrer un choix entre 1-4 \n "))
        if choix==1:
            ajouter_produits(id,"biscotte")
        if choix==2:
            ajouter_produits(id,"bicotte")
        if choix==3:
            ajouter_produits(id,"biscotte")
        if choix==4:
            ajouter_produits(id,"biscotte")
        else:
            print("Choix invalide")


if __name__ == "__main__":
    main()


#Exportation du fichier csv:
field=["id","nom","prénom","password","produits"]

# Ouvrir le fichier CSV et écrire les lignes à partir des dictionnaires
with open('essai.csv', 'w', newline='') as file:
    commerçant = csv.DictWriter(file, fieldnames=field)
    commerçant.writeheader()
    commerçant.writerows(users)


