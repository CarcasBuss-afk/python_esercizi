# Correzione Verifica Funzioni Base - Razzano Thomas

Punteggio Totale: 43/100

---

## Esercizio 1
Punteggio: 4/5

Obiettivo: Creare e chiamare funzioni senza parametri (mostra_benvenuto e mostra_orari).

Analisi del codice:
Hai definito correttamente entrambe le funzioni. Tuttavia, c'e un errore nella chiamata delle funzioni.

Errore riscontrato alla riga 23:
```python
# CHIAMA la funzione mostra_orari
mostra_benvenuto()
```

Problema: Hai chiamato `mostra_benvenuto()` invece di `mostra_orari()`. Il risultato e che il messaggio di benvenuto appare due volte, mentre il messaggio degli orari non viene mai mostrato.

Cosa dovevi scrivere:
```python
mostra_orari()
```

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
Punteggio: 4/5

Obiettivo: Riepilogo funzioni senza parametri - programma cinema.

Analisi del codice:
Hai definito tutte e quattro le funzioni e le hai chiamate nel programma principale. Il programma funziona. C'e un piccolo errore nel testo di una funzione.

Errore riscontrato alla riga 37:
```python
print("Orari spettacoli 15:00, 18:00, 21:00")
```

Problema: Manca i due punti (:) dopo "spettacoli"

Cosa dovevi scrivere:
```python
print("Orari spettacoli: 15:00, 18:00, 21:00")
```

Nota: Le funzioni sono state definite nel "programma principale" invece che nella sezione "DEFINISCI LE FUNZIONI QUI", ma questo non compromette la funzionalita del codice.

---

## Esercizio 5
Punteggio: 3/5

Obiettivo: Funzioni con un parametro.

Analisi del codice:
La seconda funzione e corretta. La prima funzione ha un errore di sintassi nella stampa che causa un output errato.

Errore riscontrato alla riga 10:
```python
print("Ciao", {nome}, ", benvenuto al corso!")
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
print(f"Ciao {nome}, benvenuto al corso!")
```

2. Usando print con piu argomenti (SENZA graffe):
```python
print("Ciao", nome, ", benvenuto al corso!")
```

Spiegazione:
- Nelle **f-string** (stringhe che iniziano con `f`), usi `{}` DENTRO la stringa per inserire variabili
- Nel **print normale**, usi virgole per separare argomenti, ma NON metti graffe intorno alle variabili

Non puoi mischiare i due approcci come hai fatto tu.

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
Esercizio completato perfettamente. Hai implementato correttamente la logica condizionale con if/else e if/elif/else.

---

## Esercizio 8
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con un parametro - gestione abbonamenti palestra.

Analisi del codice:
Hai definito le tre funzioni ma ci sono errori gravi che impediscono al programma di funzionare. Inoltre, il programma principale e quasi completamente mancante.

Errori riscontrati:

1. **Funzione calcola_costo_mensile - Ordine istruzioni (ERRORE BLOCCANTE):**

Righe 41-42:
```python
def calcola_costo_mensile(ore_settimanali):
   print(f"Costo mensile: €{costo}")
   costo = ore_settimanali * 15
```

Problema: Stai usando la variabile `costo` nel print PRIMA di averla definita. Python legge il codice dall'alto verso il basso, quindi quando arriva al print (riga 41), la variabile `costo` non esiste ancora e il programma da errore.

Cosa dovevi scrivere:
```python
def calcola_costo_mensile(ore_settimanali):
   costo = ore_settimanali * 15
   print(f"Costo mensile: €{costo}")
```

Nota l'ordine: prima CALCOLI il valore, poi lo STAMPI.

2. **Riga 46 - Errore di battitura:**
```python
print("Livello: esperto")
```
Problema: "esperto" con la minuscola invece di "Esperto" con la maiuscola

3. **Programma principale mancante:**

Riga 54:
```python
input("Inserisci il tuo nome")
```

Problema: Hai scritto solo UNA riga di input, ma non l'hai salvata in una variabile. Inoltre, mancano completamente:
- Gli altri 2 input (ore settimanali e anni esperienza)
- La conversione degli input numerici in int
- Le chiamate alle tre funzioni

