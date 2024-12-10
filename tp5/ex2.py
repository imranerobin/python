import random
import time

# Fonction de surveillance de bande passante
def surveiller_debit(seuil, iterations=10, alertes_consecutives=3):
    alertes = 0 # Compteur d'alertes consécutives
    for i in range(iterations):
        # Génère un débit réseau aléatoire (simulé en Mbps)
        debit = random.uniform(0, 100)
        print(f"Iteration {i+1}: Débit actuel = {debit:.2f} Mbps")
        
        # Vérifie si le débit dépasse le seuil
        if debit > seuil:
            alertes += 1
            print("Débit au-dessus du seuil !")
            
            # Si le débit est au-dessus du seuil plusieurs fois de suite, déclenche une alerte
            if alertes >= alertes_consecutives:
                print("ALERTE : Débit dépassé plusieurs fois consécutivement. Limitation ou coupure de la connexion.")
                break
        else:
            # Réinitialise le compteur si le débit est dans les limites
            alertes = 0
        
        # Pause pour simuler un intervalle entre chaque mesure
        time.sleep(1)

# Paramètres de simulation
seuil_bande_passante = 50 # Seuil de bande passante autorisé en Mbps
surveiller_debit(seuil_bande_passante)