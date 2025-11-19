# Correzione Verifica Stringhe Base B - Pellone Luca

Punteggio Totale: 61/100

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
Punteggio: 3/5

Obiettivo: Riepilogo len() - calcolare lunghezza di prodotto e descrizione

Analisi del codice:
Hai completato i calcoli correttamente con `len()`, ma l'output non corrisponde al formato richiesto.

Errore riscontrato:
```python
# Righe 21-22
print(f"Prodotto: {prodotto}, lunghezza: {lunghezza}")
print(f"Descrizione: {descrizione}, lunghezza: {lunghezza2}")
```

Problema: Hai scritto "lunghezza:" con la 'l' minuscola invece di "Lunghezza:" con la 'L' maiuscola.

Output prodotto:
```
Prodotto: Notebook, lunghezza: 8
Descrizione: Computer portatile, lunghezza: 18
```

Output atteso:
```
Prodotto: Notebook, Lunghezza: 8
Descrizione: Computer portatile, Lunghezza: 18
```

Cosa dovevi scrivere:
```python
print(f"Prodotto: {prodotto}, Lunghezza: {lunghezza}")
print(f"Descrizione: {descrizione}, Lunghezza: {lunghezza2}")
```

Valutazione: Errore di formato. La maiuscola sbagliata cambia il formato dell'output.

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
Punteggio: 0/5

Obiettivo: Riepilogo .upper() e .lower() - convertire hashtag e username

Analisi del codice:
Hai convertito correttamente hashtag e username usando `.upper()` e `.lower()`, ma ci sono errori multipli.

Errori riscontrati:

1. **Righe 15, 17 - Errore di battitura:**
   ```python
   hastag = input("Inserisci un hastag: ")
   hastag_maiuscolo = hastag.upper()
   ```
   Hai scritto "hastag" invece di "hashtag" (manca la 'h'). Questo è ripetuto in più righe.

2. **Righe 19-20 - Manca il formato richiesto:**
   ```python
   print(hastag_maiuscolo)
   print(username_minuscolo)
   ```

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

Mancano completamente le etichette "Hashtag:" e "Username:" nell'output.

Cosa dovevi scrivere:
```python
hashtag = input("Inserisci un hashtag: ")
username = input("Inserisci uno username: ")
hashtag_maiuscolo = hashtag.upper()
username_minuscolo = username.lower()
print(f"Hashtag: {hashtag_maiuscolo}")
print(f"Username: {username_minuscolo}")
```

Valutazione: Errore logico grave. Typo ripetuto + mancano completamente le etichette nell'output.

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
Punteggio: 3/5

Obiettivo: Riepilogo concatenazione - creare carta d'identità

Analisi del codice:
Hai completato l'esercizio con la logica corretta, ma ci sono due errori di formato.

Errori riscontrati:

1. **Riga 19 - Spazio extra all'inizio:**
   ```python
   cartaid = (f" Nome: {nome}, Cognome: {cognome}, CF {codfisc}")
   ```
   Hai uno spazio prima di "Nome:" nella f-string.

2. **Riga 19 - Mancano i due punti dopo "CF":**
   Hai scritto `CF {codfisc}` invece di `CF: {codfisc}`.

Output prodotto: ` Nome: Luigi, Cognome: Verdi, CF VRDLGU80A01H501Z` (con spazio iniziale e mancano i ":" dopo CF)

Output atteso: `Nome: Luigi, Cognome: Verdi, CF: VRDLGU80A01H501Z`

Cosa dovevi scrivere:
```python
cartaid = f"Nome: {nome}, Cognome: {cognome}, CF: {codfisc}"
print(cartaid)
```

Valutazione: Errore di formato. Spazio extra + mancano i due punti.

---

## Esercizio 10
Punteggio: 4/5

Obiettivo: Costruire un numero di telefono usando +=

Analisi del codice:
Hai usato correttamente l'operatore +=, ma c'è un errore nel formato.

Errore riscontrato:
```python
# Riga 12
telefono += "1234567"
```

