# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Creare funzione modifica(colonna, valore, id_).
"""

import mysql.connector
from mysql.connector import Error

def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(host=host_, user=user_, password=password_, database=database_)
        return conn
    except Error as e:
        return None

def modifica(colonna, valore, id_):
    conn = connessione("localhost", "root", "la_tua_password", "videogame_db")
    if conn == None:
        return
    
    cursore = conn.cursor()
    query = f"UPDATE videogiochi SET {________} = %s WHERE id = %s"  # COMPLETA: colonna
    cursore.execute(query, (________, ________))                     # COMPLETA: valore, id_
    
    conn.________()                                                  # COMPLETA: commit
    cursore.________()                                               # COMPLETA: close
    conn.close()

id_mod = int(input("ID da modificare: "))
print("1) prezzo\n2) genere")
scelta = input("Campo: ")

if scelta == "1":
    nuovo = input("Nuovo prezzo: ").replace(",", ".")
    modifica("________", nuovo, id_mod)                              # COMPLETA: prezzo
elif scelta == "2":
    nuovo = input("Nuovo genere: ")
    modifica("________", ________, ________)                         # COMPLETA: genere, nuovo, id_mod

print("Modificato!")
