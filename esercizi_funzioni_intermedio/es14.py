# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: validazione password complessa con più requisiti """

# DEFINISCI UNA FUNZIONE chiamata 'valida_password_forte' che prende 'password'
# La password è forte se soddisfa TUTTI questi requisiti:
# - Lunghezza >= 10 caratteri
# - Contiene almeno una lettera maiuscola
# - Contiene almeno una lettera minuscola
# - Contiene almeno un numero
# RESTITUISCE True se forte, False altrimenti
___ valida_password_forte(________):
    # Controlla lunghezza
    if len(________) _ 10:
        ______ _____

    # Controlla requisiti caratteri
    ha_maiuscola = _____
    ha_minuscola = _____
    ha_numero = _____

    for carattere in ________:
        if carattere.isupper():
            ___________ = ____
        if carattere.islower():
            ___________ = ____
        if carattere.isdigit():
            _________ = ____

    # Devono essere tutti True
    if ___________ ___ ___________ ___ _________:
        ______ ____
    ____:
        ______ _____


# Chiedi password
password = input("Crea una password forte: ")

# Valida e dai feedback dettagliato
if _____________________(________):
    print("✓ Password forte! Ottimo lavoro!")
____:
    print("✗ Password debole. Requisiti:")
    print("  - Almeno 10 caratteri")
    print("  - Almeno una maiuscola")
    print("  - Almeno una minuscola")
    print("  - Almeno un numero")

""" Prova con: ciao, Ciao123, Password1, MiaPassword123 """
