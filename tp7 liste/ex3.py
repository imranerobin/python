blacklist = ["192.168.1.5","10.0.0.7","172.16.0.10"]

IPs_connected = ["192.168.1.1","192.168.1.5","192.168.1.10","10.0.0.7"]



IPs_suspectes =[ip for ip in blacklist ] 

print(IPs_suspectes)

print("IP suspectes détectées :")


#print(f"{}")
#print(f"{}")

print("Action suggérée : Bloquer ces IPs.")