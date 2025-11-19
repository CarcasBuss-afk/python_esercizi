# Correzione Verifica Stringhe Base A - Roscio Giacomo

Punteggio Totale: 79/100

---

## Esercizio 1
Punteggio: 5/5

Obiettivo: Concatenare nome e cognome con uno spazio

Analisi del codice:
Esercizio completato perfettamente. Hai correttamente concatenato le stringhe usando l'operatore + con lo spazio tra nome e cognome.

---

## Esercizio 2
Punteggio: 5/5

Obiettivo: Concatenare città e nazione con input utente

Analisi del codice:
Esercizio completato correttamente. Hai usato f-string per formattare la frase, che è una scelta valida e moderna.

---

## Esercizio 3
Punteggio: 5/5

Obiettivo: Riepilogo concatenazione - scheda libro

Analisi del codice:
Esercizio completato perfettamente. Hai creato la scheda libro concatenando tutte le informazioni richieste con f-string.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Aggiungere parti a un messaggio usando l'operatore +=

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente l'operatore += per aggiungere progressivamente parti al messaggio.

---

## Esercizio 5
Punteggio: 4/5

Obiettivo: Costruire un indirizzo email usando +=

Analisi del codice:
Hai completato l'esercizio con la logica corretta. L'uso dell'operatore += è perfetto.

Errore riscontrato:
```python
# Riga 12
email += "esmpio"
```

Problema: Hai scritto "esmpio" invece di "esempio" (errore di battitura).

Output prodotto: `mario@esmpio.com`
Output atteso: `mario@esempio.com`

Cosa dovevi scrivere:
```python
email += "esempio"
```

Valutazione: La logica del codice è perfetta. Questo è solo un errore di digitazione in una stringa.

---

## Esercizio 6
Punteggio: 4/5

Obiettivo: Riepilogo operatore += - costruire una frase

Analisi del codice:
Hai completato l'esercizio con la logica corretta. L'uso dell'operatore += per costruire progressivamente la frase è perfetto.

Errore riscontrato:
```python
# Riga 15
frase += " un liguaggio"
```

Problema: Hai scritto "liguaggio" invece di "linguaggio" (manca una 'n' - errore di battitura).

Output prodotto: `Python è un liguaggio fantastico`
Output atteso: `Python è un linguaggio fantastico`

Cosa dovevi scrivere:
```python
frase += " un linguaggio"
```

Valutazione: La logica del codice è perfetta. Questo è solo un errore di digitazione in una stringa.

---

## Esercizio 7
Punteggio: 5/5

Obiettivo: Calcolare e stampare la lunghezza di una stringa

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente la funzione `len()` e stampato il risultato nel formato richiesto.

---

## Esercizio 8
Punteggio: 5/5

Obiettivo: Calcolare lunghezza di una frase inserita dall'utente

Analisi del codice:
Esercizio completato perfettamente. Hai gestito correttamente l'input dell'utente e calcolato la lunghezza con `len()`.

---

## Esercizio 9
Punteggio: 3/5

Obiettivo: Riepilogo len() - calcolare lunghezza di nome e cognome

Analisi del codice:
Hai completato i calcoli correttamente con `len()`, ma l'output non corrisponde al formato richiesto.

Errore riscontrato:
```python
# Righe 18-19
print(f"{nome}, lunghezza: {n_nome} ")
print(f"{nome1}, lunghezza: {n_nome1} ")
```

Output prodotto:
```
Marco, lunghezza: 5
Bianchi, lunghezza: 7
```

Output atteso:
```
Nome: Marco, Lunghezza: 5
Cognome: Bianchi, Lunghezza: 7
```

Cosa dovevi scrivere:
```python
print(f"Nome: {nome}, Lunghezza: {n_nome}")
print(f"Cognome: {nome1}, Lunghezza: {n_nome1}")
```

Valutazione: Mancano completamente le parole "Nome:" e "Cognome:" all'inizio, e "lunghezza" ha la 'l' minuscola invece della 'L' maiuscola. L'output non corrisponde al formato richiesto.

---

## Esercizio 10
Punteggio: 4/5

Obiettivo: Convertire un nome in maiuscolo

Analisi del codice:
Hai usato correttamente il metodo `.upper()` e il codice funziona. C'è però una piccola differenza dal valore richiesto.

Errore riscontrato:
```python
# Riga 6
nome = "Luca"
```

Problema: La traccia richiede `nome = "luca"` (tutto minuscolo), ma tu hai scritto `"Luca"` con la L maiuscola.

