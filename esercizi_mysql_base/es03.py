# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
RIEPILOGO - Creare da zero la funzione connessione() completa.
Questa funzione sarà la base di tutti i prossimi esercizi!
"""

# IMPORTA LE LIBRERIE NECESSARIE
# (mysql.connector e Error)


print("=== RIEPILOGO: FUNZIONE CONNESSIONE ===\n")

# CREA LA FUNZIONE connessione(host_, user_, password_, database_)
# La funzione deve:
# 1. Usare try/except per gestire errori
# 2. Creare la connessione con i 4 parametri
# 3. Restituire conn se tutto ok
# 4. Restituire None se c'è errore
# 5. Stampare il codice errore (e.errno) in caso di errore


# TEST della funzione
print("Test 1: Connessione valida")
conn = connessione("localhost", "root", "la_tua_password", "videogame_db")

if conn == None:
    print("✗ Test fallito\n")
else:
    print("✓ Test superato!")
    print(f"Database: {conn.database}\n")
    conn.close()

print("Test 2: Password errata")
conn_errata = connessione("localhost", "root", "password_sbagliata", "videogame_db")

if conn_errata == None:
    print("✓ Errore gestito correttamente\n")
else:
    print("✗ Doveva dare errore\n")
    conn_errata.close()

"""
RIEPILOGO:
Hai creato la funzione connessione() che:
- Accetta 4 parametri
- Gestisce errori con try/except
- Restituisce conn o None

QUESTA FUNZIONE È FONDAMENTALE:
La useremo in TUTTI i prossimi esercizi!
"""
