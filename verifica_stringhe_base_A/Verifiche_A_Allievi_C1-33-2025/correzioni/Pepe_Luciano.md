# Correzione Verifica Stringhe Base A - Pepe Luciano

Punteggio Totale: 68/100

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
Punteggio: 0/5

Obiettivo: Riepilogo concatenazione - scheda libro

Analisi del codice:
Hai tentato l'esercizio ma la concatenazione è completamente errata.

Errore riscontrato:
```python
# Riga 17
scheda = Titolo + ", " + Autore + ", " + Anno
```

Problema: Mancano completamente le etichette "Titolo: ", "Autore: ", "Anno: " nella concatenazione. Stai solo concatenando i valori delle variabili con virgole.

Output prodotto: `Il Signore degli Anelli, Tolkien, 1954`
Output atteso: `Titolo: Il Signore degli Anelli, Autore: Tolkien, Anno: 1954`

Cosa dovevi scrivere:
```python
Titolo = input("Inserisci il titolo: ")
Autore = input("Inserisci l'autore: ")
Anno = input("Inserisci l'anno: ")

scheda = "Titolo: " + Titolo + ", Autore: " + Autore + ", Anno: " + Anno
print(scheda)
```

Valutazione: Errore logico grave. L'output non ha le etichette richieste.

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
Punteggio: 5/5

Obiettivo: Calcolare e stampare la lunghezza di una stringa

Analisi del codice:
Esercizio completato perfettamente. Hai usato correttamente la funzione `len()` e stampato il risultato nel formato richiesto. Le parentesi attorno a `(lunghezza)` sono inutili ma non cambiano il risultato.

---

## Esercizio 8
Punteggio: 5/5

Obiettivo: Calcolare lunghezza di una frase inserita dall'utente

Analisi del codice:
Esercizio completato perfettamente. Hai gestito correttamente l'input dell'utente e calcolato la lunghezza con `len()`. Le parentesi attorno a `(numero_caratteri)` sono inutili ma non cambiano il risultato.

---

## Esercizio 9
Punteggio: 3/5

Obiettivo: Riepilogo len() - calcolare lunghezza di nome e cognome

Analisi del codice:
Hai completato i calcoli correttamente con `len()`, ma il formato dell'output ha spazi extra.

Errore riscontrato:
```python
# Righe 20-21
print("Nome: " ,(nome),"," "Lunghezza:", (lunghezza_nome))
print("Cognome: " ,(cognome),"," "Lunghezza:", (lunghezza_cognome))
```

Problema: Hai separato gli elementi con troppe virgole, creando spazi extra nell'output. Le parentesi attorno ai nomi delle variabili sono inutili.

Output prodotto:
```
Nome:  Marco , Lunghezza:  5
Cognome:  Bianchi , Lunghezza:  7
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
Punteggio: 0/5

Obiettivo: Riepilogo .upper() e .lower() - convertire nome e cognome

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore logico GRAVISSIMO: i nomi delle variabili sono completamente invertiti rispetto ai metodi usati.

Errore riscontrato:
```python
# Righe 17-18
nome_minuscolo = nome.upper()
cognome_maiuscolo = cognome.lower()
```

Problema:
1. Hai chiamato la variabile `nome_minuscolo` ma usi `.upper()` che converte in MAIUSCOLO
2. Hai chiamato la variabile `cognome_maiuscolo` ma usi `.lower()` che converte in minuscolo

Questo è completamente contraddittorio! I nomi delle variabili dovrebbero corrispondere a ciò che fanno.

Poi alle righe 20-21:
```python
print(f"Nome: " ,(nome_minuscolo),)
print(f"Cognome: ",(cognome_maiuscolo),)
```

Usi `nome_minuscolo` (che in realtà contiene il nome MAIUSCOLO) e `cognome_maiuscolo` (che in realtà contiene il cognome minuscolo).

Output prodotto:
```
Nome:  MARIO
Cognome:  rossi
```

Ma questo è CORRETTO per caso! Le variabili hanno nomi sbagliati ma funzionano perché i metodi sono corretti. Tuttavia, c'è anche il problema degli spazi extra causati dall'uso improprio di f-string con virgole.

Cosa dovevi scrivere:
```python
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")

nome_maiuscolo = nome.upper()
cognome_minuscolo = cognome.lower()

print(f"Nome: {nome_maiuscolo}")
print(f"Cognome: {cognome_minuscolo}")
```

Valutazione: Errore logico grave. I nomi delle variabili sono completamente invertiti, anche se per caso l'output è corretto. Questo dimostra confusione sui concetti.

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
# Righe 14-17
codice = input("Inserisci un codice: ")
codice.strip()

if codice == "ABC123":
```

Problema: Hai chiamato `codice.strip()` alla riga 15, ma NON hai salvato il risultato in nessuna variabile. Lo `.strip()` viene eseguito ma il risultato viene perso. Poi alla riga 17 confronti `codice` (la variabile ORIGINALE con gli spazi) invece del codice pulito.

