# Riepilogo metodi avanzati

""" SCOPO: Chiedi all'utente di inserire un URL.
L'URL è valido se:
- inizia con "http://" oppure "https://"
- finisce con ".com" oppure ".it"
Se entrambe le condizioni sono vere stampa "URL valido", altrimenti "URL non valido" """

""" Output atteso (esempi):
Inserisci un URL: https://esempio.com
URL valido

Inserisci un URL: http://sito.it
URL valido

Inserisci un URL: www.esempio.com
URL non valido

Inserisci un URL: https://sito.org
URL non valido
"""
url = input("Inserisci un URL: ")
url_minuscolo = url.lower()
if url_minuscolo.startswith ("http://") or ("https://") and url_minuscolo.endswith (".com") or (".it"):
    print("URL valido ")
else:
    print("URL non valido ")