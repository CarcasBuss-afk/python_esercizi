# SFIDA! Se questo esercizio ti sembra troppo difficile, puoi passare al successivo
# MINI-PROGETTO: Sistema di Gestione Biblioteca
""" Combina: dizionari, liste, validazione, funzioni composte

Crea un sistema per gestire una piccola biblioteca di libri.

Definisci queste funzioni:

1. crea_libro(titolo, autore, anno, disponibile=True)
   - RESTITUISCE un dizionario con queste chiavi
   - disponibile indica se il libro è in biblioteca o prestato

2. aggiungi_libro(biblioteca, libro)
   - biblioteca è una lista di dizionari libro
   - Aggiunge il libro alla lista
   - Stampa "Libro aggiunto: [titolo]"

3. mostra_tutti_libri(biblioteca)
   - Stampa tutti i libri numerati con tutte le informazioni
   - Indica se ogni libro è disponibile o in prestito

4. cerca_per_autore(biblioteca, autore)
   - RESTITUISCE una lista con i libri di quell'autore
   - Confronto case-insensitive (usa .lower())

5. presta_libro(biblioteca, indice)
   - indice è la posizione del libro nella lista (0, 1, 2...)
   - Cambia disponibile a False
   - Stampa "Libro prestato: [titolo]"
   - Se indice non valido: stampa "Libro non trovato"

6. restituisci_libro(biblioteca, indice)
   - Cambia disponibile a True
   - Stampa "Libro restituito: [titolo]"

7. conta_disponibili(biblioteca)
   - RESTITUISCE il numero di libri con disponibile=True

Il programma deve avere un menu:
1. Aggiungi libro
2. Mostra tutti i libri
3. Cerca per autore
4. Presta libro
5. Restituisci libro
6. Statistiche (totali, disponibili, in prestito)
7. Esci

Il programma deve:
- Creare una lista vuota per la biblioteca
- Mostrare il menu in loop
- Chiamare le funzioni appropriate in base alla scelta
- Validare gli input dove necessario

Esempio output:
  === BIBLIOTECA ===
  1. "1984" di George Orwell (1949) - Disponibile
  2. "Il Signore degli Anelli" di J.R.R. Tolkien (1954) - In prestito

  Totale libri: 2
  Disponibili: 1
  In prestito: 1

Suggerimento: parti creando le funzioni una alla volta e testale! """
