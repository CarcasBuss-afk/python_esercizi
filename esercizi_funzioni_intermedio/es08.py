# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo a far CHIAMARE UNA FUNZIONE DA UN'ALTRA FUNZIONE """

# COMPOSIZIONE = una funzione usa il risultato di un'altra funzione
# Questo rende il codice più modulare e organizzato
#
# Esempio:
# def funzione_a():
#     return 10
#
# def funzione_b():
#     valore = funzione_a()  # Chiamo funzione_a da dentro funzione_b
#     return valore * 2

# Funzione che calcola il quadrato
def calcola_quadrato(numero):
    return numero * numero

# Funzione che calcola il doppio
def calcola_doppio(numero):
    return numero * 2

# Funzione che usa le altre due funzioni
def calcola_quadrato_del_doppio(numero):
    doppio = calcola_doppio(numero)  # Prima chiamo calcola_doppio
    risultato = calcola_quadrato(doppio)  # Poi uso il risultato in calcola_quadrato
    return risultato

# Testiamo
valore = calcola_quadrato_del_doppio(5)
print(f"Quadrato del doppio di 5: {______}")
# 5 → doppio = 10 → quadrato di 10 = 100

print("\n--- Separatore ---\n")

# DEFINISCI UNA FUNZIONE chiamata 'converti_in_minuscolo' che prende 'testo'
# e RESTITUISCE testo.lower()
___ converti_in_minuscolo(_____):
    ______ _____.lower()


# DEFINISCI UNA FUNZIONE chiamata 'conta_caratteri' che prende 'testo'
# e RESTITUISCE len(testo)
___ conta_caratteri(_____):
    ______ len(_____)


# DEFINISCI UNA FUNZIONE chiamata 'analizza_testo' che prende 'testo'
# - Chiama converti_in_minuscolo(testo) e salva il risultato
# - Chiama conta_caratteri sul testo convertito
# - Stampa "Testo in minuscolo: [testo_minuscolo]"
# - Stampa "Numero caratteri: [lunghezza]"
___ analizza_testo(_____):
    testo_minuscolo = _____________________(_____)
    lunghezza = _______________(________________)
    print(f"Testo in minuscolo: {_______________}")
    print(f"Numero caratteri: {_________}")


# Testiamo
analizza_testo("CIAO Mondo")

""" Osserva come le funzioni lavorano insieme! """
