# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Integrare funzione elenco() nel menu.
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
    query = "SELECT * FROM videogiochi WHERE titolo LIKE %s"
    cursore.execute(query, (f"{ricerca_}%",))
    risultati = cursore.fetchall()
    cursore.close()
    conn.close()
    return risultati

while True:
    print("\nMENU")
    print("1) Cerca videogiochi")
    print("0) Esci")
    
    scelta = input("Scelta: ")
    
    if scelta == "________":                                         # COMPLETA: "1"
        ricerca = input("Cerca: ")
        giochi = ________(________)                                  # COMPLETA: elenco, ricerca
        
        for gioco in giochi:
            print(f"- {gioco[1]} - €{gioco[4]}")
    
    elif scelta == "0":
        ________                                                     # COMPLETA: break

print("Fine")
