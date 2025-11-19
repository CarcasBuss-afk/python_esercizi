# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Imparare a connettersi a un database MySQL usando Python.
Questo e il primo passo fondamentale per lavorare con i database!
"""

# Prima di tutto, importiamo la libreria mysql.connector
# Questa libreria ci permette di comunicare con MySQL
import mysql.connector

print("=== CONNESSIONE AL DATABASE MYSQL ===\n")

# STEP 1: Creare la connessione al database
# La funzione connect() richiede 4 parametri:
# - host: dove si trova il server MySQL (di solito localhost)
# - user: il nome utente MySQL
# - password: la password (puo essere vuota)
# - database: il nome del database a cui connettersi

connessione = mysql.connector.connect(
    host='localhost',           # Di solito e 'localhost'
    user='root',           # Il tuo username MySQL (es. 'root')
    password='docentepc',       # La tua password ('' se vuota)
    database='videogame_db'    # Il nome del nostro database
)

# STEP 2: Verificare che la connessione sia avvenuta
# Se arriviamo qui senza errori, la connessione e riuscita!
print("Connessione al database riuscita!")
print(f"Connesso al database: {connessione.database}")

# STEP 3: IMPORTANTE! Chiudere sempre la connessione quando abbiamo finito
# Questo libera risorse e previene problemi
conn.close()

print("\nConnessione chiusa correttamente.")

"""
COSA ABBIAMO IMPARATO:
1. Per usare MySQL in Python serve la libreria mysql.connector
2. La funzione connect() crea la connessione al database
3. Servono 4 parametri: host, user, password, database
4. SEMPRE chiudere la connessione con .close()

PROVA AD ESEGUIRE:
- Se vedi "Connessione riuscita" tutto funziona!
- Se vedi errori, controlla username, password e che MySQL sia avviato
"""
