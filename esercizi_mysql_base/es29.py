# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Applicazione avanzata come videogiochi.py con menu modifica completo.
"""

import mysql.connector
from mysql.connector import Error

# FUNZIONI BASE (completate)
def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(host=host_, user=user_, password=password_, database=database_)
        return conn
    except Error as e:
        print(f"Errore: {e.errno}")
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

# COMPLETA LE ALTRE FUNZIONI
def inserimento(titolo, sviluppatore, anno, prezzo, genere):
    # COMPLETA
    pass

def cancella(id):
    # COMPLETA
    pass

def modifica(colonna, valore, id_):
    # COMPLETA
    pass

# MENU PRINCIPALE
while True:
    print("\n1) Ricerca")
    print("2) Inserisci")
    print("3) Cancella")
    print("4) Modifica")
    print("0) Esci")
    
    scelta = input("Scelta: ")
    
    if scelta == "1":
        # RICERCA
        pass
        
    elif scelta == "2":
        # INSERIMENTO
        pass
        
    elif scelta == "3":
        # CANCELLAZIONE
        pass
        
    elif scelta == "4":
        # MODIFICA CON MENU
        id_mod = int(input("ID: "))
        print("1) Titolo")
        print("2) Sviluppatore")
        print("3) Anno")
        print("4) Prezzo")
        print("5) Genere")
        scelta_campo = input("Campo: ")
        
        # COMPLETA: if/elif per ogni campo
        # Usa .replace(",", ".") per il prezzo
        
    elif scelta == "0":
        break
