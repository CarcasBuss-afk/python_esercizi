# Correzione Verifica Funzioni Base - Ravera Alberto

Punteggio Totale: 93/100

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
Esercizio completato perfettamente. Hai definito tutte e quattro le funzioni richieste con l'output corretto e le hai chiamate nel programma principale.

---

## Esercizio 5
Punteggio: 5/5

Obiettivo: Funzioni con un parametro.

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente le funzioni con parametri, implementato i calcoli e chiamato le funzioni passando i parametri corretti.

---

## Esercizio 6
Punteggio: 1/5

Obiettivo: Funzioni con parametro e calcoli.

Analisi del codice:
La seconda funzione e corretta. La prima funzione ha un errore GRAVE che impedisce al programma di funzionare.

Errore riscontrato nella funzione calcola_area_quadrato:

**Riga 10 - Parametro errato (ERRORE BLOCCANTE):**
```python
def calcola_area_quadrato(area):
    area = lato * lato
```

Problema: Hai definito il parametro come `area` invece di `lato`. Poi, alla riga 11, cerchi di usare la variabile `lato` che non esiste. Questo causa un errore: Python non sa da dove prendere il valore di `lato` perche non e stato passato come parametro.

Cosa dovevi scrivere:
```python
def calcola_area_quadrato(lato):
    area = lato * lato
    print("L'area del quadrato è:", area)
```

Spiegazione:
Il nome del parametro nella definizione della funzione deve corrispondere al nome della variabile che usi nel corpo della funzione. Se nel corpo usi `lato`, il parametro deve chiamarsi `lato`, non `area`.

Quando chiami la funzione alla riga 27 con `calcola_area_quadrato(lato)`, stai passando il valore di `lato` del programma principale. Questo valore viene assegnato al primo parametro della funzione. Se il parametro si chiama `area`, la variabile `area` avra il valore, ma `lato` non esistera all'interno della funzione, causando un errore.

---

## Esercizio 7
Punteggio: 5/5

Obiettivo: Funzioni con logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica condizionale con if/else e if/elif/else.

---

## Esercizio 8
Punteggio: 3/5

Obiettivo: Riepilogo funzioni con un parametro - gestione abbonamenti palestra.

Analisi del codice:
Hai definito tutte e tre le funzioni e il programma principale funziona. Tuttavia, ci sono alcuni errori che riducono il punteggio.

Errori riscontrati:

1. **Riga 33 - Manca il simbolo dell'euro:**
```python
print(f"Costo mensile {costo}")
```
Problema: La consegna richiedeva "Costo mensile: €[costo]" ma manca il simbolo €
Correzione: `print(f"Costo mensile: €{costo}")`

2. **Riga 36 - Errore di battitura:**
```python
print(f"Anni di seperienza: {anni_esperienza}")
```
Problema: "seperienza" invece di "esperienza"
Inoltre, questo print NON era richiesto dalla consegna. La funzione doveva stampare solo il livello, non gli anni di esperienza.

3. **Riga 38 - Errore di battitura:**
```python
print("Livello eserto")
```
Problema: "eserto" invece di "Esperto"

4. **Righe 38 e 42 - Formato inconsistente:**
- Riga 38: `"Livello eserto"` (senza i due punti)
- Riga 40: `"Livello: Intermedio"` (con i due punti)
- Riga 42: `"Livello: Principiante"` (con i due punti)

La consegna richiedeva formato uniforme "Livello: [valore]" per tutti i casi.

Codice corretto della funzione verifica_livello:
```python
def verifica_livello(anni_esperienza):
    if anni_esperienza >= 5:
        print("Livello: Esperto")
    elif anni_esperienza >= 2:
        print("Livello: Intermedio")
    else:
        print("Livello: Principiante")
```

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
Esercizio completato perfettamente. Hai implementato correttamente le formule matematiche richieste (perimetro rettangolo e totale con IVA).

---

## Esercizio 12
Punteggio: 5/5

Obiettivo: Funzioni con parametri e logica.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica condizionale con AND e i confronti tra numeri. L'uso di f-string funziona bene.

---

## Esercizio 13
Punteggio: 5/5

Obiettivo: Funzioni con piu parametri e calcoli complessi.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le formule matematiche complesse (tempo di viaggio e calorie bruciate).

---

## Esercizio 14
Punteggio: 5/5

Obiettivo: Funzioni con validazione.

Analisi del codice:
Esercizio completato correttamente. Hai implementato perfettamente la logica condizionale e i calcoli degli sconti. L'uso delle variabili intermedie (percentuale) e una buona pratica che rende il codice piu leggibile.

