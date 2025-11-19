# Correzione Verifica Stringhe Base A - DiCrescenzo Lorenzo

Punteggio Totale: 67/100

---

## Esercizio 1
Punteggio: 4/5

Obiettivo: Concatenare nome e cognome con uno spazio

Analisi del codice:
Hai completato l'esercizio con la logica corretta. La concatenazione è perfetta.

Errore riscontrato:
```python
# Righe 6, 9
nome = "mario"
cognome = "rossi"
```

Problema: Hai scritto "mario" e "rossi" con lettere minuscole invece di "Mario" e "Rossi" con lettere maiuscole.

Output prodotto: `mario rossi`
Output atteso: `Mario Rossi`

Cosa dovevi scrivere:
```python
nome = "Mario"
cognome = "Rossi"
```

Valutazione: La logica del codice è perfetta. Questo è solo un errore di digitazione nelle stringhe iniziali.

---

## Esercizio 2
Punteggio: 3/5

Obiettivo: Concatenare città e nazione con input utente

Analisi del codice:
Hai usato f-string per formattare l'output, ma ci sono diversi errori di formato.

Errore riscontrato:
```python
# Riga 12
luogo = f"vivo a {citta},{nazione}"
```

Problemi:
1. "vivo" dovrebbe iniziare con la V maiuscola: "Vivo"
2. Manca lo spazio dopo la virgola: `{citta},{nazione}` dovrebbe essere `{citta}, {nazione}`

Output prodotto: `vivo a Roma,Italia`
Output atteso: `Vivo a Roma, Italia`

Cosa dovevi scrivere:
```python
luogo = f"Vivo a {citta}, {nazione}"
```

Oppure con concatenazione:
```python
luogo = "Vivo a " + citta + ", " + nazione
```

Valutazione: Errore di formato. Maiuscola sbagliata e spazio mancante.

---

## Esercizio 3
Punteggio: 0/5

Obiettivo: Riepilogo concatenazione - scheda libro

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori gravi multipli.

Errori riscontrati:

1. **Riga 9 - Prompt sbagliato:**
   ```python
   anno_publicazione = input("inserisci il nome di un libro: " )
   ```
   Il prompt dovrebbe chiedere l'anno, non "il nome di un libro".

2. **Riga 10 - Concatenazione completamente errata:**
   ```python
   scheda = libro + autore + anno_publicazione
   ```
   Mancano completamente "Titolo: ", "Autore: ", "Anno: " e le virgole di separazione.

Output prodotto: `Il Signore degli AnelliTolkien1954` (tutto attaccato)
Output atteso: `Titolo: Il Signore degli Anelli, Autore: Tolkien, Anno: 1954`

Cosa dovevi scrivere:
```python
libro = input("Inserisci il titolo: ")
autore = input("Inserisci l'autore: ")
anno_publicazione = input("Inserisci l'anno: ")
scheda = "Titolo: " + libro + ", Autore: " + autore + ", Anno: " + anno_publicazione
print(scheda)
```

Valutazione: Errore logico grave. L'output non ha nessuna somiglianza con quello richiesto.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Aggiungere parti a un messaggio usando l'operatore +=

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente l'operatore += per aggiungere progressivamente parti al messaggio.

---

## Esercizio 5
Punteggio: 5/5

Obiettivo: Costruire un indirizzo email usando +=

Analisi del codice:
Esercizio completato perfettamente. Hai costruito correttamente l'indirizzo email usando l'operatore +=.

---

## Esercizio 6
Punteggio: 5/5

Obiettivo: Riepilogo operatore += - costruire una frase

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente l'operatore += per costruire la frase nel formato richiesto.

---

## Esercizio 7
Punteggio: 4/5

Obiettivo: Calcolare e stampare la lunghezza di una stringa

Analisi del codice:
Hai usato correttamente la funzione `len()` e stampato il risultato nel formato richiesto.

Errore riscontrato:
```python
# Riga 6
parola = "programmazione"
```

Problema: La traccia richiede `"Programmazione"` con la P maiuscola, ma tu hai scritto tutto minuscolo.

Conseguenza: Il risultato della lunghezza è comunque corretto (14 caratteri), ma la parola iniziale è sbagliata.

