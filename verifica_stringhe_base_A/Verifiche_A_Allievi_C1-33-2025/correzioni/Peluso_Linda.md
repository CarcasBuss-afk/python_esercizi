# Correzione Verifica Stringhe Base A - Peluso Linda

Punteggio Totale: 71/100

---

## Esercizio 1
Punteggio: 4/5

Obiettivo: Concatenare nome e cognome con uno spazio

Analisi del codice:
Hai completato l'esercizio con la logica corretta. La concatenazione è perfetta.

Errore riscontrato:
```python
# Righe 6, 9
nome = "Linda"
cognome = "Peluso"
```

Problema: Hai scritto "Linda" e "Peluso" invece di "Mario" e "Rossi" come richiesto dalla traccia.

Output prodotto: `Linda Peluso`
Output atteso: `Mario Rossi`

Cosa dovevi scrivere:
```python
nome = "Mario"
cognome = "Rossi"
```

Valutazione: La logica del codice è perfetta. Questo è solo un errore nelle stringhe iniziali (hai usato il tuo nome invece dei valori richiesti).

---

## Esercizio 2
Punteggio: 5/5

Obiettivo: Concatenare città e nazione con input utente

Analisi del codice:
Esercizio completato perfettamente. Hai creato correttamente la variabile 'luogo' concatenando "Vivo a " + città + ", " + nazione e l'hai stampata.

---

## Esercizio 3
Punteggio: 4/5

Obiettivo: Riepilogo concatenazione - scheda libro

Analisi del codice:
Hai completato l'esercizio con la logica corretta, ma c'è uno spazio extra nell'output.

Errore riscontrato:
```python
# Riga 11
informazioni = "Titolo: " + titolo + ", " + "Autore:  " + autore + ", " + "Anno: " + anno
```

Problema: Hai scritto `"Autore:  "` con due spazi dopo i due punti invece di uno solo.

Output prodotto: `Titolo: Il Signore degli Anelli, Autore:  Tolkien, Anno: 1954` (doppio spazio dopo "Autore:")

Output atteso: `Titolo: Il Signore degli Anelli, Autore: Tolkien, Anno: 1954`

Cosa dovevi scrivere:
```python
informazioni = "Titolo: " + titolo + ", Autore: " + autore + ", Anno: " + anno
```

Valutazione: Errore minore. Uno spazio extra in una stringa.

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
Hai usato correttamente l'operatore +=, ma c'è uno spazio extra all'inizio.

Errore riscontrato:
```python
# Riga 6
email = " mario"
```

Problema: Hai scritto `" mario"` con uno spazio all'inizio invece di `"mario"`.

