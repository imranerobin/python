 # Demander à l'utilisateur de créer un mot de passe
mot_de_passe = input("Définissez votre mot de passe : ")

# Compteur de tentatives
tentatives = 0
max_tentatives = 3

# Boucle pour les tentatives de connexion
while tentatives < max_tentatives:
    mot_de_passe_tentative = input("Entrez votre mot de passe : ")
    if mot_de_passe_tentative == mot_de_passe:
        print("Connexion réussie !")
        break
    else:
        tentatives += 1
        print("Mot de passe incorrect.")

# Vérification si les tentatives sont épuisées
if tentatives == max_tentatives:
    print("Accès refusé après trop de tentatives.")