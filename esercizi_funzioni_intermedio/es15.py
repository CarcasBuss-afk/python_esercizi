# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: validazione con messaggi di errore specifici """

# DEFINISCI UNA FUNZIONE chiamata 'valida_username_dettagliato' che prende 'username'
# RESTITUISCE una tupla (valido, messaggio):
# - Se username contiene spazi: (False, "Username non può contenere spazi")
# - Se lunghezza < 4: (False, "Username troppo corto (minimo 4 caratteri)")
# - Se lunghezza > 15: (False, "Username troppo lungo (massimo 15 caratteri)")
# - Se non inizia con una lettera: (False, "Username deve iniziare con una lettera")
# - Se tutto ok: (True, "Username valido")
___ valida_username_dettagliato(________):
    # Controlla spazi
    if " " __ ________:
        ______ _____, "Username non può contenere spazi"

    # Controlla lunghezza minima
    if len(________) _ 4:
        ______ _____, "Username troppo corto (minimo 4 caratteri)"

    # Controlla lunghezza massima
    if len(________) _ 15:
        ______ _____, "Username troppo lungo (massimo 15 caratteri)"

    # Controlla primo carattere
    if not ________[0].isalpha():
        ______ _____, "Username deve iniziare con una lettera"

    # Tutto ok
    ______ ____, "Username valido"


# Chiedi username
username = input("Scegli un username: ")

# Valida
valido, messaggio = ___________________________(________)

# Mostra risultato
if ______:
    print(f"✓ {________}")
____:
    print(f"✗ {________}")

# DEFINISCI UNA FUNZIONE chiamata 'valida_eta_dettagliato' che prende 'eta' (stringa)
# RESTITUISCE (valido, messaggio):
# - Se eta non è un numero: (False, "Età deve essere un numero")
# - Se età < 0: (False, "Età non può essere negativa")
# - Se età > 120: (False, "Età non valida")
# - Se età < 18: (False, "Devi essere maggiorenne")
# - Altrimenti: (True, "Età valida")
# Suggerimento: usa .isdigit() per controllare se è un numero




# Chiedi età e valida
eta_input = input("Inserisci la tua età: ")

valido_eta, msg_eta = ______________________(__________)

if __________:
    print(f"✓ {_______}")
____:
    print(f"✗ {_______}")

""" Prova con: mario rossi, abc, 123username, 3, -5, 150 """
