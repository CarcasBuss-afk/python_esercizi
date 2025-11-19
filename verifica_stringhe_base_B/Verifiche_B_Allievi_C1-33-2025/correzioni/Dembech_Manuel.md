# Correzione Verifica Stringhe Base B - Dembech Manuel

Punteggio Totale: 89/100

---

## Esercizio 1
Punteggio: 5/5

Obiettivo: Calcolare e stampare la lunghezza del nome di uno sport

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente la funzione `len()` e stampato il risultato nel formato richiesto con f-string.

---

## Esercizio 2
Punteggio: 5/5

Obiettivo: Calcolare lunghezza del nome di un corso inserito dall'utente

Analisi del codice:
Esercizio completato perfettamente. Hai gestito correttamente l'input dell'utente e calcolato la lunghezza con `len()`.

---

## Esercizio 3
Punteggio: 5/5

Obiettivo: Riepilogo len() - calcolare lunghezza di prodotto e descrizione

Analisi del codice:
Esercizio completato perfettamente. Hai calcolato correttamente le lunghezze di entrambe le stringhe e stampato l'output nel formato richiesto.

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
Punteggio: 5/5

Obiettivo: Riepilogo .upper() e .lower() - convertire hashtag e username

Analisi del codice:
Esercizio completato perfettamente. Hai correttamente convertito l'hashtag in maiuscolo e lo username in minuscolo, stampando l'output nel formato richiesto con le etichette appropriate.

---

## Esercizio 7
Punteggio: 5/5

Obiettivo: Concatenare nome prodotto e categoria con uno spazio

Analisi del codice:
Esercizio completato perfettamente. Hai correttamente concatenato le stringhe usando l'operatore + con lo spazio tra prodotto e categoria.

---

## Esercizio 8
Punteggio: 5/5

Obiettivo: Concatenare via, numero civico e città

Analisi del codice:
Esercizio completato perfettamente. Hai creato correttamente la variabile 'indirizzo' concatenando via + " " + numero + ", " + città.

---

## Esercizio 9
Punteggio: 5/5

Obiettivo: Riepilogo concatenazione - creare carta d'identità

Analisi del codice:
Esercizio completato perfettamente. Hai creato correttamente la variabile 'carta_identità' usando un'f-string con il formato richiesto.

---

## Esercizio 10
Punteggio: 5/5

Obiettivo: Costruire un numero di telefono usando +=

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente l'operatore += per costruire il numero di telefono nel formato richiesto.

---

## Esercizio 11
Punteggio: 5/5

Obiettivo: Costruire un URL usando +=

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente l'operatore += per costruire l'URL.

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
Punteggio: 5/5

Obiettivo: Verificare un codice coupon dopo aver rimosso gli spazi

Analisi del codice:
Esercizio completato perfettamente. Hai correttamente usato `.strip()` per rimuovere gli spazi, salvato il risultato in `codice_pulito`, e poi confrontato la variabile pulita con "SCONTO20".

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
Punteggio: 4/5

Obiettivo: Validazione numero di telefono

Analisi del codice:
Hai completato l'esercizio con la logica perfetta, ma c'è un errore di battitura nell'input.

Errore riscontrato:
```python
# Riga 21
numero = input("Insersci un numero di telefono: ")
```

Problema: Hai scritto "Insersci" invece di "Inserisci" (manca la 'i' in mezzo). È solo un errore di digitazione, la logica è completamente corretta.

Output prodotto: `Insersci un numero di telefono:`
Output atteso: `Inserisci un numero di telefono:`

Cosa dovevi scrivere:
```python
numero = input("Inserisci un numero di telefono: ")
```

Valutazione: La logica del codice è perfetta. Questo è solo un errore di digitazione in una stringa.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Validazione completa username

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori GRAVISSIMI multipli che rendono il codice non funzionante.

Errori riscontrati:

