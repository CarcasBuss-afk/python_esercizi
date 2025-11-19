# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Usare SELECT con WHERE per filtrare i risultati.
Ad esempio: trovare solo i videogiochi economici o di un certo anno.
"""

import mysql.connector

print("=== RICERCA VIDEOGIOCHI CON FILTRI ===\n")

# Connessione
connessione = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='videogame_db'
)

cursore = connessione.cursor()

# --- FILTRO 1: Videogiochi economici (prezzo <= 30 euro) ---
print("Videogiochi economici (massimo 30€):\n")

query1 = "SELECT titolo, prezzo FROM videogiochi WHERE prezzo <= ________"
cursore.execute(________)

risultati = cursore.fetchall()

for gioco in risultati:
    print(f"- {gioco[0]}: €{gioco[1]}")

# --- FILTRO 2: Videogiochi recenti (dal 2020 in poi) ---
print("\nVideogiochi usciti dal 2020 in poi:\n")

query2 = "SELECT ________, ________ FROM videogiochi WHERE anno_uscita >= %s"
#        (seleziona titolo  e  anno_uscita)

cursore.execute(query2, (________,))  # Passa 2020 come parametro

risultati = cursore.fetchall()

for gioco in risultati:
    print(f"- {________} ({________})")
    #      titolo      anno

# --- FILTRO 3: Videogiochi di un genere specifico ---
genere_cercato = input("\nCerca videogiochi per genere (es. RPG, Azione): ")

query3 = "SELECT titolo, sviluppatore FROM videogiochi WHERE genere = %s"
cursore.execute(________, (________,))

risultati = cursore.fetchall()

if len(risultati) > 0:
    print(f"\nVideogiochi di genere '{genere_cercato}':")
    for gioco in risultati:
        print(f"- {gioco[0]} by {gioco[1]}")
else:
    print(f"\nNessun videogioco trovato per il genere '{genere_cercato}'")

# Chiusura
cursore.close()
connessione.close()

"""
COSA ABBIAMO IMPARATO:
1. WHERE filtra i risultati in base a condizioni
2. Operatori: =, <=, >=, <, >, !=
3. Possiamo selezionare solo alcune colonne (non per forza *)
4. Usare %s anche nei WHERE per sicurezza
5. if len(risultati) > 0 controlla se ci sono risultati

OPERATORI WHERE:
- WHERE prezzo <= 30
- WHERE anno_uscita >= 2020
- WHERE genere = 'RPG'
- WHERE titolo LIKE '%Mario%' (contiene "Mario")
"""
