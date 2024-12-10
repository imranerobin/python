Ex3 # Demander à l'utilisateur de saisir un nom de domaine
nom_domaine = input("Entrez un nom de domaine : ")

# Vérification de format de nom de domaine
def verifie_domaine(domaine):
    # Vérifie qu'il y a au moins un point
    if "." not in domaine:
        return False
    # Sépare le nom de domaine par les points
    parties = domaine.split(".")
    # Vérifie que chaque partie (sauf la dernière) est alphanumérique
    for partie in parties[:-1]:
        if not partie.isalnum():
            return False
    # Vérifie que la dernière partie a entre 2 et 6 caractères
    if not (2 <= len(parties[-1]) <= 6):
        return False
    return True

# Affichage du résultat
if verifie_domaine(nom_domaine):
    print("Nom de domaine valide.")
else:
    print("Nom de domaine invalide.")