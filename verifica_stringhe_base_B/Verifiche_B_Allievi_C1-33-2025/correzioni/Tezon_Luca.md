# Correzione Verifica Stringhe Base B - Tezon Luca

Punteggio Totale: 60/100

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
Punteggio: 3/5

Obiettivo: Riepilogo len() - calcolare lunghezza di prodotto e descrizione

Analisi del codice:
Hai completato i calcoli correttamente con `len()`, ma il formato dell'output non corrisponde a quello richiesto.

Errori riscontrati:
```python
# Righe 11-14
print(lunghezza)
print(f"Prodotto: {prodotto}, Lunghezza:  {lunghezza}")
descrizione = "Computer portatile"
print(f"Descrizione: {descrizione}, Lunghezza:  {lunghezza2}")
```

Problemi:
1. La riga 11 stampa `lunghezza` da sola senza etichette - questo non dovrebbe esserci
2. La riga 12 ha doppio spazio dopo "Lunghezza:" (`Lunghezza:  {lunghezza}`)
3. La riga 14 ha doppio spazio dopo "Lunghezza:" (`Lunghezza:  {lunghezza2}`)

Output prodotto:
```
8
Prodotto: Notebook, Lunghezza:  8
Descrizione: Computer portatile, Lunghezza:  18
```

Output atteso:
```
Prodotto: Notebook, Lunghezza: 8
Descrizione: Computer portatile, Lunghezza: 18
```

Cosa dovevi scrivere:
```python
prodotto = "Notebook"
lunghezza = len(prodotto)

descrizione = "Computer portatile"
lunghezza2 = len(descrizione)

print(f"Prodotto: {prodotto}, Lunghezza: {lunghezza}")
print(f"Descrizione: {descrizione}, Lunghezza: {lunghezza2}")
```

Valutazione: Errore di formato. C'è un print extra e spazi doppi.

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
Hai convertito correttamente hashtag e username usando `.upper()` e `.lower()`, ma l'output è completamente sbagliato.

Errore riscontrato:
```python
# Righe 19-20
print(f"Inserisci un hashtag {hashtag_maiuscolo}")
print(f"Inserisci un username {username_minuscolo}")
```

Problema: Hai scritto "Inserisci un hashtag" e "Inserisci un username" invece di "Hashtag:" e "Username:". Stai stampando di nuovo il messaggio dell'input invece delle etichette richieste!

Output prodotto:
```
Inserisci un hashtag PYTHON
Inserisci un username coder123
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

Valutazione: Errore logico grave. Il formato dell'output è completamente diverso da quello richiesto.

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
# Riga 9
numero = input("Inserisci il numerocivico ")
```

Problema: Hai scritto "numerocivico" tutto attaccato invece di "numero civico" con lo spazio. È solo un errore di battitura, la logica è corretta.

Output prodotto: `Inserisci il numerocivico` (senza spazio)
Output atteso: `Inserisci il numero civico:`

Cosa dovevi scrivere:
```python
numero = input("Inserisci il numero civico: ")
```

Valutazione: Errore di battitura. Il programma funziona ma il prompt è sbagliato.

---

## Esercizio 9
Punteggio: 3/5

Obiettivo: Riepilogo concatenazione - creare carta d'identità

Analisi del codice:
Hai completato l'esercizio con la logica corretta, ma l'output non corrisponde al formato richiesto.

Errore riscontrato:
```python
# Riga 18
print(f"Nome {nome}, Cognome {cognome}, CF {codice_fiscale} ")
```

Problema: Mancano i due punti dopo "Nome", "Cognome" e "CF".

Output prodotto: `Nome Luigi, Cognome Verdi, CF VRDLGU80A01H501Z`
Output atteso: `Nome: Luigi, Cognome: Verdi, CF: VRDLGU80A01H501Z`

Cosa dovevi scrivere:
```python
print(f"Nome: {nome}, Cognome: {cognome}, CF: {codice_fiscale}")
```

Valutazione: Errore di formato. Mancano i due punti dopo le etichette.

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

