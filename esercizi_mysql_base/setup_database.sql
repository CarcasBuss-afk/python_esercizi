-- Script per creare il database e la tabella videogiochi
-- Eseguire questo script PRIMA di iniziare gli esercizi Python

-- Crea il database (se non esiste già)
CREATE DATABASE IF NOT EXISTS videogame_db;

-- Seleziona il database
USE videogame_db;

-- Crea la tabella videogiochi
CREATE TABLE IF NOT EXISTS videogiochi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titolo VARCHAR(100) NOT NULL,
    sviluppatore VARCHAR(100),
    anno_uscita INT,
    prezzo DECIMAL(5,2),
    genere VARCHAR(50)
);

-- Messaggio di conferma
SELECT 'Database e tabella creati con successo!' AS Messaggio;
