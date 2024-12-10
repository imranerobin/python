MAIL = input("Entrez une adresse MAIL : ")


if MAIL.count('@') != 1:
    print("Adresse MAIL invalide : le format doit contenir 1 @ .")
else:
    valide = True
    octets = MAIL.split('@')
    
    for octet in octets:
        if len(octet) != 2:
            print(" Chaque octet doit contenir 2 caractere ")
            valide = False
            break
    
    if valide:
        print("Adresse MAC valide.")