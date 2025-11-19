# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Inserire MULTIPLI videogiochi contemporaneamente usando executemany().
Questo e piu efficiente che fare tanti INSERT separati!
"""

import mysql.connector

print("=== INSERIMENTO MULTIPLO ===\n")

# Connessione
connessione = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='videogame_db'
)

cursore = connessione.cursor()

# Query di inserimento (uguale a prima)
query = "INSERT INTO videogiochi (titolo, sviluppatore, anno_uscita, prezzo, genere) VALUES (%s, %s, %s, %s, %s)"

# LISTA di videogiochi da inserire
# Ogni elemento della lista e una tupla con i 5 valori
lista_videogiochi = [
    ('Hollow Knight', 'Team Cherry', 2017, 14.99, 'Metroidvania'),
    ('Celeste', 'Maddy Makes Games', 2018, 19.99, 'Platform'),
    ('Hades', '________', ________, ________, '________')
    # Completa con: Supergiant Games, 2020, 24.99, Roguelike
]

# executemany() inserisce tutti i record in una volta!
cursore.executemany(________, ________)

# Commit per salvare
________.commit()

print(f"Inseriti {________} videogiochi!")

# Chiusura
cursore.close()
connessione.close()

print("Inserimento multiplo completato!")

"""
COSA ABBIAMO IMPARATO:
1. executemany() inserisce multipli record contemporaneamente
2. Serve una lista di tuple, una per ogni record
3. Molto piu efficiente di tanti execute() separati
4. rowcount ci dice quanti record sono stati inseriti

QUANDO USARE executemany():
- Quando hai molti dati da inserire
- Quando importi dati da file (CSV, Excel, ecc.)
- Per ottimizzare le performance
"""
