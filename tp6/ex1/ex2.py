import sys
import math

def calcul_imc():
    try:
        # Demande à l'utilisateur d'entrer sa taille en cm et son poids en kg
        taille_cm = float(input("Entrez votre taille en cm : "))
        poids_kg = float(input("Entrez votre poids en kg : "))

        # Convertit la taille en mètres pour le calcul de l'IMC
        taille_m = taille_cm / 100

        # Calcul de l'IMC
        imc = poids_kg / math.pow(taille_m, 2)
        print(f"Votre IMC est : {imc:.2f}")

        # Classification de l'IMC
        if imc < 18.5:
            print("Catégorie : Maigre")
        elif 18.5 <= imc < 25:
            print("Catégorie : Normal")
        elif 25 <= imc < 30:
            print("Catégorie : Surpoids")
        elif 30 <= imc < 35:
            print("Catégorie : Obèse")
        else:
            print("Catégorie : Très obèse")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides pour la taille et le poids.")
        sys.exit(1)

# Appel de la fonction
calcul_imc()