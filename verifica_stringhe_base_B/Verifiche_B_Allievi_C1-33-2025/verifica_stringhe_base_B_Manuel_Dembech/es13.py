# COMPLETA IL CODICE DOVE TROVI ________ !

""" SCOPO del programma: verificare se la parola "online" è contenuta nella modalità del corso """

# Chiedi all'utente di inserire la modalità del corso
modalità = input("Inserisci la modalità del corso: ")

# Converti la modalità in minuscolo per il confronto
modalità_minuscola = modalità.lower()

# Verifica se "online" è contenuto nella modalità
if "online" in modalità_minuscola:
    print("Il corso è online!")
else:
    print("Il corso non è online")

""" Output atteso (esempi):
Inserisci la modalità del corso: Corso ONLINE
Il corso è online!

Inserisci la modalità del corso: Presenza
Il corso non è online
"""
