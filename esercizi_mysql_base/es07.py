# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Imparare a LEGGERE tutti i dati dalla tabella videogiochi.
Usiamo SELECT * per prendere tutti i record.
"""

import mysql.connector

print("=== VISUALIZZA TUTTI I VIDEOGIOCHI ===\n")

# Connessione
connessione = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='videogame_db'
)

cursore = connessione.cursor()

# Query per selezionare TUTTI i videogiochi
# SELECT * significa "prendi tutte le colonne"
query = "SELECT * FROM videogiochi"

# Eseguiamo la query
cursore.execute(________)

# fetchall() prende TUTTI i risultati e li mette in una lista
risultati = cursore.fetchall()

print(f"Trovati {len(risultati)} videogiochi:\n")

# Ogni risultato e una tupla con i valori delle colonne
# L'ordine e: (id, titolo, sviluppatore, anno_uscita, prezzo, genere)
for gioco in ________:
    id_gioco = gioco[0]
    titolo = gioco[1]
    sviluppatore = gioco[________]  # Indice 2
    anno = gioco[________]           # Indice 3
    prezzo = gioco[4]
    genere = gioco[5]

    print(f"ID: {id_gioco}")
    print(f"  Titolo: {titolo}")
    print(f"  Sviluppatore: {sviluppatore}")
    print(f"  Anno: {anno}")
    print(f"  Prezzo: €{prezzo}")
    print(f"  Genere: {genere}")
    print("-" * 40)

# Chiusura
cursore.close()
connessione.close()

"""
COSA ABBIAMO IMPARATO:
1. SELECT * FROM tabella prende tutti i record
2. fetchall() restituisce una lista di tuple
3. Ogni tupla rappresenta una riga del database
4. Accediamo ai valori con indici: [0], [1], [2], ecc.

METODI DI FETCH:
- fetchall() -> prende TUTTI i risultati (lista)
- fetchone() -> prende UN risultato alla volta
- fetchmany(n) -> prende n risultati
"""
