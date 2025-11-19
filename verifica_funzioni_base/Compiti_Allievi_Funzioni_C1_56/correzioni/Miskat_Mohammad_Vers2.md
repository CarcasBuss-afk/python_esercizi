# Correzione Verifica Funzioni Base - Miskat Mohammad (Versione 2)

**Studente:** Miskat Mohammad
**Data:** 2025-11-14
**Punteggio totale:** 81/100

---

## Dettaglio Esercizi

### Esercizio 01 - Funzioni senza parametri (5/5)
**Voto:** ✓ CORRETTO

Il codice è perfetto. Hai definito correttamente entrambe le funzioni con `def` e le hai chiamate nel modo giusto. L'output corrisponde esattamente a quanto richiesto.

**Punti di forza:**
- Sintassi `def` corretta
- Nome funzioni rispetta le specifiche
- Chiamate di funzione corrette
- Output identico alle specifiche

---

### Esercizio 02 - Richiamare funzioni multiple volte (5/5)
**Voto:** ✓ CORRETTO

Ottimo lavoro! Hai compreso bene il concetto di riutilizzo delle funzioni, chiamando `stampa_separatore()` due volte come richiesto.

**Punti di forza:**
- Funzioni definite correttamente
- Sequenza di chiamate corretta
- Output preciso

---

### Esercizio 03 - Menu con funzioni (5/5)
**Voto:** ✓ CORRETTO

Esercizio completo e corretto. Tutte le funzioni sono implementate con i messaggi esatti e la logica condizionale con `if/elif/else` è perfetta.

**Punti di forza:**
- Quattro funzioni implementate correttamente
- Condizioni `if/elif/else` corrette
- Output esatto per ogni opzione

---

### Esercizio 04 - Riepilogo funzioni senza parametri (5/5)
**Voto:** ✓ CORRETTO

Eccellente! Hai scritto tutto da zero seguendo le specifiche. Le quattro funzioni sono implementate perfettamente e chiamate nell'ordine corretto.

**Punti di forza:**
- Autonomia nella scrittura del codice
- Tutti i messaggi corretti
- Sequenza di chiamate giusta

---

### Esercizio 05 - Funzioni con un parametro (3.5/5)
**Voto:** ⚠ QUASI CORRETTO (-1.5 punti)

Buona comprensione generale, ma ci sono alcuni problemi:

