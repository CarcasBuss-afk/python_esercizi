# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" MINI-PROGETTO: Analizzatore di Testo
Combina: stringhe, liste, return multiplo, statistiche """

# DEFINISCI UNA FUNZIONE chiamata 'conta_parole' che prende 'testo'
# e RESTITUISCE il numero di parole (usa .split())
___ conta_parole(_____):
    parole = _____.split()
    ______ len(______)


# DEFINISCI UNA FUNZIONE chiamata 'conta_caratteri_dettagliato' che prende 'testo'
# e RESTITUISCE (totale_caratteri, caratteri_senza_spazi, solo_spazi)
___ conta_caratteri_dettagliato(_____):
    totale = len(_____)
    senza_spazi = len(_____.replace(" ", ""))
    solo_spazi = totale - ___________
    ______ ______, ___________, __________


# DEFINISCI UNA FUNZIONE chiamata 'conta_vocali_consonanti' che prende 'testo'
# e RESTITUISCE (numero_vocali, numero_consonanti)
___ conta_vocali_consonanti(_____):
    testo_minuscolo = _____.lower()
    vocali = _
    consonanti = _

    for carattere in ______________:
        if carattere.isalpha():
            if carattere __ "aeiou":
                ______ = ______ + _
            ____:
                __________ = __________ + _

    ______ ______, __________


# DEFINISCI UNA FUNZIONE chiamata 'trova_parola_piu_lunga' che prende 'testo'
# e RESTITUISCE la parola più lunga
___ trova_parola_piu_lunga(_____):
    parole = _____.split()
    if len(______) == 0:
        ______ ""

    parola_lunga = ______[0]
    for parola in ______:
        if len(______) > len(____________):
            ____________ = ______

    ______ ____________


# DEFINISCI UNA FUNZIONE chiamata 'genera_report' che prende 'testo'
# e stampa un report completo usando TUTTE le funzioni sopra
___ genera_report(_____):
    print("=== ANALISI TESTO ===\n")
    print(f"Testo analizzato:\n{_____}\n")

    # Usa le funzioni per ottenere i dati
    num_parole = ____________(_____)
    tot_car, car_senza_spazi, spazi = ___________________________(_____)
    vocali, consonanti = _______________________(_____)
    parola_lunga = ______________________(_____)

    # STAMPA tutte le statistiche



    print(f"\nNumero di parole: {__________}")
    print(f"Caratteri totali: {_______}")
    print(f"Caratteri senza spazi: {_______________}")
    print(f"Solo spazi: {______}")
    print(f"Vocali: {______}")
    print(f"Consonanti: {__________}")
    print(f"Parola più lunga: {____________}")


# Programma principale
print("=== ANALIZZATORE DI TESTO ===\n")

# Chiedi all'utente di inserire un testo (può essere multilinea)
testo_utente = input("Inserisci un testo da analizzare:\n")

# Genera il report
_____________(______________)

""" Prova con testi diversi, brevi e lunghi! """
