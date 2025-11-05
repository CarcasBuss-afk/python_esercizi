# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni con un parametro """

# DEFINISCI UNA FUNZIONE chiamata 'saluta_studente' che prende 'nome'
# e stampa "Ciao [nome], benvenuto al corso!"
def saluta_studente(nome_utente):
    print(f"Ciao", nome_utente, ", benvenuto al corso!")


# DEFINISCI UNA FUNZIONE chiamata 'calcola_doppio' che prende 'numero'
# e stampa il doppio del numero
# Formula: doppio = numero * 2
def calcola_doppio(numero_utente):
    doppio = numero_utente * 2
    print(f"Il doppio è:", doppio)


# Programma principale
nome_utente = input("Inserisci il tuo nome: ")
# CHIAMA saluta_studente passando nome_utente
saluta_studente(nome_utente)

numero_utente = input("Inserisci un numero: ")
numero_int = int(numero_utente)  # Convertiamo in intero
# CHIAMA calcola_doppio passando numero_int
calcola_doppio(numero_int)