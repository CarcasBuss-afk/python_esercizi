# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Eliminare MULTIPLI record che soddisfano una condizione.
Esempio: rimuovere tutti i videogiochi gratuiti (prezzo = 0).
"""

import mysql.connector

print("=== RIMUOVI VIDEOGIOCHI GRATUITI ===\n")

# Connessione
connessione = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='videogame_db'
)

cursore = connessione.cursor()

# Prima vediamo quali videogiochi sono gratuiti
print("Videogiochi gratuiti nel database:")
cursore.execute("SELECT titolo, sviluppatore, prezzo FROM videogiochi WHERE prezzo = 0")
giochi_gratuiti = cursore.fetchall()

if len(giochi_gratuiti) == 0:
    print("Nessun videogioco gratuito trovato.")
else:
    for gioco in giochi_gratuiti:
        print(f"- {gioco[0]} by {gioco[1]} (€{gioco[2]})")

    print(f"\nTotale: {len(giochi_gratuiti)} videogiochi")

    conferma = input("\nVuoi eliminare tutti i videogiochi gratuiti? (si/no): ")

    if conferma.lower() == 'si':
        # Eliminiamo tutti i videogiochi con prezzo = 0
        query = "DELETE FROM videogiochi WHERE ________ = ________"
        #                                     prezzo     0

        cursore.execute(________)
        ________.commit()

        print(f"\nEliminati {cursore.rowcount} videogiochi gratuiti.")

        # Verifichiamo
        print("\nVideogiochi rimanenti:")
        cursore.execute("SELECT titolo, prezzo FROM videogiochi")
        rimanenti = cursore.fetchall()

        for gioco in rimanenti:
            print(f"- {gioco[0]}: €{gioco[1]}")
    else:
        print("\nOperazione annullata.")

# Chiusura
cursore.close()
connessione.close()

"""
COSA ABBIAMO IMPARATO:
1. DELETE puo eliminare multipli record con WHERE
2. Mostrare sempre un'anteprima di cosa verra eliminato
3. Chiedere conferma e fondamentale
4. rowcount ci dice quanti record sono stati eliminati
5. Verificare il risultato dopo l'operazione

ESEMPI DI DELETE CON CONDIZIONI:
- DELETE FROM videogiochi WHERE prezzo = 0
- DELETE FROM videogiochi WHERE anno_uscita < 2010
- DELETE FROM videogiochi WHERE genere = 'Sport'
- DELETE FROM videogiochi WHERE sviluppatore = 'Nintendo'

ATTENZIONE:
Queste operazioni sono PERMANENTI!
Non esiste "annulla" nel database.
"""
