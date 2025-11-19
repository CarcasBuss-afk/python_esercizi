# COMPLETA IL CODICE DOVE TROVI ________ !

""" SCOPO del programma: chiedere all'utente via, numero civico e città e concatenarle """

# Chiedi all'utente di inserire il nome della via
via = input("Inserisci il nome della via: ")

# Chiedi all'utente di inserire il numero civico
numero = input("Inserisci il numero civico:")

# Crea la variabile 'indirizzo' concatenando: via + " " + numero + ", " + città
# Prima chiedi la città
citta = input("Inserisci la città:")

indirizzo = via + " " + numero + ", " + citta

# Stampa l'indirizzo
print(indirizzo)

""" Output atteso (esempio):
Inserisci il nome della via: Via Roma
Inserisci il numero civico: 42
Inserisci la città: Milano
Via Roma 42, Milano
"""
