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
telefono = input("inserisci un numero di telefono che inizia con +39")
lunghezza = len(telefono)
if telefono == lunghezza:
    print("Numero valido")
else:
    print("Numero non valido ")
