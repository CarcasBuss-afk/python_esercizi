# SFIDA! Se questo esercizio ti sembra troppo difficile, puoi passare al successivo
# Riepilogo es01 e es02
""" SCOPO: Crea una funzione di benvenuto personalizzabile con input dell'utente.

Definisci la funzione:
- Nome: benvenuto
- Parametri: nome, lingua="italiano", formale=True
- Comportamento:
  * Se lingua è "italiano" E formale è True: stampa "Buongiorno [nome], benvenuto!"
  * Se lingua è "italiano" E formale è False: stampa "Ciao [nome]!"
  * Se lingua è "inglese" E formale è True: stampa "Good morning [nome], welcome!"
  * Se lingua è "inglese" E formale è False: stampa "Hi [nome]!"
  * Altrimenti: stampa "Hello [nome]!"

Il programma deve:
- Chiedere all'utente di inserire il nome
- Chiedere la lingua (italiano/inglese) - se l'utente preme invio senza scrivere nulla, usa "italiano"
- Chiedere se vuole un saluto formale (si/no) - se l'utente preme invio, usa "si"
- Chiamare la funzione benvenuto con i parametri appropriati

Suggerimento:
- Usa if/elif/else con condizioni multiple (and) nella funzione
- Per gestire i default degli input: if lingua == "": lingua = "italiano"
- Converti "si"/"no" in True/False prima di passarlo alla funzione

--- BONUS (solo se hai completato l'esercizio principale) ---
Aggiungi un ciclo while che permette di ripetere il programma.
Dopo ogni saluto, chiedi "Vuoi continuare? (si/no): "
Se l'utente scrive "no", esci dal programma con un messaggio di arrivederci. """
