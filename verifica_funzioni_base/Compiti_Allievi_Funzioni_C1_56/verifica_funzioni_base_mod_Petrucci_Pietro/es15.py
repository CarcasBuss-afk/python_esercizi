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
   totale = ((prezzo * quantita) - sconto) 
   print(f"Totale: €{totale}")
   
def verifica_disponibilita(quantita_richiesta, quantita_magazzino):
   if quantita_richiesta <= quantita_magazzino:
      print("Prodotto disponibile")
   else:
      print("Prodotto non disponibile")
      

nome_input = input("Inserisci il tuo nome: ")

prodotto_input = input("Inserisci il prodotto: ")

prezzo_input = int(input("Inserisci il prezzo: "))


quantita_richiesta_input = int(input("Inserisci la quantità richiesta: "))


sconto_input = int(input("Inserisci lo sconto in euro: "))

quantita_magazzino_input = int(input("Inserisci la quantità in magazzino: "))


# SCRIVI IL PROGRAMMA PRINCIPALE QUI


stampa_ordine(nome_input,prodotto_input,quantita_richiesta_input)

calcola_totale(prezzo_input,quantita_richiesta_input,sconto_input)

verifica_disponibilita(quantita_richiesta_input,quantita_magazzino_input)





