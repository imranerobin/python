 # Demander à l'utilisateur de saisir une adresse email
adresse_email = input("Entrez une adresse email : ")

# Vérification de format d'adresse email
def verifie_email(email):
    # Vérifie qu'il y a exactement un symbole "@"
    if email.count("@") != 1:
        return False
    # Sépare l'adresse email en deux parties : avant et après le "@"
    partie_locale, domaine = email.split("@")
    # Vérifie qu'il y a un point dans la partie du domaine
    if "." not in domaine:
        return False
    # Vérifie que le domaine se termine par au moins 2 caractères
    extension = domaine.split(".")[-1]
    if len(extension) < 2:
        return False
    return True

# Affichage du résultat
if verifie_email(adresse_email):
    print("Adresse email valide.")
else:
    print("Adresse email invalide.")
