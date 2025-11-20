# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Imparare UPDATE per modificare dati esistenti.
"""

import mysql.connector
from mysql.connector import Error

def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(host=host_, user=user_, password=password_, database=database_)
        return conn
    except Error as e:
        return None

conn = connessione("localhost", "root", "la_tua_password", "videogame_db")

if conn != None:
    cursore = conn.cursor()
    
    id_mod = 1
    nuovo_prezzo = 19.99
    
    query = "UPDATE videogiochi SET prezzo = ________ WHERE id = ________"
    cursore.execute(query, (________, ________))           # COMPLETA: nuovo_prezzo, id_mod
    
    conn.________()                                        # COMPLETA: commit
    
    print(f"Prezzo ID {id_mod} aggiornato!")
    
    cursore.close()
    conn.close()
