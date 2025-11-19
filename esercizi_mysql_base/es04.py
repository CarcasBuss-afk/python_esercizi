# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

"""
SCOPO del programma:
Imparare a INSERIRE un nuovo videogioco nel database.
Usiamo il comando SQL INSERT INTO.
"""

import mysql.connector

print("=== INSERIMENTO NUOVO VIDEOGIOCO ===\n")

# Connessione al database
connessione = mysql.connector.connect(
    host='localhost',
    user='root',           # Modifica se necessario
    password='',           # Modifica se necessario
    database='videogame_db'
)

# Creiamo un cursore per eseguire le query
cursore = connessione.cursor()

# Query SQL per inserire un nuovo videogioco
# Nota: usiamo %s come segnaposto per i valori (per sicurezza!)
query = "INSERT INTO videogiochi (titolo, sviluppatore, anno_uscita, prezzo, genere) VALUES (%s, %s, %s, %s, %s)"

# I valori da inserire (in ordine!)
# Inseriamo "The Witcher 3" come esempio
valori = ('The Witcher 3', '________', ________, ________, '________')
#         titolo             sviluppatore  anno     prezzo    genere
#                           (CD Projekt)  (2015)   (39.99)   (RPG)

# Eseguiamo la query
cursore.execute(________, ________)

# IMPORTANTE! Dopo INSERT/UPDATE/DELETE dobbiamo fare COMMIT
# Il commit salva definitivamente le modifiche nel database
________.commit()

print(f"Videogioco inserito con successo!")
print(f"Righe inserite: {cursore.rowcount}")

# Chiudiamo cursore e connessione
cursore.close()
connessione.close()

print("\nDatabase aggiornato!")

"""
COSA ABBIAMO IMPARATO:
1. INSERT INTO serve per aggiungere nuovi record
2. Usiamo %s come segnaposto per i valori (previene SQL injection!)
3. I valori si passano come tupla a execute()
4. SEMPRE fare commit() dopo INSERT/UPDATE/DELETE
5. rowcount ci dice quante righe sono state modificate

NOTA DI SICUREZZA:
NON scrivere mai: f"INSERT ... VALUES ('{valore}')"
Usare SEMPRE %s e passare i valori separatamente!
"""
