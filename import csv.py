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




#Exportation du fichier csv:
with open("essai.csv", 'w', newline='', encoding="utf-8") as fichier:
    commerçant=csv.DictWriter(fichier, fieldnames=users[0].keys())
    commerçant.writeheader()
    commerçant.writerow(users)