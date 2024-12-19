import tkinter as tk
from tkinter import messagebox
from Fonction_tri_test import tri_fusion_produits
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
def est_compromis(mot_de_passe):
    try:
        with open('compromised_passwords.txt', 'r') as f:
            compromised_passwords = f.read().splitlines()
        return mot_de_passe in compromised_passwords
    except FileNotFoundError:
        print("Le fichier des mots de passe compromis n'a pas été trouvé.")
        return False

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
            server.login('')  
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print(f"E-mail envoyé à {destinataire}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")

# Fonction pour ajouter un nouvel utilisateur
def nouvel_utilisateur():
    new_id = users[-1]["id"] + 1
    password = password_entry.get()
    
    # Vérification si le mot de passe est compromis
    if est_compromis(password):
        email = email_entry.get()
        message = f"Attention, le mot de passe que vous avez choisi est compromis. Veuillez en choisir un autre."
        envoyer_email(email, "Avertissement de sécurité", message)
        messagebox.showwarning("Avertissement", "Le mot de passe est compromis, un e-mail vous a été envoyé.")
    else:
        nom = nom_entry.get()
        prénom = prénom_entry.get()
        email = email_entry.get()
        users.append({"id": new_id, "password": password, "nom": nom, "prénom": prénom, "e-mail": email})
        messagebox.showinfo("Succès", "Utilisateur ajouté avec succès.")
    return

# Fonction pour quitter le programme
def quitter():
    root.quit()

# Fonction pour afficher le menu principal
def afficher_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu Principal")

    def choisir_action(choix):
        if choix == 1:
            ajouter_produits()
        elif choix == 2:
            supprimer_utilisateur()
        elif choix == 3:
            nouvel_utilisateur()
        elif choix == 4:
            recherche()
        elif choix == 5:
            quitter()

    tk.Label(menu_window, text="Vous avez 5 options:").pack()

    btn_ajouter_produit = tk.Button(menu_window, text="Ajouter un produit", command=lambda: choisir_action(1))
    btn_ajouter_produit.pack()

    btn_supprimer_utilisateur = tk.Button(menu_window, text="Supprimer un utilisateur", command=lambda: choisir_action(2))
    btn_supprimer_utilisateur.pack()

    btn_ajouter_utilisateur = tk.Button(menu_window, text="Ajouter un utilisateur", command=lambda: choisir_action(3))
    btn_ajouter_utilisateur.pack()

    btn_rechercher_produit = tk.Button(menu_window, text="Rechercher un produit", command=lambda: choisir_action(4))
    btn_rechercher_produit.pack()

    btn_quitter = tk.Button(menu_window, text="Quitter", command=lambda: choisir_action(5))
    btn_quitter.pack()

# Fonction d'ajout de produit (simplifiée pour l'exemple)
def ajouter_produits():
    print("Ajouter un produit...")
    # Implémenter l'ajout de produits ici

# Fonction de suppression d'utilisateur (simplifiée pour l'exemple)
def supprimer_utilisateur():
    print("Supprimer un utilisateur...")
    # Implémenter la suppression d'un utilisateur ici

# Fonction de recherche de produits (simplifiée pour l'exemple)
def recherche():
    print("Rechercher un produit...")
    # Implémenter la recherche de produits ici

# Fenêtre principale
root = tk.Tk()
root.title("Menu Principal")
root.geometry("300x200")

# Afficher le menu
afficher_menu()

root.mainloop()

# Exportation du fichier CSV
field = ["id", "nom", "prénom", "password", "e-mail"]

with open('essai.csv', 'w', newline='') as file:
    commerçant = csv.DictWriter(file, fieldnames=field)
    commerçant.writeheader()
    commerçant.writerows(users)