Nota: Hai chiamato la funzione "validita_voto" invece di "valida_voto", ma hai mantenuto la coerenza chiamandola con lo stesso nome nel programma principale (riga 39), quindi il codice funziona. In futuro, cerca di seguire esattamente i nomi richiesti dalla consegna.

---

## Esercizio 15
Punteggio: 5/5

Obiettivo: Riepilogo funzioni con parametri multipli - negozio online.

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente tutte e tre le funzioni richieste e il programma principale chiama tutte le funzioni con i parametri corretti. L'uso di f-string funziona bene.

Nota: Alla riga 47 c'e un piccolo errore di battitura ("Inseirsci" invece di "Inserisci"), ma questo e solo un dettaglio nel messaggio per l'utente, non un errore di codice.

---

## Esercizio 16
Punteggio: 5/5

Obiettivo: Funzioni che restituiscono un valore con return.

Analisi del codice:
Esercizio completato perfettamente. Hai compreso correttamente l'uso di `return` per restituire valori dalle funzioni e hai salvato i risultati in variabili per usarli successivamente.

---

## Esercizio 17
Punteggio: 4/5

Obiettivo: Usare i valori restituiti dalle funzioni.

Analisi del codice:
Esercizio quasi perfetto. Il codice funziona correttamente, ma c'e un errore di battitura nel parametro della funzione.

Errore riscontrato alla riga 9:
```python
def calcola_area_cerchio(reggio):
    area = reggio * reggio * 3.14
```

Problema: Hai scritto "reggio" invece di "raggio"

Cosa dovevi scrivere:
```python
def calcola_area_cerchio(raggio):
    area = raggio * raggio * 3.14
    return area
```

Nota: Il codice funziona lo stesso perche il nome del parametro e coerente nel corpo della funzione. Tuttavia, e importante usare nomi di variabili corretti e leggibili, specialmente per termini tecnici come "raggio".

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
Esercizio completato perfettamente. Hai implementato correttamente le formule matematiche (prezzo finale con sconto e IMC) e l'uso di return.

---

## Esercizio 20
Punteggio: 5/5

Obiettivo: Riepilogo funzioni con return - statistiche gioco.

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente tutte e tre le funzioni con return e il programma principale funziona perfettamente. Il codice e ben organizzato e usa correttamente i valori restituiti dalle funzioni.

Nota minima: Alla riga 41 hai scritto "Hai vinto" invece di "Hai vinto!" (manca il punto esclamativo richiesto dalla consegna), ma questo e un dettaglio trascurabile.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione generale delle funzioni in Python
- Perfetta gestione di funzioni con parametri multipli (esercizi 9-15)
- Eccellente comprensione del concetto di `return` (esercizi 16-20 quasi tutti perfetti)
- Buona capacita di implementare logica condizionale
- Codice generalmente pulito e ben strutturato
- Uso appropriato di f-string dove necessario
- Hai completato TUTTI gli esercizi, dimostrando impegno e costanza

Aree da migliorare:

1. **Attenzione ai nomi dei parametri (CRITICO):**
   - Esercizio 6: parametro "area" invece di "lato" causa errore bloccante
   - Il nome del parametro deve corrispondere alle variabili usate nel corpo della funzione
   - Questo e un errore concettuale importante da correggere

2. **Attenzione ai dettagli della consegna:**
   - Esercizio 8: simbolo € mancante, print non richiesto
   - Formato output non uniforme tra i vari casi if/elif/else

3. **Ortografia e battitura:**
   - Esercizio 8: "seperienza" invece di "esperienza", "eserto" invece di "Esperto"
   - Esercizio 17: "reggio" invece di "raggio"
   - Questi errori riducono la leggibilita del codice

Esercizi da rivedere:

- **Esercizio 6:** Correggere il parametro della funzione calcola_area_quadrato (PRIORITA MASSIMA - errore bloccante)
- **Esercizio 8:** Aggiungere simbolo €, rimuovere print non richiesto, correggere battitura e formato uniforme

Valutazione generale:
Ottimo lavoro! Hai dimostrato una solida comprensione delle funzioni Python, completando tutti i 20 esercizi. La tua comprensione del concetto di `return` e eccellente (esercizi 16-20 tutti corretti). L'errore nell'esercizio 6 e grave ma facilmente correggibile: devi solo fare attenzione che il nome del parametro corrisponda alle variabili usate nel corpo della funzione. Gli altri errori sono minori (battitura, dettagli di formato) e non compromettono la funzionalita. Con maggiore attenzione ai dettagli e alla corrispondenza tra parametri e variabili, puoi raggiungere l'eccellenza. Continua cosi!
