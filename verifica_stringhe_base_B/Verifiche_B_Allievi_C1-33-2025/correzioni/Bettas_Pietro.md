# Correzione Verifica Stringhe Base B - Bettas Pietro

Punteggio Totale: 66/100

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
Punteggio: 2/5

Obiettivo: Riepilogo len() - calcolare lunghezza di prodotto e descrizione

Analisi del codice:
Hai completato l'esercizio con la **logica corretta** - hai usato `len()` correttamente per calcolare entrambe le lunghezze e hai stampato i risultati. Tuttavia, ci sono errori di formato nell'output.

Errori riscontrati:

1. **Righe 7-8 - Prompt imprecisi:**
   ```python
   prodotto = input("inserisci il nome del prodotto: ")
   descrizione = input("descrivi il prodotto: ")
   ```
   Problemi:
   - "inserisci" con la 'i' minuscola invece di "Inserisci" maiuscola
   - "descrivi il prodotto" invece di "Inserisci la descrizione"

2. **Righe 11-12 - Output con formato sbagliato:**
   ```python
   print(f" prodotto: {prodotto}, lunghezza: {lunghezza_prodotto}")
   print(f" descrizione: {descrizione}, lunghezza: {lunghezza_descrizione}")
   ```
   Problemi:
   - Spazio all'inizio: `" prodotto:"` invece di `"Prodotto:"`
   - "prodotto" minuscolo invece di "Prodotto" maiuscolo
   - "lunghezza" minuscolo invece di "Lunghezza" maiuscolo
   - Stesso per "descrizione"

Output prodotto:
```
 prodotto: Notebook, lunghezza: 8
 descrizione: Computer portatile, lunghezza: 18
```

Output atteso:
```
Prodotto: Notebook, Lunghezza: 8
Descrizione: Computer portatile, Lunghezza: 18
```

Cosa dovevi scrivere:
```python
prodotto = input("Inserisci il nome del prodotto: ")
descrizione = input("Inserisci la descrizione: ")
lunghezza_prodotto = len(prodotto)
lunghezza_descrizione = len(descrizione)
print(f"Prodotto: {prodotto}, Lunghezza: {lunghezza_prodotto}")
print(f"Descrizione: {descrizione}, Lunghezza: {lunghezza_descrizione}")
```

Valutazione: La logica è corretta (calcoli con `len()` perfetti), ma ci sono errori di formato: prompt imprecisi e output con minuscole/spazi extra invece delle maiuscole richieste.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Convertire un codice prodotto in maiuscolo

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente il metodo `.upper()` per convertire il codice in maiuscolo.

---

## Esercizio 5
Punteggio: 5/5

Obiettivo: Convertire uno username in minuscolo con input utente

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente il metodo `.lower()` per convertire lo username in minuscolo.

---

## Esercizio 6
Punteggio: 2/5

Obiettivo: Riepilogo .upper() e .lower() - convertire hashtag e username

Analisi del codice:
Hai completato l'esercizio con la **logica corretta** - hai usato `.upper()` e `.lower()` correttamente sulle variabili giuste (`hashtag_maiuscolo = hashtag.upper()` e `username_minuscolo = username.lower()`). Tuttavia, ci sono errori negli input e nell'output.

Errori riscontrati:

1. **Righe 7-8 - Prompt sbagliati:**
   ```python
   hashtag = input("inserisci un hashtag minuscolo: ")
   username = input("inserisci un username maiuscolo: ")
   ```
   Problemi:
   - "inserisci" minuscolo invece di "Inserisci" maiuscolo
   - "inserisci un hashtag minuscolo" invece di "Inserisci un hashtag" - non devi dire all'utente come inserire i dati!
   - "inserisci un username maiuscolo" invece di "Inserisci uno username"

2. **Righe 11-12 - Output senza etichette:**
   ```python
   print(hashtag_maiuscolo)
   print(username_minuscolo)
   ```
   Problema: Hai stampato solo i valori senza le etichette "Hashtag:" e "Username:"!

Output prodotto:
```
PYTHON
coder123
```

Output atteso:
```
Hashtag: PYTHON
Username: coder123
```

Cosa dovevi scrivere:
```python
hashtag = input("Inserisci un hashtag: ")
username = input("Inserisci uno username: ")
hashtag_maiuscolo = hashtag.upper()
username_minuscolo = username.lower()
print(f"Hashtag: {hashtag_maiuscolo}")
print(f"Username: {username_minuscolo}")
```