Conseguenza: Il risultato finale è comunque "LUCA" (corretto), quindi il codice funziona. Tuttavia, non dimostri la trasformazione completa da minuscolo a maiuscolo.

Valutazione: Hai scritto una lettera maiuscola invece di minuscola, ma il risultato finale è comunque corretto. L'errore è minore.

---

## Esercizio 11
Punteggio: 5/5

Obiettivo: Convertire una parola in minuscolo con input utente

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente il metodo `.lower()` per convertire la parola in minuscolo.

---

## Esercizio 12
Punteggio: 5/5

Obiettivo: Riepilogo .upper() e .lower() - convertire nome e cognome

Analisi del codice:
Esercizio completato perfettamente. Hai convertito correttamente il nome in maiuscolo e il cognome in minuscolo, stampando nel formato richiesto.

---

## Esercizio 13
Punteggio: 5/5

Obiettivo: Confrontare la lunghezza di due parole

Analisi del codice:
Esercizio completato perfettamente. Hai calcolato le lunghezze, confrontato i valori e stampato il messaggio corretto basandoti sulla condizione.

---

## Esercizio 14
Punteggio: 5/5

Obiettivo: Verificare se una password ha una lunghezza valida (8-16 caratteri)

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica con if/elif/else per verificare le tre condizioni (troppo corta, troppo lunga, valida).

---

## Esercizio 15
Punteggio: 0/5

Obiettivo: Verificare un codice dopo aver rimosso gli spazi

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore logico grave che rende inutile l'uso di `.strip()`.

Errore riscontrato:
```python
# Righe 14-16
codice = input("inserisci un codice")
codice1 = codice.strip()
if codice == "ABC123":  # ERRORE: usa codice invece di codice1
    print("Codice corretto")
```

Problema: Hai creato la variabile `codice1` con il codice pulito (senza spazi), ma poi nella condizione `if` usi `codice` invece di `codice1`. Stai confrontando il codice ORIGINALE (con gli spazi) invece del codice PULITO.

Conseguenza: Se l'utente inserisce "   ABC123   " (con spazi), il programma stampa "Codice errato" perché `"   ABC123   " != "ABC123"`. Lo `.strip()` della riga 15 non viene utilizzato.

Cosa dovevi scrivere:
```python
codice = input("Inserisci il codice: ")
codice1 = codice.strip()
if codice1 == "ABC123":  # Usa codice1, non codice!
    print("Codice corretto")
else:
    print("Codice errato")
```

Valutazione: Errore logico grave. Devi usare la variabile trasformata (`codice1`) per il confronto, altrimenti lo `.strip()` non serve a nulla.

---

## Esercizio 16
Punteggio: 5/5

Obiettivo: Verificare un username ignorando spazi e maiuscole/minuscole

Analisi del codice:
Esercizio completato perfettamente. Hai correttamente applicato sia `.strip()` che `.lower()` e verificato lo username pulito (qui usi correttamente la variabile trasformata!).

---

## Esercizio 17
Punteggio: 5/5

Obiettivo: Verificare se "python" è contenuto in una frase

Analisi del codice:
Esercizio completato perfettamente. Hai convertito la frase in minuscolo e usato correttamente l'operatore `in` per verificare la presenza di "python".

---

## Esercizio 18
Punteggio: 4/5

Obiettivo: Contare quante volte appare la lettera 'a' in una frase

Analisi del codice:
Hai completato l'esercizio con la logica corretta (`.count()` e condizione if/else perfetti), ma ci sono due piccoli errori di battitura/formattazione.

Errori riscontrati:

1. **Riga 18 - Errore di battitura:**
   ```python
   frase = input("Inserisci una farse: ")
   ```
   Hai scritto "farse" invece di "frase".

2. **Riga 21 - Errore di maiuscola:**
   ```python
   print(f"la lettera 'a' appare {count} volte ")
   ```
   Hai scritto "la lettera" con 'l' minuscola invece di "La lettera" con 'L' maiuscola.

Valutazione: Errori minori di digitazione/formattazione. La logica del codice è perfetta.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Verificare validità di un URL

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore logico grave nelle condizioni.

Errore riscontrato:
```python
# Riga 24
if url_minuscolo.startswith ("http://") or ("https://") and url_minuscolo.endswith (".com") or (".it"):
    print("URL valido ")
```

Problema: La sintassi delle condizioni `or` è completamente errata.

Come Python interpreta il tuo codice:
- `("https://")` è sempre `True` (stringa non vuota)
- `(".it")` è sempre `True`
- La condizione diventa praticamente sempre vera

