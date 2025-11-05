# Correzione Verifica Funzioni Base - Caltran Eros

Punteggio Totale: 68/100

---

## Esercizio 1
Punteggio: 5/5

Obiettivo: Creare e chiamare funzioni senza parametri.

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente entrambe le funzioni e le hai chiamate nel modo giusto.

---

## Esercizio 2
Punteggio: 5/5

Obiettivo: Creare funzioni e richiamarle multiple volte.

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente le funzioni e le hai chiamate tutte e tre nel programma principale.

---

## Esercizio 3
Punteggio: 5/5

Obiettivo: Menu con funzioni e logica condizionale.

Analisi del codice:
Esercizio completato correttamente. Hai definito tutte le funzioni, implementato la logica condizionale e chiamato le funzioni nel modo giusto.

Nota: Hai scritto "carello" invece di "carrello" in alcuni punti (righe 13, 25, 26, 46), ma hai mantenuto la coerenza in tutto il codice e il programma funziona correttamente. In futuro, fai attenzione all'ortografia.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Riepilogo funzioni senza parametri - programma cinema.

Analisi del codice:
Esercizio completato correttamente. Hai definito perfettamente tutte e quattro le funzioni richieste con l'output corretto.

Nel programma principale hai creato un sistema interattivo con menu, che e una soluzione piu elaborata di quella richiesta (che era semplicemente chiamare le funzioni in sequenza). Questo dimostra iniziativa e capacita di applicare le conoscenze in modo creativo.

---

## Esercizio 5
Punteggio: 5/5

Obiettivo: Funzioni con un parametro.

Analisi del codice:
Esercizio completato correttamente. Hai definito le funzioni con parametri e implementato i calcoli. Il programma funziona perfettamente.

---

## Esercizio 6
Punteggio: 5/5

Obiettivo: Funzioni con parametro e calcoli.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le formule matematiche e le chiamate alle funzioni.

---

## Esercizio 7
Punteggio: 5/5

Obiettivo: Funzioni con logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica con if/else e if/elif/else.

---

## Esercizio 8
Punteggio: 5/5

Obiettivo: Riepilogo funzioni con un parametro - gestione abbonamenti palestra.

Analisi del codice:
Esercizio completato correttamente. Hai definito tutte le funzioni richieste, implementato la logica condizionale e scritto il programma principale che chiama tutte le funzioni con i parametri corretti.

L'uso di f-string e una scelta valida e il codice funziona perfettamente.

---

## Esercizio 9
Punteggio: 5/5

Obiettivo: Funzioni con due parametri.

Analisi del codice:
Esercizio completato perfettamente. Hai gestito correttamente le funzioni con due parametri.

---

## Esercizio 10
Punteggio: 5/5

Obiettivo: Funzioni con tre parametri.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le funzioni con tre parametri e i relativi calcoli.

---

## Esercizio 11
Punteggio: 5/5

Obiettivo: Funzioni con parametri e calcoli.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le formule matematiche richieste.

---

## Esercizio 12
Punteggio: 5/5

Obiettivo: Funzioni con parametri e logica.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica con AND e i confronti tra numeri. L'uso di f-string funziona bene.

---

## Esercizio 13
Punteggio: 5/5

Obiettivo: Funzioni con piu parametri e calcoli complessi.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le formule matematiche complesse.

---

## Esercizio 14
Punteggio: 1/5

Obiettivo: Funzioni con validazione.

Analisi del codice:
La prima funzione (valida_voto) e corretta. La seconda funzione ha errori gravi che impediscono al programma di funzionare.

Errori riscontrati nella funzione calcola_sconto_eta:

1. **Sintassi errata alla riga 24 - ERRORE BLOCCANTE:**
   - Cosa hai scritto: `prezzo_scontato = int(prezzo - (prezzo * 30% / 100))`
   - Problema: In Python NON puoi scrivere `30%`. Il simbolo `%` in Python e l'operatore modulo (resto della divisione), non significa "percento"
   - Per calcolare il 30%, devi scrivere: `prezzo - (prezzo * 30 / 100)`
   - Questo errore impedisce al programma di funzionare e Python restituira un errore di sintassi

2. **Logica errata - calcolo sconto (riga 24):**
   - Hai calcolato lo sconto del 30% PRIMA del blocco if/elif, e lo usi per tutti i casi
   - Problema: La funzione deve calcolare DUE sconti diversi:
     * 20% se eta < 18
     * 30% se eta >= 65
   - Soluzione: Calcola lo sconto DENTRO ogni blocco if/elif con la percentuale corretta per ogni caso

3. **Manca il caso else:**
   - La funzione non gestisce il caso delle persone con eta tra 18 e 64 anni
   - Cosa manca:
   ```python
   else:
       print("Prezzo pieno:", prezzo)
   ```

