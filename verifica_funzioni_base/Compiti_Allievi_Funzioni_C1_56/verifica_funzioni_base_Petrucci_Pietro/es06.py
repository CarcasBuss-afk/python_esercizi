# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni con parametro e calcoli """

# DEFINISCI UNA FUNZIONE chiamata 'calcola_area_quadrato' che prende 'lato'
# e stampa "L'area del quadrato è: [area]"
# Formula: area = lato * lato
def calcola_area_quadrato(lato):
    area = lato * lato
    print("L'area del quadrato è:", {area})


# DEFINISCI UNA FUNZIONE chiamata 'converti_euro_dollari' che prende 'euro'
# e stampa "€[euro] corrispondono a $[dollari]"
# Formula: dollari = euro * 1.1
def converti_euro_dollari(euro):
    dollari = euro * 1.1
    print(f"€ {euro},  corrispondono a $ {dollari}" )

# Programma principale
lato_input = input("Inserisci il lato del quadrato: ")
lato = int(lato_input)
# CHIAMA calcola_area_quadrato
calcola_area_quadrato(lato)

euro_input = input("Inserisci l'importo in euro: ")
dollari = int(euro_input)
# CHIAMA converti_euro_dollari
converti_euro_dollari(dollari)
