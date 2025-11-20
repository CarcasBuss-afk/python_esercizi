# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Creare una FUNZIONE per la connessione che possiamo riutilizzare.
Le funzioni rendono il codice più organizzato!
"""

import mysql.connector
from mysql.connector import Error

# Funzione che crea la connessione e la restituisce
def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(
            host = ________,          # COMPLETA: usa il parametro host_
            user = ________,          # COMPLETA: usa il parametro user_
            password = ________,      # COMPLETA: usa il parametro password_
            database = ________       # COMPLETA: usa il parametro database_
        )
        return conn                   # Restituisce la connessione se ok
    except Error as e:
        print(f"Errore: {e.errno}")
        return ________               # COMPLETA: cosa restituire se errore? (None)

print("=== FUNZIONE CONNESSIONE ===\n")

# Usiamo la funzione
conn = connessione("localhost", "root", "la_tua_password", "videogame_db")

# Controlliamo se ha funzionato
if conn == ________:                  # COMPLETA: controlla se è None
    print("Connessione fallita!")
else:
    print("✓ Connessione riuscita!")
    print(f"Database: {________}")   # COMPLETA: stampa conn.database
    conn.close()

"""
COSA HAI IMPARATO:
- def nome_funzione(parametri): crea una funzione
- return restituisce un valore
- return None se c'è errore
- Controllare if conn == None prima di usarla

VANTAGGI:
Ora possiamo chiamare connessione() ogni volta che serve,
invece di riscrivere tutto il codice!
"""