Output prodotto: `+39 02 1234567` (con spazio extra tra 02 e 1234567)
Output atteso: `+39 02 1234567`

Nota: In realtà l'output sembra corretto perché alla riga 12 aggiungi "1234567" senza spazio iniziale, quindi lo spazio finale del " 02 " serve da separatore. PERÒ il problema è che hai uno spazio di troppo se consideriamo che alla riga 12 il codice dovrebbe essere `" 1234567"` con lo spazio.

Guardando la traccia originale:
- Riga 8: `telefono += " 02"` (uno spazio prima, nessuno dopo)
- Riga 11: `telefono += " 1234567"` (uno spazio prima)

Tu hai fatto:
- Riga 9: `telefono += " 02 "` (uno spazio prima E uno dopo)
- Riga 12: `telefono += "1234567"` (nessuno spazio)

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
Punteggio: 4/5

Obiettivo: Costruire un URL usando +=

Analisi del codice:
Hai usato correttamente l'operatore += per costruire l'URL, ma c'è un errore di battitura.

Errore riscontrato:
```python
# Riga 15
url += "it"
```

Problema: Hai scritto `"it"` invece di `".it"`. Manca il punto prima di "it".

Output prodotto: `http://www.negozio.it`

Aspetta, l'output sembra corretto... Lascia che verifichi meglio.

Guardando il codice:
- Riga 6: `url = "http://"`
- Riga 9: `url += "www."`
- Riga 12: `url += "negozio"`
- Riga 15: `url += "it"`

Output: `http://www.negozioeit` (SBAGLIATO! Manca il punto prima di "it")

Output atteso: `http://www.negozio.it`

Cosa dovevi scrivere:
```python
url += ".it"
```

Valutazione: Errore di battitura. Manca il punto prima di "it".

---

## Esercizio 12
Punteggio: 3/5

Obiettivo: Riepilogo operatore += - costruire un messaggio

Analisi del codice:
Hai usato correttamente l'operatore +=, ma ci sono errori multipli nel formato.

Errori riscontrati:
```python
# Righe 16-17
messaggio += ",Come stai "
messaggio += ", ?"
```

Problemi:
1. Riga 16: Manca lo spazio dopo la virgola (`,Come` invece di `, come`)
2. Riga 16: "Come" ha la "C" maiuscola invece di minuscola
3. Riga 16: Spazio extra alla fine (`"Come stai "` invece di `"come stai"`)
4. Riga 17: Virgola extra prima del punto interrogativo (`", ?"` invece di `"?"`)

Output prodotto: `Ciao,Come stai , ? Tutto bene!`
Output atteso: `Ciao, come stai? Tutto bene!`

Cosa dovevi scrivere:
```python
messaggio = "Ciao"
messaggio += ", come stai"
messaggio += "?"
messaggio += " Tutto bene"
messaggio += "!"
print(messaggio)
```

Valutazione: Errore di formato. Multiple spacing e punctuation errors.

---

## Esercizio 13
Punteggio: 0/5

Obiettivo: Verificare se "online" è contenuto nella modalità del corso

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori logici GRAVISSIMI.

Errori riscontrati:
```python
# Righe 12-15
if "online" in modalita :
    print("Il corso non è online!")
else:
    print("Il corso  è online")
```

Problemi:
1. **Logica invertita**: Se "online" è nella modalità, stampi "Il corso NON è online!" - è esattamente il contrario!
2. **Variabile sbagliata**: Hai creato `modalita_minuscola` alla riga 9 ma poi usi `modalita` (la variabile originale) nell'if. Se l'utente scrive "ONLINE" non viene trovato!
3. Riga 15: Doppio spazio in `"Il corso  è online"`

Conseguenza: Il programma fa esattamente il contrario di ciò che dovrebbe fare.

Cosa dovevi scrivere:
```python
modalita = input("Inserisci la modalità del corso: ")
modalita_minuscola = modalita.lower()

if "online" in modalita_minuscola:
    print("Il corso è online!")
else:
    print("Il corso non è online")
```

