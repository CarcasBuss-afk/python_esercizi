# Riepilogo concatenazione

""" SCOPO: Chiedi all'utente di inserire il titolo di un libro, l'autore e l'anno di pubblicazione.
Crea una variabile 'scheda' che concatena queste informazioni nel formato:
"Titolo: [titolo], Autore: [autore], Anno: [anno]"
Stampa la scheda completa. """

titolo = input("inserisci il nome di un libro ")
autore = input("inserisci l'autore del libro ")
pubblicazione = input("inserisci l'anno di pubblicazione ")

scheda = titolo + autore + pubblicazione

print(f" il titolo del libro e {titolo} l'autore è {autore} ed è stato pubblicato il {pubblicazione}")




""" Output atteso (esempio):
Inserisci il titolo: Il Signore degli Anelli
Inserisci l'autore: Tolkien
Inserisci l'anno: 1954
Titolo: Il Signore degli Anelli, Autore: Tolkien, Anno: 1954
"""

