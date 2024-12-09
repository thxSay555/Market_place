import csv
users=[{"password":"pwd","nom":"RITAL","prénom":"Reco","produits":{}},{"password":"pwd","nom":"RITAL","prénom":"Reco","produits":{}},{"password":"pwd","nom":"RITAL","prénom":"Reco","produits":{}}]


#Création des premieres fonctionalités:
def nouvel_utilisateur(nom,prénom,password,produits):
    users.append({"password":password,"nom":nom,"prénom":prénom,"produits":produits})
    return

def ajouter_produits(nom_user,nom_produits):
    for dic in users:
        for k in dic.keys():
            if k("nom")==nom_user:
                k["produits"]=nom_produits
    return

def supprimer_utilisateur(nom):
    for dic in users:
        for key in dic.keys():
            if key("nom")==nom:
                dic.clear()
    return

def login(nom,prénom):
    for dic in users:
        for key in dic.keys():
            if key("nom")==nom and key("prénom")==prénom:
                pwd=input("veuillez donner votre mot de passe")
                if pwd==key("password"):
                    print("vous êtes connecté(e)")
                    return 
            else:
                print("Casse-toi, je sais pas qui t'es!!!")
    return


#Exportation du fichier csv:
field=["password","nom","prénom","produits"]

# Ouvrir le fichier CSV et écrire les lignes à partir des dictionnaires
with open('essai.csv', 'w', newline='') as file:
    commerçant = csv.DictWriter(file, fieldnames=field)
    commerçant.writeheader()  # Écrit l'en-tête avec les noms des champs
    commerçant.writerows(users)