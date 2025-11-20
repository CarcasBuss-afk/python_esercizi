# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Menu con tutte le operazioni CRUD.
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

# COMPLETA LE FUNZIONI inserimento(), cancella(), modifica()
# (Copia dalle esercizi precedenti)

while True:
    print("\nMENU CRUD")
    print("1) Ricerca")
    print("2) Inserisci")
    print("3) Cancella")
    print("4) Modifica")
    print("0) Esci")
    
    scelta = input("Scelta: ")
    
    if scelta == "1":
        ricerca = input("Cerca: ")
        # CHIAMA elenco() E STAMPA RISULTATI
        
    elif scelta == "2":
        # CHIEDI DATI E CHIAMA inserimento()
        pass
        
    elif scelta == "3":
        # CHIEDI ID E CHIAMA cancella()
        pass
        
    elif scelta == "4":
        # CHIEDI ID, CAMPO, VALORE E CHIAMA modifica()
        pass
        
    elif scelta == "0":
        break

print("Fine programma")
