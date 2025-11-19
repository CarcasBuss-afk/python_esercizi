# Correzione Verifica Stringhe Base B - Zamboni Rudy

Punteggio Totale: 79/100

---

## Esercizio 1
Punteggio: 5/5

Obiettivo: Calcolare e stampare la lunghezza del nome di uno sport

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente la funzione `len()` e stampato il risultato nel formato richiesto.

---

## Esercizio 2
Punteggio: 5/5

Obiettivo: Calcolare lunghezza del nome di un corso inserito dall'utente

Analisi del codice:
Esercizio completato perfettamente. Hai gestito correttamente l'input dell'utente e calcolato la lunghezza con `len()`.

---

## Esercizio 3
Punteggio: 4/5

Obiettivo: Riepilogo len() - calcolare lunghezza di prodotto e descrizione

Analisi del codice:
Hai completato l'esercizio con la logica corretta, ma c'è un errore di battitura nell'input.

Errore riscontrato:
```python
# Riga 11
Descrizione = input("Inserisci la desriione del prodotto: ")
```

Problema: Hai scritto "desriione" invece di "descrizione". È un errore di digitazione. Inoltre hai usato "Descrizione" con la D maiuscola come nome di variabile, che funziona ma per convenzione le variabili si scrivono in minuscolo.

Output prodotto: `Inserisci la desriione del prodotto:`
Output atteso: `Inserisci la descrizione:`

Cosa dovevi scrivere:
```python
descrizione = input("Inserisci la descrizione: ")
```

Valutazione: Errore di battitura. Il programma funziona ma il prompt ha un typo.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Convertire un codice prodotto in maiuscolo

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente il metodo `.upper()` per convertire il codice in maiuscolo.

---

## Esercizio 5
Punteggio: 2/5

Obiettivo: Convertire uno username in minuscolo con input utente

Analisi del codice:
Hai completato l'esercizio con la **logica corretta** - hai usato `.lower()` correttamente per convertire lo username in minuscolo. Tuttavia, l'output non corrisponde al formato richiesto.

Errore riscontrato:
```python
# Riga 12
print(f"Il nome è {username_minuscolo}")
```

Problema: Hai aggiunto "Il nome è " prima dello username, ma la traccia richiede di stampare SOLO lo username in minuscolo, senza etichette.

Output prodotto: `Il nome è gamer99`
Output atteso: `gamer99`

Cosa dovevi scrivere:
```python
print(username_minuscolo)
```

Valutazione: La logica della conversione è corretta (`.lower()` usato perfettamente), ma l'output ha informazioni extra non richieste.

---

## Esercizio 6
Punteggio: 4/5

Obiettivo: Riepilogo .upper() e .lower() - convertire hashtag e username

Analisi del codice:
Hai completato l'esercizio con la logica corretta, ma ci sono errori di battitura.

Errori riscontrati:

1. **Riga 17 - Typo:**
   ```python
   hashtag = input("Inserisci un hastag: ")
   ```
   Hai scritto "hastag" invece di "hashtag" (manca la 'h').

2. **Riga 23 - Maiuscola sbagliata:**
   ```python
   print(f"username: {a_nome}")
   ```
   Hai scritto "username:" minuscolo invece di "Username:" maiuscolo.

Output prodotto:
```
Hashtag: PYTHON
username: coder123
```

Output atteso:
```
Hashtag: PYTHON
Username: coder123
```

Cosa dovevi scrivere:
```python
hashtag = input("Inserisci un hashtag: ")
# ... resto del codice ...
print(f"Username: {a_nome}")
```

Valutazione: Errori di battitura. La logica è perfetta ma ci sono typo nell'input e nell'output.

---

## Esercizio 7
Punteggio: 5/5

Obiettivo: Concatenare nome prodotto e categoria con uno spazio

Analisi del codice:
Esercizio completato perfettamente. Hai correttamente concatenato le stringhe usando l'operatore + con lo spazio tra prodotto e categoria.

---

## Esercizio 8
Punteggio: 4/5

Obiettivo: Concatenare via, numero civico e città

Analisi del codice:
Hai completato l'esercizio con la logica corretta, ma c'è un errore di battitura nell'input.

Errore riscontrato:
```python
# Riga 13
citta = input("inserisci la citta in cui abiti: ")
```

Problemi:
- "inserisci" minuscolo invece di "Inserisci" maiuscolo
- "citta in cui abiti" invece di "Inserisci la città" (prompt diverso da quello atteso)

Output prodotto: `inserisci la citta in cui abiti:`
Output atteso: `Inserisci la città:`

