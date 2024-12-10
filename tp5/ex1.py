 # Fonction pour vérifier la validité des coordonnées GPS
def verifier_coordonnees_gps(coordonnees):
    # Liste pour stocker les indices des appareils avec des coordonnées invalides
    appareils_a_verifier = []
    
    # Boucle sur chaque paire de coordonnées (latitude, longitude)
    for index, (latitude, longitude) in enumerate(coordonnees):
        if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
            # Marque l'appareil pour vérification si les coordonnées sont invalides
            appareils_a_verifier.append(index)
    
    # Affichage du résultat
    if appareils_a_verifier:
        print("Appareils avec coordonnées invalides à vérifier :", appareils_a_verifier)
    #else:
        #print("Appareils avec coordonnées invalides à vérifier :", appareils_a_verifier)
    else:
        print("Toutes les coordonnées sont valides.")

# Exemple de données de coordonnées GPS (latitude, longitude)
coordonnees = [
    (45.0, -73.0), # Valide
    (91.0, 50.0), # Invalide
    (-45.0, 180.1), # Invalide
    (60.0, -80.0) # Valide
]

# Appel de la fonction
verifier_coordonnees_gps(coordonnees)






