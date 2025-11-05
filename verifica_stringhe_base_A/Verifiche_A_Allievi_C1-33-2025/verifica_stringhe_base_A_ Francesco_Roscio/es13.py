# COMPLETA IL CODICE DOVE TROVI ________ !

""" SCOPO del programma: confrontare la lunghezza di due parole inserite dall'utente """

# Chiedi all'utente di inserire la prima parola
parola1 = input("Inserisci la prima parola: ")

# Chiedi all'utente di inserire la seconda parola
parola2 = input("inserisci la seconda parola")

# Calcola la lunghezza della prima parola
lunghezza1 = len(parola1)

# Calcola la lunghezza della seconda parola
lunghezza2 = len(parola2)

# Confronta le lunghezze
if lunghezza1 > lunghezza2:
    print("La prima parola è più lunga")
else:
    print("La seconda parola è più lunga o uguale")

""" Output atteso (esempio):
Inserisci la prima parola: casa
Inserisci la seconda parola: albero
La seconda parola è più lunga o uguale
"""
