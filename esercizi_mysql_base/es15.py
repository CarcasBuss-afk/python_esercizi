# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
RIEPILOGO DELETE - Eliminare un videogioco scelto dall'utente.
Con doppia conferma per sicurezza!
"""

import mysql.connector

print("=== ELIMINA VIDEOGIOCO (con conferma) ===\n")

# CREA LA CONNESSIONE


# CREA IL CURSORE


# Mostra tutti i videogiochi
print("Catalogo videogiochi:\n")
cursore.execute("SELECT id, titolo, sviluppatore, anno_uscita, prezzo FROM videogiochi")
tutti = cursore.fetchall()

for gioco in tutti:
    print(f"ID {gioco[0]}: {gioco[1]} - {gioco[2]} ({gioco[3]}) - €{gioco[4]}")

print(f"\nTotale videogiochi: {len(tutti)}")

# CHIEDI L'ID DA ELIMINARE
id_da_eliminare = int(input("\nInserisci l'ID del videogioco da eliminare (0 per annullare): "))

if id_da_eliminare == 0:
    print("Operazione annullata.")
else:
    # Verifica che esista
    query_select = "SELECT * FROM videogiochi WHERE id = %s"
    cursore.execute(query_select, (________,))
    gioco = cursore.fetchone()

    if gioco is None:
        print(f"\nErrore: ID {id_da_eliminare} non trovato!")
    else:
        # Mostra i dettagli del videogioco da eliminare
        print(f"\n{'='*50}")
        print("ATTENZIONE! Stai per eliminare:")
        print(f"{'='*50}")
        print(f"  ID: {gioco[0]}")
        print(f"  Titolo: {gioco[1]}")
        print(f"  Sviluppatore: {gioco[2]}")
        print(f"  Anno: {gioco[3]}")
        print(f"  Prezzo: €{gioco[4]}")
        print(f"  Genere: {gioco[5]}")
        print(f"{'='*50}")

        # PRIMA CONFERMA
        conferma1 = input("\nSei sicuro di voler eliminare questo videogioco? (si/no): ")

        if conferma1.lower() == 'si':
            # SECONDA CONFERMA
            conferma2 = input("ULTIMA CONFERMA - L'operazione e irreversibile! Procedere? (ELIMINA/annulla): ")

            if conferma2 == 'ELIMINA':
                # ESEGUI IL DELETE
                query_delete = "DELETE FROM videogiochi WHERE id = %s"
                cursore.execute(________, (________,))

                # FAI IL COMMIT


                if cursore.rowcount > 0:
                    print(f"\n'{gioco[1]}' e stato eliminato dal database.")
                else:
                    print("\nErrore: nessun record eliminato.")

                # Mostra il nuovo totale
                cursore.execute("SELECT COUNT(*) FROM videogiochi")
                nuovo_totale = cursore.fetchone()[0]
                print(f"Videogiochi rimanenti: {nuovo_totale}")
            else:
                print("\nOperazione annullata.")
        else:
            print("\nOperazione annullata.")

# CHIUDI CURSORE E CONNESSIONE



"""
COSA ABBIAMO IMPARATO:
1. Doppia conferma per operazioni pericolose
2. Mostrare sempre i dettagli di cosa si sta per eliminare
3. Dare opzioni di uscita (0 per annullare, 'annulla', ecc.)
4. Verificare sempre che rowcount > 0 dopo DELETE
5. COUNT(*) per contare i record rimanenti

PATTERN DI SICUREZZA:
1. Verifica che il record esista
2. Mostra i dettagli
3. Prima conferma (si/no)
4. Seconda conferma (parola chiave come 'ELIMINA')
5. Esegui solo se tutto confermato
6. Verifica il risultato

Questo e il modo PROFESSIONALE di gestire DELETE!
Mai eliminare dati senza conferma dell'utente.
"""