Conseguenza: Se l'utente inserisce "   ABC123   " (con spazi), il programma stampa "Codice Errato" perché confronta `"   ABC123   "` con `"ABC123"`.

Cosa dovevi scrivere:
```python
codice = input("Inserisci un codice: ")
codice_pulito = codice.strip()

if codice_pulito == "ABC123":
    print("Codice corretto")
else:
    print("Codice errato")
```

Oppure:
```python
codice = input("Inserisci un codice: ")
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
Punteggio: 0/5

Obiettivo: Contare quante volte appare la lettera 'a' in una frase

Analisi del codice:
Hai tentato l'esercizio ma ci sono errori multipli.

Errori riscontrati:

1. **Riga 22 - Variabile sbagliata:**
   ```python
   numero_a = frase.count("a")
   ```
   Hai usato `frase` invece di `frase_minuscola`. Se la frase contiene 'A' maiuscola, non viene contata.

2. **Manca completamente il controllo if/else:**
   La traccia richiede: "Se appare più di 3 volte stampa 'Ci sono molte a!', altrimenti 'Ci sono poche a'".

   Non hai implementato questa parte. Il tuo codice si ferma dopo il print della riga 24.

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

Valutazione: Errori logici gravi. Variabile sbagliata + manca metà dell'esercizio.

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
- Ottima comprensione della concatenazione di stringhe (es01, es02)
- Buon uso dell'operatore += (es04, es05, es06)
- Corretta applicazione di `len()` (es07, es08, es13)
- Ottimo uso di `.upper()` e `.lower()` (es10, es11)
- Comprensione della logica condizionale (es13, es14)
- Perfetta applicazione di `.strip()` e `.lower()` combinati (es16)
- Corretto uso dell'operatore `in` (es17)

Aree di miglioramento:

**Errori di formato:**
   - Es09: Spazi extra causati da troppi separatori nel print

**Errori logici:**
   - Es03: Mancano le etichette "Titolo:", "Autore:", "Anno:" nella concatenazione
   - Es12: Nomi delle variabili completamente invertiti (`nome_minuscolo` usa `.upper()`, `cognome_maiuscolo` usa `.lower()`)
   - Es15: `.strip()` non salvato, risultato perso
   - Es18: Variabile sbagliata (`frase` invece di `frase_minuscola`) + manca if/else
   - Es19: Non svolto
   - Es20: Non svolto

**PROBLEMA CRITICO - es12**: Hai chiamato una variabile `nome_minuscolo` ma usi `.upper()` che converte in MAIUSCOLO, e `cognome_maiuscolo` ma usi `.lower()` che converte in minuscolo. Questo è completamente contraddittorio! I nomi delle variabili devono corrispondere a ciò che fanno:
```python
# SBAGLIATO
nome_minuscolo = nome.upper()  # Nome dice "minuscolo" ma fa MAIUSCOLO!

# CORRETTO
nome_maiuscolo = nome.upper()  # Nome e azione corrispondono
```

**PROBLEMA CRITICO - es15**: Devi capire che i metodi come `.strip()` NON modificano la stringa originale, ma RITORNANO una nuova stringa. Devi salvare il risultato:
```python
# SBAGLIATO - il risultato viene perso
codice.strip()

# CORRETTO - salva il risultato
codice_pulito = codice.strip()
# oppure
codice = codice.strip()
```

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 3:** Aggiungi "Titolo: ", "Autore: ", "Anno: " nella concatenazione
- **Esercizio 12:** Cambia i nomi: `nome_maiuscolo = nome.upper()` e `cognome_minuscolo = cognome.lower()`
- **Esercizio 15:** Salva il risultato di `.strip()` prima di usarlo
- **Esercizio 18:** Usa `frase_minuscola.count("a")` e aggiungi if/else
- **Esercizio 19:** Completa l'esercizio
- **Esercizio 20:** Completa l'esercizio

Consigli per migliorare:
1. **Nomi delle variabili**: Devono descrivere il contenuto. Non chiamare `nome_minuscolo` una variabile che contiene il nome MAIUSCOLO!
2. **Metodi delle stringhe**: Ritornano NUOVE stringhe, devi salvare il risultato
3. **Completare gli esercizi**: Non lasciare esercizi vuoti
4. **F-string**: Non mescolare f-string con virgole: usa `print(f"Nome: {valore}")` non `print(f"Nome: " ,(valore),)`

Valutazione generale:
Hai dimostrato una buona comprensione dei concetti base (concatenazione, +=, len, condizioni). Gli esercizi base sono stati completati correttamente. I problemi principali sono: 1) Errore gravissimo nell'es12 (nomi variabili invertiti), 2) Errore concettuale nell'es15 (`.strip()` non salvato), 3) Es18 incompleto (variabile sbagliata + manca if/else), 4) Es19 e es20 non svolti (10% della verifica). Correggendo questi errori e completando gli esercizi mancanti puoi raggiungere 93/100.
