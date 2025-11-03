# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo a VALIDARE l'input dell'utente con funzioni """

# VALIDAZIONE = controllare se un dato è corretto prima di usarlo
#
# Le funzioni di validazione di solito:
# - Prendono un parametro da controllare
# - RESTITUISCONO True se il dato è valido, False se non lo è
#
# Questo permette di:
# - Evitare errori nel programma
# - Dare feedback all'utente
# - Mantenere i dati puliti

# Funzione che valida la lunghezza di una stringa
def valida_lunghezza(testo, lunghezza_minima):
    if len(testo) >= lunghezza_minima:
        return True
    else:
        return False

# Testiamo la funzione
password = "abc"
if valida_lunghezza(password, 5):
    print("Password valida")
else:
    print("Password troppo corta")

print("\n--- Separatore ---\n")

# DEFINISCI UNA FUNZIONE chiamata 'valida_eta' che prende 'eta'
# - Se eta >= 18: RESTITUISCE True
# - Altrimenti: RESTITUISCE False
___ valida_eta(___):
    if ___ __ 18:
        ______ ____
    ____:
        ______ _____


# Chiedi all'utente di inserire l'età
input_eta = input("Inserisci la tua età: ")
eta_utente = int(__________)

# Usa la funzione per validare
if valida_eta(___________):
    print("Accesso consentito")
____:
    print("Devi essere maggiorenne")

# DEFINISCI UNA FUNZIONE chiamata 'valida_username' che prende 'username'
# - Se la lunghezza è tra 4 e 12 caratteri: RESTITUISCE True
# - Altrimenti: RESTITUISCE False




# Chiedi username e valida
username = input("Scegli un username (4-12 caratteri): ")

if ________________(________):
    print("Username valido!")
____:
    print("Username non valido (deve essere tra 4 e 12 caratteri)")

""" Prova con username di lunghezze diverse """
