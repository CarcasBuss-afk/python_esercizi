# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni con parametri e calcoli """

# DEFINISCI UNA FUNZIONE chiamata 'calcola_perimetro_rettangolo' che prende 'base' e 'altezza'
# e stampa "Il perimetro è: [perimetro]"
# Formula: perimetro = (base + altezza) * 2
def calcola_perimetro_rettangolo(base, altezza):
    perimetro = (base + altezza) * 2
    print(f"Il perimetro è: {perimetro}")


# DEFINISCI UNA FUNZIONE chiamata 'calcola_totale_con_iva' che prende 'prezzo' e 'iva'
# e stampa "Totale con IVA: €[totale]"
# Formula: totale = prezzo + (prezzo * iva / 100)
def calcola_totale_con_iva(prezzo, iva):
    totale = prezzo + (prezzo * iva / 100)
    print(f"Totale con IVA: €{totale}")


# Programma principale
base = int(input("Base rettangolo: "))
altezza = int(input("Altezza rettangolo: "))
# CHIAMA calcola_perimetro_rettangolo
calcola_perimetro_rettangolo(base, altezza)

prezzo = int(input("Prezzo prodotto: "))
iva = int(input("Percentuale IVA: "))
# CHIAMA calcola_totale_con_iva
calcola_totale_con_iva(prezzo, iva)
