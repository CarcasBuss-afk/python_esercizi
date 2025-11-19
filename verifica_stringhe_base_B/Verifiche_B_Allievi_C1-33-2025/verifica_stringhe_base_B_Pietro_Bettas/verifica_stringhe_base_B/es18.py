# Riepilogo validazione con lunghezza e startswith

""" SCOPO: Chiedi all'utente di inserire un numero di telefono.
Il numero è valido se:
- ha una lunghezza di almeno 10 caratteri
- inizia con "+39"
Se entrambe le condizioni sono vere stampa "Numero valido", altrimenti "Numero non valido". """

""" Output atteso (esempi):
Inserisci un numero di telefono: +39 3201234567
Numero valido

Inserisci un numero di telefono: 3201234567
Numero non valido

Inserisci un numero di telefono: +39 123
Numero non valido
"""
# Scrivi il codice qui sotto
numero = input("Inserisci un numero di telefono: ")
numeri = numero.count(numero)
numero_chiave = (+39)
if numero in numero_chiave:
    print("numero valido")
elif numeri == "10":
    print("numero non valido")