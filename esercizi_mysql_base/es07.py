# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Aggiungere parametro ricerca alla funzione elenco.
Cerchiamo videogiochi per titolo esatto (WHERE titolo = ...).
"""

import mysql.connector
from mysql.connector import Error

def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(host=host_, user=user_, password=password_, database=database_)
        return conn
    except Error as e:
        print(f"Errore: {e.errno}")
        return None

def elenco(ricerca):
    conn = connessione("localhost", "root", "la_tua_password", "videogame_db")
    if conn == None:
        return []

    cursore = conn.cursor()
    query = "SELECT * FROM videogiochi WHERE titolo = ________"  # COMPLETA: %s
    cursore.execute(query, (________,))                          # COMPLETA: ricerca

    risultati = cursore.fetchall()
    cursore.close()
    conn.close()
    return risultati

print("Test ricerca:")
giochi = elenco("Minecraft")
for gioco in giochi:
    print(f"{gioco[1]} - €{gioco[4]}")
