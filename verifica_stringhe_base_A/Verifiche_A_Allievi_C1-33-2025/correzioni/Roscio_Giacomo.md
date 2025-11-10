# Correzione Verifica Stringhe Base A - Roscio Giacomo

Punteggio Totale: 71/100

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
Punteggio: 3/5

Obiettivo: Costruire un indirizzo email usando +=

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore di battitura che produce un output errato.

Errore riscontrato:
```python
# Riga 12
email += "esmpio"
```

Problema: Hai scritto "esmpio" invece di "esempio". Questo produce l'email "mario@esmpio.com" invece di "mario@esempio.com" come richiesto dall'output atteso.

Cosa dovevi scrivere:
```python
email += "esempio"
```

Nota: La logica è corretta, è solo un errore di digitazione, ma l'output non corrisponde a quello atteso.

---

## Esercizio 6
Punteggio: 3/5

Obiettivo: Riepilogo operatore += - costruire una frase

Analisi del codice:
Hai completato l'esercizio correttamente nella struttura, ma c'è un errore di battitura.

Errore riscontrato:
```python
# Riga 15
frase += " un liguaggio"
```

Problema: Hai scritto "liguaggio" invece di "linguaggio" (manca una 'n'). L'output sarà "Python è un liguaggio fantastico" invece di "Python è un linguaggio fantastico".

Cosa dovevi scrivere:
```python
frase += " un linguaggio"
```

Nota: Fai attenzione agli errori di battitura, anche se la logica del codice è corretta.

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
Hai completato i calcoli correttamente, ma l'output non corrisponde al formato richiesto.

Errore riscontrato:
```python
# Righe 18-19
print(f"{nome}, lunghezza: {n_nome} ")
print(f"{nome1}, lunghezza: {n_nome1} ")
```

Problema: L'output atteso richiede:
```
Nome: Marco, Lunghezza: 5
Cognome: Bianchi, Lunghezza: 7
```

Ma il tuo output produce:
```
Marco, lunghezza: 5
Bianchi, lunghezza: 7
```

Cosa dovevi scrivere:
```python
print(f"Nome: {nome}, Lunghezza: {n_nome}")
print(f"Cognome: {nome1}, Lunghezza: {n_nome1}")
```

Spiegazione: Mancano le parole "Nome:" e "Cognome:" all'inizio di ogni riga, e "Lunghezza" dovrebbe avere la L maiuscola.

---

## Esercizio 10
Punteggio: 3/5

Obiettivo: Convertire un nome in maiuscolo

Analisi del codice:
Hai usato correttamente il metodo `.upper()`, ma il valore iniziale della variabile non corrisponde alla traccia.

Errore riscontrato:
```python
# Riga 6
nome = "Luca"
```

Problema: La traccia richiede di iniziare con `nome = "luca"` (tutto minuscolo), ma tu hai scritto `"Luca"` con la L maiuscola. Anche se il codice funziona, l'output sarà "LUCA" in entrambi i casi, quindi tecnicamente il risultato finale è corretto.

Nota: Questo è un errore minore che non compromette la funzionalità finale, ma è importante seguire esattamente la traccia per dimostrare di aver compreso il concetto. Il metodo `.upper()` serve a convertire da minuscolo a maiuscolo, quindi partire già con una maiuscola perde il senso didattico dell'esercizio.

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
Hai tentato l'esercizio ma c'è un errore grave che rende inutile l'uso di `.strip()`.

Errore riscontrato:
```python
# Righe 14-16
codice = input("inserisci un codice")
codice1 = codice.strip()
if codice == "ABC123":
    print("Codice corretto")
```

Problema: Hai creato la variabile `codice1` con il codice pulito (senza spazi), ma poi nella condizione `if` usi `codice` invece di `codice1`. Questo significa che stai confrontando il codice ORIGINALE (con gli spazi) invece del codice PULITO.

Conseguenza: Se l'utente inserisce "   ABC123   " (con spazi), il programma stamperà "Codice errato" perché `"   ABC123   " != "ABC123"`. Lo `.strip()` che hai fatto alla riga 15 non viene utilizzato.

