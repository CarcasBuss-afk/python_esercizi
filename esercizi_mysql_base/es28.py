# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Applicazione quasi completa con validazione input.
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

def inserimento(titolo, sviluppatore, anno, prezzo, genere):
    conn = connessione("localhost", "root", "la_tua_password", "videogame_db")
    if conn == None:
        return
    cursore = conn.cursor()
    query = "INSERT INTO videogiochi (titolo, sviluppatore, anno_uscita, prezzo, genere) VALUES (%s, %s, %s, %s, %s)"
    cursore.execute(query, (titolo, sviluppatore, anno, prezzo, genere))
    conn.commit()
    cursore.close()
    conn.close()

def cancella(id):
    conn = connessione("localhost", "root", "la_tua_password", "videogame_db")
    if conn == None:
        return
    cursore = conn.cursor()
    query = "DELETE FROM videogiochi WHERE id = %s"
    cursore.execute(query, (id,))
    conn.commit()
    cursore.close()
    conn.close()

def modifica(colonna, valore, id_):
    conn = connessione("localhost", "root", "la_tua_password", "videogame_db")
    if conn == None:
        return
    cursore = conn.cursor()
    query = f"UPDATE videogiochi SET {colonna} = %s WHERE id = %s"
    cursore.execute(query, (valore, id_))
    conn.commit()
    cursore.close()
    conn.close()

# MENU PRINCIPALE
while True:
    print("\n" + "="*50)
    print("GESTIONE VIDEOGIOCHI")
    print("="*50)
    print("1) Ricerca")
    print("2) Inserisci")
    print("3) Cancella")
    print("4) Modifica")
    print("0) Esci")
    
    scelta = input("Scelta: ")
    
    if scelta == "1":
        ricerca = input("Titolo o iniziali: ")
        risultati = elenco(ricerca)
        # STAMPA RISULTATI CON FORMATO
        for gioco in risultati:
            print(f"ID {gioco[0]}: {gioco[1]} | {gioco[2]} | €{gioco[4]}")
            
    elif scelta == "2":
        # COMPLETA: chiedi tutti i dati con validazione
        # Usa replace(",", ".") per il prezzo
        titolo = input("Titolo: ")
        sviluppatore = input("Sviluppatore: ")
        anno = int(input("Anno: "))
        prezzo = float(input("Prezzo: ").________(________, ________))
        genere = input("Genere: ")
        inserimento(________, ________, ________, ________, ________)
        print("Inserito!")
        
    elif scelta == "3":
        id_del = int(input("ID da cancellare: "))
        conferma = input(f"Sicuro? (s/n): ").lower().strip()
        if conferma == "s":
            cancella(________)
            print("Cancellato!")
            
    elif scelta == "4":
        # COMPLETA: logica modifica con menu campo
        pass
        
    elif scelta == "0":
        print("Arrivederci!")
        break
