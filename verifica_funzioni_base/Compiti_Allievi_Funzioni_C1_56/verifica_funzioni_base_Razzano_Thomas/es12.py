# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni con parametri e logica """

# DEFINISCI UNA FUNZIONE chiamata 'verifica_login' che prende 'username' e 'password'
# - Se username == "admin" E password == "1234": stampa "Accesso consentito"
# - Altrimenti: stampa "Accesso negato"
def verifica_login(username, password):
    if username == "admin" and password == "1234":
        print("Accesso consentito")
    else:
        print("Accesso negato")


# DEFINISCI UNA FUNZIONE chiamata 'confronta_numeri' che prende 'a' e 'b'
# - Se a > b: stampa "[a] è maggiore di [b]"
# - Se a < b: stampa "[a] è minore di [b]"
# - Altrimenti: stampa "I numeri sono uguali"
def confronta_numeri(a, b):
    if a >= b:
        print("[a] è maggiore di [b]")
    elif a <= b:
        print("[a] è minore di [b]")
    else:
        print("I numeri sono uguali")


# Programma principale
user = input("Username: ")
pwd = input("Password: ")
# CHIAMA verifica_login
verifica_login(user, pwd)

num_a = int(input("Primo numero: "))
num_b = int(input("Secondo numero: "))
# CHIAMA confronta_numeri
confronta_numeri(num_a, num_b)