Cosa dovevi scrivere:
```python
citta = input("Inserisci la città: ")
```

Valutazione: Errore di battitura. Il programma funziona ma il prompt è diverso da quello richiesto.

---

## Esercizio 9
Punteggio: 2/5

Obiettivo: Riepilogo concatenazione - creare carta d'identità

Analisi del codice:
Hai completato l'esercizio usando la **logica corretta della concatenazione** - hai usato l'operatore `+` per unire le stringhe correttamente. Tuttavia, ci sono errori nell'output.

Errori riscontrati:

1. **Riga 20 - Etichetta sbagliata:**
   ```python
   carta_identita = "Nome: " + nome + ", Cognome: " + cognome + ", Codice Fiscale: " + cf
   ```
   Hai scritto "Codice Fiscale:" invece di "CF:".

2. **Riga 21 - Aggiunta etichetta extra:**
   ```python
   print(f"Carta d'idendità: {carta_identita}")
   ```
   Hai aggiunto "Carta d'idendità: " prima di stampare, ma non era richiesto. La traccia chiede solo di stampare la carta d'identità, non di aggiungere un'altra etichetta.

Output prodotto: `Carta d'idendità: Nome: Luigi, Cognome: Verdi, Codice Fiscale: VRDLGU80A01H501Z`

Output atteso: `Nome: Luigi, Cognome: Verdi, CF: VRDLGU80A01H501Z`

Cosa dovevi scrivere:
```python
carta_identita = "Nome: " + nome + ", Cognome: " + cognome + ", CF: " + cf
print(carta_identita)
```

Valutazione: La logica della concatenazione è corretta, ma l'output ha etichette sbagliate ("Codice Fiscale:" invece di "CF:") e informazioni extra ("Carta d'idendità:").

---

## Esercizio 10
Punteggio: 3/5

Obiettivo: Costruire un numero di telefono usando +=

Analisi del codice:
Hai usato correttamente l'operatore +=, ma c'è un errore nel formato.

Errore riscontrato:
```python
# Riga 12
telefono += "1234567"
```

Problema: Manca lo spazio prima di "1234567". La traccia richiede `" 1234567"` (con spazio), ma tu hai scritto `"1234567"` (senza spazio).

Output prodotto: `+39 021234567`
Output atteso: `+39 02 1234567`

Cosa dovevi scrivere:
```python
telefono += " 1234567"
```

Valutazione: Errore di formato. Manca uno spazio.

---

## Esercizio 11
Punteggio: 2/5

Obiettivo: Costruire un URL usando +=

Analisi del codice:
Hai completato l'esercizio con la **logica corretta** - hai usato l'operatore `+=` perfettamente per costruire l'URL. Tuttavia, l'output non corrisponde al formato richiesto.

Errore riscontrato:
```python
# Riga 18
print(f"URL: {url}")
```

Problema: Hai aggiunto "URL: " prima dell'URL, ma la traccia richiede di stampare SOLO l'URL, senza etichette.

Output prodotto: `URL: http://www.negozio.it`
Output atteso: `http://www.negozio.it`

Cosa dovevi scrivere:
```python
print(url)
```

Valutazione: La logica dell'operatore `+=` è corretta, ma l'output ha un'etichetta extra non richiesta.

---

## Esercizio 12
Punteggio: 5/5

Obiettivo: Riepilogo operatore += - costruire un messaggio

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente l'operatore += per costruire il messaggio nel formato richiesto.

---

## Esercizio 13
Punteggio: 5/5

Obiettivo: Verificare se "online" è contenuto nella modalità del corso

Analisi del codice:
Esercizio completato perfettamente. Hai convertito la modalità in minuscolo e usato correttamente l'operatore `in` per verificare la presenza di "online".

---

## Esercizio 14
Punteggio: 5/5

Obiettivo: Verificare se una parola chiave è nella descrizione del prodotto

Analisi del codice:
Esercizio completato perfettamente. Hai convertito entrambe le stringhe in minuscolo e usato correttamente l'operatore `in` per verificare la presenza della parola chiave.

---

## Esercizio 15
Punteggio: 4/5

Obiettivo: Verificare un codice coupon dopo aver rimosso gli spazi

Analisi del codice:
Hai completato l'esercizio con la logica corretta, ma c'è un errore di battitura nell'output.

Errore riscontrato:
```python
# Riga 20
print("Coupon Valido")
```

Problema: Hai scritto "Valido" con la "V" maiuscola invece di "valido" con la "v" minuscola.

Output prodotto: `Coupon Valido`
Output atteso: `Coupon valido`