Codice corretto:
```python
def calcola_sconto_eta(prezzo, eta):
    if eta < 18:
        prezzo_scontato = prezzo - (prezzo * 20 / 100)
        print("Prezzo scontato:", prezzo_scontato)
    elif eta >= 65:
        prezzo_scontato = prezzo - (prezzo * 30 / 100)
        print("Prezzo scontato:", prezzo_scontato)
    else:
        print("Prezzo pieno:", prezzo)
```

Spiegazione:
In Python, per calcolare una percentuale scrivi il numero (es. 20, 30) e lo dividi per 100. Il simbolo % e riservato all'operatore modulo. Inoltre, ogni caso if/elif deve avere il proprio calcolo con la percentuale corretta.

---

## Esercizio 15
Punteggio: 2/5

Obiettivo: Riepilogo funzioni con parametri multipli - negozio online.

Analisi del codice:
Hai definito correttamente le tre funzioni richieste, ma ci sono errori gravi nelle chiamate alle funzioni.

Errori riscontrati:

1. **Chiamata funzione stampa_ordine errata (riga 55):**
   - Cosa hai scritto: `stampa_ordine(nome)`
   - Problema: La funzione richiede TRE parametri (cliente, prodotto, quantita) ma tu passi solo UNO
   - Conseguenza: Il programma da errore quando cerca di eseguire questa riga
   - Cosa dovevi scrivere: `stampa_ordine(nome, prodotto1, quantita_richiesta)`

2. **Chiamata funzione calcola_totale errata (riga 56):**
   - Cosa hai scritto: `calcola_totale(prezzo1)`
   - Problema: La funzione richiede TRE parametri (prezzo, quantita, sconto) ma ne passi solo UNO
   - Cosa dovevi scrivere: `calcola_totale(prezzo1, quantita_richiesta, sconto1)`

3. **Chiamata funzione verifica_disponibilita errata (riga 57):**
   - Cosa hai scritto: `verifica_disponibilita(magazzino1)`
   - Problema: La funzione richiede DUE parametri (quantita_richiesta, quantita_magazzino) ma ne passi solo UNO
   - Cosa dovevi scrivere: `verifica_disponibilita(quantita_richiesta, magazzino1)`

4. **Variabili non convertite in numeri (righe 47-50):**
   - Gli input per prezzo, quantita, sconto e magazzino devono essere convertiti in interi con `int()`
   - Esempio corretto: `prezzo1 = int(prezzo_input)`

5. **Manca caso else nella funzione (riga 40):**
   - La funzione verifica_disponibilita gestisce solo il caso "disponibile"
   - Manca: `else: print("Prodotto non disponibile")`

Spiegazione concettuale:
Quando definisci una funzione con parametri (es. `def stampa_ordine(cliente, prodotto, quantita):`), quando la chiami DEVI passare tutti i parametri richiesti nello stesso ordine. Se dimentichi un parametro, Python non sa quale valore usare e da errore.

Codice corretto del programma principale:
```python
nome = input("inserisci il nome del cliente: ")
prodotto = input("inserisci il nome del prodotto: ")
prezzo = int(input("inserisci il prezzo: "))
quantita = int(input("inserisci la quantita richiesta: "))
sconto = int(input("inserisci lo sconto: "))
magazzino = int(input("inserisci la quantita in magazzino: "))

stampa_ordine(nome, prodotto, quantita)
calcola_totale(prezzo, quantita, sconto)
verifica_disponibilita(quantita, magazzino)
```

---

## Esercizio 16
Punteggio: 1/5

Obiettivo: Funzioni che restituiscono un valore con return.

Analisi del codice:
Hai frainteso il concetto di `return`. Le funzioni devono RESTITUIRE un valore, non stamparlo.

Errore principale:
Nelle righe 11 e 18, hai usato `print` invece di `return`.

- Cosa hai scritto: `print(f"{triplo}")` e `print(f"{nome_completo}")`
- Cosa dovevi scrivere: `return triplo` e `return nome_completo`

Spiegazione del concetto di return:
Questo e un concetto FONDAMENTALE che devi capire:

**La differenza tra print e return:**
- `print()` → STAMPA un valore sullo schermo per visualizzarlo
- `return` → RESTITUISCE un valore al codice che ha chiamato la funzione

Quando usi `return`, la funzione "passa indietro" il valore, che puo essere salvato in una variabile e usato in altri calcoli.

Esempio pratico:
```python
# CON RETURN (corretto):
def calcola_triplo(numero):
    triplo = numero * 3
    return triplo

risultato = calcola_triplo(5)  # risultato vale 15
print("Il triplo e:", risultato)  # Output: Il triplo e: 15

# CON PRINT (sbagliato per questo esercizio):
def calcola_triplo(numero):
    triplo = numero * 3
    print(triplo)  # Stampa 15 sullo schermo

risultato = calcola_triplo(5)  # Stampa 15, ma risultato vale None
print("Il triplo e:", risultato)  # Output: Il triplo e: None
```

Nel tuo codice, quando esegui `risultato = calcola_triplo(num)` alla riga 24, la variabile risultato diventa `None` perche la funzione non restituisce nulla (stampa solo). Poi alla riga 25 stampi `None`.

