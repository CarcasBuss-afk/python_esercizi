# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Imparare INSERT per aggiungere un videogioco.
INSERT aggiunge nuove righe alla tabella.
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
    
    query = "INSERT INTO videogiochi (titolo, sviluppatore, anno_uscita, prezzo, genere) VALUES (%s, %s, %s, %s, %s)"
    valori = ("Stardew Valley", "ConcernedApe", 2016, 13.99, "Simulazione")
    
    cursore.execute(________, ________)     # COMPLETA: query, valori
    conn.________()                         # COMPLETA: commit (salva)
    
    print(f"Videogioco inserito! ID: {cursore.lastrowid}")
    
    cursore.close()
    conn.close()
