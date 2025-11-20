# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Creare funzione cancella(id) con conferma.
"""

import mysql.connector
from mysql.connector import Error

def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(host=host_, user=user_, password=password_, database=database_)
        return conn
    except Error as e:
        return None

def cancella(id):
    conn = connessione("localhost", "root", "la_tua_password", "videogame_db")
    if conn == None:
        return
    
    cursore = conn.cursor()
    query = "DELETE FROM videogiochi WHERE ________ = %s"   # COMPLETA: id
    cursore.________(query, (________,))                    # COMPLETA: execute, id
    
    conn.________()                                         # COMPLETA: commit
    cursore.close()
    conn.________()                                         # COMPLETA: close

id_del = int(input("ID da eliminare: "))
conferma = input(f"Sei sicuro di eliminare ID {id_del}? (s/n): ").________.________()

if conferma == "s":
    cancella(________)                                      # COMPLETA: id_del
    print("Eliminato!")
else:
    print("Annullato")