Codice corretto:
```python
def calcola_triplo(numero):
    triplo = numero * 3
    return triplo

def unisci_nomi(nome, cognome):
    nome_completo = nome + " " + cognome
    return nome_completo
```

---

## Esercizio 17
Punteggio: 0/5

Obiettivo: Usare i valori restituiti dalle funzioni.

Analisi del codice:
Questo esercizio ha due errori gravi che impediscono al programma di funzionare.

Errori riscontrati:

1. **Manca return nelle funzioni (righe 11 e 18):**
   - Hai usato `print` invece di `return`
   - Rivedi la spiegazione del return nell'esercizio 16

2. **Chiamate funzioni senza parametri (righe 24 e 29) - ERRORE GRAVE:**
   - Riga 24: Hai scritto `area = calcola_area_cerchio()`
   - Problema: La funzione richiede il parametro `raggio`, ma tu hai lasciato le parentesi vuote
   - Cosa dovevi scrivere: `area = calcola_area_cerchio(r)`

   - Riga 29: Hai scritto `ore = converti_minuti_ore()`
   - Problema: La funzione richiede il parametro `minuti`, ma le parentesi sono vuote
   - Cosa dovevi scrivere: `ore = converti_minuti_ore(m)`

Spiegazione:
Le funzioni sono definite con parametri (`def calcola_area_cerchio(raggio):`), quindi quando le chiami DEVI passare i valori per quei parametri. Se non lo fai, Python da errore perche non sa quale valore usare per i calcoli.

Codice corretto:
```python
def calcola_area_cerchio(raggio):
    area = raggio * raggio * 3.14
    return area

def converti_minuti_ore(minuti):
    ore = minuti / 60
    return ore

r = int(input("Raggio del cerchio: "))
area = calcola_area_cerchio(r)  # Passa il parametro r
print("L'area del cerchio e:", area)

m = int(input("Minuti: "))
ore = converti_minuti_ore(m)  # Passa il parametro m
print(m, "minuti corrispondono a", ore, "ore")
```

---

## Esercizio 18
Punteggio: 0/5

Obiettivo: Return con logica condizionale.

Analisi del codice:
Esercizio non svolto. Il file e identico alla traccia.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Usare return in calcoli complessi.

Analisi del codice:
Esercizio non svolto. Il file e identico alla traccia.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con return.

Analisi del codice:
Esercizio non svolto. Il file e identico alla traccia.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione delle funzioni base (esercizi 1-13 quasi tutti perfetti)
- Buona gestione dei parametri nelle funzioni
- Capacita di implementare logica condizionale
- Buona comprensione di if/elif/else
- Sai scrivere codice pulito e organizzato

Aree da migliorare URGENTEMENTE:

1. **CONCETTO DI RETURN (CRITICO):**
   - Devi assolutamente capire la differenza tra `print` e `return`
   - `return` restituisce un valore che puo essere salvato e usato
   - `print` solo visualizza un valore sullo schermo
   - Senza capire il return non puoi progredire nella programmazione

2. **Passaggio parametri alle funzioni:**
   - Quando chiami una funzione, devi passare TUTTI i parametri che richiede
   - Esempio: se la funzione e `def calcola(a, b, c):`, la chiami con `calcola(1, 2, 3)`

3. **Sintassi percentuali:**
   - In Python per indicare 30% scrivi `30` e dividi per 100
   - Il simbolo `%` e l'operatore modulo, non significa "percento"

4. **Completamento esercizi:**
   - Gli ultimi 3 esercizi non sono stati completati
   - Gli esercizi di riepilogo sono molto importanti

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 14:** Correggi la sintassi (`30` invece di `30%`), calcola lo sconto nel blocco corretto, aggiungi il caso else
- **Esercizio 15:** Passa tutti i parametri richiesti alle funzioni, converti gli input in int, aggiungi else
- **Esercizio 16:** Usa `return` invece di `print` - STUDIA BENE QUESTO CONCETTO
- **Esercizio 17:** Usa `return` + passa i parametri alle funzioni quando le chiami
- **Esercizio 18:** Completare (return con logica)
- **Esercizio 19:** Completare (return con calcoli)
- **Esercizio 20:** Completare (riepilogo finale)

Consiglio per lo studio:
Concentrati sul concetto di `return`. E la chiave per capire come le funzioni comunicano tra loro. Fai esercizi supplementari su questo argomento, rivedi le lezioni, e chiedi aiuto al docente. Una volta che capisci il return, la programmazione diventera molto piu chiara.

Valutazione generale:
La tua performance e ottima nella prima meta della verifica (esercizi 1-13), dimostrando una solida comprensione dei concetti base. Hai una lacuna importante sul concetto di `return` che ti ha impedito di completare la seconda meta. Con studio mirato su questo argomento, puoi migliorare significativamente. Hai buone basi, devi solo consolidare il concetto chiave del return.
