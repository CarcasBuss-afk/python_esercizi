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
Titolo = input("Inserisci il titolo di un libro: ")
Autore = input("Inserisci l'autore del libro : ")
Anno = input("Inserisci l'anno di pubblicazione del libro: ")

scheda = Titolo + ", " + Autore + ", " + Anno

print(scheda)