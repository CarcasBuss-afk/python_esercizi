# Correzione Verifica Stringhe Base A - Trompeo Davide

Punteggio Totale: 53/100

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
Esercizio completato perfettamente. Hai creato correttamente la variabile 'luogo' concatenando "Vivo a " + città + ", " + nazione e l'hai stampata.

---

## Esercizio 3
Punteggio: 3/5

Obiettivo: Riepilogo concatenazione - scheda libro

Analisi del codice:
Hai completato l'esercizio con la logica corretta, ma ci sono spazi extra nell'output.

Errore riscontrato:
```python
# Riga 17
scheda = "Titolo: "+ titolo + ", " + " Autore: "+ autore + ", " + " Anno: "+ anno_pubbl
```

Problema: Hai aggiunto spazi extra prima di "Autore:" e "Anno:". Nota i doppi spazi: `+ ", " + " Autore: "` e `+ ", " + " Anno: "`.

Output prodotto: `Titolo: Il Signore degli Anelli,  Autore: Tolkien,  Anno: 1954` (nota i doppi spazi dopo le virgole)

Output atteso: `Titolo: Il Signore degli Anelli, Autore: Tolkien, Anno: 1954`

Cosa dovevi scrivere:
```python
scheda = "Titolo: " + titolo + ", Autore: " + autore + ", Anno: " + anno_pubbl
```

Valutazione: Errore di formato. Gli spazi extra rendono l'output diverso da quello richiesto.

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
Punteggio: 4/5

Obiettivo: Riepilogo operatore += - costruire una frase

Analisi del codice:
Hai usato correttamente l'operatore += e l'output è corretto, ma hai usato un nome di variabile sbagliato.

Errore riscontrato:
```python
# Riga 9
python = "Python"
```

Problema: La traccia richiede esplicitamente di creare una variabile chiamata `frase`, ma tu hai chiamato la variabile `python`.

Dalla traccia: "Crea una variabile **'frase'** con il valore 'Python'."

Cosa dovevi scrivere:
```python
frase = "Python"
frase += " è"
frase += " un linguaggio"
frase += " fantastico"
print(frase)
```

Valutazione: L'output è corretto, ma non hai seguito le istruzioni sul nome della variabile. Errore minore.

---

## Esercizio 7
Punteggio: 3/5

Obiettivo: Calcolare e stampare la lunghezza di una stringa

Analisi del codice:
Hai usato correttamente la funzione `len()`, ma c'è un errore nel formato del print.

Errore riscontrato:
```python
# Riga 12
print("La parola ha", [lunghezza], "caratteri")
```

Problema: Hai messo le parentesi quadre `[lunghezza]` invece di scrivere semplicemente `lunghezza`.

Output prodotto: `La parola ha [14] caratteri`
Output atteso: `La parola ha 14 caratteri`

Cosa dovevi scrivere:
```python
print("La parola ha", lunghezza, "caratteri")
```

Valutazione: Le parentesi quadre sono un errore di sintassi/formato che cambia l'output.

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
Hai completato i calcoli correttamente con `len()`, ma il formato dell'output ha spazi extra che lo rendono diverso da quello richiesto.

Errore riscontrato:
```python
# Righe 19-20
print("Nome:", nome, ", ", "Lunghezza: ", lung_nome)
print("Cognome: ", cognome, ", ", "Lunghezza: ", lung_cognome)
```

Problema: Hai separato gli elementi con troppe virgole, creando spazi extra nell'output.

Output prodotto:
```
Nome: Marco ,  Lunghezza:  5
Cognome:  Bianchi ,  Lunghezza:  7
```

Output atteso:
```
Nome: Marco, Lunghezza: 5
Cognome: Bianchi, Lunghezza: 7
```

Cosa dovevi scrivere:
```python
print("Nome:", nome + ", Lunghezza:", lung_nome)
print("Cognome:", cognome + ", Lunghezza:", lung_cognome)
```

