note = int(input("entrer votre note: "))

if note >=18:
    print("Excellent.")
elif 14<= note<18:
    print("Tres bien.")
elif 10<= note<14:
    print("Assez bien.")
elif 5<= note<10:
    print("Insuffisant")
elif note<5:
    print("Catastrophique")