Cosa dovevi scrivere:
```python
codice = input("Inserisci il codice: ")
codice1 = codice.strip()
if codice1 == "ABC123":  # Usa codice1, non codice!
    print("Codice corretto")
else:
    print("Codice errato")
```

Spiegazione concettuale:
Quando crei una nuova variabile (`codice1`) con una trasformazione (`.strip()`), devi usare QUELLA variabile nei passaggi successivi, non quella originale. Il senso dello `.strip()` è proprio rimuovere gli spazi per fare un confronto pulito.

---

## Esercizio 16
Punteggio: 5/5

Obiettivo: Verificare un username ignorando spazi e maiuscole/minuscole

Analisi del codice:
Esercizio completato perfettamente. Hai correttamente applicato sia `.strip()` che `.lower()` e verificato lo username pulito.

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
Hai completato l'esercizio con la logica corretta, ma ci sono due piccoli errori.

Errori riscontrati:

1. **Riga 18 - Errore di battitura nell'input:**
   ```python
   frase = input("Inserisci una farse: ")
   ```
   Hai scritto "farse" invece di "frase" (errore di battitura minore).

2. **Riga 21 - Formattazione output:**
   ```python
   print(f"la lettera 'a' appare {count} volte ")
   ```
   Hai scritto "la lettera" con la 'l' minuscola, mentre l'output atteso richiede "La lettera" con la 'L' maiuscola.

La logica con `.count()` e la condizione if/else sono corrette.

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

Problema: La sintassi delle condizioni `or` è completamente errata. Questo è uno degli errori più comuni in Python.

Come Python interpreta il tuo codice:
```python
if (url_minuscolo.startswith("http://")) or ("https://") and (url_minuscolo.endswith(".com")) or (".it"):
```

Perché è sbagliato:
1. `("https://")` è sempre `True` (una stringa non vuota è sempre vera)
2. `(".it")` è sempre `True`
3. Quindi la condizione diventa praticamente sempre vera

Cosa dovevi scrivere:
```python
# Prima parte: verifica inizio
inizia_corretto = url_minuscolo.startswith("http://") or url_minuscolo.startswith("https://")

# Seconda parte: verifica fine
finisce_corretto = url_minuscolo.endswith(".com") or url_minuscolo.endswith(".it")

# Combina le due condizioni
if inizia_corretto and finisce_corretto:
    print("URL valido")
else:
    print("URL non valido")
```

Oppure tutto in una riga (ma meno leggibile):
```python
if (url_minuscolo.startswith("http://") or url_minuscolo.startswith("https://")) and (url_minuscolo.endswith(".com") or url_minuscolo.endswith(".it")):
    print("URL valido")
else:
    print("URL non valido")
```

Spiegazione concettuale:
Quando usi `or`, devi RIPETERE il metodo per ogni opzione. Non puoi scrivere `.startswith("a") or ("b")`, devi scrivere `.startswith("a") or .startswith("b")`. E quando combini condizioni con `and` e `or`, usa le parentesi per chiarire l'ordine.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Validazione completa di un indirizzo email

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori gravi multipli.

Errori riscontrati:

1. **Manca la pulizia dell'email (CRITICO):**
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

Cosa dovevi scrivere:
```python
email = input("Inserisci un indirizzo email: ")

# 1. Pulisci l'email
email = email.strip()
email = email.lower()

# 2. Calcola la lunghezza
lunghezza = len(email)

# 3. Verifica TUTTE le condizioni
contiene_chiocciola = "@" in email
lunghezza_valida = lunghezza >= 5
dominio_valido = email.endswith(".com") or email.endswith(".it")

# 4. Controlla se TUTTE le condizioni sono vere
if contiene_chiocciola and lunghezza_valida and dominio_valido:
    print("Email valida")
else:
    print("Email non valida")
```

Oppure in forma compatta:
```python
email = input("Inserisci un indirizzo email: ")
email = email.strip().lower()
lunghezza = len(email)

if "@" in email and lunghezza >= 5 and (email.endswith(".com") or email.endswith(".it")):
    print("Email valida")
else:
    print("Email non valida")
```

