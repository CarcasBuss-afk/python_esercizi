# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Imparare a ELIMINARE un record dal database con DELETE.
ATTENZIONE: DELETE e un'operazione irreversibile!
"""

import mysql.connector

print("=== ELIMINA VIDEOGIOCO PER ID ===\n")

# Connessione
connessione = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='videogame_db'
)

cursore = connessione.cursor()

# Mostra i videogiochi disponibili
print("Videogiochi nel database:")
cursore.execute("SELECT id, titolo FROM videogiochi")
tutti = cursore.fetchall()

for gioco in tutti:
    print(f"ID {gioco[0]}: {gioco[1]}")

# Scegliamo di eliminare un videogioco specifico
id_da_eliminare = 100  # Usiamo un ID che probabilmente non esiste

# Prima verifichiamo se esiste
cursore.execute("SELECT * FROM videogiochi WHERE id = %s", (id_da_eliminare,))
gioco_da_eliminare = cursore.fetchone()

if gioco_da_eliminare is None:
    print(f"\nID {id_da_eliminare} non trovato. Nessuna eliminazione effettuata.")
else:
    print(f"\nStai per eliminare: {gioco_da_eliminare[1]}")

    # Query DELETE: elimina il record con l'ID specificato
    query = "DELETE FROM videogiochi WHERE id = ________"

    cursore.execute(________, (________,))
    #                          id_da_eliminare

    # IMPORTANTE! Fare il commit
    ________.commit()

    print(f"Videogioco eliminato! Righe eliminate: {cursore.rowcount}")

# Verifichiamo che sia stato eliminato
print("\nVideogiochi rimasti:")
cursore.execute("SELECT id, titolo FROM videogiochi")
tutti = cursore.fetchall()

for gioco in tutti:
    print(f"ID {gioco[0]}: {gioco[1]}")

# Chiusura
cursore.close()
connessione.close()

"""
COSA ABBIAMO IMPARATO:
1. DELETE FROM tabella WHERE condizione elimina record
2. Senza WHERE eliminerebbe TUTTI i record! (PERICOLOSISSIMO!)
3. Sempre verificare che il record esista prima di eliminare
4. DELETE e irreversibile (non c'e CTRL+Z!)
5. rowcount ci dice quante righe sono state eliminate

ATTENZIONE:
DELETE senza WHERE cancella TUTTO!
Esempio PERICOLOSO: DELETE FROM videogiochi
(cancellerebbe TUTTI i videogiochi!)

BUONE PRATICHE:
1. Verificare sempre che il record esista
2. Mostrare un'anteprima
3. Chiedere conferma all'utente
4. Fare backup regolari del database
"""
