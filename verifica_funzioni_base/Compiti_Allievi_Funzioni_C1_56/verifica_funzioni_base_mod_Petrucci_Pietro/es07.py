# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni con logica condizionale """

# DEFINISCI UNA FUNZIONE chiamata 'verifica_maggiorenne' che prende 'eta'
# - Se eta >= 18: stampa "Sei maggiorenne"
# - Altrimenti: stampa "Sei minorenne"
def verifica_maggiorenne(eta):
    if eta >= 18:
        print("Sei maggiorenne")
    else:
        print("Sei minorenne")


# DEFINISCI UNA FUNZIONE chiamata 'verifica_temperatura' che prende 'gradi'
# - Se gradi > 30: stampa "Fa molto caldo"
# - Se gradi >= 20: stampa "Temperatura piacevole"
# - Altrimenti: stampa "Fa freddo"
def verifica_temperatura(gradi):
    if gradi > 30:
        print("Fa molto caldo")
    elif gradi >= 20:
            print("Temperatura piacevole")
    else:
        print("Fa freddo")
# Programma principale
eta_input = input("Inserisci la tua età: ")
eta = int(eta_input)
# CHIAMA verifica_maggiorenne
verifica_maggiorenne(eta)

temp_input = input("Inserisci la temperatura: ")
gradi = int(temp_input)
# CHIAMA verifica_temperatura
verifica_temperatura(gradi)