Valutazione: Errore logico gravissimo. La logica è invertita E usi la variabile sbagliata.

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
Hai tentato l'esercizio ma ci sono errori GRAVISSIMI.

Errore riscontrato:
```python
# Righe 16-17
codice = input("Inserisci un codice coupon")
codice.strip
```

Problemi:
1. **Mancano le parentesi**: Hai scritto `codice.strip` senza le parentesi. In Python i metodi devono essere chiamati con le parentesi: `codice.strip()`. Senza parentesi il metodo non viene eseguito!
2. **Risultato non salvato**: Anche se avessi scritto `codice.strip()`, il risultato non viene salvato in nessuna variabile. Poi alla riga 18 confronti `codice` (la variabile ORIGINALE con gli spazi) invece del codice pulito.

Conseguenza: Il `.strip` non viene eseguito (mancano le parentesi), e anche se fosse eseguito il risultato viene perso. Il confronto viene fatto sulla stringa originale con gli spazi.

Cosa dovevi scrivere:
```python
codice = input("Inserisci il codice coupon: ")
codice_pulito = codice.strip()

if codice_pulito == "SCONTO20":
    print("Coupon valido")
else:
    print("Coupon non valido")
```

Oppure:
```python
codice = input("Inserisci il codice coupon: ")
codice = codice.strip()  # Salva il risultato nella stessa variabile

if codice == "SCONTO20":
    print("Coupon valido")
else:
    print("Coupon non valido")
```

Valutazione: Errore logico gravissimo. Mancano le parentesi E non salvi il risultato.

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
Hai tentato l'esercizio ma c'è un errore logico GRAVISSIMO che rende il codice completamente sbagliato.

Errore riscontrato:
```python
# Righe 21-22
lunghezza = len(telefono)
if telefono == lunghezza:
```

Problema: Stai confrontando una **stringa** (`telefono`) con un **numero intero** (`lunghezza`)! Questo confronto non ha senso logico e sarà SEMPRE falso.

Ad esempio:
- `telefono = "+39 3201234567"` (una stringa)
- `lunghezza = 15` (un numero)
- `telefono == lunghezza` → `"+39 3201234567" == 15` → SEMPRE falso!

Inoltre manca completamente il controllo con `.startswith("+39")`.

Cosa dovevi scrivere:
```python
telefono = input("Inserisci un numero di telefono: ")

lunghezza = len(telefono)
inizia_corretto = telefono.startswith("+39")

if lunghezza >= 10 and inizia_corretto:
    print("Numero valido")
else:
    print("Numero non valido")
```

Spiegazione: Devi verificare DUE condizioni:
1. `lunghezza >= 10` (la lunghezza è almeno 10)
2. `inizia_corretto` (inizia con "+39")

Entrambe devono essere vere (`and`) per stampare "Numero valido".

Valutazione: Errore logico gravissimo. Confronti una stringa con un numero - errore concettuale grave.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Validazione completa username

Analisi del codice:
**Esercizio NON completato.** Il file si interrompe alla riga 26 con codice incompleto.

Codice presente:
```python
username = input("Insaerisci uno username")
username =
```

Il codice si ferma qui, senza nulla dopo l'uguale. L'esercizio non è stato completato.

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

Valutazione: Esercizio non completato.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Validazione completa codice prodotto

Analisi del codice:
**Esercizio NON svolto.** Il file contiene solo i commenti della traccia, nessun codice.

Il codice completo doveva essere:
```python
codice = input("Inserisci un codice prodotto: ")

# Pulisci il codice
codice_pulito = codice.strip().upper()

# Verifica le condizioni
lunghezza_ok = len(codice_pulito) == 7
contiene_trattino = "-" in codice_pulito
inizia_abc = codice_pulito.startswith("ABC")

if lunghezza_ok and contiene_trattino and inizia_abc:
    print("Codice valido")
else:
    print("Codice non valido")
```

