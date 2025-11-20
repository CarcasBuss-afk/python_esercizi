# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Usare LIKE e % per ricerca parziale.
Ora "Mine" troverà "Minecraft"!
"""

import mysql.connector
from mysql.connector import Error

def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(host=host_, user=user_, password=password_, database=database_)
        return conn
    except Error as e:
        return None

def elenco(ricerca_=""):
    conn = connessione("localhost", "root", "la_tua_password", "videogame_db")
    if conn == None:
        return []

    cursore = conn.cursor()
    query = "SELECT * FROM videogiochi WHERE titolo ________ %s"  # COMPLETA: LIKE
    cursore.execute(query, (f"{ricerca_}________",))              # COMPLETA: %

    risultati = cursore.________()                                # COMPLETA: fetchall
    cursore.close()
    conn.________()                                               # COMPLETA: close
    return ________                                               # COMPLETA: risultati

ricerca = input("Cerca videogioco: ")
giochi = elenco(ricerca)
print(f"Trovati: {len(giochi)}")
for gioco in giochi:
    print(f"- {gioco[1]}")
