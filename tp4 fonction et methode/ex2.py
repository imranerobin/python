MAC = input("Entrez une adresse MAC : ")

# Vérification de la présence de trois points
if MAC.count(':') != 5:
    print("Adresse MAC invalide : le format doit contenir 6 octets séparés par des : .")
else:
    valide = True
    octets = MAC.split(':')
    
    for octet in octets:
        if len(octet) != 2:
            print(" Chaque octet doit contenir 2 caractere ")
            valide = False
            break

    for caractere in octet:
        if caractere.lower() not in "abcdef0123456789":
            print(f"{caractere} n'est pas un caractère hexadécimal valide")
            break



    if valide:
        print("Adresse MAC valide.")