# Correzione Verifica Funzioni Base - Razzano Thomas

Punteggio Totale: 35/100

---

## Esercizio 1
Punteggio: 0/5

Obiettivo: Creare e chiamare funzioni senza parametri (mostra_benvenuto e mostra_orari).

Analisi del codice:
Hai definito correttamente entrambe le funzioni, ma c'è un errore nella chiamata.

Errore riscontrato:
```python
# Riga 23
mostra_benvenuto()  # ERRORE!
```

Problema: Alla riga 23 dovresti chiamare `mostra_orari()`, ma hai chiamato di nuovo `mostra_benvenuto()`. Questo significa che il programma stampa due volte il benvenuto invece di mostrare anche gli orari.

Cosa dovevi scrivere:
```python
mostra_orari()
```

---

## Esercizio 2
Punteggio: 5/5

Obiettivo: Creare funzioni e richiamarle multiple volte (stampa_separatore e stampa_titolo_corso).

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente entrambe le funzioni e le hai chiamate nell'ordine giusto.

---

## Esercizio 3
Punteggio: 5/5

Obiettivo: Menu con funzioni e logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte le funzioni richieste e implementato correttamente la logica condizionale con if/elif/else.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Riepilogo funzioni senza parametri - programma cinema.

Analisi del codice:
Esercizio completato correttamente. Hai definito tutte le funzioni richieste e le hai chiamate nel programma principale.

Nota minore: Alla riga 37 hai scritto `"Orari spettacoli 15:00..."` senza i due punti dopo "spettacoli". La consegna richiedeva `"Orari spettacoli: 15:00..."` con i due punti. È un dettaglio molto piccolo che non compromette la funzionalità, quindi non penalizzo, ma in futuro fai attenzione a rispettare esattamente il formato richiesto.

---

## Esercizio 5
Punteggio: 0/5

Obiettivo: Funzioni con un parametro.

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore di sintassi che causa output errato.

Errore riscontrato:
```python
# Riga 10
print("Ciao", {nome}, ", benvenuto al corso!")
```

Problema: Hai usato le parentesi graffe `{nome}` invece del nome della variabile direttamente. Le parentesi graffe in questo contesto creano un **set** (insieme), non accedono alla variabile.

Se l'utente inserisce "Mario", il programma stamperà:
```
Ciao {'Mario'} , benvenuto al corso!
```

Invece di:
```
Ciao Mario , benvenuto al corso!
```

Cosa dovevi scrivere:
```python
print("Ciao", nome, ", benvenuto al corso!")
```

Oppure con f-string:
```python
print(f"Ciao {nome}, benvenuto al corso!")
```

Nota: Le parentesi graffe si usano SOLO nelle f-string (stringhe che iniziano con `f"`), non nelle print normali con virgole.

---

## Esercizio 6
Punteggio: 5/5

Obiettivo: Funzioni con parametro e calcoli.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente entrambe le funzioni con i calcoli richiesti.

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
Hai tentato l'esercizio ma ci sono errori gravi che impediscono al programma di funzionare.

Errori riscontrati:

1. **Ordine sbagliato nella funzione calcola_costo_mensile (ERRORE BLOCCANTE):**
   ```python
   # Righe 40-42
   def calcola_costo_mensile(ore_settimanali):
      print(f"Costo mensile: €{costo}")  # ERRORE: costo non esiste ancora!
      costo = ore_settimanali * 15
   ```

   Problema: Stai cercando di stampare la variabile `costo` PRIMA di averla calcolata. Questo causa un **NameError** perché Python non sa cosa sia `costo` quando cerca di stamparlo.

   Cosa dovevi scrivere:
   ```python
   def calcola_costo_mensile(ore_settimanali):
      costo = ore_settimanali * 15
      print(f"Costo mensile: €{costo}")
   ```

   IMPORTANTE: Le istruzioni devono essere nell'ordine giusto - prima CALCOLI, poi STAMPI.

2. **Programma principale incompleto:**
   ```python
   # Riga 54
   input("Inserisci il tuo nome")
   ```

   Problema: Chiedi l'input ma non lo salvi in nessuna variabile e non chiami nessuna funzione. Il programma è incompleto.

   Cosa dovevi scrivere:
   ```python
   nome = input("Inserisci il tuo nome: ")
   ore = int(input("Inserisci ore settimanali: "))
   anni = int(input("Inserisci anni di esperienza: "))

   stampa_nome_abbonato(nome)
   calcola_costo_mensile(ore)
   verifica_livello(anni)
   ```

3. **Funzione stampa_nome_abbonato corretta:**
   La tua funzione `stampa_nome_abbonato` è scritta correttamente, bene!

4. **Funzione verifica_livello corretta:**
   La tua funzione `verifica_livello` è scritta correttamente, bene!

L'esercizio non funziona a causa dell'errore di ordinamento delle istruzioni e del programma principale incompleto.

---

## Esercizio 9
Punteggio: 5/5

Obiettivo: Funzioni con due parametri.

Analisi del codice:
Esercizio completato perfettamente. Hai gestito correttamente i parametri multipli e le chiamate di funzione.

