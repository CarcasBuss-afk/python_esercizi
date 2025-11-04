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
   print(f"Cliente: {cliente}, Prodotto: {prodotto}, Quantità: {quantita}")

def calcola_totale(prezzo, quantita, sconto):
   totale = (prezzo * quantita) - sconto
   print(f"Totale: €{totale}")

def verifica_disponibilita(quantita_richiesta, quantita_magazzino):
   if quantita_richiesta <= quantita_magazzino:
      print("Prodotto disponibile")
   else:
      print("Prodotto non disponibile")


# SCRIVI IL PROGRAMMA PRINCIPALE QUI

nome_cliente = input("Inseirsci il tuo nome: ")
nome_prodotto = input("Inserisci il nome del prodotto che desideri: ")
prezzo = int(input("Inserisci il prezzo del prodotto: "))
quantita_richiesta = int(input("Inserisci la quantita richiesta: "))
sconto = int(input("Inserisci lo sconto se disponibile: "))
quantita_magazzino = int(input("Inserisci la quantita disponibile in magazzino: "))

stampa_ordine(nome_cliente, nome_prodotto, quantita_richiesta)
calcola_totale(prezzo, quantita_richiesta, sconto)
verifica_disponibilita(quantita_richiesta, quantita_magazzino)