Cosa dovevi scrivere:
```python
print("Coupon valido")
```

Valutazione: Errore di battitura. La logica è perfetta ma c'è una maiuscola sbagliata.

---

## Esercizio 16
Punteggio: 5/5

Obiettivo: Contare quante vocali 'e' ci sono in una frase

Analisi del codice:
Esercizio completato perfettamente. Hai convertito la frase in minuscolo e usato correttamente il metodo `.count()` per contare le lettere 'e'.

---

## Esercizio 17
Punteggio: 5/5

Obiettivo: Contare gli spazi in una descrizione e classificarla

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente `.count(" ")` per contare gli spazi e implementato la logica if/else per classificare la descrizione.

---

## Esercizio 18
Punteggio: 5/5

Obiettivo: Validazione numero di telefono

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente entrambe le verifiche: lunghezza >= 10 usando `len()` e inizio con "+39" usando `.startswith()`, combinandole con `and`.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Validazione completa username

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori GRAVISSIMI che rendono la logica completamente sbagliata.

Errori riscontrati:

1. **Riga 30 - Metodo completamente sbagliato:**
   ```python
   num = nome.isalnum()
   ```
   Problema: `isalnum()` verifica se la stringa contiene **SOLO** caratteri alfanumerici (lettere e numeri, nessun spazio o carattere speciale). NON verifica se la stringa "contiene almeno un numero"!

   Differenza:
   - `isalnum()` ritorna `True` per "Gamer99" (solo lettere e numeri) MA anche per "player" (solo lettere)!
   - "Gamer99".isalnum() → True (corretto)
   - "player".isalnum() → True (SBAGLIATO! Non ha numeri ma isalnum() ritorna True perché non ha caratteri speciali)

   La traccia richiede: "contiene **almeno un numero**", che è completamente diverso!

2. **Riga 35 - Condizione sbagliata:**
   ```python
   if lung > 5 and lung < 15 and num == True:
   ```
   Problema: La lunghezza deve essere **tra 5 e 15** (inclusi), quindi `>= 5 and <= 15`, ma tu hai scritto `> 5 and < 15` che esclude 5 e 15.

   Conseguenza:
   - "Game5" (5 caratteri) → non valido (dovrebbe essere valido!)
   - "GamerPlayerPro" (15 caratteri) → non valido (dovrebbe essere valido!)

3. **Righe 27-28 - Ordine operazioni sbagliato:**
   ```python
   nome = username.lower()
   nome = username.strip()
   ```
   Problema: Prima converti in minuscolo, poi fai `.strip()` su `username` (originale) invece che su `nome`. Il risultato di `.lower()` viene sovrascritto e perso!

   Conseguenza: `nome` contiene solo `.strip()` senza `.lower()`.

Cosa dovevi scrivere:
```python
username = input("Inserisci uno username: ")

username_pulito = username.strip().lower()

lunghezza_originale = len(username)
lunghezza_pulita = len(username_pulito)

no_spazi = lunghezza_originale == lunghezza_pulita
lunghezza_ok = 5 <= lunghezza_pulita <= 15

contiene_numero = ("0" in username_pulito or "1" in username_pulito or
                   "2" in username_pulito or "3" in username_pulito or
                   "4" in username_pulito or "5" in username_pulito or
                   "6" in username_pulito or "7" in username_pulito or
                   "8" in username_pulito or "9" in username_pulito)

if no_spazi and lunghezza_ok and contiene_numero:
    print("Username valido")
else:
    print("Username non valido")
```

Spiegazione:
- `isalnum()` verifica se **tutti** i caratteri sono alfanumerici (no spazi, no simboli)
- Per verificare "contiene almeno un numero", devi controllare se almeno una cifra 0-9 è presente usando `in`
- La lunghezza deve essere `>= 5 and <= 15`, non `> 5 and < 15`

Valutazione: Errori logici gravissimi. Uso di metodo completamente sbagliato (`isalnum()` invece di verificare presenza numeri) + condizione di lunghezza errata.

---

## Esercizio 20
Punteggio: 4/5

Obiettivo: Validazione completa codice prodotto

Analisi del codice:
Hai completato l'esercizio con la logica perfetta, ma ci sono errori di battitura nell'output.

Errore riscontrato:
```python
# Righe 33-35
print("CODICE VALIDO")
# ...
print("CODICE NON VALIDO")
```

Problema: Hai scritto "CODICE VALIDO" e "CODICE NON VALIDO" tutto in maiuscolo, ma la traccia richiede "Codice valido" e "Codice non valido" (solo prima lettera maiuscola).

