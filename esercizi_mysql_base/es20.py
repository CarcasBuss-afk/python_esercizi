# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
ESERCIZIO FINALE - Crea un'applicazione completa di gestione videogiochi
con funzionalita avanzate:
- CRUD completo
- Ricerca avanzata
- Report e statistiche
- Esportazione dati

Questo e il tuo progetto finale! Scrivi tu la maggior parte del codice.
"""

import mysql.connector

# FUNZIONE: Connessione al database
def connetti_db():
    """Crea e restituisce connessione al database"""
    # SCRIVI IL CODICE PER CONNETTERTI AL DATABASE


# FUNZIONE: Menu principale
def mostra_menu():
    """Mostra il menu con tutte le opzioni"""
    print("\n" + "=" * 70)
    print(" " * 20 + "VIDEOGAME MANAGER PRO")
    print("=" * 70)
    print("1. Visualizza catalogo")
    print("2. Cerca per nome")
    print("3. Filtra per fascia prezzo")
    print("4. Aggiungi videogioco")
    print("5. Modifica videogioco")
    print("6. Elimina videogioco")
    print("7. Applica sconto")
    print("8. Report completo")
    print("9. Esporta in TXT")
    print("0. Esci")
    print("=" * 70)

# FUNZIONE 1: Visualizza catalogo ordinato
def visualizza_catalogo(cursore):
    """Mostra tutti i videogiochi in formato tabella"""
    print("\n" + "=" * 100)
    print(f"{'ID':<5} {'TITOLO':<30} {'SVILUPPATORE':<20} {'ANNO':<6} {'PREZZO':<10} {'GENERE':<15}")
    print("=" * 100)

    # SCRIVI LA QUERY per prendere tutti i videogiochi ordinati per titolo


    # ESEGUI LA QUERY E PRENDI I RISULTATI


    # CICLO PER STAMPARE I RISULTATI IN FORMATO TABELLA


    print("=" * 100)
    print(f"Totale videogiochi: {________}")

# FUNZIONE 2: Cerca per nome (con LIKE)
def cerca_per_nome(cursore):
    """Cerca videogiochi che contengono una parola nel titolo"""
    parola = input("\nInserisci parte del titolo da cercare: ")

    # Usa LIKE con % per cercare anche match parziali
    # Esempio: WHERE titolo LIKE '%parola%'
    query = "SELECT * FROM videogiochi WHERE titolo LIKE %s"
    cursore.execute(query, (f'%{parola}%',))

    risultati = cursore.fetchall()

    if len(risultati) > 0:
        print(f"\nTrovati {len(risultati)} risultati:")
        for gioco in risultati:
            print(f"  {gioco[1]} - {gioco[2]} ({gioco[3]}) - €{gioco[4]:.2f}")
    else:
        print("Nessun risultato trovato")

# FUNZIONE 3: Filtra per fascia prezzo
def filtra_per_prezzo(cursore):
    """Filtra videogiochi in una fascia di prezzo"""
    print("\nFiltra per fascia di prezzo:")
    min_prezzo = float(input("Prezzo minimo: "))
    max_prezzo = float(input("Prezzo massimo: "))

    # SCRIVI LA QUERY con BETWEEN o con due WHERE


    # ESEGUI E MOSTRA I RISULTATI


# FUNZIONE 4: Aggiungi con validazione
def aggiungi_videogioco(cursore, connessione):
    """Aggiungi nuovo videogioco con validazione input"""
    print("\n--- AGGIUNGI VIDEOGIOCO ---")

    titolo = input("Titolo: ")

    # Verifica se esiste gia
    cursore.execute("SELECT COUNT(*) FROM videogiochi WHERE titolo = %s", (titolo,))
    if cursore.fetchone()[0] > 0:
        print(f"ATTENZIONE: '{titolo}' esiste gia nel database!")
        return

    sviluppatore = input("Sviluppatore: ")

    # Validazione anno
    while True:
        anno = int(input("Anno di uscita (1970-2024): "))
        if 1970 <= anno <= 2024:
            break
        print("Anno non valido!")

    # Validazione prezzo
    while True:
        prezzo = float(input("Prezzo (0-999): "))
        if 0 <= prezzo <= 999:
            break
        print("Prezzo non valido!")

    genere = input("Genere: ")

    # SCRIVI ED ESEGUI LA QUERY INSERT


    print(f"'{titolo}' aggiunto con successo!")

# FUNZIONE 5: Modifica completa
def modifica_videogioco(cursore, connessione):
    """Modifica tutti i campi di un videogioco"""
    # SCRIVI IL CODICE PER:
    # 1. Mostrare tutti i videogiochi con ID
    # 2. Chiedere quale ID modificare
    # 3. Mostrare i dati attuali
    # 4. Chiedere i nuovi dati (con possibilita di mantenere i vecchi)
    # 5. Eseguire l'UPDATE
    # 6. Confermare la modifica

    pass  # Sostituisci con il tuo codice

# FUNZIONE 6: Elimina con conferma
def elimina_videogioco(cursore, connessione):
    """Elimina con doppia conferma"""
    # SCRIVI IL CODICE PER:
    # 1. Mostrare i videogiochi
    # 2. Chiedere ID da eliminare
    # 3. Mostrare dettagli
    # 4. Chiedere doppia conferma
    # 5. Eseguire DELETE
    # 6. Confermare eliminazione

    pass  # Sostituisci con il tuo codice

# FUNZIONE 7: Applica sconto percentuale
def applica_sconto(cursore, connessione):
    """Applica uno sconto percentuale a videogiochi selezionati"""
    print("\n--- APPLICA SCONTO ---")

    print("Scegli categoria da scontare:")
    print("1. Per genere")
    print("2. Per anno")
    print("3. Tutti i videogiochi")

    scelta = input("\nScelta: ")

    percentuale_sconto = float(input("Percentuale sconto (es. 20 per 20%): "))
    moltiplicatore = 1 - (percentuale_sconto / 100)

    # SCRIVI LA LOGICA PER APPLICARE LO SCONTO IN BASE ALLA SCELTA
    # Mostra anteprima e chiedi conferma prima di applicare


# FUNZIONE 8: Report completo
def genera_report(cursore):
    """Genera un report dettagliato con tutte le statistiche"""
    print("\n" + "=" * 80)
    print(" " * 25 + "REPORT COMPLETO")
    print("=" * 80)

    # Totale videogiochi
    cursore.execute("SELECT COUNT(*) FROM videogiochi")
    totale = cursore.fetchone()[0]

    # Statistiche prezzi
    cursore.execute("SELECT AVG(prezzo), MIN(prezzo), MAX(prezzo), SUM(prezzo) FROM videogiochi")
    stats_prezzo = cursore.fetchone()

    # Anno piu vecchio e piu recente
    cursore.execute("SELECT MIN(anno_uscita), MAX(anno_uscita) FROM videogiochi")
    stats_anno = cursore.fetchone()

    print(f"\nGENERALE:")
    print(f"  Totale videogiochi: {totale}")
    print(f"  Valore totale catalogo: €{stats_prezzo[3]:.2f}")

    print(f"\nPREZZI:")
    print(f"  Prezzo medio: €{stats_prezzo[0]:.2f}")
    print(f"  Piu economico: €{stats_prezzo[1]:.2f}")
    print(f"  Piu costoso: €{stats_prezzo[2]:.2f}")

    print(f"\nANNI:")
    print(f"  Videogioco piu vecchio: {stats_anno[0]}")
    print(f"  Videogioco piu recente: {stats_anno[1]}")

    # AGGIUNGI ALTRE STATISTICHE (per genere, per sviluppatore, ecc.)


    print("=" * 80)

# FUNZIONE 9: Esporta in file TXT
def esporta_txt(cursore):
    """Esporta l'intero catalogo in un file TXT"""
    nome_file = "catalogo_videogiochi.txt"

    cursore.execute("SELECT * FROM videogiochi ORDER BY titolo")
    tutti = cursore.fetchall()

    with open(nome_file, 'w', encoding='utf-8') as file:
        file.write("=" * 80 + "\n")
        file.write(" " * 25 + "CATALOGO VIDEOGIOCHI\n")
        file.write("=" * 80 + "\n\n")

        for gioco in tutti:
            file.write(f"ID: {gioco[0]}\n")
            file.write(f"Titolo: {gioco[1]}\n")
            file.write(f"Sviluppatore: {gioco[2]}\n")
            file.write(f"Anno: {gioco[3]}\n")
            file.write(f"Prezzo: €{gioco[4]:.2f}\n")
            file.write(f"Genere: {gioco[5]}\n")
            file.write("-" * 80 + "\n")

    print(f"\nCatalogo esportato in '{nome_file}'!")

