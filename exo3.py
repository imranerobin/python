from random import randint
 
nbr1=randint(1,20)
nbr2=randint(1,20)
nbr_essais=0

#print(f"L'ordinateur a généré  {nbr1} et {nbr2}: ")

continuer = "o"

while continuer == "o":

    continuer = input(f"Tapez 'o' pour continuer ou autre pour quitter:  ")

    nbr1=randint(1,20)

    nbr2=randint(1,20)

    print(f"L'ordinateur a généré  {nbr1} et {nbr2}: ")

    nbr_essais +=1

    if nbr1 == nbr2:
         print("Bravo")
         print(f"vous avez fait :{nbr_essais} essais ")
         continuer = ""
    

