# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: validazione email con condizioni specifiche """

# DEFINISCI UNA FUNZIONE chiamata 'valida_email' che prende 'email'
# L'email è valida se:
# - Contiene esattamente un simbolo '@' (usa .count('@'))
# - Contiene almeno un punto '.' dopo la '@'
# - La lunghezza totale è >= 5 caratteri
# RESTITUISCE True se valida, False altrimenti
___ valida_email(_____):
    # Controlla lunghezza minima
    if len(_____) _ 5:
        ______ _____

    # Controlla che ci sia esattamente una '@'
    if _____.count("_") __ 1:
        ______ _____

    # Trova la posizione della '@'
    posizione_chiocciola = _____.find("_")

    # Controlla che ci sia un punto dopo la '@'
    parte_dopo_chiocciola = _____[__________________:]
    if "_" __ parte_dopo_chiocciola:
        ______ ____
    ____:
        ______ _____


# Chiedi email
email_utente = input("Inserisci la tua email: ")

# Valida
if ____________(_____________):
    print("Email valida!")
____:
    print("Email non valida")

# DEFINISCI UNA FUNZIONE chiamata 'valida_telefono' che prende 'telefono'
# Il telefono è valido se:
# - Lunghezza esattamente 10 caratteri
# - Contiene solo numeri
# - Inizia con '3' (cellulare italiano)
# RESTITUISCE True se valido, False altrimenti




# Chiedi telefono e valida
telefono = input("Inserisci il numero di telefono (10 cifre): ")

if ________________(_______):
    print("Numero valido!")
____:
    print("Numero non valido (deve essere 10 cifre che iniziano con 3)")

""" Prova con: mario@test.com, test@, 3401234567, 0612345678 """
