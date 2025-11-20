# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Imparare a connettersi al database MySQL e gestire gli errori con try/except.
Questo è il primo passo per lavorare con database in Python!
"""

# Importiamo le librerie necessarie
import mysql.connector
from mysql.connector import Error

print("=== CONNESSIONE AL DATABASE ===\n")

# try = prova a eseguire questo codice
# except = se c'è un errore, fai quest'altro

try:
    # Creiamo la connessione al database
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',              # Modifica con il tuo username
        password = '________',      # COMPLETA: la tua password MySQL
        database = 'videogame_db'
    )

    print("✓ Connessione riuscita!")
    print(f"Database: {conn.database}")

    # Chiudiamo la connessione
    conn.________()                 # COMPLETA: chiudi la connessione
    print("✓ Connessione chiusa")

except Error as e:
    # Se c'è un errore, lo stampiamo
    print("✗ Errore di connessione!")
    print(f"Codice errore: {e.errno}")
    print(f"Messaggio: {e}")

"""
COSA HAI IMPARATO:
- import mysql.connector per connettersi a MySQL
- from mysql.connector import Error per gestire errori
- try/except previene crash del programma
- conn.close() chiude sempre la connessione

PROVA:
- Esegui con credenziali corrette (dovrebbe funzionare)
- Prova con password sbagliata (dovresti vedere l'errore gestito)
"""
