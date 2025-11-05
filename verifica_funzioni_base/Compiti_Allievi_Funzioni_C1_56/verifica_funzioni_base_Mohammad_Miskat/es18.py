# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: return con logica condizionale """

# DEFINISCI UNA FUNZIONE chiamata 'trova_massimo' che prende 'a' e 'b'
# e RESTITUISCE il numero più grande tra i due
def trova_massimo(a, b):
    if a > b:
        return a
    else:
        return b


# DEFINISCI UNA FUNZIONE chiamata 'controlla_password' che prende 'password'
# - Se lunghezza >= 8: RESTITUISCE "Password sicura"
# - Altrimenti: RESTITUISCE "Password debole"
def controllo_password(password):
    if len(password) >= 8:
        print("Password sicura")
    else:
        print ("Password debole")


# Programma principale
num1 = int(input("Primo numero: "))
num2 = int(input("Secondo numero: "))
massimo = trova_massimo(num1, num2)
print("Il numero maggiore è:", massimo)

pwd = input("Inserisci una password: ")
sicurezza = controllo_password(pwd)
print(sicurezza)
