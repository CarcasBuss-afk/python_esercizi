# Correzione Verifica Stringhe Base A - Roscio Francesco

Punteggio Totale: 46/100

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
Punteggio: 0/5

Obiettivo: Concatenare città e nazione con input utente

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori gravi che stravolgono completamente l'output richiesto.

Errori riscontrati:

1. **Riga 9 - Errore di battitura:**
   ```python
   nazione = input ("inserisic il nome di una nazione: ")
   ```
   Hai scritto "inserisic" invece di "Inserisci".

2. **Riga 12 - Concatenazione errata:**
   ```python
   luogo = citta + nazione
   ```
   Manca completamente "Vivo a " all'inizio e ", " tra città e nazione.

3. **Riga 14 - Output completamente diverso:**
   ```python
   print(f"vivi a {citta} e ti trovi in {nazione}")
   ```
   Hai creato un output completamente diverso da quello richiesto.

Output prodotto: `vivi a Roma e ti trovi in Italia`
Output atteso: `Vivo a Roma, Italia`

Cosa dovevi scrivere:
```python
citta = input("Inserisci il nome di una città: ")
nazione = input("Inserisci il nome di una nazione: ")
luogo = "Vivo a " + citta + ", " + nazione
print(luogo)
```

Valutazione: Errore logico grave. Hai cambiato completamente il formato richiesto invece di seguire le istruzioni.

---

## Esercizio 3
Punteggio: 0/5

Obiettivo: Riepilogo concatenazione - scheda libro

Analisi del codice:
Hai tentato l'esercizio ma l'output non corrisponde minimamente al formato richiesto.

Errori riscontrati:

1. **Riga 12 - Variabile 'scheda' non usata:**
   ```python
   scheda = titolo + autore + pubblicazione
   ```
   Hai creato la variabile ma non l'hai usata per il print.

2. **Riga 14 - Output completamente diverso:**
   ```python
   print(f" il titolo del libro e {titolo} l'autore è {autore} ed è stato pubblicato il {pubblicazione}")
   ```

Output prodotto: ` il titolo del libro e Il Signore degli Anelli l'autore è Tolkien ed è stato pubblicato il 1954`

Output atteso: `Titolo: Il Signore degli Anelli, Autore: Tolkien, Anno: 1954`

Cosa dovevi scrivere:
```python
titolo = input("Inserisci il titolo: ")
autore = input("Inserisci l'autore: ")
pubblicazione = input("Inserisci l'anno: ")
scheda = "Titolo: " + titolo + ", Autore: " + autore + ", Anno: " + pubblicazione
print(scheda)
```

Valutazione: Errore logico grave. Il formato richiesto è completamente diverso da quello che hai prodotto.

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
Punteggio: 3/5

Obiettivo: Riepilogo operatore += - costruire una frase

Analisi del codice:
Hai usato correttamente l'operatore +=, ma ci sono errori nel formato dell'output.

Errori riscontrati:

1. **Riga 10 - Stringa iniziale errata:**
   ```python
   frase = "python "
   ```
   Doveva essere `"Python"` (maiuscola, senza spazio finale).

2. **Righe 11-13 - Spazi aggiunti in posizioni sbagliate:**
   ```python
   frase += "è "
   frase += "un linguaggio "
   frase += "fantastico "
   ```
   Gli spazi vanno prima delle parole, non dopo.

Output prodotto: `python è un linguaggio fantastico ` (minuscola + spazio finale)
Output atteso: `Python è un linguaggio fantastico`

Cosa dovevi scrivere:
```python
frase = "Python"
frase += " è"
frase += " un linguaggio"
frase += " fantastico"
```

Valutazione: Errore di formato. L'output ha maiuscole sbagliate e spazi in eccesso.

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

Errori riscontrati:

1. **Riga 9 - Errore di battitura:**
   ```python
   cognome = input ("inserisci il to cognome: ")
   ```
   Hai scritto "to" invece di "tuo".

