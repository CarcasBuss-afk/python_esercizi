# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Imparare a MODIFICARE un record esistente con UPDATE.
Ad esempio: cambiare il prezzo di un videogioco.
"""

import mysql.connector

print("=== MODIFICA PREZZO VIDEOGIOCO ===\n")

# Connessione
connessione = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='videogame_db'
)

cursore = connessione.cursor()

# Prima vediamo il prezzo attuale di "Minecraft"
print("Prezzo attuale:")
cursore.execute("SELECT titolo, prezzo FROM videogiochi WHERE titolo = 'Minecraft'")
risultato = cursore.fetchone()
print(f"{risultato[0]}: €{risultato[1]}\n")

# Ora modifichiamo il prezzo a 19.99
nuovo_prezzo = 19.99

# Query UPDATE: modifica il campo 'prezzo' dove il titolo e 'Minecraft'
query = "UPDATE videogiochi SET prezzo = %s WHERE titolo = %s"

cursore.execute(________, (________, 'Minecraft'))
#                         nuovo_prezzo

# IMPORTANTE! Fare il commit per salvare le modifiche
________.commit()

print(f"Prezzo aggiornato! Righe modificate: {cursore.rowcount}")

# Verifichiamo la modifica
print("\nPrezzo dopo la modifica:")
cursore.execute("SELECT titolo, prezzo FROM videogiochi WHERE titolo = 'Minecraft'")
risultato = cursore.fetchone()
print(f"{risultato[0]}: €{________}")

# Chiusura
cursore.close()
connessione.close()

"""
COSA ABBIAMO IMPARATO:
1. UPDATE tabella SET campo = valore WHERE condizione
2. Senza WHERE modificheremmo TUTTI i record! (pericoloso!)
3. Sempre fare commit() dopo UPDATE
4. rowcount ci dice quante righe sono state modificate
5. Possiamo verificare la modifica con un SELECT

ATTENZIONE:
UPDATE senza WHERE modifica TUTTO!
Esempio PERICOLOSO: UPDATE videogiochi SET prezzo = 0
(metterebbe TUTTI i prezzi a 0!)

Usa SEMPRE WHERE per specificare quali record modificare!
"""
