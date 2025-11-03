# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo a creare funzioni che lavorano con le LISTE """

# Le funzioni possono ricevere liste come parametri e:
# - Analizzarle (calcolare somma, media, minimo, massimo)
# - Modificarle
# - Restituire nuove liste
# - Restituire statistiche

# Funzione che calcola la somma degli elementi di una lista
def calcola_somma(lista):
    totale = 0
    for numero in lista:
        totale = totale + numero
    return totale

# Testiamo
numeri = [10, 20, 30, 40]
somma = calcola_somma(numeri)
print(f"Somma: {______}")

print("\n--- Separatore ---\n")

# DEFINISCI UNA FUNZIONE chiamata 'calcola_media' che prende 'lista'
# e RESTITUISCE la media: sum(lista) / len(lista)
___ calcola_media(_____):
    ______ sum(_____) / len(_____)


# Lista di voti
voti = [7, 8, 6, 9, 7, 8]

# Calcola la media
media = _____________(____)
print(f"Media voti: {_____}")

# DEFINISCI UNA FUNZIONE chiamata 'trova_massimo' che prende 'lista'
# e RESTITUISCE il valore massimo usando max(lista)




# Lista di temperature
temperature = [15, 22, 18, 25, 20]

# Trova il massimo
temp_max = ______________(___________)
print(f"Temperatura massima: {________}")

# DEFINISCI UNA FUNZIONE chiamata 'conta_positivi' che prende 'lista'
# e RESTITUISCE quanti numeri sono maggiori di 0




# Lista con numeri misti
numeri_misti = [5, -3, 8, -1, 0, 12, -7]

# Conta i positivi
positivi = ______________(_____________)
print(f"Numeri positivi: {_________}")

""" Osserva come le funzioni rendono il codice più organizzato! """
