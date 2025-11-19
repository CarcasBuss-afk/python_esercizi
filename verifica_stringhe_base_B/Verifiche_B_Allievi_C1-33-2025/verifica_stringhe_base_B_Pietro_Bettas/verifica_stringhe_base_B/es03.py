# Riepilogo len()

""" SCOPO: Chiedi all'utente di inserire il nome di un prodotto e la sua descrizione (due input separati).
Calcola la lunghezza di entrambi.
Stampa "Prodotto: [prodotto], Lunghezza: [lunghezza_prodotto]"
Stampa "Descrizione: [descrizione], Lunghezza: [lunghezza_descrizione]" """
prodotto = input("inserisci il nome del prodotto: ")
descrizione = input("descrivi il prodotto: ")
lunghezza_prodotto = len(prodotto)
lunghezza_descrizione = len(descrizione)
print(f" prodotto: {prodotto}, lunghezza: {lunghezza_prodotto}")
print(f" descrizione: {descrizione}, lunghezza: {lunghezza_descrizione}")

""" Output atteso (esempio):
Inserisci il nome del prodotto: Notebook
Inserisci la descrizione: Computer portatile
Prodotto: Notebook, Lunghezza: 8
Descrizione: Computer portatile, Lunghezza: 18
"""

# Scrivi il codice qui sotto

