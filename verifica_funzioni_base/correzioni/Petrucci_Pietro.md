# Correzione Verifica Funzioni Base - Petrucci Pietro

Punteggio Totale: 60/100

---

## Esercizio 1
Punteggio: 5/5

Obiettivo: Creare e chiamare funzioni senza parametri (mostra_benvenuto e mostra_orari).

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente entrambe le funzioni e le hai chiamate nel programma principale.

---

## Esercizio 2
Punteggio: 5/5

Obiettivo: Creare funzioni e richiamarle multiple volte (stampa_separatore e stampa_titolo_corso).

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente le funzioni e le hai chiamate tutte e tre nel programma principale.

---

## Esercizio 3
Punteggio: 5/5

Obiettivo: Menu con funzioni e logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte le funzioni, implementato la logica condizionale con if/elif/else e chiamato le funzioni nel modo giusto.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Riepilogo funzioni senza parametri - programma cinema.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte le funzioni richieste e le hai chiamate nel programma principale. L'output e corretto e completo.

---

## Esercizio 5
Punteggio: 3/5

Obiettivo: Funzioni con un parametro.

Analisi del codice:
La logica della funzione e corretta, ma c'e un errore di sintassi nella stampa che causa un output errato.

Errore riscontrato alla riga 12:
```python
print(f"Ciao", {nome_utente}, ", benvenuto al corso!")
```

Problema: Hai usato le graffe `{}` in modo errato. Le graffe in questo contesto creano un "set" (insieme), non inseriscono il valore della variabile. Quando esegui il programma, l'output sara simile a:
```
Ciao {'Mario'} , benvenuto al corso!
```

Nota le graffe e gli apici che compaiono nell'output, invece di stampare solo il nome.

Cosa dovevi scrivere:
Ci sono due modi corretti per scrivere questa riga:

1. Usando f-string (SENZA virgole tra le parti):
```python
print(f"Ciao {nome_utente}, benvenuto al corso!")
```

2. Usando print con piu argomenti (SENZA graffe):
```python
print("Ciao", nome_utente, ", benvenuto al corso!")
```

Spiegazione:
- Nelle **f-string** (stringhe che iniziano con `f`), usi `{}` DENTRO la stringa per inserire variabili
- Nel **print normale**, usi virgole per separare argomenti, ma NON metti graffe intorno alle variabili

Non puoi mischiare i due approcci come hai fatto tu.

---

## Esercizio 6
Punteggio: 3/5

Obiettivo: Funzioni con parametro e calcoli.

Analisi del codice:
La funzione e i calcoli sono corretti, ma c'e lo stesso errore di sintassi nelle stampe.

Errore riscontrato alla riga 18:
```python
print("L'area del quadrato è:", {area})
```

Problema: Le graffe `{}` creano un set, non stampano il valore della variabile.

Cosa dovevi scrivere:
```python
print("L'area del quadrato è:", area)
```

Spiegazione:
Quando usi print con piu argomenti separati da virgole, NON devi mettere graffe intorno alle variabili. Le graffe si usano solo dentro le f-string.

---

## Esercizio 7
Punteggio: 5/5

Obiettivo: Funzioni con logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica condizionale con if/else e if/elif/else.

---

## Esercizio 8
Punteggio: 5/5

Obiettivo: Riepilogo funzioni con un parametro - gestione abbonamenti palestra.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte le funzioni richieste, implementato la logica condizionale e scritto il programma principale che chiama tutte le funzioni con i parametri corretti.

---

## Esercizio 9
Punteggio: 3/5

Obiettivo: Funzioni con due parametri.

Analisi del codice:
Le funzioni sono definite correttamente e i calcoli funzionano, ma c'e l'errore di sintassi con le graffe.

Errore riscontrato alla riga 18:
```python
print(f"Studente:", {nome}, ", Corso:", {corso})
```

Problema: Stai mischiando f-string con graffe usate come set. Questo produce output errato.

Cosa dovevi scrivere:
Opzione 1 (f-string):
```python
print(f"Studente: {nome}, Corso: {corso}")
```

Opzione 2 (print normale):
```python
print("Studente:", nome, ", Corso:", corso)
```

---

## Esercizio 10
Punteggio: 2/5

Obiettivo: Funzioni con tre parametri.

Analisi del codice:
Le funzioni sono definite correttamente, ma ci sono due tipi di errori: sintassi nella stampa e un errore di battitura.

Errori riscontrati:

1. **Riga 18 - Errore di sintassi:**
```python
print("Media:", {media})
```
Problema: Graffe usate in modo errato (stesso errore degli esercizi precedenti)
Correzione: `print("Media:", media)`

2. **Riga 10 - Errore di battitura:**
```python
def mostra_prodotto(nome, qualita, prezzo):
```
Problema: Hai scritto "qualita" invece di "quantita"
Il parametro dovrebbe chiamarsi `quantita` (con la 'n')

Nota: Questo errore si propaga poi nelle righe dove usi la variabile (righe 11, 32, 33).