# PROGRAMMA PRINCIPALE
def main():
    """Funzione principale con menu"""
    connessione = connetti_db()
    cursore = connessione.cursor()

    print("\nBenvenuto in VIDEOGAME MANAGER PRO!")

    while True:
        mostra_menu()
        scelta = input("\nScegli un'opzione: ")

        # COMPLETA IL CODICE PER CHIAMARE LE FUNZIONI GIUSTE
        if scelta == '1':
            visualizza_catalogo(cursore)
        elif scelta == '2':
            cerca_per_nome(cursore)
        elif scelta == '3':
            ________
        # ... completa gli altri casi
        elif scelta == '0':
            print("\nGrazie per aver usato Videogame Manager Pro!")
            break
        else:
            print("\nOpzione non valida!")

    cursore.close()
    connessione.close()

# Avvia il programma
if __name__ == "__main__":
    main()

"""
CONGRATULAZIONI!
Hai completato tutti i 20 esercizi su MySQL con Python!

COSA HAI IMPARATO:
1. Connessione a database MySQL
2. INSERT - Inserimento dati
3. SELECT - Lettura e ricerca
4. UPDATE - Modifica dati
5. DELETE - Eliminazione
6. Query avanzate (COUNT, AVG, GROUP BY, ORDER BY, LIMIT)
7. Applicazioni CRUD complete
8. Validazione input
9. Esportazione dati
10. Organizzazione codice con funzioni

PROSSIMI PASSI:
- Studia le relazioni tra tabelle (JOIN)
- Impara le transazioni (BEGIN, COMMIT, ROLLBACK)
- Esplora gli indici per ottimizzare le query
- Prova framework come SQLAlchemy
- Crea progetti piu complessi!

Ottimo lavoro! Continua cosi! 🚀
"""
