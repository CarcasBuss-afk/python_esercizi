# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: usare i valori restituiti dalle funzioni """

# DEFINISCI UNA FUNZIONE chiamata 'calcola_area_cerchio' che prende 'raggio'
# e RESTITUISCE l'area (raggio * raggio * 3.14)
def calcola_area_cerchio(raggio):
    area = raggio * raggio * 3.14
    return area


# DEFINISCI UNA FUNZIONE chiamata 'converti_minuti_ore' che prende 'minuti'
# e RESTITUISCE le ore (minuti / 60)
def converti_minuti_ore(minuti):
    ore = minuti / 60
    return ore                       

# Programma principale
r = int(input("Raggio del cerchio: "))
# CHIAMA calcola_area_cerchio e salva in 'area'
areacerchio = calcola_area_cerchio(r)
print(f"L'area del cerchio è: {areacerchio}")

m = int(input("Minuti: "))
# CHIAMA converti_minuti_ore e salva in 'ore'
minuts = converti_minuti_ore(m)
print(m, "minuti corrispondono a", minuts, "ore")
