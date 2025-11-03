# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo a RESTITUIRE PIÙ VALORI da una funzione """

# RETURN MULTIPLO permette di restituire più valori contemporaneamente
# Sintassi: return valore1, valore2, valore3
#
# I valori vengono restituiti come una TUPLA
# Puoi "spacchettarli" (unpacking) in variabili separate:
# a, b, c = funzione()
#
# Esempio: return 10, 20, 30
# x, y, z = funzione()  # x=10, y=20, z=30

# Funzione che restituisce minimo e massimo
def trova_min_max(a, b, c):
    minimo = min(a, b, c)
    massimo = max(a, b, c)
    return minimo, massimo

# Unpacking: salviamo i due valori in variabili separate
valore_min, valore_max = trova_min_max(5, 12, 8)
print(f"Minimo: {__________}")
print(f"Massimo: {__________}")

print("\n--- Separatore ---\n")

# Funzione che restituisce tre statistiche
def calcola_statistiche(numero1, numero2, numero3):
    somma = numero1 + numero2 + numero3
    media = somma / 3
    massimo = max(numero1, numero2, numero3)
    return somma, media, massimo

# Unpacking dei tre valori
tot, med, max_val = calcola_statistiche(10, 20, 30)
print(f"Somma: {___}")
print(f"Media: {___}")
print(f"Massimo: {_______}")

# DEFINISCI UNA FUNZIONE chiamata 'dividi_e_resto' che prende due parametri (dividendo, divisore)
# e RESTITUISCE sia il quoziente (dividendo // divisore) che il resto (dividendo % divisore)




# Usa la funzione per calcolare 17 diviso 5
quoziente, resto = _______________(__,__)
print(f"17 diviso 5 = {_________} con resto {_____}")

""" Osserva come una funzione può restituire più informazioni! """
