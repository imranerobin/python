Ex2 # Demander à l'utilisateur de saisir une adresse MAC
adresse_mac = input("Entrez une adresse MAC : ")

# Vérification de format d'adresse MAC
def verifie_mac(mac):
    # Sépare l'adresse par les ":"
    parties = mac.split(":")
    if len(parties) != 6:
        return False
    # Vérifie chaque partie
    for partie in parties:
        if len(partie) != 2:
            return False
        if not all(c in "0123456789ABCDEF" for c in partie): # Vérifie que chaque caractère est hexadécimal
            return False
    return True

# Affichage du résultat
if verifie_mac(adresse_mac.upper()):
    print("Adresse MAC valide.")
else:
    print("Adresse MAC invalide.")