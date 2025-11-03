# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo a usare PARAMETRI CON VALORI DEFAULT """

# I PARAMETRI DEFAULT permettono di rendere alcuni parametri OPZIONALI
# Sintassi: def nome_funzione(parametro_obbligatorio, parametro_opzionale=valore_default):
#
# - Se chiami la funzione SENZA il parametro opzionale, usa il valore default
# - Se chiami la funzione CON il parametro opzionale, usa il valore che passi
#
# IMPORTANTE: i parametri con default devono venire DOPO quelli obbligatori!

# Funzione con parametro default
def saluta(nome, saluto="Ciao"):
    print(f"{saluto} {nome}!")

# Chiamata SENZA il secondo parametro (usa "Ciao")
saluta("Mario")

# Chiamata CON il secondo parametro (sovrascrive "Ciao")
saluta("Anna", "Buongiorno")
saluta("______", "Buonasera")

print("\n--- Separatore ---\n")

# Funzione potenza con esponente default
def calcola_potenza(base, esponente=2):
    risultato = base ** esponente
    return risultato

# Chiamata senza esponente (calcola il quadrato)
quadrato = calcola_potenza(5)
print(f"5 al quadrato = {________}")

# Chiamata con esponente (calcola il cubo)
cubo = calcola_potenza(5, _)
print(f"5 al cubo = {____}")

# DEFINISCI UNA FUNZIONE chiamata 'moltiplica' con parametri (numero, moltiplicatore=10)
# che RESTITUISCE numero * moltiplicatore




# Chiamala senza il secondo parametro con il numero 7
risultato1 = ___________(_)
print(f"Risultato 1: {__________}")

# Chiamala con entrambi i parametri: 7 e 5
risultato2 = ___________(_ , _)
print(f"Risultato 2: {__________}")

""" Osserva come i parametri default rendono le funzioni più flessibili! """
