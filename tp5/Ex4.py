def verifier_mot_de_passe():
    mot_de_passe_defini = "admin123" # Mot de passe correct prédéfini
    tentatives_restantes = 3 # Nombre de tentatives autorisées

    for tentative in range(1, tentatives_restantes + 1):
        mot_de_passe = input("Veuillez entrer le mot de passe : ")
        
        if mot_de_passe == mot_de_passe_defini:
            print("Accès autorisé !")
            return
        else:
            print("Mot de passe incorrect.")
            if tentative == tentatives_restantes:
                print("ALERTE : Accès bloqué après trois tentatives échouées.")
            else:
                print(f"Il vous reste {tentatives_restantes - tentative} tentative(s).")

# Exemple d'utilisation
verifier_mot_de_passe()