Cosa dovevi scrivere:
```python
if (url_minuscolo.startswith("http://") or url_minuscolo.startswith("https://")) and (url_minuscolo.endswith(".com") or url_minuscolo.endswith(".it")):
    print("URL valido")
else:
    print("URL non valido")
```

Oppure più leggibile:
```python
inizia_corretto = url_minuscolo.startswith("http://") or url_minuscolo.startswith("https://")
finisce_corretto = url_minuscolo.endswith(".com") or url_minuscolo.endswith(".it")

if inizia_corretto and finisce_corretto:
    print("URL valido")
else:
    print("URL non valido")
```

Spiegazione: Quando usi `or`, devi RIPETERE il metodo per ogni opzione. Non puoi scrivere `.startswith("a") or ("b")`, devi scrivere `.startswith("a") or .startswith("b")`.

Valutazione: Errore logico grave nella sintassi delle condizioni.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Validazione completa di un indirizzo email

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori logici gravi multipli.

Errori riscontrati:

1. **Manca la pulizia dell'email (ERRORE GRAVE):**
   La consegna richiede esplicitamente:
   > "Prima pulisci l'email rimuovendo gli spazi e convertendo in minuscolo"

   Non hai fatto nessuna delle due cose. Mancano:
   ```python
   email = email.strip()
   email = email.lower()
   ```

2. **Condizioni `or` malformate (ERRORE LOGICO):**
   ```python
   # Riga 26
   if "@" in  email and lungh >5 and email.endswith (".it") or (".com"):
   ```

   Stesso errore dell'esercizio 19: `or (".com")` è sempre `True`.

3. **Condizione lunghezza errata:**
   La traccia dice "almeno 5 caratteri", quindi `lunghezza >= 5`, ma tu hai scritto `lungh >5` (maggiore di 5, non maggiore o uguale).

Cosa dovevi scrivere:
```python
email = input("Inserisci un indirizzo email: ")

# 1. Pulisci l'email
email = email.strip()
email = email.lower()

# 2. Verifica condizioni
lunghezza = len(email)

if "@" in email and lunghezza >= 5 and (email.endswith(".com") or email.endswith(".it")):
    print("Email valida")
else:
    print("Email non valida")
```

Valutazione: Multipli errori logici gravi.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione della concatenazione di stringhe (es01-04)
- Buon uso dell'operatore += (es04, es06)
- Corretta applicazione di `len()` (es07, es08, es13, es14)
- Ottimo uso di `.upper()` e `.lower()` (es11, es12, es16, es17)
- Comprensione della logica condizionale base (es13, es14)
- Ottimo uso di `.strip()` e `.lower()` combinati (es16)
- Corretto uso di `.count()` e operatore `in` (es17, es18)

Aree di miglioramento:

**Errori di battitura:**
   - Es05: "esmpio" invece di "esempio"
   - Es06: "liguaggio" invece di "linguaggio"
   - Es10: "Luca" invece di "luca"
   - Es18: "farse" invece di "frase" + "la" invece di "La"

**Errori di formato:**
   - Es09: Output manca "Nome:" e "Cognome:" all'inizio

**Errori logici:**
   - Es15: Usa variabile sbagliata (codice invece di codice1)
   - Es19: Sintassi condizioni OR completamente errata
   - Es20: Manca pulizia email + condizioni OR errate + condizione lunghezza errata

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 15:** Usare `codice1` (variabile pulita) invece di `codice`
- **Esercizio 19:** Riscrivere le condizioni: `.startswith("a") or .startswith("b")`
- **Esercizio 20:** Aggiungere `strip()` e `lower()`, correggere condizioni OR, usare `>=` invece di `>`

Pattern da studiare:
```python
# SBAGLIATO
if testo.startswith("a") or ("b"):  # ("b") è sempre True!

# CORRETTO
if testo.startswith("a") or testo.startswith("b"):

# Con parentesi per chiarezza
if (testo.startswith("a") or testo.startswith("b")) and (testo.endswith("x") or testo.endswith("y")):
```

Valutazione generale:
Hai dimostrato una buona comprensione dei concetti base delle stringhe. Gli errori di battitura sono minori e non compromettono la logica del codice. I problemi principali sono tre errori logici (es15, es19, es20) che riguardano: 1) usare le variabili trasformate dopo averle create, 2) sintassi corretta delle condizioni OR con metodi. Concentrati su questi tre esercizi per migliorare significativamente il tuo punteggio (potenziale: 94/100).
