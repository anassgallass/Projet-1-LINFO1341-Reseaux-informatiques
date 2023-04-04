# 2. Couche réseau

Le code script.py utilise la bibliothèque Scapy pour analyser un fichier de capture de paquets (fichier pcap) et extraire les adresses IP de destination de chaque paquet. Ensuite, il résout les noms de domaine correspondants aux adresses IP à l'aide de la fonction "getfqdn" de la bibliothèque socket. Le script utilise ensuite la classe Counter pour compter le nombre d'occurrences de chaque nom de domaine. Enfin, le script affiche les résultats sous forme de tableau, triés par ordre décroissant d'occurrences. Chaque ligne du tableau indique le nombre d'occurrences, l'adresse IP correspondante et le nom de domaine.

Par exemple, supposons que le nom du fichier pcap soit "capture.pcap" et que les noms de domaine suivants ont été extraits et comptés :

- example.com : 50 occurrences
- google.com : 25 occurrences
- facebook.com : 10 occurrences

L'exécution du script afficherait un tableau comme suit :

Résultats pour le fichier capture.pcap:
| Occurrence | Adresses IP de destination | Noms de domaine correspondants |
| --- | --- | --- |
| 50 | 192.0.2.1 | example.com |
| 25 | 172.217.3.14 | google.com |
| 10 | 31.13.66.35 | facebook.com |


Pour faire tourner le code, il suffit d'intégrer les fichiers pcap dans le dossier courant et d'exécuter depuis le terminal la commande suivante :  
```bash
sh script.sh
```
