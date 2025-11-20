# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Imparare a usare SELECT per leggere dati dal database.
Usiamo cursore e fetchall() per ottenere tutti i risultati.
"""

import mysql.connector
from mysql.connector import Error

def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(
            host = host_,
            user = user_,
            password = password_,
            database = database_
        )
        return conn
    except Error as e:
        print(f"Errore: {e.errno}")
        return None

print("=== SELECT - LEGGI TUTTI I VIDEOGIOCHI ===\n")

conn = connessione("localhost", "root", "la_tua_password", "videogame_db")

if conn == None:
    print("Connessione fallita!")
else:
    # Il cursore serve per eseguire query
    cursore = conn.cursor()

    # Query SQL per selezionare tutto
    query = "SELECT * FROM videogiochi"
    cursore.________(query)           # COMPLETA: esegui la query

    # fetchall() prende tutti i risultati
    risultati = cursore.________()    # COMPLETA: prendi tutti i risultati

    print(f"Trovati {len(risultati)} videogiochi:\n")

    # Ogni risultato è una tupla (id, titolo, sviluppatore, anno, prezzo, genere)
    for gioco in risultati:
        print(f"ID {gioco[0]}: {gioco[1]} - {gioco[2]} ({gioco[3]}) - €{gioco[4]}")

    cursore.close()
    conn.________()                   # COMPLETA: chiudi connessione

"""
COSA HAI IMPARATO:
- conn.cursor() crea un cursore
- cursore.execute(query) esegue la query
- cursore.fetchall() prende tutti i risultati
- Ogni risultato è una tupla con i campi
- SEMPRE chiudere cursore e connessione
"""
