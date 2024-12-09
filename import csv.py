import csv
users=[{"password":"pwd","nom":"RITAL","prénom":"Reco","produits":{}},{"password":"pwd","nom":"RITAL","prénom":"Reco","produits":{}},{"password":"pwd","nom":"RITAL","prénom":"Reco","produits":{}},{"password":"pwd","nom":"RITAL","prénom":"Reco","produits":{}},{"password":"pwd","nom":"RITAL","prénom":"Reco","produits":{}}]


#Création des premieres fonctionalités:
def nouvelle_utilisateur(nom,prénom,password,produits):
    users.append({"password":password,"nom":nom,"prénom":prénom,"produits":produits})
    return

def ajouter_produits(nom_user,nom_produits):
    for dic in users:
        for k in dic.keys():
            if k("nom")==nom_user:
                k("produits")=nom_produits
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
            else:
                print("Casse-toi, je sais pas qui t'es!!!")
    return



#Exportation du fichier csv:
with open("essai.csv", 'w', newline='', encoding="utf-8") as fichier:
    commerçant=csv.DictWriter(fichier, fieldnames=users[0].keys())
    commerçant.writeheader()
    commerçant.writerow(users)