Valutazione: La logica delle conversioni è corretta (`.upper()` e `.lower()` usati perfettamente), ma mancano le etichette nell'output.

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
Hai completato l'esercizio con la logica corretta, ma ci sono errori di battitura negli input.

Errore riscontrato:
```python
# Righe 9, 13
numero = input("Inserisci il numero civico:")
citta = input("Inserisci la città:")
```

Problema: Manca lo spazio dopo i due punti. Dovrebbe essere `"Inserisci il numero civico: "` con uno spazio dopo i `:`.

Output prodotto:
```
Inserisci il numero civico:42
Inserisci la città:Milano
```

Output atteso:
```
Inserisci il numero civico: 42
Inserisci la città: Milano
```

Cosa dovevi scrivere:
```python
numero = input("Inserisci il numero civico: ")
citta = input("Inserisci la città: ")
```

Valutazione: Errori di battitura. Mancano gli spazi dopo i due punti nei prompt.

---

## Esercizio 9
Punteggio: 2/5

Obiettivo: Riepilogo concatenazione - creare carta d'identità

Analisi del codice:
Hai completato l'esercizio usando la **logica corretta della concatenazione** - hai usato l'operatore `+` per unire le stringhe. Tuttavia, l'output non corrisponde al formato richiesto perché mancano completamente le etichette.

Errore riscontrato:
```python
# Riga 10
carta_didentita = nome + " " + cognome + "," + cf
```

Problema: Hai concatenato solo i valori senza le etichette "Nome:", "Cognome:", "CF:". L'esercizio richiede un formato specifico con queste etichette.

Output prodotto: `Luigi Verdi,VRDLGU80A01H501Z`

Output atteso: `Nome: Luigi, Cognome: Verdi, CF: VRDLGU80A01H501Z`

Cosa dovevi scrivere:
```python
nome = input("Inserisci il nome: ")
cognome = input("Inserisci il cognome: ")
cf = input("Inserisci il codice fiscale: ")
carta_identita = f"Nome: {nome}, Cognome: {cognome}, CF: {cf}"
print(carta_identita)
```