Valutazione: Errore minore nella stringa iniziale, ma la logica è perfetta.

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
# Righe 11-12
print(f"Nome: {nome} lunghezza: {lunghezza_n}")
print(f"cognome: {cognome} lunghezza: {lunghezza_co}")
```

Problemi:
1. Manca la virgola dopo `{nome}` e dopo `{cognome}`
2. "cognome:" ha la 'c' minuscola invece della 'C' maiuscola
3. "lunghezza:" ha la 'l' minuscola invece della 'L' maiuscola

Output prodotto:
```
Nome: Marco lunghezza: 5
cognome: Bianchi lunghezza: 7
```

Output atteso:
```
Nome: Marco, Lunghezza: 5
Cognome: Bianchi, Lunghezza: 7
```

Cosa dovevi scrivere:
```python
print(f"Nome: {nome}, Lunghezza: {lunghezza_n}")
print(f"Cognome: {cognome}, Lunghezza: {lunghezza_co}")
```

Valutazione: Errore di formato. Mancano virgole e le maiuscole sono sbagliate.

---

## Esercizio 10
Punteggio: 5/5

Obiettivo: Convertire un nome in maiuscolo

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente il metodo `.upper()` per convertire il nome in maiuscolo.

---

## Esercizio 11
Punteggio: 5/5

Obiettivo: Convertire una parola in minuscolo con input utente

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente il metodo `.lower()` per convertire la parola in minuscolo.

---

## Esercizio 12
Punteggio: 0/5

Obiettivo: Riepilogo .upper() e .lower() - convertire nome e cognome

Analisi del codice:
Hai convertito correttamente nome e cognome usando `.upper()` e `.lower()`, ma l'output è completamente sbagliato.

Errore riscontrato:
```python
# Righe 11-12
print(f"nome: {nome_maiuscolo} ")
print(f"nome: {cognome_minuscolo} ")
```

Problemi:
1. "nome:" ha la 'n' minuscola invece della 'N' maiuscola
2. Nella seconda riga hai scritto "nome:" invece di "Cognome:"
3. Manca i due punti dopo le label

Output prodotto:
```
nome: MARIO
nome: rossi
```

Output atteso:
```
Nome: MARIO
Cognome: rossi
```

Cosa dovevi scrivere:
```python
print(f"Nome: {nome_maiuscolo}")
print(f"Cognome: {cognome_minuscolo}")
```

Valutazione: Errore logico grave. Hai stampato "nome:" per entrambe le righe invece di "Nome:" e "Cognome:".

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
Hai tentato l'esercizio ma c'è un errore logico GRAVE.

Errore riscontrato:
```python
# Righe 6-8
codice = input("inserisci codice: ")
codice.strip()
if codice == "ABC123":
```

Problema: Hai chiamato `codice.strip()` alla riga 7, ma NON hai salvato il risultato in nessuna variabile. Lo `.strip()` viene eseguito ma il risultato viene perso. Poi alla riga 8 confronti `codice` (la variabile ORIGINALE con gli spazi) invece del codice pulito.

Conseguenza: Se l'utente inserisce "   ABC123   " (con spazi), il programma stampa "Codice errato" perché confronta `"   ABC123   "` con `"ABC123"`.

Cosa dovevi scrivere:
```python
codice = input("Inserisci il codice: ")
codice_pulito = codice.strip()
if codice_pulito == "ABC123":
    print("Codice corretto")
else:
    print("Codice errato")
```

Oppure:
```python
codice = input("Inserisci il codice: ")
codice = codice.strip()  # Salva il risultato nella stessa variabile
if codice == "ABC123":
    print("Codice corretto")
else:
    print("Codice errato")
```

Valutazione: Errore logico grave. Non hai capito che `.strip()` ritorna una NUOVA stringa e devi salvarla.

---

## Esercizio 16
Punteggio: 5/5

Obiettivo: Verificare un username ignorando spazi e maiuscole/minuscole

Analisi del codice:
Esercizio completato perfettamente. Hai correttamente applicato sia `.strip()` che `.lower()` e salvato i risultati in `username_pulito`, poi hai usato la variabile corretta nel confronto.

---

## Esercizio 17
Punteggio: 5/5

Obiettivo: Verificare se "python" è contenuto in una frase

Analisi del codice:
Esercizio completato perfettamente. Hai convertito la frase in minuscolo e usato correttamente l'operatore `in` per verificare la presenza di "python".

---

## Esercizio 18
Punteggio: 3/5

Obiettivo: Contare quante volte appare la lettera 'a' in una frase

Analisi del codice:
Hai completato correttamente la conversione in minuscolo e il conteggio con `.count()`, ma ci sono due problemi.

Errori riscontrati:

1. **Riga 11 - Formato output diverso:**
   ```python
   print("La lettera a compare", numero_a,"volte")
   ```
   Hai scritto "a compare" invece di "'a' appare", e manca il formato con le virgolette attorno alla 'a'.

2. **Manca completamente il controllo if/else:**
   La traccia richiede: "Se appare più di 3 volte stampa 'Ci sono molte a!', altrimenti 'Ci sono poche a'".

   Non hai implementato questa parte.

Output prodotto: `La lettera a compare 6 volte`
Output atteso:
```
La lettera 'a' appare 6 volte
Ci sono molte 'a'!
```

Cosa dovevi scrivere:
```python
frase = input("Inserisci una frase: ")
frase_minuscola = frase.lower()
numero_a = frase_minuscola.count("a")
print(f"La lettera 'a' appare {numero_a} volte")

