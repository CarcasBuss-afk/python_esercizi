# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo il CIFRARIO DI CESARE, un antico metodo di crittografia.
Ogni lettera viene sostituita con quella che si trova N posizioni dopo nell'alfabeto. """

# ALGORITMO CIFRARIO DI CESARE
# Il cifrario di Cesare sposta ogni lettera di N posizioni nell'alfabeto.
# Esempio con shift di 3:
# A → D, B → E, C → F, ..., X → A, Y → B, Z → C
#
# Usiamo le funzioni:
# - ord(carattere) = restituisce il codice ASCII del carattere
#   Esempio: ord('A') = 65, ord('a') = 97
# - chr(codice) = restituisce il carattere dal codice ASCII
#   Esempio: chr(65) = 'A', chr(97) = 'a'
#
# Algoritmo:
# 1. Prendi ogni carattere
# 2. Se è una lettera, trova il suo codice ASCII
# 3. Aggiungi lo shift
# 4. Gestisci il "wrap around" (dopo Z torna ad A)
# 5. Converti di nuovo in carattere

messaggio = "CIAO"
shift = 3

print(f"Messaggio originale: {messaggio}")
print(f"Shift: {shift}")

messaggio_cifrato = ""

for carattere in messaggio:
    if carattere.isalpha():
        # Prendiamo il codice ASCII
        codice = ord(carattere)

        # Per le maiuscole (A-Z hanno codici 65-90)
        if carattere.isupper():
            # Spostiamo di shift posizioni
            nuovo_codice = codice + ____
            # Se superiamo 90 (Z), torniamo indietro
            if nuovo_codice > 90:
                nuovo_codice = nuovo_codice - 26
            messaggio_cifrato = messaggio_cifrato + chr(________)
    else:
        # Se non è una lettera, la lasciamo così
        messaggio_cifrato = messaggio_cifrato + carattere

print(f"Messaggio cifrato: {_________________}")

# CHIEDI ALL'UTENTE UN MESSAGGIO (SOLO MAIUSCOLE PER SEMPLICITÀ)


# Cifra il messaggio con shift 3
testo_cifrato = ""
for car in ______________:
    if car.isalpha() and car.isupper():
        nuovo = ord(car) + __
        if nuovo _ 90:
            nuovo = nuovo - __
        testo_cifrato = testo_cifrato + chr(_____)
    else:
        testo_cifrato = testo_cifrato + car

# STAMPA IL MESSAGGIO CIFRATO


""" Prova con: "PYTHON", "CIAO MONDO", "ABC" """