Valutazione: La logica della concatenazione è corretta (sai usare l'operatore `+`), ma non hai capito che il formato richiede le etichette "Nome:", "Cognome:", "CF:".

---

## Esercizio 10
Punteggio: 3/5

Obiettivo: Costruire un numero di telefono usando +=

Analisi del codice:
Hai usato correttamente l'operatore +=, ma c'è un errore nel formato.

Errore riscontrato:
```python
# Riga 9
telefono += " 02 "
```

Problema: Hai aggiunto uno spazio extra dopo "02". La traccia richiede `" 02"` (uno spazio prima), ma tu hai scritto `" 02 "` (uno spazio prima E uno dopo).

Output visivamente uguale ma logica sbagliata nella divisione degli spazi.

Cosa dovevi scrivere:
```python
telefono = "+39"
telefono += " 02"
telefono += " 1234567"
print(telefono)
```

Valutazione: Errore di formato. Gli spazi sono nella posizione sbagliata anche se l'output finale visivo è corretto.

---

## Esercizio 11
Punteggio: 5/5

Obiettivo: Costruire un URL usando +=

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente l'operatore += per costruire l'URL.

---

## Esercizio 12
Punteggio: 3/5

Obiettivo: Riepilogo operatore += - costruire un messaggio

Analisi del codice:
Hai usato correttamente l'operatore +=, ma c'è un errore nel formato.

Errore riscontrato:
```python
# Riga 19
messaggio += "Tutto bene"
```

Problema: Manca lo spazio prima di "Tutto bene". Dopo il "?" non c'è spazio, quindi l'output sarà "...stai?Tutto bene!" invece di "...stai? Tutto bene!".

Output prodotto: `Ciao, come stai?Tutto bene!`
Output atteso: `Ciao, come stai? Tutto bene!`

Cosa dovevi scrivere:
```python
messaggio += " Tutto bene"  # Con lo spazio prima
```

Valutazione: Errore di formato. Manca uno spazio prima di "Tutto bene".

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
Punteggio: 0/5

Obiettivo: Verificare un codice coupon dopo aver rimosso gli spazi

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori GRAVISSIMI che stravolgono completamente la logica richiesta.

Errori riscontrati:

1. **Non hai usato `.strip()`:**
   La traccia dice esplicitamente "Rimuovi gli spazi all'inizio e alla fine del codice" ma tu non hai chiamato `.strip()` da nessuna parte!

2. **Riga 17 - Operatore sbagliato:**
   ```python
   if "SCONTO20" in coupon:
   ```
   Problema: Hai usato l'operatore `in` invece di `==`. Questo è completamente sbagliato!

   Differenza:
   - `in` verifica se "SCONTO20" è **contenuto** nel coupon
   - `==` verifica se il coupon è **uguale** a "SCONTO20"

   Se l'utente inserisce "SCONTO2019" o "PROMO_SCONTO20_EXTRA", il tuo programma accetta il coupon perché "SCONTO20" è contenuto in quelle stringhe!

   La traccia richiede: "Se il codice pulito è **uguale** a 'SCONTO20'", non "se contiene SCONTO20"!

Cosa dovevi scrivere:
```python
codice = input("Inserisci il codice coupon: ")
codice_pulito = codice.strip()

if codice_pulito == "SCONTO20":
    print("Coupon valido")
else:
    print("Coupon non valido")
```

Valutazione: Errori logici gravissimi. Non usi `.strip()` E usi `in` invece di `==`.

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
Punteggio: 0/5

Obiettivo: Validazione numero di telefono

Analisi del codice:
Hai tentato l'esercizio ma il codice è COMPLETAMENTE SBAGLIATO con errori gravissimi che rendono il programma probabilmente non eseguibile.

Errori riscontrati:

1. **Riga 21 - Logica completamente sbagliata:**
   ```python
   numeri = numero.count(numero)
   ```
   Problema: `.count()` conta quante volte un carattere/sottostringa appare in una stringa. Stai chiedendo "quante volte la stringa intera appare in se stessa" → **sempre 1**! Questo non ha senso.

2. **Riga 22 - Tipo sbagliato:**
   ```python
   numero_chiave = (+39)
   ```
   Problema: `(+39)` è un **numero** (39), non la **stringa** "+39"! Dovresti scrivere `"+39"` con le virgolette.

3. **Riga 23 - Errore di tipo:**
   ```python
   if numero in numero_chiave:
   ```
   Problema: Stai cercando se una **stringa** (`numero`) è contenuta in un **numero** (`numero_chiave = 39`). Questo probabilmente darà un errore di tipo! E anche la logica è invertita - dovresti verificare se `numero` **inizia con** "+39", non se è contenuto!

4. **Riga 25 - Confronto sbagliato:**
   ```python
   elif numeri == "10":
   ```
   Problema: `numeri` è un numero intero (risultato di `.count()`), ma lo confronti con la stringa `"10"`. Dovresti confrontare `numeri == 10` (senza virgolette). Ma la logica è comunque completamente sbagliata!

5. **Manca la verifica corretta:**
   L'esercizio richiede di verificare:
   - Lunghezza >= 10: devi usare `len(numero) >= 10`
   - Inizia con "+39": devi usare `numero.startswith("+39")`

Il tuo codice non implementa nessuna di queste verifiche correttamente.

Cosa dovevi scrivere:
```python
numero = input("Inserisci un numero di telefono: ")

lunghezza = len(numero)
inizia_corretto = numero.startswith("+39")

if lunghezza >= 10 and inizia_corretto:
    print("Numero valido")
else:
    print("Numero non valido")
```

Valutazione: Errori logici gravissimi. Il codice è completamente sbagliato e probabilmente non eseguibile.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Validazione completa username

Analisi del codice:
**Esercizio NON svolto.** Il file contiene solo i commenti della traccia, nessun codice.

Il codice completo doveva essere:
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

Valutazione: Esercizio non consegnato.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Validazione completa codice prodotto

Analisi del codice:
**Esercizio NON svolto.** Il file contiene solo i commenti della traccia, nessun codice.

Il codice completo doveva essere:
```python
codice = input("Inserisci un codice prodotto: ")

codice_pulito = codice.strip().upper()

lunghezza = len(codice_pulito)

if (lunghezza == 7) and ("-" in codice_pulito) and (codice_pulito.startswith("ABC")):
    print("Codice valido")
else:
    print("Codice non valido")
```

Valutazione: Esercizio non consegnato.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Buona comprensione di `len()` (es01, es02)
- Corretto uso di `.upper()` e `.lower()` dal punto di vista logico (es04, es05, es06)
- Ottima applicazione della concatenazione base (es07)
- Corretto uso dell'operatore += (es11)
- Perfetta comprensione dell'operatore `in` quando usato correttamente (es13, es14)
- Ottimo uso di `.count()` (es16, es17)

Aree di miglioramento:

**Errori di formato/battitura (4/5 o 3/5):**
   - Es08: Mancano spazi dopo ":" nei prompt
   - Es10: Spazi nella posizione sbagliata
   - Es12: Manca spazio prima di "Tutto bene"

**Logica corretta ma output impreciso (2/5):**
   - Es03: Usa `len()` correttamente ma output con minuscole/spazi extra
   - Es06: Usa `.upper()` e `.lower()` correttamente ma mancano etichette nell'output
   - Es09: Usa concatenazione correttamente ma mancano etichette

**Errori logici gravi (0/5):**
   - Es15: Non usa `.strip()` + usa `in` invece di `==` (accetta "SCONTO2019"!)
   - Es18: Codice completamente illogico (logica assurda, errori di tipo)
   - Es19: Non svolto
   - Es20: Non svolto

**PROBLEMA CRITICO - es15**: Hai usato `in` invece di `==`. Questo è un errore gravissimo!

```python
# IL TUO CODICE (SBAGLIATO)
if "SCONTO20" in coupon:  # Verifica se "SCONTO20" è contenuto

# Problema: accetta anche questi codici!
"SCONTO2019" → contiene "SCONTO20" → VALIDO (SBAGLIATO!)
"PROMO_SCONTO20" → contiene "SCONTO20" → VALIDO (SBAGLIATO!)

# CODICE CORRETTO
if codice_pulito == "SCONTO20":  # Verifica se è esattamente uguale
```

**PROBLEMA CRITICO - es18**: Il codice è completamente illogico:

```python
numeri = numero.count(numero)  # Conta quante volte la stringa appare in se stessa → sempre 1!
numero_chiave = (+39)          # Crea un numero (39) non una stringa!
if numero in numero_chiave:    # Cerca una stringa in un numero → ERRORE!
```

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 3:** Correggi i prompt (maiuscole), usa maiuscole per "Prodotto", "Descrizione", "Lunghezza"
- **Esercizio 6:** Aggiungi le etichette "Hashtag:" e "Username:" nell'output
- **Esercizio 9:** Aggiungi le etichette "Nome:", "Cognome:", "CF:" usando f-string
- **Esercizio 15:** Usa `.strip()` E usa `==` invece di `in`
- **Esercizio 18:** Riscrivi completamente usando `len()` e `.startswith()`
- **Esercizio 19:** Completa l'esercizio
- **Esercizio 20:** Completa l'esercizio

Pattern da studiare:
```python
# Differenza tra "contiene" e "uguale"
"SCONTO20" in "SCONTO2019"     # True - è contenuto
"SCONTO2019" == "SCONTO20"     # False - non è uguale

# Verifica inizio stringa
numero.startswith("+39")       # Verifica se inizia con "+39"
"+39" in numero                # Verifica se contiene "+39" (può essere ovunque!)

# Lunghezza stringa
len(numero) >= 10              # Corretto
numero.count(numero) == 10     # SBAGLIATO - logica assurda!
```

Valutazione generale:
Hai dimostrato una comprensione base dei concetti semplici (len, upper, lower, count, in) e la logica fondamentale è spesso corretta. I principali problemi sono: 1) Errori di formato negli output (es03, es06, es09) - sai usare le funzioni ma non leggi attentamente il formato richiesto, 2) Es15 usa `in` invece di `==` (errore concettuale grave), 3) Es18 ha logica completamente assurda, 4) Es19 e es20 non svolti (10% della verifica). Quando la logica è corretta ma l'output è impreciso, hai ricevuto 2/5 per incoraggiare il tuo sforzo. Concentrati sulla lettura attenta delle specifiche richieste e sulla comprensione delle differenze tra operatori (`in` vs `==`, `.count()` vs `len()`). Correggendo tutti gli errori e completando gli esercizi mancanti puoi raggiungere 85-90/100.
