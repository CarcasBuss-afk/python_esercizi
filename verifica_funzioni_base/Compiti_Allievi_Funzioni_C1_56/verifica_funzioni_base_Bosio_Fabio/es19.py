# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: usare return in calcoli complessi """

# DEFINISCI UNA FUNZIONE chiamata 'calcola_prezzo_finale' che prende 'prezzo' e 'sconto'
# e RESTITUISCE il prezzo finale dopo lo sconto
# Formula: prezzo_finale = prezzo - (prezzo * sconto / 100)
def calcola_prezzo_finale(prezzo, sconto):
    prezzo_finnale = prezzo - (prezzo * sconto / 100)
    return prezzo_finnale


# DEFINISCI UNA FUNZIONE chiamata 'calcola_imc' che prende 'peso' e 'altezza'
# e RESTITUISCE l'indice di massa corporea (IMC)
# Formula: imc = peso / (altezza * altezza)
def calcola_imc(peso, altezza):
    imc = peso / (altezza * altezza)
    return imc


# Programma principale
prezzo_originale = int(input("Prezzo originale: "))
percentuale_sconto = int(input("Sconto %: "))
# CHIAMA calcola_prezzo_finale
prezzo_scontato = calcola_prezzo_finale(prezzo_originale, percentuale_sconto)
print("Prezzo finale: €", prezzo_scontato)

peso_kg = int(input("Peso (kg): "))
altezza_m = float(input("Altezza (m): "))
# CHIAMA calcola_imc
imc = calcola_imc(peso_kg, altezza_m)
print("Il tuo IMC è:", imc)
