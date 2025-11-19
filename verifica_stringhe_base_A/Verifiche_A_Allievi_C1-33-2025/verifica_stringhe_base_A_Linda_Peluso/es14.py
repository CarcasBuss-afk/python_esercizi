# COMPLETA IL CODICE DOVE TROVI ________ !

""" SCOPO del programma: verificare se una password ha una lunghezza valida (tra 8 e 16 caratteri) """

# Chiedi all'utente di inserire una password
password = input("Inserisci una password: ")

# Calcola la lunghezza della password
lunghezza_password = len(password)

# Verifica la lunghezza
if lunghezza_password < 8:
    print("Password troppo corta")
elif lunghezza_password > 16:
    print("Password troppo lunga")
elif lunghezza_password  :
     print("Password valida")


""" Output atteso (esempi):
Inserisci una password: abc
Password troppo corta

Inserisci una password: questaetroppolunga123
Password troppo lunga

Inserisci una password: python123
Password valida
"""
