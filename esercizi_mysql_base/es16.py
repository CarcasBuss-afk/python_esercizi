# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Usare COUNT e GROUP BY per creare statistiche sui videogiochi.
Conta quanti videogiochi ci sono per ogni genere e sviluppatore.
"""

import mysql.connector

print("=== STATISTICHE VIDEOGIOCHI ===\n")

# Connessione
connessione = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='videogame_db'
)

cursore = connessione.cursor()

# --- STATISTICA 1: Videogiochi per genere ---
print("Distribuzione per GENERE:")
print("-" * 40)

# COUNT(*) conta il numero di record
# GROUP BY genere raggruppa i risultati per genere
query1 = "SELECT genere, COUNT(*) FROM videogiochi GROUP BY ________"

cursore.execute(________)
risultati_generi = cursore.fetchall()

for genere in risultati_generi:
    print(f"{genere[0]}: {genere[1]} giochi")

# --- STATISTICA 2: Videogiochi per sviluppatore ---
print("\nDistribuzione per SVILUPPATORE:")
print("-" * 40)

query2 = "SELECT ________, ________ FROM videogiochi GROUP BY sviluppatore"
#        sviluppatore  COUNT(*)

cursore.execute(query2)
risultati_sviluppatori = cursore.fetchall()

for sviluppatore in risultati_sviluppatori:
    print(f"{sviluppatore[0]}: {________} giochi")
    #                           sviluppatore[1]

# --- STATISTICA 3: Totale videogiochi nel database ---
print("\n" + "=" * 40)
cursore.execute("SELECT ________ FROM videogiochi")
#                COUNT(*)
totale = cursore.fetchone()[0]
print(f"Totale videogiochi nel database: {totale}")

# --- STATISTICA 4: Genere piu popolare (con piu giochi) ---
print("\n" + "=" * 40)
print("Genere con piu videogiochi:")
query3 = "SELECT genere, COUNT(*) as numero FROM videogiochi GROUP BY genere ORDER BY numero DESC LIMIT 1"
cursore.execute(query3)
genere_top = cursore.fetchone()
print(f"{genere_top[0]}: {genere_top[1]} giochi")

# Chiusura
cursore.close()
connessione.close()

"""
COSA ABBIAMO IMPARATO:
1. COUNT(*) conta il numero di record
2. GROUP BY raggruppa i risultati per un campo
3. AS crea un alias per il risultato (es. COUNT(*) as numero)
4. ORDER BY ordina i risultati (DESC = decrescente)
5. LIMIT 1 prende solo il primo risultato

FUNZIONI DI AGGREGAZIONE:
- COUNT(*) -> conta i record
- COUNT(campo) -> conta i valori non-NULL
- SUM(campo) -> somma i valori
- AVG(campo) -> media dei valori
- MIN(campo) -> valore minimo
- MAX(campo) -> valore massimo

GROUP BY e fondamentale per creare report e statistiche!
"""
