# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
RIEPILOGO UPDATE - Modificare un videogioco scelto dall'utente.
Mostrare i dati prima e dopo la modifica.
"""

import mysql.connector

print("=== MODIFICA VIDEOGIOCO ===\n")

# CREA LA CONNESSIONE


# CREA IL CURSORE


# Mostra tutti i videogiochi con ID
print("Videogiochi disponibili:")
cursore.execute("SELECT id, titolo, sviluppatore, prezzo FROM videogiochi")
tutti = cursore.fetchall()

for gioco in tutti:
    print(f"ID {gioco[0]}: {gioco[1]} - {gioco[2]} - €{gioco[3]}")

# CHIEDI ALL'UTENTE QUALE VIDEOGIOCO MODIFICARE
id_da_modificare = int(input("\nInserisci l'ID del videogioco da modificare: "))

# Mostra i dati attuali del videogioco scelto
query_select = "SELECT * FROM videogiochi WHERE id = %s"
cursore.execute(query_select, (________,))
gioco_attuale = cursore.fetchone()

if gioco_attuale is None:
    print("Errore: ID non trovato!")
else:
    print(f"\nDati attuali:")
    print(f"  Titolo: {gioco_attuale[1]}")
    print(f"  Sviluppatore: {gioco_attuale[2]}")
    print(f"  Anno: {gioco_attuale[3]}")
    print(f"  Prezzo: €{gioco_attuale[4]}")
    print(f"  Genere: {gioco_attuale[5]}")

    # CHIEDI I NUOVI DATI
    print("\nInserisci i nuovi dati (premi INVIO per mantenere il valore attuale):")

    nuovo_titolo = input(f"Nuovo titolo [{gioco_attuale[1]}]: ") or gioco_attuale[1]
    nuovo_sviluppatore = input(f"Nuovo sviluppatore [{gioco_attuale[2]}]: ") or gioco_attuale[2]
    nuovo_anno_input = input(f"Nuovo anno [{gioco_attuale[3]}]: ")
    nuovo_anno = int(nuovo_anno_input) if nuovo_anno_input else gioco_attuale[3]
    nuovo_prezzo_input = input(f"Nuovo prezzo [{gioco_attuale[4]}]: ")
    nuovo_prezzo = float(nuovo_prezzo_input) if nuovo_prezzo_input else gioco_attuale[4]
    nuovo_genere = input(f"Nuovo genere [{gioco_attuale[5]}]: ") or gioco_attuale[5]

    # ESEGUI L'UPDATE
    query_update = """UPDATE videogiochi
                      SET titolo = %s, sviluppatore = %s, anno_uscita = %s, prezzo = %s, genere = %s
                      WHERE id = %s"""

    # COMPLETA LA TUPLA CON I VALORI (nell'ordine della query!)
    valori = (________, ________, ________, ________, ________, ________)
    #         nuovo_titolo, sviluppatore, anno, prezzo, genere, id_da_modificare

    cursore.execute(query_update, valori)

    # FAI IL COMMIT


    print(f"\nVideogioco aggiornato! Righe modificate: {cursore.rowcount}")

    # Verifica finale
    cursore.execute(query_select, (id_da_modificare,))
    gioco_modificato = cursore.fetchone()

    print(f"\nNuovi dati:")
    print(f"  Titolo: {gioco_modificato[1]}")
    print(f"  Sviluppatore: {gioco_modificato[2]}")
    print(f"  Anno: {gioco_modificato[3]}")
    print(f"  Prezzo: €{gioco_modificato[4]}")
    print(f"  Genere: {gioco_modificato[5]}")

# CHIUDI CURSORE E CONNESSIONE



"""
COSA ABBIAMO IMPARATO:
1. UPDATE di multipli campi contemporaneamente
2. Usare 'or valore_default' per mantenere valori esistenti
3. Verificare che l'ID esista prima di modificare
4. Mostrare anteprima prima e conferma dopo la modifica
5. Validare l'input dell'utente

TRUCCO:
input("Testo: ") or default
Se l'utente preme solo INVIO (stringa vuota), usa 'default'

Questo e il pattern standard per le applicazioni CRUD!
"""
