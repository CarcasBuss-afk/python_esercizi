-- Script per inserire i dati iniziali nella tabella videogiochi
-- Eseguire DOPO aver creato il database con setup_database.sql

USE videogame_db;

-- Inserisce 10 videogiochi popolari
INSERT INTO videogiochi (titolo, sviluppatore, anno_uscita, prezzo, genere) VALUES
('The Legend of Zelda', 'Nintendo', 2017, 59.99, 'Avventura'),
('Minecraft', 'Mojang', 2011, 26.99, 'Sandbox'),
('Fortnite', 'Epic Games', 2017, 0.00, 'Battle Royale'),
('FIFA 24', 'EA Sports', 2023, 69.99, 'Sport'),
('Call of Duty', 'Activision', 2023, 69.99, 'Sparatutto'),
('GTA V', 'Rockstar', 2013, 29.99, 'Azione'),
('Among Us', 'InnerSloth', 2018, 4.99, 'Party'),
('Valorant', 'Riot Games', 2020, 0.00, 'Sparatutto'),
('Pokemon Scarlet', 'Nintendo', 2022, 59.99, 'RPG'),
('Elden Ring', 'FromSoftware', 2022, 59.99, 'RPG');

-- Messaggio di conferma
SELECT 'Dati inseriti con successo!' AS Messaggio;
SELECT COUNT(*) AS 'Numero videogiochi inseriti' FROM videogiochi;