1. **Riga 36 - Condizione vuota:**
   ```python
   if (lunghezza_username == lunghezza_username_pulito) and () and (username.isdecimal == True):
   ```
   Hai scritto `and ()` - c'è una condizione completamente vuota tra le parentesi! Questo è un errore di sintassi.

2. **Riga 36 - Metodo senza parentesi:**
   ```python
   username.isdecimal == True
   ```
   `isdecimal` è un **metodo**, non una proprietà. Devi chiamarlo con le parentesi: `username.isdecimal()`.

3. **Riga 36 - Metodo sbagliato per la verifica:**
   Anche se aggiungessi le parentesi, `isdecimal()` è il metodo **completamente sbagliato** per questo esercizio!

   - `isdecimal()` ritorna `True` SOLO se **TUTTI** i caratteri sono numeri (0-9)
   - "Gamer99" ha lettere E numeri, quindi `"Gamer99".isdecimal()` ritorna `False`
   - "123456".isdecimal()` ritorna `True` perché sono tutti numeri

   La traccia richiede di verificare se lo username "**contiene almeno un numero**", non se è composto solo da numeri!

4. **Manca la verifica della lunghezza tra 5 e 15:**
   Non hai implementato il controllo `5 <= lunghezza <= 15`. La condizione vuota `()` probabilmente doveva essere questa verifica.

5. **Variabile sbagliata:**
   Hai creato `username_minuscolo` alla riga 28 ma poi non lo usi. Usi `username` (la variabile originale) invece di quella convertita.

Cosa dovevi scrivere:
```python
username = input("Inserisci uno username: ")

username_pulito = username.strip().lower()

lunghezza_originale = len(username)
lunghezza_pulita = len(username_pulito)

no_spazi = lunghezza_originale == lunghezza_pulita
lunghezza_ok = 5 <= lunghezza_pulita <= 15

# Per verificare "contiene almeno un numero"
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
- `isdecimal()` verifica se **tutti** i caratteri sono numeri
- Per verificare "almeno un numero", devi controllare se almeno una delle cifre 0-9 è contenuta nello username usando `in`
- La lunghezza deve essere verificata con `5 <= lunghezza <= 15`

Valutazione: Errori logici gravissimi. Condizione vuota + metodo senza parentesi + metodo concettualmente sbagliato.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Validazione completa codice prodotto

Analisi del codice:
Hai tentato l'esercizio con una logica quasi corretta, ma c'è un errore GRAVE: non converti il codice in maiuscolo come richiesto dalla traccia.

Errore riscontrato:
```python
# Riga 28
codice_pulito = codice.strip()
```

Problema: La traccia dice esplicitamente "Prima **pulisci il codice rimuovendo gli spazi e convertendo in maiuscolo**." Tu hai solo fatto `.strip()` (rimuove spazi) ma NON hai fatto `.upper()` (converte in maiuscolo).

Conseguenza: Se l'utente inserisce "   abc-123   " (in minuscolo come nell'esempio dell'output atteso), il programma:
1. Rimuove gli spazi → `codice_pulito = "abc-123"` (ancora minuscolo!)
2. Verifica `codice_pulito.startswith("ABC")` → `"abc-123".startswith("ABC")` → **False!**
3. Stampa "Codice non valido" invece di "Codice valido"

Dall'output atteso della traccia:
```
Inserisci un codice prodotto:   abc-123
Codice valido
```

Questo conferma che il codice inserito "abc-123" (minuscolo) dovrebbe essere validato come corretto, ma il tuo programma lo rifiuterebbe.

Cosa dovevi scrivere:
```python
codice = input("Inserisci un codice prodotto: ")

codice_pulito = codice.strip().upper()  # Rimuovi spazi E converti in maiuscolo

lunghezza = len(codice_pulito)

if (lunghezza == 7) and ("-" in codice_pulito) and (codice_pulito.startswith("ABC")):
    print("Codice valido")
else:
    print("Codice non valido")
```