Output prodotto: ` mario@esempio.com` (con spazio all'inizio)
Output atteso: `mario@esempio.com`

Cosa dovevi scrivere:
```python
email = "mario"
```

Valutazione: Errore minore. Uno spazio extra all'inizio della stringa.

---

## Esercizio 6
Punteggio: 4/5

Obiettivo: Riepilogo operatore += - costruire una frase

Analisi del codice:
Hai usato correttamente l'operatore +=, ma hai aggiunto spazi extra in posizioni sbagliate.

Errore riscontrato:
```python
# Righe 10-13
frase = "Python "
frase += "è "
frase += "un linguaggio "
frase += "fantastico "
```

Problema: Hai aggiunto gli spazi DOPO ogni parola invece che PRIMA. Questo crea uno spazio finale extra.

Output prodotto: `Python è un linguaggio fantastico ` (con spazio finale)
Output atteso: `Python è un linguaggio fantastico`

Cosa dovevi scrivere:
```python
frase = "Python"
frase += " è"
frase += " un linguaggio"
frase += " fantastico"
```

Valutazione: Errore minore. Spazi posizionati in modo sbagliato creano uno spazio finale extra.

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
Hai completato i calcoli correttamente con `len()`, ma il formato dell'output ha spazi extra.

Errore riscontrato:
```python
# Righe 14-15
print("Nome: ", nome, ", ",  "Lunghezza: ", lunghezza_nome)
print("Cognome:", cognome, ", ", "Lunghezza: ", lunghezza_cognome)
```

Problema: Hai separato gli elementi con troppe virgole, creando spazi extra nell'output.

Output prodotto:
```
Nome:  Marco ,  Lunghezza:  5
Cognome: Bianchi ,  Lunghezza:  7
```

Output atteso:
```
Nome: Marco, Lunghezza: 5
Cognome: Bianchi, Lunghezza: 7
```

Cosa dovevi scrivere:
```python
print(f"Nome: {nome}, Lunghezza: {lunghezza_nome}")
print(f"Cognome: {cognome}, Lunghezza: {lunghezza_cognome}")
```

Valutazione: Errore di formato. Gli spazi extra rendono l'output diverso da quello richiesto.

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
Punteggio: 3/5

Obiettivo: Riepilogo .upper() e .lower() - convertire nome e cognome

Analisi del codice:
Hai convertito correttamente nome e cognome usando `.upper()` e `.lower()`, ma il formato dell'output ha spazi extra.

Errore riscontrato:
```python
# Righe 14-15
print("Nome: ", nome_maiuscolo)
print("Cognome: ", cognome_minuscolo)
```

Problema: Hai messo uno spazio dopo i due punti e poi un altro spazio per la virgola del print, creando spazi doppi.

Output prodotto:
```
Nome:  MARIO
Cognome:  rossi
```

Output atteso:
```
Nome: MARIO
Cognome: rossi
```

Cosa dovevi scrivere:
```python
print("Nome:", nome_maiuscolo)
print("Cognome:", cognome_minuscolo)
```

Oppure:
```python
print(f"Nome: {nome_maiuscolo}")
print(f"Cognome: {cognome_minuscolo}")
```

Valutazione: Errore di formato. Spazi doppi nell'output.

---

## Esercizio 13
Punteggio: 5/5

Obiettivo: Confrontare la lunghezza di due parole

Analisi del codice:
Esercizio completato perfettamente. Hai calcolato le lunghezze, confrontato i valori e stampato il messaggio corretto basandoti sulla condizione.

---

## Esercizio 14
Punteggio: 0/5

Obiettivo: Verificare se una password ha una lunghezza valida (8-16 caratteri)

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore di sintassi GRAVE che rende il codice non eseguibile.

Errore riscontrato:
```python
# Righe 12-17
if lunghezza_password < 8:
    print("Password troppo corta")
elif lunghezza_password > 16:
    print("Password troppo lunga")
elif lunghezza_password  :
     print("Password valida")
```

Problema: La riga 16 ha `elif lunghezza_password :` senza una condizione completa. Questo è un **errore di sintassi**. Python darà un errore e il programma non può essere eseguito.

Cosa dovevi scrivere:
```python
if lunghezza_password < 8:
    print("Password troppo corta")
elif lunghezza_password > 16:
    print("Password troppo lunga")
else:
    print("Password valida")
```

Spiegazione: Dopo aver verificato "troppo corta" e "troppo lunga", l'unico caso rimanente è "valida". Non serve un'altra condizione, basta `else:`.

Valutazione: Errore logico grave. Il codice ha un errore di sintassi e non può essere eseguito.

---

## Esercizio 15
Punteggio: 5/5

Obiettivo: Verificare un codice dopo aver rimosso gli spazi

Analisi del codice:
Esercizio completato perfettamente. Hai correttamente usato `.strip()` per rimuovere gli spazi, salvato il risultato in `codice_pulito`, e poi confrontato la variabile pulita con "ABC123".

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
Punteggio: 0/5

Obiettivo: Contare quante volte appare la lettera 'a' in una frase

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori multipli.

Errori riscontrati:

1. **Riga 11 - Variabile sbagliata:**
   ```python
   numero = frase.count("a")
   ```
   Hai usato `frase` invece di `frase_minuscola`. Se la frase contiene 'A' maiuscola, non viene contata.

2. **Riga 12 - Formato output diverso:**
   ```python
   print(f"La lettera A compare {numero} volte")
   ```
   Hai scritto "A compare" invece di "'a' appare". Mancano le virgolette attorno alla 'a' e il verbo è sbagliato.

3. **Manca completamente il controllo if/else:**
   La traccia richiede: "Se appare più di 3 volte stampa 'Ci sono molte a!', altrimenti 'Ci sono poche a'".

   Non hai implementato questa parte.

Output prodotto: `La lettera A compare 6 volte`

Output atteso:
```
La lettera 'a' appare 6 volte
Ci sono molte 'a'!
```

Cosa dovevi scrivere:
```python
frase = input("Inserisci una frase: ")
frase_minuscola = frase.lower()
numero = frase_minuscola.count("a")
print(f"La lettera 'a' appare {numero} volte")

if numero > 3:
    print("Ci sono molte 'a'!")
else:
    print("Ci sono poche 'a'")
```

Valutazione: Errori logici gravi. Variabile sbagliata + formato errato + manca metà dell'esercizio.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Verificare validità di un URL

Analisi del codice:
**Esercizio NON svolto.** Il file contiene solo i commenti della traccia, nessun codice.

Il codice deve essere scritto completamente:
```python
url = input("Inserisci un URL: ")
url_minuscolo = url.lower()

if (url_minuscolo.startswith("http://") or url_minuscolo.startswith("https://")) and (url_minuscolo.endswith(".com") or url_minuscolo.endswith(".it")):
    print("URL valido")
else:
    print("URL non valido")
```

Valutazione: Esercizio non consegnato.

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
- Ottima comprensione della concatenazione di stringhe (es02)
- Buon uso dell'operatore += (es04)
- Corretta applicazione di `len()` (es07, es08, es13)
- Ottimo uso di `.upper()` e `.lower()` (es10, es11)
- Comprensione della logica condizionale (es13)
- Perfetta applicazione di `.strip()` e `.lower()` combinati (es15, es16)
- Corretto uso dell'operatore `in` (es17)

Aree di miglioramento:

**Errori minori:**
   - Es01: Usato il tuo nome invece dei valori richiesti
   - Es03: Doppio spazio dopo "Autore:"
   - Es05: Spazio extra all'inizio di "mario"
   - Es06: Spazi posizionati alla fine invece che all'inizio

**Errori di formato:**
   - Es09: Spazi extra causati da troppi separatori nel print
   - Es12: Spazi doppi dopo "Nome:" e "Cognome:"

**Errori logici:**
   - Es14: Errore di sintassi (`elif lunghezza_password :` senza condizione)
   - Es18: Variabile sbagliata (`frase` invece di `frase_minuscola`) + formato diverso + manca if/else
   - Es19: Non svolto
   - Es20: Non svolto

**PROBLEMA CRITICO - es14**: Hai scritto `elif lunghezza_password :` senza una condizione. Questo è un **errore di sintassi** che impedisce l'esecuzione del programma. Quando hai già controllato tutti i casi specifici (< 8 e > 16), usa semplicemente `else:` per il caso rimanente.

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 14:** Cambia `elif lunghezza_password :` in `else:`
- **Esercizio 18:** Usa `frase_minuscola.count("a")`, correggi il formato, aggiungi if/else
- **Esercizio 19:** Completa l'esercizio
- **Esercizio 20:** Completa l'esercizio

Consigli per migliorare:
1. **Spazi nei print**: Usa f-string per evitare spazi doppi: `print(f"Nome: {valore}")` invece di `print("Nome: ", valore)`
2. **Spazi nelle concatenazioni**: Metti gli spazi PRIMA delle parole, non DOPO: `frase += " è"` non `frase += "è "`
3. **Sintassi if/elif/else**: Se hai controllato tutti i casi specifici, usa `else:` per il caso rimanente, non `elif variabile :` senza condizione
4. **Completare gli esercizi**: Non lasciare esercizi vuoti

Valutazione generale:
Hai dimostrato una buona comprensione dei concetti base (concatenazione, +=, len, upper, lower, strip). Gli esercizi intermedi sono stati completati correttamente. I problemi principali sono: 1) Errore di sintassi grave nell'es14, 2) Errori multipli nell'es18 (variabile sbagliata + manca if/else), 3) Es19 e es20 non svolti (10% della verifica). Correggendo questi errori e completando gli esercizi mancanti puoi raggiungere 96/100.