---

## Esercizio 11
Punteggio: 2/5

Obiettivo: Funzioni con parametri e calcoli.

Analisi del codice:
La prima funzione e corretta. La seconda funzione ha un errore di logica grave e un errore di sintassi.

Errori riscontrati nella funzione calcola_totale_con_iva:

1. **Riga 19 - Formula incompleta (ERRORE GRAVE):**
```python
totale = (prezzo * iva / 100)
```
Problema: Questa formula calcola SOLO l'IVA, non il totale con IVA
Cosa dovevi scrivere: `totale = prezzo + (prezzo * iva / 100)`

Spiegazione: Il totale con IVA e il prezzo originale PIU l'IVA aggiunta. Tu hai calcolato solo la parte dell'IVA, senza sommarla al prezzo.

2. **Riga 20 - Errore di sintassi:**
```python
print("Totale con IVA: €", {totale})
```
Problema: Graffe usate in modo errato
Correzione: `print("Totale con IVA: €", totale)`

Codice corretto della funzione:
```python
def calcola_totale_con_iva(prezzo, iva):
    totale = prezzo + (prezzo * iva / 100)
    print("Totale con IVA: €", totale)
```

---

## Esercizio 12
Punteggio: 5/5

Obiettivo: Funzioni con parametri e logica.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica condizionale con AND e i confronti tra numeri. L'uso di f-string funziona bene.

---

## Esercizio 13
Punteggio: 3/5

Obiettivo: Funzioni con piu parametri e calcoli complessi.

Analisi del codice:
Le funzioni sono definite correttamente e le formule sono giuste, ma ci sono errori di sintassi nelle stampe.

Errori riscontrati:

Riga 12:
```python
print("Tempo di viaggio:", {tempo}, "ore")
```

Riga 20:
```python
print("Calorie bruciate:", {formula})
```

Problema: Graffe usate in modo errato (stesso errore visto negli esercizi precedenti)

Cosa dovevi scrivere:
```python
print("Tempo di viaggio:", tempo, "ore")
print("Calorie bruciate:", formula)
```

---

## Esercizio 14
Punteggio: 5/5

Obiettivo: Funzioni con validazione.

Analisi del codice:
Esercizio completato correttamente. Hai implementato correttamente la logica condizionale e i calcoli degli sconti.

Nota: Hai chiamato la funzione "validita_voto" invece di "valida_voto", ma hai mantenuto la coerenza chiamandola con lo stesso nome nel programma principale (riga 39), quindi il codice funziona. In futuro, cerca di seguire esattamente i nomi richiesti dalla consegna.

---

## Esercizio 15
Punteggio: 3/5

Obiettivo: Riepilogo funzioni con parametri multipli - negozio online.

Analisi del codice:
Hai definito correttamente tutte e tre le funzioni richieste. Ottimo lavoro nella parte delle funzioni! Tuttavia, ci sono errori gravi nel programma principale che impediscono al codice di funzionare.

Errori riscontrati nel programma principale:

1. **Righe 56 e 59 - Conversione errata (ERRORE BLOCCANTE):**

Riga 56:
```python
sconto_input = input("Inserisci lo sconto: ")
sconto_input = int
```

Riga 59:
```python
quantita_magazzino_input = input("Inserisci la quantità in magazzino: ")
quantita_magazzino_input = int
```

Problema: Nella seconda riga di ciascun blocco, hai scritto `= int` invece di `= int(...)`. In questo modo NON stai convertendo il valore in numero intero. Stai solo assegnando il "tipo" int alla variabile, ma il valore rimane una stringa (o diventa il tipo stesso).

Cosa dovevi scrivere:
```python
sconto_input = input("Inserisci lo sconto: ")
sconto_input = int(sconto_input)
```

Oppure, piu semplicemente, in una sola riga:
```python
sconto_input = int(input("Inserisci lo sconto: "))
```

Spiegazione:
In Python, per convertire una stringa in numero intero devi CHIAMARE la funzione `int()` con le parentesi e passare il valore da convertire. Se scrivi solo `int` senza parentesi, non stai facendo alcuna conversione.

Nota positiva: Per le righe 49 e 52 hai fatto la conversione correttamente in una sola riga. Cerca di usare sempre questo approccio, e piu semplice ed evita errori.

---

## Esercizio 16
Punteggio: 1/5

Obiettivo: Funzioni che restituiscono un valore con return.

Analisi del codice:
Questo esercizio presenta un fraintendimento del concetto di `return`. Inoltre, ci sono errori di sintassi.

Errore principale - Manca return:

Nelle righe 11 e 18, hai usato `print` invece di `return`.

- Riga 11: `print(f"Il triplo di {numero} è {triplo}")`
- Riga 18: `print(f"{nome_completo}")`

Problema: La consegna richiedeva di RESTITUIRE il valore con `return`, non di stamparlo.

Cosa dovevi scrivere:
```python
def calcola_triplo(numero):
    triplo = numero * 3
    return triplo

def unisci_nomi(nome, cognome):
    nome_completo = nome + " " + cognome
    return nome_completo
```

