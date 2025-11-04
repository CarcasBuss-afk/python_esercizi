# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" Riepilogo: funzioni con return

Crea un programma per calcolare statistiche di un gioco.

Definisci queste funzioni:

1. calcola_punteggio_totale(livello1, livello2, livello3)
   - RESTITUISCE la somma dei tre punteggi

2. calcola_media_punteggi(totale, numero_livelli)
   - RESTITUISCE la media (totale / numero_livelli)

3. verifica_vittoria(punteggio_totale)
   - Se punteggio_totale >= 150: RESTITUISCE "Hai vinto!"
   - Altrimenti: RESTITUISCE "Riprova"

Il programma deve:
- Chiedere i punteggi dei 3 livelli
- Chiamare calcola_punteggio_totale e salvare il risultato
- Chiamare calcola_media_punteggi e salvare il risultato
- Chiamare verifica_vittoria e salvare il risultato
- Stampare: punteggio totale, media, e messaggio vittoria
"""

# DEFINISCI LE FUNZIONI QUI

def calcola_punteggio_totale(livello1, livello2, livello3):
   totale = livello1 + livello2 + livello3
   return totale

def calcola_media_punteggi(totale, numero_livelli):
   media = totale / numero_livelli
   return media

def verifica_vittoria(punteggio_totale):
   if punteggio_totale >= 150:
      return "Hai vinto"
   else:
      return "Riprova"


# SCRIVI IL PROGRAMMA PRINCIPALE QUI

l1 = int(input("Inserisci il punteggio fatto nel primo livello: "))
l2 = int(input("Inserisci il punteggio fatto nel secondo livello: "))
l3 = int(input("Inserisci il punteggio fatto nel terzo livello: "))
risultato = calcola_punteggio_totale(l1, l2, l3)
print(f"Il totale dei punti fatti nei 3 livelli è: {risultato}")

media = calcola_media_punteggi(risultato, 3)
print(f"La media del totale dei punti è: {media}")

verifica = verifica_vittoria(risultato)
print(verifica)