---

## Esercizio 10
Punteggio: 0/5

Obiettivo: Funzioni con tre parametri.

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore di sintassi che impedisce al programma di funzionare.

Errore riscontrato:
```python
# Riga 11
media = ( + voto1 + voto2 + voto3) / 3
```

Problema: C'è un segno `+` in più all'inizio dell'espressione, prima di `voto1`. Questo causa un **SyntaxError** e il programma non può essere eseguito.

Cosa dovevi scrivere:
```python
media = (voto1 + voto2 + voto3) / 3
```

Nota: La funzione `stampa_prodotto` è corretta, bene!

---

## Esercizio 11
Punteggio: 5/5

Obiettivo: Funzioni con parametri e calcoli.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente entrambe le formule matematiche.

Nota: Alla riga 19 hai usato `Totale` con la T maiuscola invece di `totale` minuscolo. In Python è buona pratica usare le minuscole per le variabili, ma dato che sei stato coerente (l'hai usato sempre con la maiuscola) il codice funziona. In futuro, usa le minuscole per le variabili.

---

## Esercizio 12
Punteggio: 0/5

Obiettivo: Funzioni con parametri e logica.

Analisi del codice:
Hai completato la prima funzione `verifica_login` perfettamente, ma la seconda funzione `confronta_numeri` contiene un errore di logica grave.

Errori riscontrati:

1. **Funzione verifica_login: CORRETTA ✓**
   La logica con `and` e if/else è perfetta.

2. **Funzione confronta_numeri: ERRORE GRAVE DI LOGICA**
   ```python
   # Righe 21-27
   def confronta_numeri(a, b):
       if a >= b:
           print("[a] è maggiore di [b]")
       elif a <= b:
           print("[a] è minore di [b]")
       else:
           print("I numeri sono uguali")
   ```

   Problema concettuale: La logica è completamente sbagliata.

   - Se `a >= b` (a maggiore o uguale a b), stampa il primo messaggio
   - Se `a <= b` (a minore o uguale a b), stampa il secondo messaggio
   - L'`else` dice "sono uguali" ma NON VERRÀ MAI ESEGUITO

   Perché? Perché OGNI coppia di numeri deve soddisfare almeno una delle due condizioni:
   - Se a = 5, b = 3 → `a >= b` è vera → stampa "[a] è maggiore di [b]" ✓
   - Se a = 3, b = 5 → `a >= b` è falsa, ma `a <= b` è vera → stampa "[a] è minore di [b]" ✓
   - Se a = 5, b = 5 → `a >= b` è vera → stampa "[a] è maggiore di [b]" ✗ SBAGLIATO!

   Quando i numeri sono uguali, il programma stampa "è maggiore" invece di "sono uguali".

   Cosa dovevi scrivere:
   ```python
   def confronta_numeri(a, b):
       if a > b:  # Solo maggiore, NON uguale
           print(a, "è maggiore di", b)
       elif a < b:  # Solo minore, NON uguale
           print(a, "è minore di", b)
       else:  # L'unico caso rimasto: a == b
           print("I numeri sono uguali")
   ```

   Oppure:
   ```python
   def confronta_numeri(a, b):
       if a > b:
           print(f"{a} è maggiore di {b}")
       elif a < b:
           print(f"{a} è minore di {b}")
       else:
           print("I numeri sono uguali")
   ```

   Nota anche che hai stampato letteralmente `"[a]"` e `"[b]"` invece dei valori delle variabili. Dovresti stampare i valori veri di a e b, non le lettere "a" e "b".

Questo è un errore concettuale importante sulla differenza tra:
- `>` (strettamente maggiore)
- `>=` (maggiore o uguale)
- `<` (strettamente minore)
- `<=` (minore o uguale)

---

## Esercizio 13
Punteggio: 0/5

Obiettivo: Funzioni con più parametri e calcoli complessi.

Analisi del codice:
L'esercizio non è stato completato. Il file contiene ancora tutti gli spazi vuoti (________) da riempire.

Cosa dovevi fare:
Completare le due funzioni con le formule indicate e chiamarle nel programma principale.

---

## Esercizio 14
Punteggio: 0/5

Obiettivo: Funzioni con validazione.

Analisi del codice:
L'esercizio non è stato completato. Il file contiene ancora tutti gli spazi vuoti (________) da riempire.

Cosa dovevi fare:
Implementare le due funzioni con la logica condizionale richiesta e chiamarle nel programma principale.

---

## Esercizio 15
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con parametri multipli - negozio online.

Analisi del codice:
L'esercizio non è stato svolto. Il file è completamente vuoto.

Cosa dovevi fare:
Definire tre funzioni:
1. stampa_ordine(cliente, prodotto, quantita)
2. calcola_totale(prezzo, quantita, sconto)
3. verifica_disponibilita(quantita_richiesta, quantita_magazzino)

E scrivere il programma principale che chiede i dati all'utente e chiama tutte e tre le funzioni.

---

## Esercizio 16
Punteggio: 0/5

Obiettivo: Funzioni che restituiscono un valore con return.

Analisi del codice:
L'esercizio non è stato completato. Il file contiene ancora tutti gli spazi vuoti (________) da riempire.

Cosa dovevi fare:
Completare le funzioni con `return` per restituire i valori calcolati invece di stamparli.

---

## Esercizio 17
Punteggio: 0/5

Obiettivo: Usare i valori restituiti dalle funzioni.

Analisi del codice:
L'esercizio non è stato completato. Il file contiene ancora tutti gli spazi vuoti (________) da riempire.

Cosa dovevi fare:
Implementare le funzioni con `return` e usare i valori restituiti nel programma principale.

---

## Esercizio 18
Punteggio: 0/5

Obiettivo: Return con logica condizionale.

Analisi del codice:
L'esercizio non è stato completato. Il file contiene ancora tutti gli spazi vuoti (________) da riempire.

Cosa dovevi fare:
Implementare funzioni che usano `return` all'interno di strutture condizionali (if/else).

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Usare return in calcoli complessi.

Analisi del codice:
L'esercizio non è stato completato. Il file contiene ancora tutti gli spazi vuoti (________) da riempire.

Cosa dovevi fare:
Implementare le funzioni con formule matematiche che restituiscono il risultato con `return`.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con return - statistiche gioco.

Analisi del codice:
L'esercizio non è stato svolto. Il file è completamente vuoto.

Cosa dovevi fare:
Definire tre funzioni che usano `return`:
1. calcola_punteggio_totale(livello1, livello2, livello3) - restituisce la somma
2. calcola_media_punteggi(totale, numero_livelli) - restituisce la media
3. verifica_vittoria(punteggio_totale) - restituisce un messaggio

E scrivere il programma principale che chiama tutte le funzioni, salva i risultati restituiti e li stampa.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Buona comprensione di base delle funzioni senza parametri (es02, es03, es04)
- Capacità di implementare funzioni con parametri semplici (es06, es07, es09)
- Comprensione della logica condizionale di base (es03, es07)
- Capacità di implementare calcoli matematici in funzioni (es06, es11)

Aree da migliorare URGENTEMENTE:

1. **Attenzione nella chiamata delle funzioni (CRITICO):**
   - Es01: Hai chiamato la funzione sbagliata (mostra_benvenuto invece di mostra_orari)
   - Rileggi sempre il codice per verificare che le chiamate siano corrette

2. **Sintassi Python di base:**
   - Es05: Confusione tra `{nome}` (set) e `nome` (variabile)
   - Le parentesi graffe `{}` si usano SOLO con f-string (`f"Ciao {nome}"`), NON con print normale
   - Es10: Errore di sintassi con `+` in più

3. **Ordine delle istruzioni (ERRORE BLOCCANTE):**
   - Es08: Hai stampato `costo` prima di calcolarlo
   - REGOLA: Prima CALCOLI, poi STAMPI/USI il valore
   - Esempio corretto:
     ```python
     risultato = calcolo  # PRIMA calcola
     print(risultato)     # POI stampa
     ```

4. **Logica condizionale complessa (CONCETTO DA RIVEDERE):**
   - Es12: Confusione tra `>` e `>=`, `<` e `<=`
   - `a >= b` significa "a maggiore O uguale a b"
   - `a > b` significa "a strettamente maggiore di b" (esclude l'uguaglianza)
   - Quando usi if/elif/else, le condizioni devono essere **mutualmente esclusive** (solo una può essere vera alla volta)

5. **Completamento degli esercizi:**
   - Hai lasciato incompleti 8 esercizi (es13-20)
   - Questo rappresenta il 40% della verifica
   - Devi imparare a gestire meglio il tempo e completare tutti gli esercizi

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 01:** Correggere la chiamata alla funzione sbagliata
- **Esercizio 05:** Correggere la sintassi della print (togliere le graffe da nome)
- **Esercizio 08:** Correggere l'ordine delle istruzioni e completare il programma principale
- **Esercizio 10:** Rimuovere il `+` in eccesso nella formula
- **Esercizio 12:** Riscrivere la funzione confronta_numeri con la logica corretta
- **Esercizi 13-20:** Completare tutti gli esercizi rimasti

Esercizi da studiare come riferimento:
- Guarda l'esercizio 17 di Bosio Fabio per capire come usare `return` correttamente
- Studia gli esempi negli esercizi didattici per comprendere la differenza tra `>` e `>=`

Valutazione generale:
Hai dimostrato una comprensione parziale dei concetti base delle funzioni Python, ma ci sono lacune importanti. I tuoi punti di forza sono nelle funzioni semplici senza parametri e nei calcoli base. Gli errori principali sono: errori di sintassi (parentesi graffe, operatori extra), ordine sbagliato delle istruzioni (stampare prima di calcolare), e logica condizionale errata (uso scorretto di >= e <=). Il problema più grave è che hai lasciato incompleti 8 esercizi su 20, che rappresentano tutta la seconda metà della verifica sulle funzioni con `return` - un argomento fondamentale. Devi concentrarti sul completare TUTTI gli esercizi, fare più attenzione alla sintassi Python, e soprattutto comprendere l'ordine corretto delle operazioni (prima calcolare, poi usare).
