 # Riepilogo concatenazione
""" SCOPO: Chiedi all'utente di inserire il titolo di un libro, l'autore e l'anno di pubblicazione.
Crea una variabile 'scheda' che concatena queste informazioni nel formato:
"Titolo: [titolo], Autore: [autore], Anno: [anno]"
Stampa la scheda completa. """

""" Output atteso (esempio):
Inserisci il titolo: Il Signore degli Anelli
Inserisci l'autore: Tolkien
Inserisci l'anno: 1954
Titolo: Il Signore degli Anelli, Autore: Tolkien, Anno: 1954
"""
titolo = input("inserisci il titolo di un libro: ")
autore = input("inserisci il nome dell'autore: ")
anno_pubbl = input("inserisci l'anno in cui e stato pubblicato:")

scheda = "Titolo: "+ titolo + ", " + " Autore: "+ autore + ", " + " Anno: "+ anno_pubbl

print(scheda)
