# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" Riepilogo: funzioni con parametri multipli

Crea un programma per un negozio online.

Definisci queste funzioni:

1. stampa_ordine(cliente, prodotto, quantita)
   - Stampa "Cliente: [cliente], Prodotto: [prodotto], Quantità: [quantita]"

2. calcola_totale(prezzo, quantita, sconto)
   - Stampa "Totale: €[totale]"
   - Formula: totale = (prezzo * quantita) - sconto

3. verifica_disponibilita(quantita_richiesta, quantita_magazzino)
   - Se quantita_richiesta <= quantita_magazzino: stampa "Prodotto disponibile"
   - Altrimenti: stampa "Prodotto non disponibile"

Il programma deve:
- Chiedere: nome cliente, nome prodotto, prezzo, quantità richiesta, sconto, quantità in magazzino
- Chiamare stampa_ordine con i dati del cliente
- Chiamare calcola_totale per il prezzo finale
- Chiamare verifica_disponibilita per controllare la disponibilità
"""

# DEFINISCI LE FUNZIONI QUI
def stampa_ordine(cliente, prodotto, quantita):
   print(f"Cliente: {cliente}, prodotto: {prodotto}, quantità: {quantita} ")

def calcola_totale(prezzo, quantita, sconto):
   totale = (prezzo * quantita) - sconto
   print(f"Totale {totale}")
   
def verifica_disponibilita(quantita_richiesta, quantita_magazzino):
   if quantita_richiesta <= quantita_magazzino: 
      print("Prodotto disponibile")




# SCRIVI IL PROGRAMMA PRINCIPALE QUI
nome_input = input("inserisci il nome del cliente: ")
nome_prodotto = input("inserisci il nome del prodotto: ") 
prezzo_input = input("inserisci il prezzo: ") 
quantita_input = input("inserisci la quantita richiesta: ") 
sconto_input = input("inserisci lo sconto: ") 
magazzino_input = input("inserisci la quantita in magazzino: ")
nome = nome_input
prodotto1 = nome_prodotto
prezzo1 = prezzo_input
magazzino1 = magazzino_input
stampa_ordine(nome)
calcola_totale(prezzo1)
verifica_disponibilita(magazzino1)