Cosa dovevi scrivere:
```python
nome = input("Inserisci il tuo nome: ")
ore_settimanali = int(input("Inserisci le ore settimanali: "))
anni_esperienza = int(input("Inserisci gli anni di esperienza: "))

stampa_nome_abbonato(nome)
calcola_costo_mensile(ore_settimanali)
verifica_livello(anni_esperienza)
```

Codice corretto completo della funzione calcola_costo_mensile:
```python
def calcola_costo_mensile(ore_settimanali):
   costo = ore_settimanali * 15
   print(f"Costo mensile: €{costo}")
```

---

## Esercizio 9
Punteggio: 5/5

Obiettivo: Funzioni con due parametri.

Analisi del codice:
Esercizio completato perfettamente. Hai gestito correttamente le funzioni con due parametri.

---

## Esercizio 10
Punteggio: 2/5

Obiettivo: Funzioni con tre parametri.

Analisi del codice:
La seconda funzione e corretta. La prima funzione ha un errore di sintassi grave nella formula che impedisce al programma di funzionare.

Errore riscontrato alla riga 11:
```python
media = ( + voto1 + voto2 + voto3) / 3
```

Problema: C'e un operatore `+` extra all'inizio della formula, prima di `voto1`. Questo causa un errore di sintassi: Python si aspetta un valore prima del `+`, ma trova solo una parentesi aperta.

Cosa dovevi scrivere:
```python
media = (voto1 + voto2 + voto3) / 3
```

Spiegazione:
L'operatore `+` serve per sommare due valori. Non puo stare all'inizio di un'espressione senza avere nulla prima. Questa e probabilmente una svista durante la scrittura del codice.

---

## Esercizio 11
Punteggio: 5/5

Obiettivo: Funzioni con parametri e calcoli.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le formule matematiche richieste (perimetro rettangolo e totale con IVA).

Nota minima: Alla riga 19 hai usato "Totale" con la maiuscola invece di "totale" minuscolo, ma questa e solo una convenzione di naming e non compromette la funzionalita.

---

## Esercizio 12
Punteggio: 0/5

Obiettivo: Funzioni con parametri e logica.

Analisi del codice:
La prima funzione e corretta. La seconda funzione ha errori logici GRAVI che impediscono al programma di funzionare correttamente.

Errori riscontrati nella funzione confronta_numeri:

1. **Logica condizionale completamente errata (ERRORE GRAVE):**

Righe 22-27:
```python
def confronta_numeri(a, b):
    if a >= b:
        print("[a] è maggiore di [b]")
    elif a <= b:
        print("[a] è minore di [b]")
    else:
        print("I numeri sono uguali")
```

Problema 1 - Operatori sbagliati:
- Hai usato `>=` invece di `>`
- Hai usato `<=` invece di `<`

Conseguenza: Se i numeri sono uguali, entrambe le condizioni (a >= b e a <= b) sono vere. Il programma entra nel primo if e stampa "maggiore" anche quando i numeri sono uguali. L'else non viene mai raggiunto.

Problema 2 - Stampa letterale di "[a]" e "[b]":
Hai scritto letteralmente `"[a] è maggiore di [b]"` tra virgolette. Python stampa esattamente quello che vede, quindi l'output sara:
```
[a] è maggiore di [b]
```

Invece di mostrare i valori reali dei numeri (ad esempio "5 è maggiore di 3").

Cosa dovevi scrivere:
```python
def confronta_numeri(a, b):
    if a > b:
        print(f"{a} è maggiore di {b}")
    elif a < b:
        print(f"{a} è minore di {b}")
    else:
        print("I numeri sono uguali")
```

Oppure:
```python
def confronta_numeri(a, b):
    if a > b:
        print(a, "è maggiore di", b)
    elif a < b:
        print(a, "è minore di", b)
    else:
        print("I numeri sono uguali")
```

Spiegazione:
- Quando vedi `[a]` nella consegna, significa che devi inserire IL VALORE della variabile `a`, non scrivere letteralmente "[a]"
- Per inserire il valore di una variabile in una stringa usa f-string: `f"{a}"` o separala con virgole nel print

---

## Esercizio 13
Punteggio: 0/5

