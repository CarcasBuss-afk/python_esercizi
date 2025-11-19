# COMPLETA IL CODICE DOVE TROVI ________ !

""" SCOPO del programma: contare quante vocali 'e' ci sono in una frase """

# Chiedi all'utente di inserire una frase
frase = input("Inserisci una frase: ")

# Converti la frase in minuscolo
frase_minuscola = frase.lower()

# Conta quante volte appare la lettera 'e'
numero_e = frase_minuscola.count("e")

# Stampa quante volte appare
print(f"La lettera 'e' appare {numero_e} volte")

""" Output atteso (esempio):
Inserisci una frase: Le persone erano entusiaste
La lettera 'e' appare 6 volte
"""
