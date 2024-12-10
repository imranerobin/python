import random

# Seuil critique de température
seuil_critique = 35.0

# Génération et surveillance des températures
for i in range(10):
    temperature = random.uniform(20, 40)
    print(f"Température mesurée : {temperature:.2f}°C")
    if temperature > seuil_critique:
        print("Alerte : Température critique dépassée !")