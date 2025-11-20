# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
RIEPILOGO - Creare da zero la funzione elenco_tutti().
Restituisce tutti i videogiochi dal database.
"""

# IMPORTA LE LIBRERIE


# CREA LA FUNZIONE connessione() (uguale a es03)


# CREA LA FUNZIONE elenco_tutti()
# La funzione deve:
# 1. Connettersi al database
# 2. Controllare if conn == None (restituire [])
# 3. Creare cursore
# 4. Eseguire SELECT * FROM videogiochi
# 5. Prendere i risultati con fetchall()
# 6. Chiudere cursore e connessione
# 7. Restituire i risultati


print("=== TEST FUNZIONE ELENCO_TUTTI() ===\n")

# TEST
giochi = elenco_tutti()

if len(giochi) == 0:
    print("Nessun videogioco trovato!")
else:
    print(f"Trovati {len(giochi)} videogiochi:\n")
    for gioco in giochi:
        print(f"ID {gioco[0]}: {gioco[1]} - {gioco[2]}")
        print(f"  Anno: {gioco[3]} | Prezzo: €{gioco[4]} | Genere: {gioco[5]}\n")

"""
RIEPILOGO:
Hai creato elenco_tutti() che:
- Gestisce connessione e query
- Restituisce lista di tuple
- Gestisce errori (return [])

PROSSIMO: Aggiungeremo un parametro per cercare!
"""
