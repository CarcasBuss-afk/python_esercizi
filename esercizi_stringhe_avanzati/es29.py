# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: creiamo un cifrario di Cesare con shift variabile scelto dall'utente.
Il programma deve gestire sia maiuscole che minuscole. """

# CHIEDI ALL'UTENTE UN MESSAGGIO


# CHIEDI ALL'UTENTE LO SHIFT (NUMERO DA 1 A 25)


# Convertiamo lo shift in intero
shift = int(_______)

messaggio_cifrato = ""

for carattere in messaggio:
    if carattere.______():
        codice = ord(carattere)

        # Gestiamo maiuscole (A-Z: 65-90)
        if carattere.isupper():
            nuovo_codice = codice + ______
            if nuovo_codice _ 90:
                nuovo_codice = nuovo_codice - __
            messaggio_cifrato = messaggio_cifrato + chr(__________)

        # Gestiamo minuscole (a-z: 97-122)
        else:
            nuovo_codice = codice + ______
            if nuovo_codice _ 122:
                nuovo_codice = nuovo_codice - __
            messaggio_cifrato = messaggio_cifrato + chr(__________)
    else:
        # Spazi e punteggiatura rimangono invariati
        messaggio_cifrato = messaggio_cifrato + carattere

# STAMPA IL MESSAGGIO ORIGINALE E QUELLO CIFRATO



""" Prova con diversi shift: 1, 5, 13, 25 """
