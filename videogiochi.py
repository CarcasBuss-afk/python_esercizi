import mysql.connector
from mysql.connector import Error
import os

def pulisci_terminale():
    os.system('cls' if os.name == 'nt' else 'clear')


# Crea la connessione e controlla se ci sono errori
def connessione(host_, user_, password_, database_):
    try:
        conn = mysql.connector.connect(
            host = host_,
            user = user_,
            password = password_,
            database = database_
        )
        return conn
    except Error as e:
        print(f"Errore numero: {e.errno}")
        return None

def elenco(ricerca_=""):
    conn = connessione("localhost", "root", "docentepc", "videogame_db")
    if conn == None:
        print("Connessione non riuscita!!")
    else:
        cursore = conn.cursor()
        query = f"SELECT * FROM videogiochi WHERE titolo like %s"
        cursore.execute(query, (f"{ricerca_}%",))
        risultato = cursore.fetchall()
        cursore.close()
        conn.close()
        return risultato
    
def inserimento(titolo, sviluppatore, anno, prezzo, genere):
    conn = connessione("localhost", "root", "docentepc", "videogame_db")
    if conn == None:
        print("Connessione non riuscita!!")
    else:
        cursore = conn.cursor()
        query = f"INSERT INTO videogiochi (titolo, sviluppatore, anno_uscita, prezzo, genere) VALUES (%s, %s, %s, %s, %s)"
        cursore.execute(query, (titolo, sviluppatore, anno, prezzo, genere))
        conn.commit()
        cursore.close()
        conn.close()

def cancella(id):
    conn = connessione("localhost", "root", "docentepc", "videogame_db")
    if conn == None:
        print("Connessione non riuscita!!")
    else:
        cursore = conn.cursor()
        query = "DELETE FROM videogiochi WHERE  id = %s"
        cursore.execute(query, (id,))
        conn.commit()
        cursore.close()
        conn.close()

def modifica(colonna, valore, id_):
    conn = connessione("localhost", "root", "docentepc", "videogame_db")
    if conn == None:
        print("Connessione non riuscita!!")
    else:
        cursore = conn.cursor()
        query = f"UPDATE videogiochi SET {colonna} = {valore} WHERE id = %s"
        cursore.execute(query, (id_,))
        conn.commit()
        cursore.close()
        conn.close()



while True:
    pulisci_terminale()
    print("1) Ricerca")
    print("2) Inserisci nuovo gioco")
    print("3) Cancella")
    print("4) Modifica")
    print("0) Esci")
    scelta = input("fai la tua scelta: ")
    if scelta == "1":
        pulisci_terminale()
        ricerca = input("Inserisci il titolo o le sue iniziali: ")
        risultato = elenco(ricerca)
        print("______________________________________________________________________")
        for gioco in risultato:
            print(f"Id: {gioco[0]}|, Titolo: {gioco[1]}|, Sviluppatore: {gioco[2]}|, Anno: {gioco[3]}|, Prezzo: {gioco[4]}|, Genere: {gioco[5]}|")
            print("______________________________________________________________________")
        input("Premi 'Invio' per terminare")
    elif scelta == "2":
        pulisci_terminale()
        titolo = input("Inserisci titolo: ")
        sviluppatore = input("Inserisci lo sviluppatore: ")
        anno = input("Inserisci l'anno: ")
        prezzo = input("Inserisci il prezzo: ").replace(",",".")
        genere = input("Inserisci il genere: ")
        inserimento(titolo, sviluppatore, anno, prezzo, genere)
    
    elif scelta == "3":
        pulisci_terminale()
        id_del = input("Inserisci l'id del videgioco da cancellare: ")
        scelta = input(f"Sei scirudo di voler cancellare l'id {id_del} s/n").lower().strip()
        if scelta == "s":
            cancella(id_del)

    elif scelta == "4":
        pulisci_terminale()
        id_mod = input("Inserisci l'id da modificare: ")
        print("1) Titolo")
        print("2) Sviluppatore")
        print("3) Data")
        print("4) Prezzo")
        print("5) Genere")
        scelta = input("Scegli il campo da modificare: ")
        if scelta == "1":
            campo = "Titolo"
            valore = input("Inserisci il nuovo titolo: ").strip()
            modifica(campo, valore, id_mod)
        elif scelta == "2":
            campo = "Sviluppatore"
            valore = input("Inserisci il nuovo valore: ").strip()
            modifica(campo, valore, id_mod)
        elif scelta == "3":
            campo = "anno_uscita"
            valore = input("Inserisci il nuovo anno di uscita: ").strip()
            modifica(campo, valore, id_mod)
        elif scelta == "4":
            campo = "prezzo"
            valore = input("Inserisci il nuovo prezzo: ").strip().replace(",", ".")
            modifica(campo, valore, id_mod)
        elif scelta == "5":
            campo = "genere"
            valore = input("Inserisci il nuovo genere: ").strip()
            modifica(campo, valore, id_mod)
        else:
            print("Scelta non valida")

    elif scelta == "0":
        print("PROGRAMMA TERMINATO")
        break     
    else:
        print("Scelta non valida. Ripeti la scelta")

        