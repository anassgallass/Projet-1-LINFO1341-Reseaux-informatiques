import sys
from scapy.all import *
from collections import Counter

# Récupérer le nom du fichier pcap en argument
if len(sys.argv) < 2:
    print("Veuillez fournir un nom de fichier pcap en argument.")
    sys.exit()
pcap_file = sys.argv[1]

# Ouvrir le fichier pcap
pkts = rdpcap(pcap_file)

# Extraire toutes les adresses IP de destination des paquets
dst_ips = []
for pkt in pkts:
    if IP in pkt:
        dst_ips.append(pkt[IP].dst)
    elif IPv6 in pkt:
        dst_ips.append(pkt[IPv6].dst)

# Résoudre les noms de domaine correspondants aux adresses IP
dst_domains = [socket.getfqdn(ip) for ip in dst_ips]

# Compter les occurrences de chaque nom de domaine
domain_counts = Counter(dst_domains)

# Afficher les résultats sous forme de tableau
print(f"\n\nRésultats pour le fichier {pcap_file}:")
print("Occurrence\tAdresses IP de destination\t\t\tNoms de domaine correspondants")
print("-"*100)
for domain, count in domain_counts.most_common():
    ip = dst_ips[dst_domains.index(domain)]
    print(f'{count}\t\t{ip: <30}\t\t{domain}')
print(f"\n\n")