if numero_a > 3:
    print("Ci sono molte 'a'!")
else:
    print("Ci sono poche 'a'")
```

Valutazione: Errore di formato e manca metà dell'esercizio (il controllo if/else).

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Verificare validità di un URL

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori gravi multipli.

Errore riscontrato:
```python
# Riga 10
if url_minuscolo.startswith("http//") or ("https//") and url_minuscolo.endswith(".com") or (".it"):
```

Problemi:

1. **Mancano i due punti ":" dopo http e https:**
   Hai scritto `"http//"` e `"https//"`, ma dovrebbe essere `"http://"` e `"https://"` (con i due punti).

2. **Sintassi OR completamente errata:**
   Stesso errore già visto in altri esercizi: `or ("https//")` è sempre `True` (stringa non vuota), e `or (".it")` è sempre `True`.

Come Python interpreta il tuo codice:
- `("https//")` è sempre `True`
- `(".it")` è sempre `True`
- La condizione diventa praticamente sempre vera

Cosa dovevi scrivere:
```python
url = input("Inserisci un URL: ")
url_minuscolo = url.lower()

if (url_minuscolo.startswith("http://") or url_minuscolo.startswith("https://")) and (url_minuscolo.endswith(".com") or url_minuscolo.endswith(".it")):
    print("URL valido")
else:
    print("URL non valido")
```

Valutazione: Errore logico grave. Sintassi OR errata + mancano i ":" negli URL.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Validazione completa di un indirizzo email

Analisi del codice:
**Esercizio NON svolto.** Il file contiene solo i commenti della traccia, nessun codice.

Il codice deve essere scritto completamente:
```python
email = input("Inserisci un indirizzo email: ")

# Pulisci l'email
email = email.strip()
email = email.lower()

# Verifica condizioni
lunghezza = len(email)

if "@" in email and lunghezza >= 5 and (email.endswith(".com") or email.endswith(".it")):
    print("Email valida")
else:
    print("Email non valida")
```

Valutazione: Esercizio non consegnato.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione della concatenazione e operatore += (es04, 05, 06)
- Corretta applicazione di `len()` (es08, es13, es14)
- Ottimo uso di `.upper()` e `.lower()` (es10, es11)
- Comprensione della logica condizionale (es13, es14)
- Perfetta applicazione di `.strip()` e `.lower()` combinati (es16)
- Corretto uso dell'operatore `in` (es17)

Aree di miglioramento:

**Errori di battitura:**
   - Es01: "mario" e "rossi" invece di "Mario" e "Rossi"
   - Es07: "programmazione" invece di "Programmazione"

**Errori di formato:**
   - Es02: "vivo" minuscolo, spazio mancante dopo virgola
   - Es09: Mancano virgole, maiuscole sbagliate
   - Es18: Formato output diverso, manca if/else

**Errori logici:**
   - Es03: Concatenazione completamente sbagliata, output totalmente diverso
   - Es12: Stampato "nome:" per entrambe le righe invece di "Nome:" e "Cognome:"
   - Es15: `.strip()` non salvato, risultato perso
   - Es19: Mancano ":" negli URL, sintassi OR errata
   - Es20: Non svolto

**PROBLEMA CHIAVE - es15**: Devi capire che i metodi come `.strip()`, `.lower()`, `.upper()` NON modificano la stringa originale, ma RITORNANO una nuova stringa. Devi salvare il risultato:
```python
# SBAGLIATO - il risultato viene perso
codice.strip()

# CORRETTO - salva il risultato
codice_pulito = codice.strip()
# oppure
codice = codice.strip()
```

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 3:** Usa il formato "Titolo: ..., Autore: ..., Anno: ..."
- **Esercizio 12:** La seconda riga deve stampare "Cognome:", non "nome:"
- **Esercizio 15:** Salva il risultato di `.strip()` prima di usarlo
- **Esercizio 18:** Aggiungi il controllo if/else per stampare "Ci sono molte 'a'!" o "Ci sono poche 'a'"
- **Esercizio 19:** Aggiungi ":" dopo http e https, e correggi la sintassi OR
- **Esercizio 20:** Completa l'esercizio

Pattern da studiare (sintassi OR corretta):
```python
# SBAGLIATO
if testo.startswith("a") or ("b"):  # ("b") è sempre True!

# CORRETTO
if testo.startswith("a") or testo.startswith("b"):
```

Valutazione generale:
Hai dimostrato una buona comprensione dei concetti base (concatenazione, +=, len, upper, lower, strip). Gli esercizi più semplici sono stati completati correttamente. I problemi principali sono: 1) Non capire che i metodi delle stringhe ritornano nuove stringhe (es15), 2) Errori di formato ricorrenti (maiuscole, virgole, spazi), 3) Sintassi OR errata nell'es19, 4) Es20 non svolto. Correggendo questi errori puoi raggiungere 92/100.
