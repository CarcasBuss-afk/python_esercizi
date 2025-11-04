# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni con più parametri e calcoli complessi """

# DEFINISCI UNA FUNZIONE chiamata 'calcola_tempo_viaggio' che prende 'distanza' e 'velocita'
# e stampa "Tempo di viaggio: [tempo] ore"
# Formula: tempo = distanza / velocita
def calcola_tempo_viaggio(distanza, velocita):
    tempo = distanza / velocita
    print("Tempo di viaggio:", tempo, "ore")


# DEFINISCI UNA FUNZIONE chiamata 'calcola_calorie' che prende 'peso' e 'minuti'
# e stampa "Calorie bruciate: [calorie]"
# Formula: calorie = peso * minuti * 0.05
def calcola_calorie(peso, minuti):
    calorie = peso * minuti * 0.05
    print("Calorie bruciate:", calorie)


# Programma principale
dist = int(input("Distanza (km): "))
vel = int(input("Velocità media (km/h): "))
# CHIAMA calcola_tempo_viaggio
calcola_tempo_viaggio(dist, vel)

peso = int(input("Peso corporeo (kg): "))
min_corsa = int(input("Minuti di corsa: "))
# CHIAMA calcola_calorie
calcola_calorie(peso, min_corsa)
