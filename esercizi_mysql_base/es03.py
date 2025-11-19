# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Esercizio di RIEPILOGO - Connessione completa con verifica.
Scrivi tu tutto il codice per connetterti al database e verificare
che la tabella videogiochi esista!
"""

# IMPORTA LA LIBRERIA NECESSARIA


print("=== VERIFICA CONNESSIONE E TABELLA ===\n")

# CREA LE VARIABILI PER I PARAMETRI DI CONNESSIONE
# (host, user, password, database)


# CREA LA CONNESSIONE AL DATABASE


print("Connessione riuscita al database videogame_db!")

# Ora verifichiamo che la tabella 'videogiochi' esista
# Per farlo usiamo un CURSORE (lo vedremo meglio nei prossimi esercizi)
cursore = connessione.cursor()

# Questa query mostra tutte le tabelle nel database
cursore.execute("SHOW TABLES")

# Prendiamo i risultati
tabelle = cursore.fetchall()

print("\nTabelle presenti nel database:")
for tabella in tabelle:
    print(f"- {tabella[0]}")

# CHIUDI IL CURSORE


# CHIUDI LA CONNESSIONE


print("\nVerifica completata! Tutto pronto per gli esercizi successivi.")

"""
COSA ABBIAMO IMPARATO:
1. Come connettersi al database
2. Come usare un cursore per eseguire query
3. Come verificare l'esistenza di tabelle
4. Sempre chiudere cursore E connessione

PROSSIMI PASSI:
- Nei prossimi esercizi impareremo a inserire dati (INSERT)
- Poi a leggerli (SELECT)
- Modificarli (UPDATE)
- Ed eliminarli (DELETE)
"""