Valutazione: Esercizio non consegnato.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione di `len()` (es01, es02)
- Buon uso di `.upper()` e `.lower()` (es04, es05)
- Corretta applicazione della concatenazione (es07)
- Corretto uso di `.count()` (es16, es17)
- Corretto uso dell'operatore `in` quando applicato correttamente (es14)

Aree di miglioramento:

**Errori di formato:**
   - Es03: Print extra + spazi doppi
   - Es09: Mancano i due punti dopo "Nome", "Cognome", "CF"
   - Es10: Spazi nella posizione sbagliata
   - Es12: Errori multipli di spaziatura e punteggiatura

**Errori di battitura:**
   - Es08: "numerocivico" invece di "numero civico"
   - Es11: Manca il punto prima di "it"

**Errori logici gravissimi:**
   - Es06: Stampi il messaggio dell'input invece delle etichette richieste
   - Es13: Logica completamente invertita + usi la variabile sbagliata
   - Es15: Mancano le parentesi su `.strip` E non salvi il risultato
   - Es18: Confronti una stringa con un numero - errore concettuale grave
   - Es19: Non completato (file interrotto)
   - Es20: Non svolto

**PROBLEMA CRITICO - es15**: Hai scritto `codice.strip` senza parentesi. In Python, i metodi devono essere chiamati con le parentesi: `codice.strip()`. Senza parentesi il metodo NON viene eseguito! Inoltre, anche se fosse eseguito, devi salvare il risultato:

```python
# SBAGLIATO
codice.strip  # Non fa nulla, mancano le parenthesi!

# SBAGLIATO
codice.strip()  # Esegue ma il risultato viene perso

# CORRETTO
codice = codice.strip()  # Esegue e salva il risultato
```

**PROBLEMA CRITICO - es13**: Hai invertito completamente la logica. Se "online" è nella modalità, stampi "Il corso NON è online!" - è esattamente il contrario! Inoltre hai creato `modalita_minuscola` ma poi non la usi.

**PROBLEMA CRITICO - es18**: Stai confrontando `telefono` (una stringa) con `lunghezza` (un numero). Questo è un errore concettuale gravissimo - non si può confrontare una stringa con un numero!

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 6:** Usa "Hashtag:" e "Username:" invece di "Inserisci un hashtag" e "Inserisci un username"
- **Esercizio 13:** Inverti la logica (se "online" IN modalita, stampa "è online") e usa `modalita_minuscola`
- **Esercizio 15:** Aggiungi parentesi a `.strip()` e salva il risultato
- **Esercizio 18:** Devi verificare DUE condizioni separate: lunghezza >= 10 AND inizia con "+39"
- **Esercizio 19:** Completa l'esercizio
- **Esercizio 20:** Completa l'esercizio

Pattern da studiare:
```python
# Chiamare metodi - SERVONO LE PARENTESI!
stringa.strip()   # CORRETTO
stringa.strip     # SBAGLIATO - non fa nulla!

# Salvare il risultato
codice = codice.strip()  # CORRETTO - salva il risultato
codice.strip()           # SBAGLIATO - il risultato viene perso

# Confrontare stringhe con numeri
if telefono == lunghezza:  # SBAGLIATO - stringa vs numero
if lunghezza >= 10:        # CORRETTO - numero vs numero

# Logica booleana
if "online" in modalita:
    print("è online")      # CORRETTO
if "online" in modalita:
    print("NON è online")  # SBAGLIATO - logica invertita!
```

Valutazione generale:
Hai dimostrato una comprensione base dei concetti fondamentali (len, upper, lower, count), ma ci sono problemi GRAVI negli esercizi più complessi: 1) Es06 ha output completamente sbagliato, 2) Es13 ha logica invertita, 3) Es15 non chiama il metodo correttamente, 4) Es18 confronta stringa con numero (errore concettuale), 5) Es19 e es20 non completati (10% della verifica). Correggendo questi errori e completando gli esercizi mancanti puoi raggiungere 90-95/100.
