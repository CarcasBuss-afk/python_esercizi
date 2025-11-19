# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
RIEPILOGO Query Avanzate - Creare una Top 5 dei videogiochi.
Usa ORDER BY e LIMIT per creare classifiche interessanti!
"""

import mysql.connector

print("=" * 80)
print(" " * 30 + "TOP 5 VIDEOGIOCHI")
print("=" * 80)

# CREA LA CONNESSIONE


# CREA IL CURSORE


# --- TOP 5: Videogiochi piu RECENTI ---
print("\nTOP 5 - Videogiochi piu RECENTI:")
print("-" * 80)

# SCRIVI LA QUERY per prendere i 5 videogiochi piu recenti
# Ordina per anno_uscita decrescente e limita a 5
query_recenti = "________"

cursore.execute(query_recenti)
top_recenti = cursore.fetchall()

posizione = 1
for gioco in top_recenti:
    print(f"{posizione}. {gioco[0]} ({gioco[1]}) - {gioco[2]}")
    posizione += 1

# --- TOP 5: Videogiochi piu COSTOSI ---
print("\nTOP 5 - Videogiochi piu COSTOSI:")
print("-" * 80)

query_costosi = "SELECT titolo, prezzo, genere FROM videogiochi ORDER BY ________ DESC LIMIT ________"
#                                                                  prezzo           5

cursore.execute(________)
top_costosi = cursore.fetchall()

posizione = 1
for gioco in top_costosi:
    print(f"{posizione}. {gioco[0]}: €{gioco[1]:.2f} ({gioco[2]})")
    posizione += 1

# --- TOP 5: Videogiochi piu ECONOMICI (escludendo i gratuiti) ---
print("\nTOP 5 - Videogiochi piu ECONOMICI (escludendo gratuiti):")
print("-" * 80)

# SCRIVI LA QUERY per prendere i 5 piu economici MA escludendo quelli con prezzo = 0
# Usa WHERE prezzo > 0
query_economici = "________"

cursore.execute(query_economici)
top_economici = cursore.fetchall()

posizione = 1
for gioco in top_economici:
    print(f"{posizione}. {________}: €{________:.2f}")
    #      gioco[0] (titolo)    gioco[1] (prezzo)
    posizione += 1

# --- CLASSIFICA: Sviluppatori con piu giochi ---
print("\nTOP SVILUPPATORI (con piu giochi in catalogo):")
print("-" * 80)

query_sviluppatori = "SELECT sviluppatore, COUNT(*) as num_giochi FROM videogiochi GROUP BY sviluppatore ORDER BY num_giochi DESC LIMIT 5"
cursore.execute(query_sviluppatori)
top_sviluppatori = cursore.fetchall()

posizione = 1
for sviluppatore in top_sviluppatori:
    print(f"{posizione}. {sviluppatore[0]}: {sviluppatore[1]} giochi")
    posizione += 1

# --- GIOCHI COMPRESI TRA 20 E 40 EURO ---
print("\nVideogiochi nella fascia 20-40€:")
print("-" * 80)

# Usa WHERE con BETWEEN o con due condizioni
query_fascia = "SELECT titolo, prezzo FROM videogiochi WHERE prezzo BETWEEN 20 AND 40 ORDER BY prezzo"
cursore.execute(query_fascia)
fascia_prezzo = cursore.fetchall()

if len(fascia_prezzo) > 0:
    for gioco in fascia_prezzo:
        print(f"  {gioco[0]}: €{gioco[1]:.2f}")
else:
    print("  Nessun videogioco in questa fascia di prezzo")

print("\n" + "=" * 80)

# CHIUDI CURSORE E CONNESSIONE



"""
COSA ABBIAMO IMPARATO:
1. ORDER BY campo ASC/DESC per ordinare risultati
2. LIMIT n per limitare il numero di risultati
3. Combinare ORDER BY e LIMIT per creare Top N
4. BETWEEN per cercare valori in un intervallo
5. WHERE prezzo > 0 per escludere valori specifici
6. Usare as alias per rendere le query piu leggibili

ESEMPI UTILI:
- Top 10: ORDER BY campo DESC LIMIT 10
- Bottom 10: ORDER BY campo ASC LIMIT 10
- Intervallo: WHERE campo BETWEEN min AND max
- Multipli criteri: WHERE campo > 0 AND campo < 100

APPLICAZIONI PRATICHE:
- Classifiche e ranking
- Ricerche filtrate
- Dashboard e report
- Analisi dati
"""
