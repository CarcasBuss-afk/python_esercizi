# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: chiediamo all'utente una stringa. Verifichiamo se contiene solo numeri.
Se contiene solo numeri stampiamo "La stringa contiene solo numeri", altrimenti
"La stringa non contiene solo numeri" """

# Chiedi all'utente di inserire una stringa
stringa = input("Inserisci una stringa: ")

# Il metodo .isdigit() verifica se una stringa contiene SOLO numeri (cifre)
# Restituisce True se tutti i caratteri sono numeri, False altrimenti
# Il metodo .isalpha() verifica se una stringa contiene SOLO lettere
# Il metodo .isalnum() verifica se una stringa contiene SOLO lettere e numeri (no spazi o simboli)

# Verifichiamo se la stringa contiene solo numeri
if stringa.isdigit():
    print("La stringa contiene ____ numeri")
____:
    print("La stringa ___ contiene solo numeri")

""" Prova con: "12345", "abc", "123abc", "45 67" """
