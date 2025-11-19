# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
RIEPILOGO SELECT - Visualizzare i videogiochi in formato tabella elegante.
Creiamo un output bello da vedere!
"""

import mysql.connector

print("=" * 100)
print(" " * 35 + "CATALOGO VIDEOGIOCHI")
print("=" * 100)

# CREA LA CONNESSIONE


# CREA IL CURSORE


# SELEZIONA TUTTI I VIDEOGIOCHI ORDINATI PER TITOLO
# Usa ORDER BY per ordinare alfabeticamente
query = "SELECT * FROM videogiochi ORDER BY ________ ASC"
#                                            titolo (ASC = crescente)

# ESEGUI LA QUERY


# PRENDI TUTTI I RISULTATI


# Intestazione della tabella
print(f"\n{'ID':<5} {'TITOLO':<25} {'SVILUPPATORE':<20} {'ANNO':<6} {'PREZZO':<8} {'GENERE':<15}")
print("-" * 100)

# CICLO SUI RISULTATI E STAMPA IN FORMATO TABELLA
for gioco in ________:
    # Formattazione elegante con larghezze fisse
    print(f"{gioco[0]:<5} {gioco[1]:<25} {gioco[2]:<20} {gioco[3]:<6} €{gioco[4]:<7.2f} {gioco[5]:<15}")

print("-" * 100)
print(f"\nTotale videogiochi: {________}")  # Numero di risultati

# Statistiche rapide
print("\n" + "=" * 100)
print("STATISTICHE")
print("=" * 100)

# Conta quanti giochi ci sono per ogni genere
query_generi = "SELECT genere, COUNT(*) FROM videogiochi GROUP BY genere"
cursore.execute(query_generi)
generi = cursore.fetchall()

print("\nVideogiochi per genere:")
for genere in generi:
    print(f"  {genere[0]}: {genere[1]} giochi")

# CHIUDI CURSORE E CONNESSIONE



"""
COSA ABBIAMO IMPARATO:
1. ORDER BY ordina i risultati (ASC = crescente, DESC = decrescente)
2. Formattazione stringhe con {variabile:<larghezza} per output allineato
3. GROUP BY raggruppa risultati (utile con COUNT)
4. COUNT(*) conta il numero di record
5. len(risultati) ci da il numero totale di righe

FORMATTAZIONE OUTPUT:
- {valore:<10} -> allinea a sinistra, larghezza 10
- {valore:>10} -> allinea a destra
- {valore:.2f} -> numero con 2 decimali

Questo tipo di output rende l'applicazione professionale!
"""
