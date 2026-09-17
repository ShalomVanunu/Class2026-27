from scapy.all import sniff, IP, TCP, Raw

def handle_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src = packet[IP].src
        dst = packet[IP].dst
        sport = packet[TCP].sport
        dport = packet[TCP].dport

        print(f"HTTP: {src}:{sport} -> {dst}:{dport}")

        if packet.haslayer(Raw):
            print(packet[Raw].load.decode(errors="replace"))
            print("-" * 60)

sniff(
    filter="tcp port 80",
    prn=handle_packet,
    store=False
)