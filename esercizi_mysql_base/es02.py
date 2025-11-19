# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Usare VARIABILI per i parametri di connessione.
Questo rende il codice piu pulito e riutilizzabile!
"""

import mysql.connector

print("=== CONNESSIONE CON VARIABILI ===\n")

# Invece di scrivere i parametri direttamente nella funzione connect(),
# e meglio salvarli in variabili separate

# COMPLETA le variabili con i tuoi dati
db_host = '________'        # localhost
db_user = '________'        # il tuo username
db_password = '________'    # la tua password
db_database = '________'    # videogame_db

# Ora usiamo le variabili nella connessione
# Nota come usiamo i nomi dei parametri (host=, user=, ecc.)
connessione = mysql.connector.connect(
    host=________,
    user=________,
    password=________,
    database=________
)

print("Connessione riuscita!")

# Possiamo vedere alcune informazioni sulla connessione
print(f"Server: {________}")
print(f"Database: {connessione.database}")
print(f"User: {________}")

# CHIUDI LA CONNESSIONE
________

print("\nConnessione chiusa.")

"""
COSA ABBIAMO IMPARATO:
1. Usare variabili per i parametri rende il codice piu leggibile
2. Possiamo accedere a informazioni della connessione (database, ecc.)
3. I parametri si passano con nome (host=, user=, ecc.)

VANTAGGI delle variabili:
- Piu facile modificare i parametri
- Codice piu chiaro e organizzato
- Preparazione per file di configurazione separati
"""