**Errori riscontrati:**
1. **Riga 18:** Output errato - hai scritto `"Il doppio è: {doppio}"` ma la traccia richiede `"Il doppio è:", doppio` (senza i due punti nell'f-string) (-0.5)
2. **Riga 27:** Errore logico grave - hai scritto `int(4)` invece di `int(numero_utente)`, quindi il programma ignora completamente l'input dell'utente e calcola sempre il doppio di 4! (-1.0)

**Punti di forza:**
- Funzione `saluta_studente` perfetta
- Uso corretto delle f-string
- Struttura generale corretta

**Suggerimenti:**
Fai attenzione quando converti gli input: `int(numero_utente)`, non valori fissi come `int(4)`.

---

### Esercizio 06 - Funzioni con parametro e calcoli (4.5/5)
**Voto:** ⚠ QUASI CORRETTO (-0.5 punti)

Ottimo lavoro complessivo, con un solo piccolo errore di formattazione.

**Errore riscontrato:**
- **Riga 20:** Output errato - hai scritto `f"€{euro}, corrispondono a ${dollari}"` con una virgola dopo `{euro}`, ma la traccia richiede uno spazio: `"€", euro, " corrispondono a $", dollari` (-0.5)

**Punti di forza:**
- Calcoli corretti in entrambe le funzioni
- Uso appropriato delle f-string
- Conversioni input corrette

**Suggerimento:**
Verifica sempre la punteggiatura negli output: gli spazi contano!

---

### Esercizio 07 - Funzioni con logica condizionale (5/5)
**Voto:** ✓ CORRETTO

Perfetto! Hai implementato correttamente tutte le condizioni con `if/elif/else` e i messaggi sono esatti.

**Punti di forza:**
- Condizioni logiche corrette (`>=`, `>`)
- Uso corretto di `elif` e `else`
- Output preciso

---

### Esercizio 08 - Riepilogo funzioni con un parametro (3.5/5)
**Voto:** ⚠ PARZIALMENTE CORRETTO (-1.5 punti)

Buon lavoro sulla logica, ma ci sono errori nell'output richiesto.

**Errori riscontrati:**
1. **Riga 29:** Output completamente errato - hai scritto solo `print(nome)` ma la traccia richiede `"Abbonato: [nome]"` (-1.0)
2. **Riga 46:** Conversione ridondante - `str(nome_in)` è inutile perché `input()` restituisce già una stringa (-0.5)

**Punti di forza:**
- Logica condizionale in `verifica_livello` corretta
- Calcolo del costo corretto
- Chiamate funzioni corrette

**Suggerimento:**
Rileggi sempre attentamente il formato dell'output richiesto nelle tracce.

---

### Esercizio 09 - Funzioni con due parametri (5/5)
**Voto:** ✓ CORRETTO

Eccellente! Entrambe le funzioni sono implementate perfettamente con i due parametri e l'output è corretto.

**Punti di forza:**
- Parametri multipli gestiti correttamente
- F-string ben formattate
- Calcoli corretti

---

### Esercizio 10 - Funzioni con tre parametri (5/5)
**Voto:** ✓ CORRETTO

Perfetto! Hai gestito correttamente i tre parametri in entrambe le funzioni e i calcoli sono esatti.

**Punti di forza:**
- Calcolo media corretto
- Uso appropriato delle f-string
- Parametri multipli gestiti bene

---

### Esercizio 11 - Funzioni con parametri e calcoli (5/5)
**Voto:** ✓ CORRETTO

Ottimo! Formule matematiche corrette e output perfettamente formattati.

**Punti di forza:**
- Formula perimetro corretta: `(base + altezza) * 2`
- Formula IVA corretta: `prezzo + (prezzo * iva / 100)`
- Nomi variabili appropriati

---

### Esercizio 12 - Funzioni con parametri e logica (4.5/5)
**Voto:** ⚠ QUASI CORRETTO (-0.5 punti)

Quasi perfetto, ma c'è un piccolo errore nell'output.

**Errore riscontrato:**
- **Riga 25:** Output errato - hai scritto `f"{a} minore di {b}"` ma manca "è": la traccia richiede `"[a] è minore di [b]"` (-0.5)

**Punti di forza:**
- Logica condizionale corretta
- Operatore `and` usato correttamente
- Prima funzione perfetta

**Suggerimento:**
Attenzione ai dettagli grammaticali nell'output!

---

### Esercizio 13 - Funzioni con calcoli complessi (4.5/5)
**Voto:** ⚠ QUASI CORRETTO (-0.5 punti)

Buon lavoro, con un piccolo errore di punteggiatura.

**Errore riscontrato:**
- **Riga 12:** Output errato - hai scritto `f"Tempo di viaggio: {tempo}, ore"` con una virgola, ma la traccia richiede `"Tempo di viaggio: [tempo] ore"` senza virgola (-0.5)

**Punti di forza:**
- Formule matematiche corrette
- Variabili ben nominate
- Seconda funzione perfetta

---

### Esercizio 14 - Funzioni con validazione (4.5/5)
**Voto:** ⚠ QUASI CORRETTO (-0.5 punti)

Ottima logica, ma attenzione al nome della funzione.

**Errore riscontrato:**
- **Riga 22:** Nome funzione errato - hai scritto `calc_sconto_eta` ma la traccia richiede `calcola_sconto_eta` (manca "ola") (-0.5)

**Punti di forza:**
- Logica condizionale perfetta
- Calcoli sconti corretti (20% e 30%)
- Output formattato bene
- Chiamata funzione coerente (anche se con nome sbagliato)

**Suggerimento:**
Usa nomi completi per le funzioni: `calcola`, non `calc`.

---

### Esercizio 15 - Riepilogo funzioni con parametri multipli (5/5)
**Voto:** ✓ CORRETTO

Eccellente riepilogo! Tutte e tre le funzioni sono implementate correttamente con i giusti parametri e la logica è perfetta. Hai anche scritto il programma principale in modo completo.

**Punti di forza:**
- Tre funzioni corrette
- Formula totale corretta: `(prezzo * quantita) - sconto`
- Condizione disponibilità corretta
- Input ben gestiti

**Nota:** Ci sono alcuni errori di battitura nei prompt (`inseriscri` invece di `inserisci`), ma questo non influisce sul funzionamento del codice.

---

### Esercizio 16 - Return (5/5)
**Voto:** ✓ CORRETTO

Perfetto! Hai compreso bene il concetto di `return` e come usare i valori restituiti.

**Punti di forza:**
- `return` usato correttamente in entrambe le funzioni
- Valori salvati in variabili
- Output corretto

---

### Esercizio 17 - Usare valori restituiti (3/5)
**Voto:** ⚠ PARZIALMENTE CORRETTO (-2 punti)

Hai compreso il concetto di `return`, ma ci sono errori nei nomi e nell'output.

**Errori riscontrati:**
1. **Riga 9:** Nome funzione errato - hai scritto `calcola_area` invece di `calcola_area_cerchio` (-0.5)
2. **Riga 16:** Nome funzione errato - hai scritto `converti_numeri` invece di `converti_minuti_ore` (-0.5)
3. **Riga 30:** Output errato - hai scritto `f"{m}, minuti corrispondono a {h}, ore"` con virgole, ma la traccia richiede `m, "minuti corrispondono a", h, "ore"` (senza virgole) (-0.5)
4. **Riga 24-29:** Nomi variabili errati - hai usato `a` e `h` invece di `area` e `ore` come richiesto dalla traccia (-0.5)

**Punti di forza:**
- Logica `return` corretta
- Calcoli matematici esatti
- Struttura generale buona

**Suggerimento:**
Leggi attentamente i nomi richiesti per funzioni e variabili!

---

### Esercizio 18 - Return con logica condizionale (2.5/5)
**Voto:** ⚠ PARZIALMENTE CORRETTO (-2.5 punti)

Buona logica in `trova_massimo`, ma gravi errori in `controlla_password`.

**Errori riscontrati:**
1. **Riga 19:** Nome funzione errato - hai scritto `controllo_password` invece di `controlla_password` (-0.5)
2. **Riga 21-23:** Errore concettuale grave - hai usato `print` invece di `return`! La funzione deve RESTITUIRE il messaggio, non stamparlo (-1.5)
3. **Riga 34:** Output errato - stampi `None` perché la funzione non restituisce nulla (conseguenza dell'errore precedente) (-0.5)

**Punti di forza:**
- Prima funzione perfetta
- Condizione `len(password) >= 8` corretta

**Suggerimento:**
Quando la traccia dice "RESTITUISCE", devi usare `return`, non `print`!

---

### Esercizio 19 - Return con calcoli complessi (4.5/5)
**Voto:** ⚠ QUASI CORRETTO (-0.5 punti)

Ottimo lavoro sui calcoli, con un piccolo errore nel nome della funzione.

**Errore riscontrato:**
- **Riga 18:** Nome funzione errato - hai scritto `calc_imc` invece di `calcola_imc` (-0.5)

**Punti di forza:**
- Formule matematiche corrette
- `return` usato correttamente
- Prima funzione perfetta

**Suggerimento:**
Mantieni coerenza nei nomi: usa sempre `calcola`, non abbreviazioni come `calc`.

---

### Esercizio 20 - Riepilogo return (0/5)
**Voto:** ✗ NON SVOLTO

L'esercizio è completamente vuoto, non hai scritto né le funzioni né il programma principale.

**Cosa mancava:**
- `calcola_punteggio_totale(livello1, livello2, livello3)` - return somma
- `calcola_media_punteggi(totale, numero_livelli)` - return media
- `verifica_vittoria(punteggio_totale)` - return messaggio
- Programma principale con input e stampe

**Suggerimento:**
Gestisci meglio il tempo durante la verifica per completare tutti gli esercizi!

---

## Riepilogo Finale

### Punteggio per Categoria
- **Funzioni senza parametri (es01-04):** 20/20 ✓
- **Funzioni con un parametro (es05-08):** 16.5/20 ⚠
- **Funzioni con parametri multipli (es09-15):** 33.5/35 ✓
- **Funzioni con return (es16-20):** 15/25 ⚠

### Punti di Forza
1. **Eccellente comprensione delle funzioni base** - I primi 4 esercizi sono perfetti
2. **Buona gestione dei parametri multipli** - Hai dimostrato di saper lavorare con 2-3 parametri
3. **Logica condizionale solida** - Le tue condizioni `if/elif/else` sono quasi sempre corrette
4. **Formule matematiche corrette** - Tutti i calcoli sono implementati bene
5. **Uso appropriato delle f-string** - Ottima formattazione nella maggior parte dei casi

### Aree da Migliorare
1. **Attenzione ai dettagli dell'output** - Rileggi sempre il formato esatto richiesto (spazi, virgole, punteggiatura)
2. **Differenza tra `print` e `return`** - Quando vedi "RESTITUISCE" devi usare `return`, non `print`
3. **Nomi completi delle funzioni** - Evita abbreviazioni (`calcola` non `calc`, `controlla` non `controllo`)
4. **Gestione del tempo** - L'esercizio 20 è rimasto vuoto, cerca di distribuire meglio il tempo
5. **Verifica dell'input** - Attenzione agli errori come `int(4)` invece di `int(numero_utente)`

### Consigli per il Futuro
- **Prima di consegnare**, rileggi tutte le tracce e confronta il tuo output
- **Testa il codice** eseguendolo per verificare che funzioni come previsto
- **Gestisci il tempo**: lascia 10-15 minuti finali per controllare tutto
- **Concentrati sulla differenza tra `print` e `return`** - è fondamentale!

---

## Conclusione

Hai dimostrato una buona comprensione generale delle funzioni in Python, con eccellenti risultati negli esercizi base e con parametri multipli. I principali problemi riguardano:
- Piccoli errori di formattazione nell'output
- Confusione tra `print` e `return` negli esercizi con return
- Gestione del tempo (esercizio 20 non svolto)

Con più attenzione ai dettagli e una migliore comprensione del concetto di `return`, potrai raggiungere ottimi risultati!

**Punteggio finale: 81/100**

Buon lavoro e continua così!
