def saisir():
    nb= 0.0
    while nb ==0:
        nb_str = input("saisir votre moyenne")
        try:
            nb=float(nb_str)
        except:
            print("Vous n avez pas saisis une valeur numerique!")
        else:
            if nb == 0:
                print("Vous avez saisis zero")
            elif nb<0:
                print("Vous avez saisis une valeur negative!")
                nb=0.0
    return nb