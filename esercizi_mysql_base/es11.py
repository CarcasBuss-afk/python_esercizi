# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Modificare MULTIPLI record con un'unica query UPDATE.
Esempio: applicare uno sconto del 20% a tutti i giochi vecchi!
"""

import mysql.connector

print("=== SCONTO SU VIDEOGIOCHI VECCHI ===\n")

# Connessione
connessione = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='videogame_db'
)

cursore = connessione.cursor()

# Prima vediamo quali giochi saranno scontati (usciti prima del 2018)
print("Videogiochi che saranno scontati (usciti prima del 2018):")
cursore.execute("SELECT titolo, anno_uscita, prezzo FROM videogiochi WHERE anno_uscita < 2018")
giochi_vecchi = cursore.fetchall()

for gioco in giochi_vecchi:
    prezzo_scontato = gioco[2] * 0.8  # Sconto del 20% (prezzo * 0.8)
    print(f"- {gioco[0]} ({gioco[1]}): €{gioco[2]} -> €{prezzo_scontato:.2f}")

print(f"\nTotale giochi da scontare: {len(giochi_vecchi)}")

conferma = input("\nVuoi applicare lo sconto del 20%? (si/no): ")

if conferma.lower() == 'si':
    # Applichiamo lo sconto: nuovo prezzo = prezzo attuale * 0.8
    query = "UPDATE videogiochi SET prezzo = ________ WHERE anno_uscita < %s"
    #                                        prezzo * 0.8

    cursore.execute(query, (________,))  # anno 2018
    ________.commit()

    print(f"\nSconto applicato! {cursore.rowcount} videogiochi aggiornati.")

    # Verifichiamo i nuovi prezzi
    print("\nNuovi prezzi:")
    cursore.execute("SELECT titolo, prezzo FROM videogiochi WHERE anno_uscita < 2018")
    risultati = cursore.fetchall()

    for gioco in risultati:
        print(f"- {gioco[0]}: €{gioco[1]:.2f}")
else:
    print("\nOperazione annullata.")

# Chiusura
cursore.close()
connessione.close()

"""
COSA ABBIAMO IMPARATO:
1. UPDATE puo modificare multipli record con WHERE
2. Possiamo fare calcoli nella query (prezzo = prezzo * 0.8)
3. E buona pratica mostrare un'anteprima prima di modificare
4. Chiedere conferma all'utente e importante
5. rowcount ci dice quanti record sono stati modificati

OPERAZIONI MATEMATICHE IN UPDATE:
- prezzo = prezzo * 0.8 (sconto 20%)
- prezzo = prezzo + 5 (aumenta di 5€)
- prezzo = prezzo - 10 (sconta 10€)
- anno_uscita = anno_uscita + 1

SEMPRE verificare cosa si sta per modificare!
"""
