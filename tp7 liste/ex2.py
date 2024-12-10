logs = [
    ("192.168.1.1", "2024-09-12  12:15:10"),
    ("192.168.1.2", "2024-09-12  12:16:15"),
    ("192.168.1.1", "2024-09-12  12:20:20"),
    ("192.168.1.3", "2024-09-12  12:30:25"),
    ("192.168.1.1", "2024-09-12  12:35:30"),

]



nb_tentatives_connexion = logs.count("192.168.1.1")

print(f"l'addrese ip 192.168.1.1 a tenter de se connecter {nb_tentatives_connexion}")


print(" IP connectées plus de 3 fois : " )
print(f" premier connexion : {(logs[0])}")
print(f" dernier connexion : {(logs[4])}")
print(f"Nombre total de connexion unique 3")