# Correzione Verifica Funzioni Base - Bosio Fabio

Punteggio Totale: 76/100

---

## Esercizio 1
Punteggio: 4/5

Obiettivo: Creare e chiamare funzioni senza parametri (mostra_benvenuto e mostra_orari).

Analisi del codice:
Hai completato correttamente quasi tutto l'esercizio. Le definizioni delle funzioni sono corrette e hai chiamato correttamente la prima funzione.

Errore riscontrato:
Alla riga 23 manca la chiamata alla funzione mostra_orari(). La riga e rimasta vuota.

Cosa dovevi scrivere:
```python
mostra_orari()
```

Spiegazione:
Per chiamare una funzione in Python, devi scrivere il nome della funzione seguito dalle parentesi tonde. Nel tuo codice hai lasciato la riga 23 vuota invece di scrivere la chiamata alla funzione.

---

## Esercizio 2
Punteggio: 0/5

Obiettivo: Creare funzioni e richiamarle multiple volte (stampa_separatore e stampa_titolo_corso).

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia, tutti gli spazi vuoti (___) sono rimasti invariati.

Cosa dovevi fare:
1. Alla riga 9: sostituire `___` con `def` e `________________` con `stampa_separatore`
2. Alla riga 15: sostituire `___` con `def` e `__________________` con `stampa_titolo_corso`
3. Alla riga 20: sostituire `________________` con `stampa_separatore()`
4. Alla riga 23: sostituire `__________________` con `stampa_titolo_corso()`
5. Alla riga 26: sostituire `________________` con `stampa_separatore()`

Codice corretto:
```python
def stampa_separatore():
    print("------------------------")

def stampa_titolo_corso():
    print("CORSO DI PROGRAMMAZIONE PYTHON")

stampa_separatore()
stampa_titolo_corso()
stampa_separatore()
```

---

## Esercizio 3
Punteggio: 5/5

Obiettivo: Menu con funzioni e logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente tutte le funzioni, implementato la logica condizionale con if/elif/else e chiamato le funzioni nel modo giusto.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Riepilogo funzioni senza parametri - programma cinema.

Analisi del codice:
Esercizio completato correttamente. Hai definito tutte le funzioni richieste e le hai chiamate nel programma principale.

Hai scelto di strutturare l'output in modo diverso (con print multipli separati) rispetto alla consegna, ma le funzioni contengono tutte le informazioni richieste e il programma funziona correttamente. Le funzioni sono ben definite e chiamate correttamente.

---

## Esercizio 5
Punteggio: 5/5

Obiettivo: Funzioni con un parametro.

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente le funzioni con parametri, completato i calcoli e chiamato le funzioni passando i parametri corretti.

---

## Esercizio 6
Punteggio: 5/5

Obiettivo: Funzioni con parametro e calcoli.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le funzioni calcola_area_quadrato e converti_euro_dollari, con i relativi calcoli e le chiamate corrette.

---

## Esercizio 7
Punteggio: 5/5

Obiettivo: Funzioni con logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica condizionale con if/else e if/elif/else e il programma funziona correttamente.

Nota: Alla riga 10 hai scritto `verifica_maggiorene` invece di `verifica_maggiorenne` (manca una 'n'), ma hai mantenuto la coerenza chiamando la funzione con lo stesso nome alla riga 34, quindi il codice funziona. In futuro, fai attenzione all'ortografia.

---

## Esercizio 8
Punteggio: 5/5

Obiettivo: Riepilogo funzioni con un parametro - gestione abbonamenti palestra.

Analisi del codice:
Esercizio completato correttamente. Hai definito tutte le funzioni richieste, implementato la logica condizionale e scritto il programma principale che chiama tutte le funzioni con i parametri corretti.

Il codice funziona perfettamente. Hai organizzato il programma principale insieme alle definizioni delle funzioni invece di separarlo, ma questo non compromette la funzionalita.

---

## Esercizio 9
Punteggio: 5/5

Obiettivo: Funzioni con due parametri.

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente le funzioni con due parametri, implementato i calcoli e chiamato le funzioni nel modo giusto.

---

## Esercizio 10
Punteggio: 5/5

Obiettivo: Funzioni con tre parametri.

Analisi del codice:
Esercizio completato perfettamente. Hai gestito correttamente le funzioni con tre parametri, implementando sia i calcoli (media) che l'output formattato.

---

## Esercizio 11
Punteggio: 5/5

Obiettivo: Funzioni con parametri e calcoli.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le formule matematiche richieste (perimetro rettangolo e totale con IVA).

---

## Esercizio 12
Punteggio: 5/5

Obiettivo: Funzioni con parametri e logica.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica condizionale (verifica login con AND, confronto numeri con if/elif/else).

---

## Esercizio 13
Punteggio: 5/5

Obiettivo: Funzioni con piu parametri e calcoli complessi.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le formule matematiche (tempo di viaggio e calorie bruciate).

---

## Esercizio 14
Punteggio: 2/5

Obiettivo: Funzioni con validazione.

Analisi del codice:
Hai iniziato l'esercizio ma ci sono errori logici gravi che impediscono al codice di funzionare correttamente.

Errori riscontrati:

1. Parametri della funzione (riga 23):
   - Cosa hai scritto: `def calcola_sconto_eta(prezzo, eta, ):`
   - Problema: C'e una virgola extra dopo "eta"
   - Cosa dovevi scrivere:
   ```python
   def calcola_sconto_eta(prezzo, eta):
   ```

