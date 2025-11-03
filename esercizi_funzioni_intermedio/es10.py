# SFIDA! Se questo esercizio ti sembra troppo difficile, puoi passare al successivo
# Riepilogo es08 e es09
""" SCOPO: Crea un sistema di calcolo sconto con funzioni che si chiamano tra loro.

Definisci queste funzioni:

1. calcola_sconto(prezzo, percentuale)
   - RESTITUISCE: prezzo * percentuale / 100

2. applica_sconto(prezzo, percentuale)
   - Chiama calcola_sconto(prezzo, percentuale) per ottenere l'importo dello sconto
   - RESTITUISCE: prezzo - importo_sconto

3. aggiungi_iva(prezzo, iva_percentuale=22)
   - RESTITUISCE: prezzo + (prezzo * iva_percentuale / 100)

4. calcola_prezzo_finale(prezzo_iniziale, sconto_percentuale, iva_percentuale=22)
   - Chiama applica_sconto(prezzo_iniziale, sconto_percentuale) → prezzo_scontato
   - Chiama aggiungi_iva(prezzo_scontato, iva_percentuale) → prezzo_finale
   - RESTITUISCE: prezzo_finale

Il programma deve:
- Chiedere all'utente il prezzo iniziale (converti in float)
- Chiedere la percentuale di sconto (converti in float)
- Chiedere se vuole specificare una percentuale IVA personalizzata (si/no)
  * Se "si": chiedi la percentuale IVA
  * Se "no": usa il default (22)
- Chiamare calcola_prezzo_finale con i parametri appropriati
- Stampare:
  * "Prezzo iniziale: [prezzo_iniziale] €"
  * "Prezzo finale: [prezzo_finale] €"

Suggerimento: ogni funzione ha un compito specifico e alcune funzioni chiamano altre funzioni! """