Obiettivo: Funzioni con piu parametri e calcoli complessi.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia, tutti gli spazi vuoti (___) sono rimasti invariati.

---

## Esercizio 14
Punteggio: 0/5

Obiettivo: Funzioni con validazione.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia, tutti gli spazi vuoti (___) sono rimasti invariati.

---

## Esercizio 15
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con parametri multipli - negozio online.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia.

---

## Esercizio 16
Punteggio: 0/5

Obiettivo: Funzioni che restituiscono un valore con return.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia, tutti gli spazi vuoti (___) sono rimasti invariati.

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
- Capacita di implementare logica condizionale semplice (esercizi 3, 7)
- Definizione corretta di funzioni con uno, due e tre parametri (esercizi 5, 6, 9)
- Implementazione di formule matematiche (esercizi 6, 11)

Aree da migliorare URGENTEMENTE:

1. **Ordine delle istruzioni (CRITICO):**
   - Esercizio 8: devi definire una variabile PRIMA di usarla
   - Questo e un errore grave che blocca l'esecuzione del programma
   - In Python, l'ordine e fondamentale: calcola PRIMA, stampa DOPO

2. **Sintassi delle graffe `{}` con print:**
   - Esercizio 5: stesso errore visto in altri studenti
   - Le graffe NON si usano cosi: `print("Testo", {variabile})`
   - Usa f-string OPPURE print normale, non mischiarli

3. **Attenzione ai dettagli della sintassi:**
   - Esercizio 10: operatore `+` extra nella formula
   - Questi errori bloccano completamente il programma

4. **Comprensione della logica condizionale:**
   - Esercizio 12: hai confuso `>` con `>=` e `<` con `<=`
   - Hai stampato letteralmente "[a]" invece del valore di `a`
   - Devi capire quando una condizione e vera o falsa

5. **Completamento esercizi (MOLTO CRITICO):**
   - Hai lasciato incompleti 11 esercizi su 20 (dal 13 al 20 + parte di 8)
   - Gli esercizi sul `return` (16-20) sono fondamentali per progredire
   - Questi esercizi rappresentano il 55% della verifica

6. **Programma principale incompleto:**
   - Esercizio 8: hai scritto solo UNA riga di input senza salvarla
   - Mancano le chiamate alle funzioni
   - Devi completare TUTTO il programma, non solo le funzioni

Esercizi da rifare OBBLIGATORIAMENTE:

- **Esercizio 1:** Chiamare mostra_orari() invece di mostra_benvenuto()
- **Esercizio 5:** Correggere la sintassi del print (rimuovere graffe)
- **Esercizio 8:** Correggere l'ordine delle istruzioni (calcola PRIMA, stampa DOPO) + completare il programma principale
- **Esercizio 10:** Rimuovere il `+` extra nella formula
- **Esercizio 12:** Correggere la logica (usare `>` e `<`) e stampare i VALORI delle variabili, non "[a]" e "[b]"
- **Esercizi 13-20:** Completare TUTTI gli esercizi rimasti

Consiglio per lo studio:
Devi assolutamente completare gli esercizi rimasti. La seconda meta della verifica (esercizi con return) e fondamentale per capire come le funzioni restituiscono valori. Senza questo concetto, non puoi progredire nella programmazione. Inoltre, presta molta attenzione all'ordine delle istruzioni: in Python, devi sempre definire/calcolare un valore PRIMA di usarlo. Rivedi gli esercizi, completa quelli mancanti, e chiedi aiuto al docente per chiarire i concetti che non hai capito.

Valutazione generale:
Hai dimostrato una comprensione base delle funzioni nei primi esercizi, ma ci sono lacune importanti. Gli errori principali sono: ordine delle istruzioni (esercizio 8), errori di sintassi (esercizi 5, 10), logica errata (esercizio 12) e soprattutto il fatto di aver lasciato incompleti piu della meta degli esercizi. Gli esercizi sul return (16-20) sono essenziali per capire come le funzioni comunicano tra loro. Devi impegnarti a completare tutti gli esercizi e a correggere gli errori fondamentali. Il tuo punteggio puo migliorare notevolmente se completi il lavoro.
