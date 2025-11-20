# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Creare la funzione elenco_tutti() che restituisce tutti i videogiochi.
Questo rende il codice riutilizzabile!
"""

import mysql.connector
from mysql.connector import Error

def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(host = host_, user = user_, password = password_, database = database_)
        return conn
    except Error as e:
        print(f"Errore: {e.errno}")
        return None

def elenco_tutti():
    """Restituisce tutti i videogiochi dal database"""
    conn = connessione("localhost", "root", "la_tua_password", "videogame_db")

    if conn == None:
        return []                     # Lista vuota se errore

    cursore = conn.________()         # COMPLETA: crea cursore

    query = "________"                # COMPLETA: SELECT * FROM videogiochi
    cursore.execute(query)

    risultati = cursore.________()    # COMPLETA: prendi tutti i risultati

    cursore.________()                # COMPLETA: chiudi cursore
    conn.________()                   # COMPLETA: chiudi connessione

    return ________                   # COMPLETA: restituisci risultati

print("=== FUNZIONE ELENCO_TUTTI() ===\n")

giochi = elenco_tutti()
print(f"Trovati {len(giochi)} videogiochi:\n")

for gioco in giochi:
    print(f"{gioco[1]} ({gioco[3]}) - €{gioco[4]}")

"""
COSA HAI IMPARATO:
- Creare funzioni che restituiscono dati
- return [] per lista vuota
- return risultati per restituire dati
- La funzione gestisce tutto: connessione, query, chiusura
"""
