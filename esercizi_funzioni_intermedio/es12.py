# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: validazione con condizioni multiple """

# DEFINISCI UNA FUNZIONE chiamata 'valida_password_base' che prende 'password'
# La password è valida se:
# - Lunghezza >= 8 caratteri
# - Contiene almeno una lettera maiuscola
# RESTITUISCE True se entrambe le condizioni sono vere, False altrimenti
___ valida_password_base(________):
    # Controlla lunghezza
    lunghezza_ok = len(________) __ 8

    # Controlla se c'è almeno una maiuscola
    contiene_maiuscola = False
    for carattere in ________:
        if carattere.isupper():
            contiene_maiuscola = ____
            break  # Esci dal ciclo appena ne trovi una

    # Entrambe le condizioni devono essere vere
    if lunghezza_ok ___ contiene_maiuscola:
        ______ ____
    ____:
        ______ _____


# Chiedi la password
password_utente = input("Inserisci una password: ")

# Valida
if ___________________(_________________):
    print("Password valida!")
____:
    print("Password non valida (minimo 8 caratteri e almeno una maiuscola)")

# DEFINISCI UNA FUNZIONE chiamata 'valida_codice' che prende 'codice'
# Il codice è valido se:
# - Lunghezza esattamente 6 caratteri
# - Contiene solo numeri (usa .isdigit())
# RESTITUISCE True se valido, False altrimenti




# Chiedi codice e valida
codice = input("Inserisci un codice a 6 cifre: ")

if ____________(_____):
    print("Codice valido!")
____:
    print("Codice non valido (deve essere 6 cifre)")

""" Prova con: 123456, abc123, 12345, 1234567 """