Spiegazione del concetto di return:
Questo e un concetto FONDAMENTALE:

- `print()` → STAMPA un valore sullo schermo
- `return` → RESTITUISCE un valore che puo essere salvato in una variabile

Quando una funzione usa `return`, il valore viene "passato indietro" al codice che ha chiamato la funzione. Nel tuo codice, alle righe 24 e 30, cerchi di salvare il risultato in variabili (`risultato` e `nome_completo`), ma siccome le funzioni usano `print` invece di `return`, le variabili diventano `None` (nessun valore).

Errori di sintassi aggiuntivi:

Riga 17:
```python
nome_completo = {nome} + " " + {cognome}
```
Problema: Le graffe `{}` creano set, non possono essere usate cosi fuori da una f-string.
Correzione: `nome_completo = nome + " " + cognome`

Righe 25 e 31:
```python
print("Il triplo è:", {risultato})
print("Nome completo:", {nome_completo})
```
Problema: Stesso errore con le graffe
Correzione: Rimuovi le graffe

---

## Esercizio 17
Punteggio: 0/5

Obiettivo: Usare i valori restituiti dalle funzioni.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia, tutti gli spazi vuoti (___) sono rimasti invariati.

---

## Esercizio 18
Punteggio: 0/5

Obiettivo: Return con logica condizionale.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia, tutti gli spazi vuoti (___) sono rimasti invariati.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Usare return in calcoli complessi.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia, tutti gli spazi vuoti (___) sono rimasti invariati.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con return - statistiche gioco.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Buona comprensione delle funzioni senza parametri (esercizi 1-4)
- Ottima gestione della logica condizionale (esercizi 3, 7, 8, 12, 14)
- Capacita di definire funzioni con parametri multipli (esercizi 9, 10, 11, 13, 15)
- Definizioni delle funzioni generalmente corrette
- Quando completi un esercizio, la logica e quasi sempre giusta

Aree da migliorare URGENTEMENTE:

1. **Sintassi delle graffe `{}` con print (ERRORE RICORRENTE):**
   - Hai ripetuto questo errore in 6 esercizi (5, 6, 9, 10, 11, 13, 16)
   - Ricorda:
     * **F-string**: `print(f"Testo {variabile} altro testo")`
     * **Print normale**: `print("Testo", variabile, "altro testo")`
   - NON puoi usare `print("Testo", {variabile})` → le graffe creano un set!

2. **Concetto di `return` (CRITICO):**
   - Esercizio 16: hai usato `print` invece di `return`
   - Devi capire la differenza:
     * `print` visualizza sullo schermo
     * `return` restituisce un valore utilizzabile
   - Senza capire il `return` non puoi procedere nella programmazione

3. **Conversione tipi con `int()`:**
   - Esercizio 15: hai scritto `= int` invece di `= int(valore)`
   - La conversione richiede le parentesi e il valore da convertire

4. **Attenzione ai dettagli:**
   - Esercizio 10: "qualita" invece di "quantita"
   - Esercizio 11: Formula incompleta (manca il prezzo iniziale)
   - Esercizio 14: Nome funzione diverso dalla consegna

5. **Completamento esercizi:**
   - Hai lasciato incompleti 4 esercizi (17-20)
   - Gli esercizi sul `return` sono fondamentali per progredire

Esercizi da rifare OBBLIGATORIAMENTE:

- **Esercizi 5, 6, 9, 10, 13:** Correggere la sintassi delle graffe nel print
- **Esercizio 10:** Correggere "qualita" in "quantita"
- **Esercizio 11:** Completare la formula del totale con IVA (aggiungere il prezzo)
- **Esercizio 15:** Correggere la conversione con int() usando le parentesi
- **Esercizio 16:** Usare `return` invece di `print` e correggere le graffe - STUDIA BENE IL CONCETTO DI RETURN
- **Esercizi 17-20:** Completare tutti gli esercizi sul return

Consiglio per lo studio:
Il tuo errore piu frequente e la confusione con la sintassi delle graffe nel print. Fai pratica con questi due pattern:
1. F-string: tutto dentro una stringa con f davanti
2. Print con argomenti: virgole per separare, niente graffe

Inoltre, devi assolutamente studiare il concetto di `return`. E la base per creare funzioni riutilizzabili. Rivedi le lezioni, fai esercizi supplementari e chiedi aiuto al docente su questo argomento.

Valutazione generale:
Hai dimostrato una discreta comprensione dei concetti base delle funzioni. La tua logica e generalmente corretta, ma hai un problema ricorrente con la sintassi del print (uso errato delle graffe) che ti ha fatto perdere molti punti. Inoltre, non hai ancora compreso il concetto di `return`, fondamentale per progredire. Correggendo questi due aspetti e completando gli esercizi rimasti, puoi migliorare significativamente il tuo punteggio. Il potenziale c'e, devi solo prestare piu attenzione alla sintassi e studiare meglio il return.