Oppure con f-string:
```python
print(f"Nome: {nome}, Lunghezza: {lung_nome}")
print(f"Cognome: {cognome}, Lunghezza: {lung_cognome}")
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
Punteggio: 0/5

Obiettivo: Convertire una parola in minuscolo con input utente

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore logico GRAVE: hai usato il metodo sbagliato.

Errore riscontrato:
```python
# Riga 9
parola_minuscola = parola.upper()
```

Problema: L'esercizio richiede di convertire in MINUSCOLO (`.lower()`), ma tu hai usato `.upper()` che converte in MAIUSCOLO.

Conseguenza: Se l'utente inserisce "PYTHON", il programma stampa "PYTHON" invece di "python".

Cosa dovevi scrivere:
```python
parola_minuscola = parola.lower()
```

Valutazione: Errore logico grave. Hai usato il metodo opposto a quello richiesto. Il programma fa esattamente il contrario di ciò che dovrebbe fare.

---

## Esercizio 12
Punteggio: 0/5

Obiettivo: Riepilogo .upper() e .lower() - convertire nome e cognome

Analisi del codice:
Hai convertito correttamente nome e cognome usando `.upper()` e `.lower()`, ma l'output è completamente sbagliato.

Errore riscontrato:
```python
# Righe 20-21
print(nome_maiuscolo)
print(cognome_minuscolo)
```

Problema: Hai stampato solo i valori delle variabili, senza le etichette "Nome:" e "Cognome:" richieste.

Output prodotto:
```
MARIO
rossi
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

Valutazione: Errore logico grave. Manca completamente il formato richiesto con le etichette.

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
Hai iniziato l'esercizio correttamente (input e strip), ma non l'hai completato. Il codice è incompleto e contiene un errore di sintassi.

Errore riscontrato:
```python
# Righe 15-19
codice = input("inserisci un codice: ")

codice_no_spazi = codice.strip()

if codice_no_spazi = :

```

Problema:
1. La riga 19 ha `if codice_no_spazi = :` che è sintatticamente errata (usa `=` invece di `==` e manca il valore da confrontare)
2. Il codice è incompleto, manca tutto il corpo dell'if e l'else
3. Il file termina in modo incompleto

Il codice deve essere completato:
```python
codice = input("Inserisci il codice: ")
codice_no_spazi = codice.strip()

if codice_no_spazi == "ABC123":
    print("Codice corretto")
else:
    print("Codice errato")
```

Valutazione: Esercizio non completato. Il codice è interrotto a metà e contiene errori di sintassi.

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
- Ottima comprensione della concatenazione di stringhe (es01, es02)
- Buon uso dell'operatore += (es04, es05)
- Corretta applicazione di `len()` (es08, es13)
- Ottimo uso di `.upper()` (es10)
- Comprensione della logica condizionale (es13, es14)

Aree di miglioramento:

**Errori minori:**
   - Es06: Nome variabile sbagliato ("python" invece di "frase")

**Errori di formato:**
   - Es03: Spazi extra nell'output (doppi spazi dopo virgole)
   - Es07: Parentesi quadre `[lunghezza]` invece di `lunghezza`
   - Es09: Spazi extra causati da troppi separatori nel print

**Errori logici:**
   - Es11: Usato `.upper()` invece di `.lower()` - metodo completamente sbagliato
   - Es12: Mancano le etichette "Nome:" e "Cognome:" nell'output
   - Es15: Codice incompleto con errore di sintassi (`if codice_no_spazi = :`)

**Esercizi non svolti (6 su 20):**
   - Es16: Username validation
   - Es17: Operatore in
   - Es18: Metodo count
   - Es19: Validazione URL
   - Es20: Validazione email completa

**PROBLEMA PRINCIPALE**: Hai consegnato solo 14 esercizi su 20. Gli ultimi 6 esercizi (dal 15 al 20) sono incompleti o vuoti. Inoltre, l'esercizio 15 è stato interrotto a metà con un errore di sintassi. Questo ha impattato significativamente il tuo punteggio finale.

Esercizi da completare OBBLIGATORIAMENTE:
- **Esercizio 15-20:** Completa tutti gli esercizi mancanti
- **Esercizio 11:** Cambia `.upper()` in `.lower()`
- **Esercizio 12:** Aggiungi "Nome:" e "Cognome:" nell'output
- **Esercizio 3, 7, 9:** Fai attenzione agli spazi extra e al formato corretto

Errori da evitare:
1. **Confusione tra `.upper()` e `.lower()`**: `.upper()` converte in MAIUSCOLO, `.lower()` converte in minuscolo
2. **Parentesi quadre nel print**: `print(x)` non `print([x])`
3. **Spazi extra**: Fai attenzione a non aggiungere spazi doppi quando concateni stringhe
4. **Completare gli esercizi**: Non lasciare esercizi a metà o con errori di sintassi

Valutazione generale:
Hai dimostrato una buona comprensione dei concetti base (concatenazione, +=, len, upper). Tuttavia, ci sono problemi significativi: 1) Non hai completato il 30% della verifica (6 esercizi su 20), 2) L'esercizio 11 usa il metodo completamente opposto a quello richiesto, 3) Errori di formato ricorrenti negli esercizi 3, 7, 9. Completa tutti gli esercizi e fai più attenzione ai dettagli del formato richiesto per migliorare significativamente (potenziale: 85-90/100 se completi tutto correttamente e correggi gli errori).
