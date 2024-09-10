from random import randint
 
nbr1=randint(1,10)
nbr2=randint(1,10)


print(f"L'ordinateur a généré  {nbr1} et {nbr2}: ")


somme= nbr1+nbr2

# reponse =int(input("la somme est: "))

# if reponse ==somme:
#     print("Bravo")
# else:
#     print("Vouler vous rejouer")
            
continuer = "o"

while continuer == "o":
    resultat = int(input(f"Calculer la somme de {nbr1} + {nbr2}: "))

    if resultat == somme:
         print("Bravo")
         continuer = ""
    else:
        continuer = input(f"Tapez 'o' pour continuer ou autre pour quitter:  ")