Problema: Manca lo spazio prima di "1234567". La traccia richiede `" 02"` e poi `" 1234567"` (con spazio), ma tu hai scritto `"1234567"` senza spazio.

Output prodotto: `+39 021234567`
Output atteso: `+39 02 1234567`

Cosa dovevi scrivere:
```python
telefono += " 1234567"
```

Valutazione: Errore minore. Manca uno spazio.

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
Punteggio: 0/5

Obiettivo: Verificare se "online" è contenuto nella modalità del corso

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore logico GRAVISSIMO.

Errore riscontrato:
```python
# Riga 12
if "online" > modalita  :
    print("Il corso è online!")
```

Problema: Hai usato l'operatore `>` (maggiore di) invece di `in`. Stai confrontando se la stringa "online" è "maggiore" della modalità inserita, che è completamente sbagliato!

L'operatore `in` serve per verificare se una stringa è **contenuta** in un'altra.

Conseguenza: Il programma non funziona correttamente. Il confronto `"online" > modalita` usa l'ordinamento lessicografico delle stringhe, non verifica la presenza.

Cosa dovevi scrivere:
```python
if "online" in modalita_minuscola:
    print("Il corso è online!")
else:
    print("Il corso non è online")
```

Nota: Hai anche creato `modalita_minuscola` ma non l'hai usata! Devi usare la variabile convertita in minuscolo.

Valutazione: Errore logico gravissimo. Usi `>` invece di `in`, e non usi la variabile convertita.

---

## Esercizio 14
Punteggio: 0/5

Obiettivo: Verificare se una parola chiave è nella descrizione del prodotto

Analisi del codice:
Hai tentato l'esercizio ma c'è lo stesso errore grave dell'esercizio 13.

Errore riscontrato:
```python
# Riga 16
if parola_minuscola > descrizione_minuscola:
    print("Parola chiave trovata!")
```

Problema: Hai usato l'operatore `>` (maggiore di) invece di `in`. Questo è lo stesso identico errore dell'esercizio precedente!

Cosa dovevi scrivere:
```python
if parola_minuscola in descrizione_minuscola:
    print("Parola chiave trovata!")
else:
    print("Parola chiave non trovata")
```

Valutazione: Errore logico gravissimo. Usi `>` invece di `in`.

---

## Esercizio 15
Punteggio: 0/5

Obiettivo: Verificare un codice coupon dopo aver rimosso gli spazi

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore logico GRAVE.

Errore riscontrato:
```python
# Righe 17-19
codice = input("Inserisci un codice coupon: ")
codice.strip()
if codice == "SCONTO20":
```

Problema: Hai chiamato `codice.strip()` alla riga 18, ma NON hai salvato il risultato in nessuna variabile. Lo `.strip()` viene eseguito ma il risultato viene perso. Poi alla riga 19 confronti `codice` (la variabile ORIGINALE con gli spazi) invece del codice pulito.

Conseguenza: Se l'utente inserisce "   SCONTO20   " (con spazi), il programma stampa "Coupon non valido" perché confronta `"   SCONTO20   "` con `"SCONTO20"`.

Cosa dovevi scrivere:
```python
codice = input("Inserisci un codice coupon: ")
codice_pulito = codice.strip()

if codice_pulito == "SCONTO20":
    print("Coupon valido")
else:
    print("Coupon non valido")
```

Oppure:
```python
codice = input("Inserisci un codice coupon: ")
codice = codice.strip()  # Salva il risultato nella stessa variabile

if codice == "SCONTO20":
    print("Coupon valido")
else:
    print("Coupon non valido")
```

Valutazione: Errore logico grave. Non hai capito che `.strip()` ritorna una NUOVA stringa e devi salvarla.

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
**Esercizio NON svolto.** Il file contiene solo i commenti della traccia, nessun codice.

Il codice deve essere scritto completamente:
```python
telefono = input("Inserisci un numero di telefono: ")

lunghezza = len(telefono)
inizia_corretto = telefono.startswith("+39")

if lunghezza >= 10 and inizia_corretto:
    print("Numero valido")
else:
    print("Numero non valido")
```