Spiegazione:
- Manca completamente la fase di pulizia (strip e lower)
- La condizione `>5` dovrebbe essere `>=5` (almeno 5 caratteri, non più di 5)
- Il problema con `or (".com")` è lo stesso dell'esercizio 19

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione della concatenazione di stringhe (es01-04)
- Buon uso dell'operatore += (es04, es06)
- Corretta applicazione di `len()` per calcolare lunghezze (es07, es08, es13, es14)
- Ottimo uso di `.upper()` e `.lower()` (es11, es12, es16, es17)
- Comprensione della logica condizionale base (es13, es14)
- Ottimo uso di `.strip()` e `.lower()` combinati (es16)
- Corretto uso di `.count()` e operatore `in` (es17, es18)

Aree da migliorare URGENTEMENTE:

1. **Attenzione agli errori di battitura (NON CRITICO ma da migliorare):**
   - Es05: "esmpio" invece di "esempio"
   - Es06: "liguaggio" invece di "linguaggio"
   - Es18: "farse" invece di "frase"
   - Rileggi sempre il codice prima di consegnarlo

2. **Formattazione dell'output (IMPORTANTE):**
   - Es09: Output manca "Nome:" e "Cognome:" all'inizio
   - Es18: "la lettera" invece di "La lettera" (maiuscola)
   - Segui ESATTAMENTE il formato richiesto nell'output atteso

3. **Uso corretto delle variabili trasformate (CRITICO - Es15):**
   - Quando crei una variabile trasformata (`codice1 = codice.strip()`), devi usare la variabile TRASFORMATA (`codice1`) nei passaggi successivi
   - Altrimenti la trasformazione è inutile
   - Questo è un errore concettuale importante

4. **Sintassi delle condizioni `or` con metodi di stringa (CRITICO - Es19, Es20):**
   - **ERRORE COMUNE**: NON puoi scrivere `.startswith("a") or ("b")`
   - **CORRETTO**: Devi scrivere `.startswith("a") or .startswith("b")`
   - Devi RIPETERE il metodo per ogni opzione
   - Quando combini `and` e `or`, usa le parentesi per chiarezza
   - Questo è un errore logico fondamentale da correggere

5. **Leggere attentamente la consegna (CRITICO - Es20):**
   - Es20 richiedeva esplicitamente di pulire l'email con `.strip()` e `.lower()`
   - Hai saltato completamente questo passaggio
   - Leggi OGNI parola della consegna, non solo lo scopo generale

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 15:** Usare `codice1` (variabile pulita) invece di `codice` (variabile originale)
- **Esercizio 19:** Riscrivere completamente le condizioni OR in modo corretto
- **Esercizio 20:** Aggiungere strip() e lower(), correggere le condizioni OR, cambiare >5 in >=5

Pattern da studiare:
```python
# SBAGLIATO - Non funziona!
if testo.startswith("a") or ("b"):

# CORRETTO - Funziona!
if testo.startswith("a") or testo.startswith("b"):

# OPPURE con parentesi per chiarezza
if (testo.startswith("a") or testo.startswith("b")) and (testo.endswith("x") or testo.endswith("y")):
```

Valutazione generale:
Hai dimostrato una buona comprensione dei concetti base delle stringhe in Python. I tuoi punti di forza sono nella concatenazione, nell'uso di len(), upper(), lower() e nella logica condizionale semplice. Hai anche dimostrato di saper combinare strip() e lower() correttamente (es16). Gli errori principali sono tre: 1) disattenzione negli errori di battitura (es05, es06, es18), 2) non usare le variabili trasformate nei passaggi successivi (es15), e 3) sintassi errata delle condizioni OR con metodi di stringa (es19, es20). Quest'ultimo è un errore concettuale comune ma importante da correggere. Correggendo questi tre aspetti e facendo più attenzione alla formattazione dell'output, puoi facilmente raggiungere l'eccellenza.
