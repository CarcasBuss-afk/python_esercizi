# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
RIEPILOGO INSERT - Inserire un videogioco chiedendo i dati all'utente.
Questo e un'applicazione pratica e interattiva!
"""

import mysql.connector

print("=== AGGIUNGI UN NUOVO VIDEOGIOCO ===\n")

# CHIEDI ALL'UTENTE I DATI DEL VIDEOGIOCO
titolo = input("Titolo del videogioco: ")
sviluppatore = input("Sviluppatore: ")
anno = int(input("Anno di uscita: "))
prezzo = float(input("Prezzo (€): "))
genere = input("Genere: ")

print(f"\nStai per inserire: {titolo} ({anno})")

# CREA LA CONNESSIONE AL DATABASE


# CREA IL CURSORE


# CREA LA QUERY INSERT (usa %s per i segnaposto!)


# CREA LA TUPLA CON I VALORI DELL'UTENTE


# ESEGUI LA QUERY


# FAI IL COMMIT


# Messaggio di conferma
print(f"\n'{titolo}' e stato aggiunto al database!")
print(f"ID assegnato: {cursore.lastrowid}")  # lastrowid ci da l'ID auto-generato!

# CHIUDI CURSORE E CONNESSIONE



print("\nOperazione completata!")

"""
COSA ABBIAMO IMPARATO:
1. Come prendere input dall'utente per il database
2. Conversione tipi: int() per anno, float() per prezzo
3. lastrowid ci da l'ID del record appena inserito
4. Creazione di un'applicazione interattiva

MIGLIORAMENTI POSSIBILI (per il futuro):
- Validare l'input (anno valido, prezzo positivo, ecc.)
- Gestire errori con try/except
- Chiedere conferma prima di inserire
"""
