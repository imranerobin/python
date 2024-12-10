packets = [
    (500, "TCP"),
    (1000, "UDP"),
    (2000, "TCP"),
    (50, "ICMP"),
    (1600, "TCP"),
    (800, "UDP")
]

large_packets = [packet for packet in packets if packet[0]>1500]
for packet in large_packets:
    print(packet)



    