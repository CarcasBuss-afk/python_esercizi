# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Creare funzione inserimento() con 5 parametri.
"""

import mysql.connector
from mysql.connector import Error

def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(host=host_, user=user_, password=password_, database=database_)
        return conn
    except Error as e:
        return None

def inserimento(titolo, sviluppatore, anno, prezzo, genere):
    conn = connessione("localhost", "root", "la_tua_password", "videogame_db")
    if conn == None:
        return
    
    cursore = conn.________()               # COMPLETA: cursor
    
    query = "________"                      # COMPLETA: INSERT INTO videogiochi...
    cursore.execute(query, (________, ________, ________, ________, ________))
    
    conn.________()                         # COMPLETA: commit
    cursore.close()
    conn.________()                         # COMPLETA: close

print("Aggiungi videogioco:")
titolo = input("Titolo: ")
sviluppatore = input("Sviluppatore: ")
anno = int(input("Anno: "))
prezzo = float(input("Prezzo: ").replace(",", "."))
genere = input("Genere: ")

inserimento(________, ________, ________, ________, ________)
print("Inserito!")
