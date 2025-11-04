# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni con due parametri """

# DEFINISCI UNA FUNZIONE chiamata 'stampa_studente' che prende 'nome' e 'corso'
# e stampa "Studente: [nome], Corso: [corso]"
def stampa_studente(nome, corso):
    print("Studente:", nome, ", Corso:", corso)


# DEFINISCI UNA FUNZIONE chiamata 'calcola_somma' che prende 'num1' e 'num2'
# e stampa "La somma è: [risultato]"
def calcola_somma(num1, num2):
    risultato = num1 + num2
    print("La somma è:", risultato)


# Programma principale
nome_input = input("Inserisci nome studente: ")
corso_input = input("Inserisci nome corso: ")
# CHIAMA stampa_studente con nome_input e corso_input
stampa_studente(nome_input, corso_input)

n1 = input("Inserisci primo numero: ")
n2 = input("Inserisci secondo numero: ")
num1 = int(n1)
num2 = int(n2)
# CHIAMA calcola_somma con num1 e num2
calcola_somma(num1, num2)
