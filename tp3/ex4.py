
# Demander à l'utilisateur d'entrer une clé Wi-Fi
cle_wifi = input("Entrez votre clé Wi-Fi (WPA/WPA2) : ")

# Vérification de la longueur et du format
if 8 <= len(cle_wifi) <= 63 and cle_wifi.isalnum():
    print("Clé Wi-Fi valide.")
else:
    print("Clé Wi-Fi invalide. Elle doit contenir entre 8 et 63 caractères alphanumériques.")
