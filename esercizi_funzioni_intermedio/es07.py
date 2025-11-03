# SFIDA! Se questo esercizio ti sembra troppo difficile, puoi passare al successivo
# Riepilogo es04, es05 e es06
""" SCOPO: Crea una funzione che analizza un prezzo e calcola diverse informazioni.

Definisci la funzione:
- Nome: analizza_prezzo
- Parametri: prezzo, iva_percentuale=22
- RESTITUISCE (con return multiplo):
  1. L'importo dell'IVA: prezzo * iva_percentuale / 100
  2. Il prezzo finale con IVA: prezzo + importo_iva
  3. Il prezzo arrotondato: int(prezzo_finale)

Il programma deve:
- Chiedere all'utente di inserire un prezzo (converti in float)
- Chiedere se vuole specificare una percentuale IVA personalizzata (si/no)
  * Se "si": chiedi la percentuale (converti in float)
  * Se "no": usa il valore default (22)
- Chiamare la funzione analizza_prezzo con i parametri appropriati
- Fare l'unpacking dei 3 valori restituiti
- Stampare:
  * "Prezzo base: [prezzo]"
  * "IVA ([percentuale]%): [importo_iva]"
  * "Prezzo finale: [prezzo_finale]"
  * "Prezzo arrotondato: [prezzo_arrotondato]"

Suggerimento: ricorda di gestire il parametro default quando chiami la funzione """
