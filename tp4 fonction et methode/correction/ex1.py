Ex1 # Demander à l'utilisateur de saisir une adresse IP
adresse_ip = input("Entrez une adresse IP : ")

# Vérification de format d'adresse IP
def verifie_ip(ip):
    # Vérifie s'il y a exactement trois points
    octets = ip.split(".")
    if len(octets) != 4:
        return False
    # Vérifie chaque octet
    for octet in octets:
        if not octet.isdigit(): # Vérifie que chaque octet est un nombre
            return False
        if not 0 <= int(octet) <= 255: # Vérifie que l'octet est dans la plage 0-255
            return False
    return True

# Affichage du résultat
if verifie_ip(adresse_ip):
    print("Adresse IP valide.")
else:
    print("Adresse IP invalide.")