Output prodotto: `CODICE VALIDO` / `CODICE NON VALIDO`
Output atteso: `Codice valido` / `Codice non valido`

Cosa dovevi scrivere:
```python
if lung == 7 and "-" in cod and cod.startswith("ABC"):
    print("Codice valido")
else:
    print("Codice non valido")
```

Valutazione: Errore di battitura. La logica è perfetta (usi `.strip()`, `.upper()`, verifichi tutte le condizioni correttamente) ma l'output ha maiuscole sbagliate.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione di `len()` (es01, es02, es18)
- Perfetto uso di `.upper()` e `.lower()` (es04, es05, es06)
- Corretta applicazione della concatenazione (es07, es08)
- Ottimo uso dell'operatore += (es10, es12)
- Perfetta comprensione dell'operatore `in` (es13, es14)
- Eccellente uso di `.strip()` (es15, es20)
- Ottimo uso di `.count()` (es16, es17)
- Perfetta implementazione di validazione con `.startswith()` e `len()` (es18, es20)

Aree di miglioramento:

**Errori di battitura (4/5):**
   - Es03: "desriione" invece di "descrizione"
   - Es06: "hastag" invece di "hashtag", "username:" invece di "Username:"
   - Es08: "inserisci" minuscola, prompt diverso
   - Es15: "Valido" invece di "valido"
   - Es20: "CODICE VALIDO" tutto maiuscolo invece di "Codice valido"

**Logica corretta ma output impreciso (2/5):**
   - Es05: Aggiunge "Il nome è " non richiesto
   - Es09: Usa "Codice Fiscale:" invece di "CF:" + aggiunge "Carta d'idendità:"
   - Es11: Aggiunge "URL: " non richiesto

**Errori di formato (3/5):**
   - Es10: Manca spazio prima di "1234567"

**Errori logici gravi (0/5):**
   - Es19: Usa `isalnum()` invece di verificare "contiene almeno un numero" + condizione lunghezza sbagliata (`> 5 and < 15` invece di `>= 5 and <= 15`)

**PROBLEMA CRITICO - es19**: Hai usato `isalnum()` che verifica se **tutti** i caratteri sono alfanumerici, NON se la stringa "contiene almeno un numero"!

```python
# DIFFERENZA TRA isalnum() E "contiene almeno un numero"

"Gamer99".isalnum()  # True - solo lettere e numeri
"player".isalnum()   # True - SBAGLIATO! Non ha numeri ma ritorna True!

# "player" NON contiene numeri, ma isalnum() ritorna True perché non ha spazi/caratteri speciali

# Per verificare "contiene almeno un numero":
"0" in "player" or "1" in "player" or ... or "9" in "player"  # False - corretto!
"0" in "Gamer99" or "1" in "player" or ... or "9" in "player"  # True - corretto!
```

Inoltre, la condizione di lunghezza deve essere `>= 5 and <= 15` (tra 5 e 15 **inclusi**), non `> 5 and < 15` (che esclude 5 e 15).

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 19:** Sostituisci `isalnum()` con il controllo "contiene almeno un numero" usando `in`, e cambia `> 5 and < 15` in `>= 5 and <= 15`

Consigli per migliorare:
1. **Leggere attentamente l'output atteso**: Es05, es09, es11 aggiungono etichette non richieste
2. **Attenzione alle maiuscole**: Es06, es15, es20 hanno maiuscole sbagliate
3. **Differenza tra "tutti alfanumerici" e "contiene almeno un numero"**: `isalnum()` vs `"0" in stringa or "1" in stringa ...`
4. **Condizioni di lunghezza inclusive**: `>= 5 and <= 15` non `> 5 and < 15`

Valutazione generale:
Ottimo lavoro complessivo! Hai dimostrato una solida comprensione dei concetti fondamentali (len, upper, lower, strip, count, in, startswith) e la maggior parte degli esercizi sono corretti. I principali problemi sono: 1) Errori di battitura in diversi esercizi (typo nei prompt, maiuscole sbagliate), 2) Output con informazioni extra non richieste (es05, es09, es11), 3) Errore concettuale grave nell'es19 (uso di `isalnum()` invece di verificare presenza numeri). La tua logica di programmazione è generalmente buona - devi solo fare più attenzione ai dettagli dell'output richiesto e alla differenza tra metodi come `isalnum()` e il controllo specifico "contiene almeno un numero". Correggendo l'es19 e facendo più attenzione ai dettagli puoi facilmente raggiungere 90-95/100. Ottimo lavoro!
