# COMPLETA IL CODICE DOVE TROVI ________ !

""" SCOPO del programma: verificare se la parola "python" è contenuta in una frase """

# Chiedi all'utente di inserire una frase
frase = input("Inserisci una frase: ")

# Converti la frase in minuscolo per il confronto
frase_minuscola = frase.lower()

# Verifica se "python" è contenuto nella frase
if  "python" in frase_minuscola:
    print("Python trovato!")
else:
    print("Python non trovato")

""" Output atteso (esempi):
Inserisci una frase: Mi piace Python
Python trovato!

Inserisci una frase: Amo programmare
Python non trovato
"""
