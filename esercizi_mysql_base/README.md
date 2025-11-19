# Esercizi MySQL Base - Gestione Database Videogiochi

Questa cartella contiene 20 esercizi progressivi per imparare a usare **MySQL con Python** attraverso la libreria `mysql-connector-python`.

## Prerequisiti

Prima di iniziare gli esercizi, assicurati di avere:

- Python 3.x installato
- MySQL Server installato (XAMPP, MySQL Workbench, o standalone)
- Conoscenze base di SQL (SELECT, INSERT, UPDATE, DELETE)

## Setup Iniziale

### 1. Installare la libreria mysql-connector-python

Apri il terminale/prompt dei comandi e digita:

```bash
pip install mysql-connector-python
```

### 2. Avviare MySQL Server

- Se usi **XAMPP**: Avvia Apache e MySQL dal pannello di controllo
- Se usi **MySQL standalone**: Assicurati che il servizio MySQL sia attivo

### 3. Creare il database e la tabella

Esegui questi script SQL in ordine (usando phpMyAdmin, MySQL Workbench, o terminale):

**Primo script** - `setup_database.sql`:
```bash
mysql -u root -p < setup_database.sql
```

**Secondo script** - `insert_data.sql`:
```bash
mysql -u root -p < insert_data.sql
```

Oppure copia-incolla il contenuto degli script in phpMyAdmin.

### 4. Configurare le credenziali

1. Copia il file `config_esempio.py` e rinominalo in `config.py`
2. Apri `config.py` e modifica le credenziali con le tue:
   ```python
   DB_USER = 'root'        # Il tuo username MySQL
   DB_PASSWORD = ''        # La tua password (vuota per XAMPP default)
   ```

**IMPORTANTE**: NON condividere il file `config.py` perche contiene la tua password!

## Struttura Database

**Nome Database**: `videogame_db`

**Tabella**: `videogiochi`

| Campo | Tipo | Descrizione |
|-------|------|-------------|
| id | INT | ID auto-incrementale (PRIMARY KEY) |
| titolo | VARCHAR(100) | Nome del videogioco |
| sviluppatore | VARCHAR(100) | Casa sviluppatrice |
| anno_uscita | INT | Anno di pubblicazione |
| prezzo | DECIMAL(5,2) | Prezzo in euro |
| genere | VARCHAR(50) | Genere (RPG, Azione, ecc.) |

## Progressione Esercizi

### Blocco 1: Setup e Connessione (es01-03)
Impara a connetterti al database MySQL da Python.

### Blocco 2: INSERT - Inserimento Dati (es04-06)
Impara a inserire nuovi videogiochi nel database.

### Blocco 3: SELECT - Lettura Dati (es07-09)
Impara a leggere e visualizzare i dati dal database.

### Blocco 4: UPDATE - Modifica Dati (es10-12)
Impara a modificare i dati esistenti.

### Blocco 5: DELETE - Cancellazione Dati (es13-15)
Impara a eliminare record dal database.

### Blocco 6: Query Avanzate (es16-18)
Impara a usare COUNT, AVG, ORDER BY, LIMIT.

### Blocco 7: Applicazioni Complete (es19-20)
Crea applicazioni CRUD complete e interattive.

## Come Eseguire gli Esercizi

```bash
# Dalla cartella esercizi_mysql_base/
python es01.py
python es02.py
# ... e cosi via
```

## Risoluzione Problemi

### Errore: "Access denied for user"
- Verifica username e password in `config.py`
- Se usi XAMPP, la password di default e vuota

### Errore: "Unknown database 'videogame_db'"
- Esegui lo script `setup_database.sql` per creare il database

### Errore: "No module named 'mysql.connector'"
- Installa la libreria: `pip install mysql-connector-python`

### Errore: "Can't connect to MySQL server"
- Assicurati che MySQL Server sia in esecuzione
- Controlla che il servizio MySQL sia avviato

## Note Importanti

- Chiudi sempre le connessioni al database con `connessione.close()`
- Usa `cursor.close()` dopo aver finito di usare il cursore
- Ricorda di fare `connessione.commit()` dopo INSERT, UPDATE, DELETE
- Non committare il file `config.py` su git (contiene credenziali!)

## Risorse Utili

- [Documentazione mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/)
- [Tutorial MySQL](https://www.w3schools.com/mysql/)
- [SQL Cheat Sheet](https://www.sqltutorial.org/sql-cheat-sheet/)

Buon lavoro! 🚀
