# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Creare un MENU INTERATTIVO con tutte le operazioni CRUD:
- Create (INSERT)
- Read (SELECT)
- Update (UPDATE)
- Delete (DELETE)

Questa e un'applicazione completa di gestione database!
"""

import mysql.connector

def mostra_menu():
    """Mostra il menu principale"""
    print("\n" + "=" * 60)
    print(" " * 15 + "GESTIONE VIDEOGIOCHI")
    print("=" * 60)
    print("1. Visualizza tutti i videogiochi")
    print("2. Cerca videogioco per genere")
    print("3. Aggiungi nuovo videogioco")
    print("4. Modifica prezzo")
    print("5. Elimina videogioco")
    print("6. Statistiche")
    print("0. Esci")
    print("=" * 60)

def connetti_db():
    """Crea e restituisce la connessione al database"""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='videogame_db'
    )

def visualizza_tutti(cursore):
    """Visualizza tutti i videogiochi"""
    print("\n--- CATALOGO COMPLETO ---")
    cursore.execute("SELECT * FROM videogiochi ORDER BY titolo")
    giochi = cursore.fetchall()

    for gioco in giochi:
        print(f"ID {gioco[0]}: {gioco[1]} - {gioco[2]} ({gioco[3]}) - €{gioco[4]:.2f} [{gioco[5]}]")

    print(f"\nTotale: {len(giochi)} videogiochi")

def cerca_per_genere(cursore):
    """Cerca videogiochi per genere"""
    genere = input("\nInserisci il genere da cercare: ")

    query = "SELECT * FROM videogiochi WHERE genere = %s"
    cursore.execute(________, (________,))
    risultati = cursore.fetchall()

    if len(risultati) > 0:
        print(f"\nTrovati {len(risultati)} videogiochi di genere '{genere}':")
        for gioco in risultati:
            print(f"  {gioco[1]} - {gioco[2]} - €{gioco[4]:.2f}")
    else:
        print(f"Nessun videogioco trovato per il genere '{genere}'")

def aggiungi_videogioco(cursore, connessione):
    """Aggiunge un nuovo videogioco"""
    print("\n--- AGGIUNGI NUOVO VIDEOGIOCO ---")

    titolo = input("Titolo: ")
    sviluppatore = input("Sviluppatore: ")
    anno = int(input("Anno di uscita: "))
    prezzo = float(input("Prezzo (€): "))
    genere = input("Genere: ")

    query = "INSERT INTO videogiochi (titolo, sviluppatore, anno_uscita, prezzo, genere) VALUES (%s, %s, %s, %s, %s)"
    valori = (________, ________, ________, ________, ________)

    cursore.execute(query, valori)
    connessione.commit()

    print(f"\n'{titolo}' aggiunto con successo! ID: {cursore.lastrowid}")

def modifica_prezzo(cursore, connessione):
    """Modifica il prezzo di un videogioco"""
    print("\n--- MODIFICA PREZZO ---")

    # Mostra i videogiochi
    cursore.execute("SELECT id, titolo, prezzo FROM videogiochi ORDER BY titolo")
    for gioco in cursore.fetchall():
        print(f"ID {gioco[0]}: {gioco[1]} - €{gioco[2]:.2f}")

    id_gioco = int(input("\nID del videogioco da modificare: "))
    nuovo_prezzo = float(input("Nuovo prezzo: "))

    query = "UPDATE videogiochi SET ________ = %s WHERE ________ = %s"
    #                                prezzo              id

    cursore.execute(________, (________, ________))
    #                         nuovo_prezzo  id_gioco

    ________.commit()

    if cursore.rowcount > 0:
        print("Prezzo aggiornato con successo!")
    else:
        print("Errore: ID non trovato")

def elimina_videogioco(cursore, connessione):
    """Elimina un videogioco"""
    print("\n--- ELIMINA VIDEOGIOCO ---")

    # Mostra i videogiochi
    cursore.execute("SELECT id, titolo FROM videogiochi ORDER BY titolo")
    for gioco in cursore.fetchall():
        print(f"ID {gioco[0]}: {gioco[1]}")

    id_gioco = int(input("\nID del videogioco da eliminare (0 per annullare): "))

    if id_gioco != 0:
        conferma = input(f"Confermi l'eliminazione del videogioco ID {id_gioco}? (si/no): ")

        if conferma.lower() == 'si':
            query = "DELETE FROM videogiochi WHERE id = %s"
            cursore.execute(________, (________,))
            connessione.commit()

            if cursore.rowcount > 0:
                print("Videogioco eliminato!")
            else:
                print("Errore: ID non trovato")
        else:
            print("Operazione annullata")

def mostra_statistiche(cursore):
    """Mostra statistiche sui videogiochi"""
    print("\n--- STATISTICHE ---")

    # Totale
    cursore.execute("SELECT COUNT(*) FROM videogiochi")
    totale = cursore.fetchone()[0]
    print(f"Totale videogiochi: {totale}")

    # Prezzo medio
    cursore.execute("SELECT AVG(prezzo) FROM videogiochi")
    media = cursore.fetchone()[0]
    print(f"Prezzo medio: €{media:.2f}")

    # Per genere
    print("\nDistribuzione per genere:")
    cursore.execute("SELECT genere, COUNT(*) FROM videogiochi GROUP BY genere")
    for genere in cursore.fetchall():
        print(f"  {genere[0]}: {genere[1]} giochi")

# PROGRAMMA PRINCIPALE
def main():
    connessione = connetti_db()
    cursore = connessione.cursor()

    while True:
        mostra_menu()
        scelta = input("\nScegli un'opzione: ")

        if scelta == '1':
            visualizza_tutti(cursore)
        elif scelta == '2':
            cerca_per_genere(cursore)
        elif scelta == '3':
            aggiungi_videogioco(cursore, connessione)
        elif scelta == '4':
            modifica_prezzo(cursore, connessione)
        elif scelta == '5':
            elimina_videogioco(cursore, connessione)
        elif scelta == '6':
            mostra_statistiche(cursore)
        elif scelta == '0':
            print("\nArrivederci!")
            break
        else:
            print("\nOpzione non valida!")

    cursore.close()
    connessione.close()

# Avvia il programma
if __name__ == "__main__":
    main()

"""
COSA ABBIAMO IMPARATO:
1. Come creare un'applicazione CRUD completa
2. Usare funzioni per organizzare il codice
3. Menu interattivo con loop while True
4. Passare connessione e cursore alle funzioni
5. if __name__ == "__main__" per codice eseguibile

STRUTTURA APPLICAZIONE:
- Funzioni separate per ogni operazione
- Menu principale con loop
- Gestione input utente
- Connessione condivisa

Questo e il pattern base per TUTTE le applicazioni database!
"""
