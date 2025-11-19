# Riepilogo len()

""" SCOPO: Chiedi all'utente di inserire il nome di un prodotto e la sua descrizione (due input separati).
Calcola la lunghezza di entrambi.
Stampa "Prodotto: [prodotto], Lunghezza: [lunghezza_prodotto]"
Stampa "Descrizione: [descrizione], Lunghezza: [lunghezza_descrizione]" """

""" Output atteso (esempio):
Inserisci il nome del prodotto: Notebook
Inserisci la descrizione: Computer portatile
Prodotto: Notebook, Lunghezza: 8
Descrizione: Computer portatile, Lunghezza: 18
"""

# Scrivi il codice qui sotto

prodotto = input("Inserisci il nome del prodotto: ")
descrizione = input("Inserisci la descrizione: ")
lunghezza_prodotto = len(prodotto)
lunghezza_descrizione = len(descrizione)
print(f"Prodotto: {prodotto}, Lunghezza: {lunghezza_prodotto}")
print(f"Descrizione: {descrizione}, Lunghezza: {lunghezza_descrizione}")