2. Ordine delle istruzioni (righe 25-26 e 28-29):
   - Cosa hai scritto:
   ```python
   print("Prezzo scontato €", sconto)
   sconto = prezzo - (prezzo * 20 / 100)
   ```
   - Problema: Stai usando la variabile `sconto` nel print PRIMA di averla definita. Python legge il codice dall'alto verso il basso, quindi quando arriva al print, la variabile `sconto` non esiste ancora e il programma da errore
   - Cosa dovevi scrivere:
   ```python
   sconto = prezzo - (prezzo * 20 / 100)
   print("Prezzo scontato: €", sconto)
   ```
   Nota l'ordine: prima CALCOLI il valore, poi lo STAMPI.

3. Caso else mancante:
   - Problema: La tua funzione gestisce solo i casi eta < 18 e eta >= 65, ma non gestisce il caso intermedio (18 <= eta < 65)
   - Cosa dovevi scrivere: aggiungere un else dopo l'elif:
   ```python
   else:
       print("Prezzo pieno: €", prezzo)
   ```

Codice corretto completo:
```python
def calcola_sconto_eta(prezzo, eta):
    if eta < 18:
        sconto = prezzo - (prezzo * 20 / 100)
        print("Prezzo scontato: €", sconto)
    elif eta >= 65:
        sconto = prezzo - (prezzo * 30 / 100)
        print("Prezzo scontato: €", sconto)
    else:
        print("Prezzo pieno: €", prezzo)
```

Spiegazione concettuale:
In Python, devi sempre definire una variabile PRIMA di usarla. L'ordine delle istruzioni e fondamentale. Pensa alla programmazione come a una ricetta: non puoi "servire il piatto" prima di averlo "cucinato".

---

## Esercizio 15
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con parametri multipli - negozio online.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia.

Cosa dovevi fare:
Definire tre funzioni:
1. stampa_ordine(cliente, prodotto, quantita)
2. calcola_totale(prezzo, quantita, sconto)
3. verifica_disponibilita(quantita_richiesta, quantita_magazzino)

E scrivere il programma principale che chiede i dati all'utente e chiama tutte e tre le funzioni.

Questo era un esercizio di riepilogo importante che richiedeva di mettere insieme tutte le competenze viste negli esercizi precedenti.

---

## Esercizio 16
Punteggio: 5/5

Obiettivo: Funzioni che restituiscono un valore con return.

Analisi del codice:
Esercizio completato perfettamente. Hai compreso correttamente l'uso di `return` per restituire valori dalle funzioni e hai salvato i risultati in variabili per usarli successivamente.

Nota: Alla riga 11 hai scritto `return (numero * 3)` invece di `return triplo`, ma funziona comunque perche il risultato e lo stesso. Sarebbe stato piu corretto usare la variabile `triplo` gia calcolata alla riga 10, ma e una piccola ridondanza che non compromette la funzionalita.

---

## Esercizio 17
Punteggio: 5/5

Obiettivo: Usare i valori restituiti dalle funzioni.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le funzioni con return, salvato i valori restituiti in variabili e utilizzato questi valori nel programma.

---

## Esercizio 18
Punteggio: 5/5

Obiettivo: Return con logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente l'uso di return all'interno di strutture condizionali (if/else).

---

## Esercizio 19
Punteggio: 5/5

Obiettivo: Usare return in calcoli complessi.

Analisi del codice:
Esercizio completato correttamente. Hai implementato le funzioni con formule matematiche e return.

Nota: Alla riga 11 hai scritto `prezzo_finnale` con due 'n' invece di `prezzo_finale`, ma hai mantenuto la coerenza nel resto del codice e il programma funziona. In futuro, fai attenzione all'ortografia.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con return - statistiche gioco.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia.

Cosa dovevi fare:
Definire tre funzioni che restituiscono valori:
1. calcola_punteggio_totale(livello1, livello2, livello3) - restituisce la somma
2. calcola_media_punteggi(totale, numero_livelli) - restituisce la media
3. verifica_vittoria(punteggio_totale) - restituisce un messaggio

E scrivere il programma principale che chiama tutte le funzioni, salva i risultati e li stampa.

Questo era un esercizio di riepilogo finale molto importante che univa tutti i concetti della verifica (funzioni, parametri multipli, return, logica condizionale).

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione delle funzioni con parametri (esercizi 5, 6, 9, 10, 11, 12, 13)
- Buona comprensione del concetto di return (esercizi 16, 17, 18, 19)
- Capacita di implementare logica condizionale nelle funzioni (esercizi 3, 7, 12, 18)
- Codice che funziona correttamente nella maggior parte degli esercizi

Aree da migliorare:

1. **Completare tutti gli esercizi:**
   - Hai lasciato incompleti 3 esercizi (2, 15, 20)
   - Gli esercizi di riepilogo sono molto importanti per consolidare l'apprendimento

2. **Attenzione all'ordine delle istruzioni (CRITICO):**
   - Esercizio 14: devi definire una variabile PRIMA di usarla
   - Questo e un errore grave che blocca l'esecuzione del programma

3. **Gestione di tutti i casi nella logica:**
   - Esercizio 14: ricorda di gestire tutti i casi possibili con else

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 1:** Aggiungere la chiamata mancante a mostra_orari()
- **Esercizio 2:** Completare l'esercizio
- **Esercizio 14:** Correggere l'ordine delle istruzioni (calcola PRIMA, stampa DOPO) e aggiungere il caso else
- **Esercizio 15:** Completare l'esercizio di riepilogo
- **Esercizio 20:** Completare l'esercizio di riepilogo finale

Valutazione generale:
Hai dimostrato una solida comprensione dei concetti delle funzioni Python. I tuoi punti di forza sono nell'uso di parametri, return e logica condizionale. L'errore principale e nell'esercizio 14 dove hai invertito l'ordine delle istruzioni - questo e un errore concettuale importante da correggere. Completando gli esercizi rimasti e correggendo l'ordine delle istruzioni, puoi migliorare significativamente il tuo punteggio.
