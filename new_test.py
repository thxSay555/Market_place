import Fonction_tri_test
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import hashlib
import requests
import pandas

#Pwned API



# Liste des utilisateurs existants
users = [{"id": 0, "nom": "admin", "prénom": None, "password": "admin", "e-mail": "tkt"}]

# Liste des produits
list_product = [
    {"nom_du_produit": "ananas", "prix": 10.5, "quantité": 5, "id_marchand": 0},
    {"nom_du_produit": "bannanes", "prix": 7.2, "quantité": 8, "id_marchand": 3},
    {"nom_du_produit": "pommes", "prix": 15.0, "quantité": 2, "id_marchand": 5},
    {"nom_du_produit": "What the heck", "prix": 3.8, "quantité": 10, "id_marchand": 0},
]

# Fonction pour vérifier si le mot de passe est compromis
def est_compromis(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url=f"https://api.pwnedpasswords.com/range/{prefix}"
    response=requests.get(url)

    if response.status_code !=200:
        raise RuntimeError(f"Error: {response.status_code}")

    found = False
    hashes = (line.split(':') for line in response.text.splitlines())
    for returned_suffix, count in hashes:
        if returned_suffix == suffix:
            print("Il claqué au sol ce mot de passe!!!\nFaut en trouver un autre.\n")
            found=True
            return False
    if not found:
        print("Très bon mot de passe!!!")
    return


# Fonction pour envoyer un e-mail d'avertissement
def envoyer_email(destinataire, sujet, message):
    msg = MIMEMultipart()
    msg['From'] = 'ilyass.boinahery.cpge@gmail.com' 
    msg['To'] = destinataire
    msg['Subject'] = sujet

    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server: 
            server.starttls()
            server.login('ilyass.boinahery.cpge@gmail.com', 'Tadjidine2')  
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print(f"E-mail envoyé à {destinataire}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")

# Fonction pour ajouter un nouvel utilisateur
def nouvel_utilisateur():
    new_id = users[-1]["id"] + 1
    password = input("password \n")
    
    # Vérification si le mot de passe est compromis
    if est_compromis(password):
        email = input("Entrez votre e-mail: \n")
        message = f"Attention, le mot de passe que vous avez choisi est compromis. Veuillez en choisir un autre."
        envoyer_email(email, "Avertissement de sécurité", message)
        print("Le mot de passe est compromis, un e-mail vous a été envoyé.")
    else:
        nom = input("nom \n")
        prénom = input("prénom \n")
        email = input("e-mail \n")
        users.append({"id": new_id, "password": password, "nom": nom, "prénom": prénom, "e-mail": email})
        print("Utilisateur ajouté avec succès.")
    return

def login():
    e_mail=input("e-mail\n")
    mot_de_passe=input("mot de passe\n")
    for dic in users:
        if dic["e-mail"] == e_mail and dic["password"] == mot_de_passe:
            print("Vous êtes connecté(e)")
            return
        else:
            print("Identifiants incorects")
            return login()

# Fonction main du code
def main():
    
    while True:
        login()
        print("Vous avez 5 options:\n1:ajouter un produit\n2:supprimer un utilisateur\n3:ajouter un utilisateur\n4:rechercher un produit\n5:sortir du menu\n")
        choix = int(input("Il faut entrer un choix entre 1-5 \n "))
        if choix == 1:
            ajouter_produits()
        elif choix == 2:
            supprimer_utilisateur()
        elif choix == 3:
            nouvel_utilisateur()
        elif choix == 4:
            recherche()
        elif choix == 5:
            print("See u!!!")
            break
        else:
            print("Choix invalide")

if __name__ == "__main__":
    main()

# Exportation du fichier CSV
field = ["id", "nom", "prénom", "password", "e-mail"]

with open('essai.csv', 'w', newline='') as file:
    commerçant = csv.DictWriter(file, fieldnames=field)
    commerçant.writeheader()
    commerçant.writerows(users)
