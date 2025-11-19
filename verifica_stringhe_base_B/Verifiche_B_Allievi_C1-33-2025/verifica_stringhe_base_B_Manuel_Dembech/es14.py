# COMPLETA IL CODICE DOVE TROVI ________ !

""" SCOPO del programma: chiedere una parola chiave e verificare se è nella descrizione del prodotto """

# Chiedi all'utente di inserire una descrizione del prodotto
descrizione = input("Inserisci la descrizione del prodotto: ")

# Chiedi all'utente la parola chiave da cercare
parola_chiave = input("Inserisci la parola chiave: ")

# Converti entrambe in minuscolo
descrizione_minuscola = descrizione.lower()
parola_minuscola = parola_chiave.lower()

# Verifica se la parola chiave è contenuta nella descrizione
if parola_minuscola in descrizione_minuscola:
    print("Parola chiave trovata!")
else:
    print("Parola chiave non trovata")

""" Output atteso (esempi):
Inserisci la descrizione del prodotto: Smartphone con fotocamera
Inserisci la parola chiave: FOTOCAMERA
Parola chiave trovata!

Inserisci la descrizione del prodotto: Tablet Android
Inserisci la parola chiave: Apple
Parola chiave non trovata
"""
