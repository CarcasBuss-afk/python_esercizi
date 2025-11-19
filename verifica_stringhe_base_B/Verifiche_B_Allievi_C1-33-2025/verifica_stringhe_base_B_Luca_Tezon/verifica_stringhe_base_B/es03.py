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

prodotto = input("Inserisci il nome di un prodotto ")
descrizione = input("Inserisci ladescrizione del prodotto ")
lunghezza_1 = len(prodotto)
lunghezza_2 = len(descrizione)

print(f"Il nome del prodotto {prodotto}")
print(f"Inserisci la descrizione {descrizione}")
print("Prodotto",{prodotto}, "lunghezza" , {lunghezza_1})
print("Descrizione",{descrizione} , "Lunghezza" , {lunghezza_2})