Oppure:
```python
codice = input("Inserisci un codice prodotto: ")
codice_pulito = codice.strip()
codice_pulito = codice_pulito.upper()  # Due righe separate
# resto del codice...
```

Valutazione: Errore logico grave. Manca la conversione in maiuscolo richiesta dalla traccia, rendendo il programma non conforme alle specifiche.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- **Eccellente comprensione dei concetti fondamentali** (es01-es17 perfetti!)
- Ottima padronanza di `len()` (es01, es02, es03)
- Perfetto uso di `.upper()` e `.lower()` (es04, es05, es06)
- Corretta applicazione della concatenazione (es07, es08, es09)
- Ottimo uso dell'operatore += (es10, es11, es12)
- Perfetta comprensione dell'operatore `in` (es13, es14)
- Corretto uso di `.strip()` (es15)
- Ottimo uso di `.count()` (es16, es17)
- Buona comprensione della logica booleana (es18)

Aree di miglioramento:

**Errore di battitura:**
   - Es18: "Insersci" invece di "Inserisci"

**Errori logici gravissimi:**
   - Es19: Condizione vuota `()` + metodo senza parentesi + metodo concettualmente sbagliato
   - Es20: Manca la conversione in maiuscolo richiesta

**PROBLEMA CRITICO - es19**: Hai usato `isdecimal()` che verifica se **TUTTI** i caratteri sono numeri. Ma la traccia chiede di verificare se lo username "**contiene almeno un numero**", che è completamente diverso!

```python
# DIFFERENZA TRA isdecimal() E "contiene almeno un numero"

"123456".isdecimal()  # True - tutti caratteri sono numeri
"Gamer99".isdecimal() # False - ha lettere!

# Ma "Gamer99" CONTIENE numeri (9 e 9)!
# Per verificare "contiene almeno un numero":
"0" in "Gamer99" or "1" in "Gamer99" or ... or "9" in "Gamer99"  # True
```

Inoltre, `isdecimal` è un metodo e deve essere chiamato con parentesi: `username.isdecimal()` non `username.isdecimal`.

**PROBLEMA CRITICO - es20**: Hai dimenticato di convertire in maiuscolo! La traccia dice esplicitamente "convertendo in maiuscolo" ma tu hai fatto solo `.strip()`.

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 19:** Implementa correttamente la verifica "contiene almeno un numero" usando `in`, completa la condizione vuota `()` con la verifica della lunghezza `5 <= lunghezza <= 15`, e rimuovi `isdecimal`
- **Esercizio 20:** Aggiungi `.upper()` dopo `.strip()` per convertire in maiuscolo come richiesto

Pattern da studiare:
```python
# Metodi - SEMPRE con parentesi!
stringa.isdecimal()   # CORRETTO
stringa.isdecimal     # SBAGLIATO - non chiama il metodo!

# Differenza tra "tutti numeri" e "contiene almeno un numero"
"123".isdecimal()     # True - tutti numeri
"abc123".isdecimal()  # False - ha lettere

# Verificare "contiene almeno un numero"
"0" in "abc123" or "1" in "abc123" or ... or "9" in "abc123"  # True

# Pulizia completa con strip E upper
codice = codice.strip().upper()  # Rimuove spazi E maiuscolo
```

Valutazione generale:
Hai dimostrato un'**eccellente comprensione** dei concetti base e intermedi delle stringhe. I primi 17 esercizi sono stati completati perfettamente, il che mostra una solida padronanza di len, upper, lower, concatenazione, +=, in, strip e count. Gli unici problemi sono: 1) Un typo nell'es18 (minimo), 2) Errori concettuali nell'es19 (uso sbagliato di isdecimal), 3) Dimenticato .upper() nell'es20. Correggendo questi ultimi due esercizi puoi facilmente raggiungere 99/100. Ottimo lavoro complessivo!
