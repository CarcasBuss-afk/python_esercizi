# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni che restituiscono un valore con return """

# DEFINISCI UNA FUNZIONE chiamata 'calcola_triplo' che prende 'numero'
# e RESTITUISCE il triplo del numero (numero * 3)
def calcola_triplo(numero):
    triplo = numero * 3
    return triplo


# DEFINISCI UNA FUNZIONE chiamata 'unisci_nomi' che prende 'nome' e 'cognome'
# e RESTITUISCE nome e cognome uniti (es. "Mario Rossi")
def unisci_nomi(nome, cognome):
    nome_completo = nome + " " + cognome
    return nome_completo


# Programma principale
num = int(input("Inserisci un numero: "))
# CHIAMA calcola_triplo e salva il risultato in 'risultato'
risultato = calcola_triplo(num)
print("Il triplo è:", risultato)

nome_input = input("Nome: ")
cognome_input = input("Cognome: ")
# CHIAMA unisci_nomi e salva il risultato in 'nome_completo'
nome_completo = unisci_nomi(nome_input, cognome_input)
print("Nome completo:", nome_completo)