2. **Righe 16-17 - Formato output errato:**
   ```python
   print("nome:", nome,", i caratteri sono:", lunghezza_nome,)
   print("cognome:", cognome,",e i caratteri sono:", lunghezza_cognome,)
   ```

Output prodotto:
```
nome: Marco , i caratteri sono: 5
cognome: Bianchi ,e i caratteri sono: 7
```

Output atteso:
```
Nome: Marco, Lunghezza: 5
Cognome: Bianchi, Lunghezza: 7
```

Cosa dovevi scrivere:
```python
print("Nome:", nome + ", Lunghezza:", str(lunghezza_nome))
print("Cognome:", cognome + ", Lunghezza:", str(lunghezza_cognome))
```

Valutazione: L'output è in un formato completamente diverso da quello richiesto. Manca "Nome:" con maiuscola, e "Lunghezza:" è sostituito da "i caratteri sono:".

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
Hai convertito correttamente nome e cognome usando `.upper()` e `.lower()`, ma l'output non corrisponde al formato richiesto.

Errori riscontrati:

1. **Riga 14 - Errore di battitura:**
   ```python
   nome = input("inserisi il tuo nome")
   ```
   Hai scritto "inserisi" invece di "Inserisci".

2. **Righe 20-21 - Formato output errato:**
   ```python
   print ("nome:", nome_maiuscolo)
   print ("cognome:", cognome_minuscolo,)
   ```

Output prodotto:
```
nome: MARIO
cognome: rossi
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

Valutazione: Le label hanno la lettera iniziale minuscola invece che maiuscola. È un errore di formato.

---

## Esercizio 13
Punteggio: 4/5

Obiettivo: Confrontare la lunghezza di due parole

Analisi del codice:
Hai completato l'esercizio con la logica perfetta. Calcoli, confronto e condizioni sono tutti corretti.

Errore riscontrato:
```python
# Riga 9
parola2 = input("inserisci la seconda parola")
```

Problema: Manca ": " alla fine del prompt (dovrebbe essere `"Inserisci la seconda parola: "`). Inoltre "inserisci" ha la 'i' minuscola invece della 'I' maiuscola.

Valutazione: Errore minore nel formato del prompt. La logica è perfetta.

---

## Esercizio 14
Punteggio: 0/5

Obiettivo: Verificare se una password ha una lunghezza valida (8-16 caratteri)

Analisi del codice:
**Esercizio NON svolto.** Il file contiene ancora gli spazi vuoti `______` da completare.

Il codice deve essere scritto completamente:
```python
password = input("Inserisci una password: ")
lunghezza_password = len(password)

if lunghezza_password < 8:
    print("Password troppo corta")
elif lunghezza_password > 16:
    print("Password troppo lunga")
else:
    print("Password valida")
```

Valutazione: Esercizio non consegnato.

---

## Esercizio 15
Punteggio: 0/5

Obiettivo: Verificare un codice dopo aver rimosso gli spazi

Analisi del codice:
**Esercizio NON svolto.** Il file contiene solo i commenti della traccia, nessun codice.

Il codice deve essere scritto completamente:
```python
codice = input("Inserisci il codice: ")
codice_pulito = codice.strip()

if codice_pulito == "ABC123":
    print("Codice corretto")
else:
    print("Codice errato")
```

Valutazione: Esercizio non consegnato.

---

## Esercizio 16
Punteggio: 0/5

Obiettivo: Verificare un username ignorando spazi e maiuscole/minuscole

Analisi del codice:
**Esercizio NON svolto.** Il file contiene ancora gli spazi vuoti `______` da completare.

Il codice deve essere scritto completamente:
```python
username = input("Inserisci lo username: ")
username_pulito = username.strip()
username_pulito = username_pulito.lower()

if username_pulito == "admin":
    print("Accesso consentito")
else:
    print("Accesso negato")
