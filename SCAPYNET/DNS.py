from scapy.all import sniff, DNS, DNSQR, IP

def show_dns(packet):
    if packet.haslayer(DNS) and packet.haslayer(DNSQR):
        query = packet[DNSQR].qname.decode("utf-8", errors="ignore").rstrip(".")

        if packet.haslayer(IP):
            src = packet[IP].src
            dst = packet[IP].dst
            print(f"{src} -> {dst}   DNS Query: {query}")

print("Sniffing DNS queries... Press Ctrl+C to stop.")

sniff(
    filter="udp port 53 or tcp port 53",
    prn=show_dns,
    store=False
)