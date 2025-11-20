# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Imparare DELETE per eliminare un videogioco.
DELETE è IRREVERSIBILE - attenzione!
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
    
    id_da_eliminare = 100  # Cambia con un ID esistente
    
    query = "DELETE FROM videogiochi WHERE id = ________"  # COMPLETA: %s
    cursore.execute(query, (________,))                    # COMPLETA: id_da_eliminare
    
    conn.________()                                        # COMPLETA: commit
    
    if cursore.rowcount > 0:
        print(f"Videogioco ID {id_da_eliminare} eliminato!")
    else:
        print(f"ID {id_da_eliminare} non trovato")
    
    cursore.close()
    conn.close()