Valutazione: Esercizio non consegnato.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Validazione completa username

Analisi del codice:
**Esercizio NON svolto.** Il file contiene solo i commenti della traccia, nessun codice.

Il codice deve essere scritto completamente. Questo esercizio è complesso e richiede:
1. Pulizia dello username con `.strip()` e `.lower()`
2. Verifica che non contenga spazi
3. Verifica lunghezza tra 5 e 15 caratteri
4. Verifica che contenga almeno un numero

Valutazione: Esercizio non consegnato.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Validazione completa codice prodotto

Analisi del codice:
**Esercizio NON svolto.** Il file contiene solo i commenti della traccia, nessun codice.

Il codice deve essere scritto completamente. Questo esercizio richiede:
1. Pulizia del codice con `.strip()` e `.upper()`
2. Verifica lunghezza esatta di 7 caratteri
3. Verifica che contenga il simbolo '-'
4. Verifica che inizi con "ABC"

Valutazione: Esercizio non consegnato.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione di `len()` (es01, es02)
- Buon uso di `.upper()` e `.lower()` (es04, es05)
- Corretta applicazione della concatenazione (es07, es08)
- Ottimo uso dell'operatore += (es11, es12)
- Corretto uso di `.count()` (es16, es17)

Aree di miglioramento:

**Errori minori:**
   - Es03: "lunghezza:" minuscola invece di "Lunghezza:"
   - Es10: Manca uno spazio prima di "1234567"

**Errori di formato:**
   - Es09: Spazio extra all'inizio + mancano ":" dopo "CF"

**Errori logici:**
   - Es06: Typo "hastag" invece di "hashtag" + mancano etichette nell'output
   - Es13: Usa `>` invece di `in` per verificare la presenza di una stringa
   - Es14: Usa `>` invece di `in` per verificare la presenza di una stringa
   - Es15: `.strip()` non salvato, risultato perso
   - Es18: Non svolto
   - Es19: Non svolto
   - Es20: Non svolto

**PROBLEMA CRITICO - es13 e es14**: Hai usato l'operatore `>` (maggiore di) invece di `in` per verificare se una stringa è contenuta in un'altra. Questo è un errore concettuale grave:

```python
# SBAGLIATO
if "online" > modalita:  # Questo confronta le stringhe lessicograficamente!

# CORRETTO
if "online" in modalita:  # Questo verifica se "online" è contenuto in modalita
```

L'operatore `in` serve per verificare la **presenza** di una sottostringa, non `>`.

**PROBLEMA CRITICO - es15**: Stesso errore visto in altri studenti - non salvi il risultato di `.strip()`.

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 6:** Correggi "hastag" in "hashtag" e aggiungi le etichette "Hashtag:" e "Username:"
- **Esercizio 13:** Usa `in` invece di `>`, e usa `modalita_minuscola` invece di `modalita`
- **Esercizio 14:** Usa `in` invece di `>`
- **Esercizio 15:** Salva il risultato di `.strip()` prima di usarlo
- **Esercizio 18:** Completa l'esercizio
- **Esercizio 19:** Completa l'esercizio
- **Esercizio 20:** Completa l'esercizio

Pattern da studiare:
```python
# Operatore IN (verifica presenza)
if "python" in frase:  # Verifica se "python" è contenuto in frase
    print("Trovato!")

# Operatore > (confronto lessicografico)
if "zebra" > "ape":  # Confronta l'ordine alfabetico
    print("zebra viene dopo ape")
```

Valutazione generale:
Hai dimostrato una buona comprensione dei concetti base (len, upper, lower, concatenazione, +=, count). Gli esercizi più semplici sono stati completati correttamente. I problemi principali sono: 1) Confusione tra operatore `>` e `in` (es13, es14), 2) Errore concettuale con `.strip()` non salvato (es15), 3) 3 esercizi non svolti (15% della verifica). Correggendo questi errori e completando gli esercizi mancanti puoi raggiungere 86/100.