```

Valutazione: Esercizio non consegnato.

---

## Esercizio 17
Punteggio: 0/5

Obiettivo: Verificare se "python" è contenuto in una frase

Analisi del codice:
**Esercizio NON svolto.** Il file contiene ancora gli spazi vuoti `______` da completare.

Il codice deve essere scritto completamente:
```python
frase = input("Inserisci una frase: ")
frase_minuscola = frase.lower()

if "python" in frase_minuscola:
    print("Python trovato!")
else:
    print("Python non trovato")
```

Valutazione: Esercizio non consegnato.

---

## Esercizio 18
Punteggio: 0/5

Obiettivo: Contare quante volte appare la lettera 'a' in una frase

Analisi del codice:
**Esercizio NON svolto.** Il file contiene solo i commenti della traccia, nessun codice.

Il codice deve essere scritto completamente:
```python
frase = input("Inserisci una frase: ")
frase_minuscola = frase.lower()
count = frase_minuscola.count("a")

print(f"La lettera 'a' appare {count} volte")

if count > 3:
    print("Ci sono molte 'a'!")
else:
    print("Ci sono poche 'a'")
```

Valutazione: Esercizio non consegnato.

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

inizia_corretto = url_minuscolo.startswith("http://") or url_minuscolo.startswith("https://")
finisce_corretto = url_minuscolo.endswith(".com") or url_minuscolo.endswith(".it")

if inizia_corretto and finisce_corretto:
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
- Buona comprensione dell'operatore += (es04, es05)
- Corretta applicazione di `len()` base (es08)
- Ottimo uso di `.upper()` e `.lower()` (es10, es11)
- Comprensione della logica condizionale base (es13)

Aree di miglioramento:

**Errori di battitura:**
   - Es01: "mario" e "rossi" invece di "Mario" e "Rossi"
   - Es07: "programmazione" invece di "Programmazione"
   - Es09: "to" invece di "tuo"
   - Es12: "inserisi" invece di "Inserisci"
   - Es13: formato prompt non corretto

**Errori di formato:**
   - Es06: maiuscola sbagliata e spazi in eccesso
   - Es09: Output completamente diverso dal formato richiesto
   - Es12: Label con minuscole invece di maiuscole

**Errori logici:**
   - Es02: Output completamente stravolto rispetto alla traccia
   - Es03: Formato output completamente diverso da quello richiesto

**Esercizi non svolti (7 su 20):**
   - Es14: Validazione password
   - Es15: Verifica codice con strip
   - Es16: Username validation
   - Es17: Operatore in
   - Es18: Metodo count
   - Es19: Validazione URL
   - Es20: Validazione email completa

**PROBLEMA PRINCIPALE**: Hai consegnato solo 13 esercizi su 20. Gli ultimi 7 esercizi (dal 14 al 20) sono completamente vuoti o non completati. Questo ha gravemente impattato il tuo punteggio finale.

Esercizi da completare OBBLIGATORIAMENTE:
- **Esercizio 14-20:** Completa tutti gli esercizi mancanti
- **Esercizio 2:** Segui ESATTAMENTE il formato richiesto: "Vivo a [città], [nazione]"
- **Esercizio 3:** Il formato deve essere: "Titolo: [titolo], Autore: [autore], Anno: [anno]"
- **Esercizio 6, 9, 12:** Correggi il formato dell'output per corrispondere esattamente a quello richiesto

Suggerimento importante:
Leggi ATTENTAMENTE i commenti "Output atteso" in ogni esercizio. Il tuo output deve corrispondere ESATTAMENTE a quello mostrato negli esempi, incluse maiuscole, punteggiatura e spaziatura.

Valutazione generale:
Hai dimostrato di comprendere i concetti base (concatenazione, +=, len, upper/lower) quando li applichi. Tuttavia, ci sono due problemi critici: 1) Non hai completato il 35% della verifica (7 esercizi su 20), 2) In alcuni esercizi hai cambiato arbitrariamente l'output richiesto invece di seguire le istruzioni. Completa tutti gli esercizi e fai attenzione al formato richiesto per migliorare significativamente (potenziale: 85-90/100 se completi tutto correttamente).
