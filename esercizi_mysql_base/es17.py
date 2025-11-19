# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Usare AVG, MIN, MAX per calcolare statistiche sui prezzi.
Trova prezzo medio, piu economico, piu costoso, e altro!
"""

import mysql.connector

print("=== ANALISI PREZZI VIDEOGIOCHI ===\n")

# Connessione
connessione = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='videogame_db'
)

cursore = connessione.cursor()

# --- PREZZO MEDIO ---
print("Statistiche generali:")
print("-" * 50)

query_avg = "SELECT AVG(prezzo) FROM videogiochi"
cursore.execute(________)
prezzo_medio = cursore.fetchone()[0]
print(f"Prezzo medio: €{________:.2f}")

# --- PREZZO MINIMO E MASSIMO ---
query_minmax = "SELECT MIN(________), MAX(________) FROM videogiochi"
#                       prezzo         prezzo

cursore.execute(query_minmax)
min_max = cursore.fetchone()
print(f"Prezzo minimo: €{min_max[0]:.2f}")
print(f"Prezzo massimo: €{min_max[1]:.2f}")

# --- TOTALE VALORE DEL CATALOGO ---
query_sum = "SELECT SUM(prezzo) FROM videogiochi"
cursore.execute(query_sum)
totale_valore = cursore.fetchone()[0]
print(f"Valore totale catalogo: €{totale_valore:.2f}")

# --- VIDEOGIOCO PIU ECONOMICO (dettagli completi) ---
print("\n" + "=" * 50)
print("Videogioco piu ECONOMICO:")
query_economico = "SELECT titolo, sviluppatore, prezzo FROM videogiochi ORDER BY prezzo ASC LIMIT 1"
cursore.execute(query_economico)
economico = cursore.fetchone()
print(f"  {economico[0]} - {economico[1]}")
print(f"  Prezzo: €{economico[2]:.2f}")

# --- VIDEOGIOCO PIU COSTOSO (dettagli completi) ---
print("\nVideogioco piu COSTOSO:")
query_costoso = "SELECT titolo, sviluppatore, prezzo FROM videogiochi ORDER BY ________ DESC LIMIT ________"
#                                                                       prezzo           1

cursore.execute(________)
costoso = cursore.fetchone()
print(f"  {costoso[0]} - {costoso[1]}")
print(f"  Prezzo: €{costoso[2]:.2f}")

# --- PREZZO MEDIO PER GENERE ---
print("\n" + "=" * 50)
print("Prezzo medio per GENERE:")
print("-" * 50)

query_avg_genere = "SELECT genere, AVG(prezzo), COUNT(*) FROM videogiochi GROUP BY genere ORDER BY AVG(prezzo) DESC"
cursore.execute(query_avg_genere)
prezzi_generi = cursore.fetchall()

for genere in prezzi_generi:
    print(f"{genere[0]}: €{genere[1]:.2f} (media su {genere[2]} giochi)")

# --- VIDEOGIOCHI SOPRA LA MEDIA ---
print("\n" + "=" * 50)
print(f"Videogiochi con prezzo SOPRA la media (€{prezzo_medio:.2f}):")
query_sopra = "SELECT titolo, prezzo FROM videogiochi WHERE prezzo > %s ORDER BY prezzo DESC"
cursore.execute(query_sopra, (________,))
#                             prezzo_medio

sopra_media = cursore.fetchall()
for gioco in sopra_media:
    differenza = gioco[1] - prezzo_medio
    print(f"  {gioco[0]}: €{gioco[1]:.2f} (+€{differenza:.2f})")

# Chiusura
cursore.close()
connessione.close()

"""
COSA ABBIAMO IMPARATO:
1. AVG(campo) calcola la media
2. MIN(campo) trova il valore minimo
3. MAX(campo) trova il valore massimo
4. SUM(campo) somma tutti i valori
5. Combinare aggregazioni con GROUP BY per statistiche dettagliate
6. ORDER BY ASC (crescente) o DESC (decrescente)
7. LIMIT 1 per prendere solo il primo risultato

FORMATTAZIONE NUMERI:
- {valore:.2f} -> 2 decimali
- {valore:.0f} -> nessun decimale
- {valore:,.2f} -> con separatore migliaia

QUERY UTILI:
- Trovare il valore piu alto: ORDER BY campo DESC LIMIT 1
- Trovare il valore piu basso: ORDER BY campo ASC LIMIT 1
- Calcolare differenze: WHERE campo > (SELECT AVG(campo) ...)
"""
