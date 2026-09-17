from scapy.all import sniff, IP, ICMP

def handle_packet(packet):
    if packet.haslayer(ICMP):
        src = packet[IP].src
        dst = packet[IP].dst
        icmp_type = packet[ICMP].type
        icmp_code = packet[ICMP].code

        print(
            f"ICMP packet: {src} -> {dst} "
            f"type={icmp_type}, code={icmp_code}"
        )

sniff(filter="icmp", prn=handle_packet, store=False)