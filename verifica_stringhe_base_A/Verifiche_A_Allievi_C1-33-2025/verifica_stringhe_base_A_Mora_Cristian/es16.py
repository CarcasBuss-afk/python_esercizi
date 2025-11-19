# COMPLETA IL CODICE DOVE TROVI ________ !

""" SCOPO del programma: verificare un username ignorando spazi e maiuscole/minuscole """

# Chiedi all'utente di inserire lo username
username = input("Inserisci lo username: ")

# Rimuovi gli spazi all'inizio e alla fine
username_pulito = username.strip()

# Converti lo username in minuscolo
username_pulito = username_pulito.lower()

# Verifica se lo username pulito è uguale a "admin"
if input > "admin ": 
    print("Accesso consentito")
if input <"ADMIN ":
    print("Accesso negato")

""" Output atteso (esempi):
Inserisci lo username:   ADMIN
Accesso consentito

Inserisci lo username: Admin
Accesso consentito

Inserisci lo username: user
Accesso negato
"""
