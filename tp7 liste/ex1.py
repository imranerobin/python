packets = [
    (500, "TCP"),
    (1000, "UDP"),
    (2000, "TCP"),
    (50, "ICMP"),
    (1600, "TCP"),
    (800, "UDP")
]

#for element in packets:
#    print({element})
 


print("paquets qui dépassent 1500 octet:")

large_packets = [packet for packet in packets if packet[0]>1500]
for packet in large_packets:
    print(packet)
 
#large_paquets_detected = any(paquets> 1500 for paquets in packets)
#print(large_paquets_detected)



#print(packets[2])
#print(packets[4])
