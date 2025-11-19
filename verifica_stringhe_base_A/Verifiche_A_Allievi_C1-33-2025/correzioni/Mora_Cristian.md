# Correzione Verifica Stringhe Base A - Mora Cristian

Punteggio Totale: 25/100

---

## Esercizio 1
Punteggio: 3.5/5

Obiettivo: Concatenare nome e cognome con uno spazio tra di essi.

Analisi del codice:
Hai capito il concetto base della concatenazione, ma hai aggiunto spazi extra dove non servivano.

Errori riscontrati:
- Riga 6: `nome = "Mario "`
- Riga 9: `cognome = "Rossi "`
- Riga 12: `nome_completo = "Mario " + "Rossi "`

Problemi:
1. Hai aggiunto uno spazio dentro le stringhe "Mario " e "Rossi " (spazi alla fine)
2. Hai scritto le stringhe letterali invece di usare le variabili
3. Il risultato sarà "Mario Rossi " con spazio finale extra

Cosa dovevi scrivere:
```python
nome = "Mario"
cognome = "Rossi"
nome_completo = nome + " " + cognome
```

Spiegazione:
Quando concateni stringhe, devi usare i NOMI delle variabili, non i loro valori scritti letteralmente. La variabile `nome` contiene già "Mario", quindi scrivi `nome`, non `"Mario"` di nuovo. Lo spazio va aggiunto SOLO tra le due parole usando `+ " " +`, non dentro le stringhe stesse.

---

## Esercizio 2
Punteggio: 0/5

Obiettivo: Chiedere all'utente città e nazione e concatenarle.

Analisi del codice:
L'esercizio non è stato svolto correttamente. Il codice contiene errori di sintassi gravi che impedirebbero l'esecuzione.

Errori riscontrati:
- Riga 9: `nazione = input("Italia ")`
  - Problema: Non chiedi all'utente di inserire una nazione, hai messo "Italia" come messaggio di input
  - Cosa dovevi scrivere: `nazione = input("Inserisci il nome di una nazione: ")`

- Riga 12: `luogo = Output= "Vivo a Roma =+ " " Roma + Italia "`
  - Problema: Sintassi completamente errata, `Output=` non è valido, uso errato di `=+`, stringhe non concatenate correttamente
  - Cosa dovevi scrivere: `luogo = "Vivo a " + citta + ", " + nazione`

Spiegazione:
La concatenazione in Python richiede l'operatore `+` tra le parti. Devi collegare:
1. La stringa fissa `"Vivo a "`
2. La variabile `citta` (che contiene l'input dell'utente)
3. La stringa fissa `", "`
4. La variabile `nazione` (che contiene l'input dell'utente)

Non devi scrivere i valori letterali "Roma" o "Italia", ma usare le variabili che contengono quello che l'utente ha scritto.

---

## Esercizio 3
Punteggio: 0/5

Obiettivo: Creare una scheda libro concatenando titolo, autore e anno.

Analisi del codice:
Hai raccolto gli input dall'utente, ma non hai usato le variabili per costruire la scheda. Hai scritto valori fissi invece di usare i dati inseriti.

Errori riscontrati:
- Riga 14-18: Gli input sono corretti (con piccoli errori di battitura "Inserisce" invece di "Inserisci")
- Riga 20: `Scheda = Output= "Il signore degli Anelli ,Tolkien , 1954 "`
  - Problema 1: Sintassi errata `Output=` non è valido
  - Problema 2: Hai scritto valori fissi invece di usare le variabili
  - Problema 3: Mancano le etichette "Titolo:", "Autore:", "Anno:"

Cosa dovevi scrivere:
```python
titolo = input("Inserisci il titolo: ")
autore = input("Inserisci l'autore: ")
anno = input("Inserisci l'anno: ")
scheda = "Titolo: " + titolo + ", Autore: " + autore + ", Anno: " + anno
print(scheda)
```

Spiegazione:
Le variabili servono a memorizzare i dati. Una volta che hai chiesto `titolo = input(...)`, quella variabile contiene quello che l'utente ha scritto. Devi usare `titolo`, non scrivere "Il signore degli Anelli" di nuovo. Il programma deve funzionare con QUALSIASI libro inserito dall'utente, non solo con valori fissi.

---

## Esercizio 4
Punteggio: 1/5

Obiettivo: Aggiungere parti a un messaggio usando l'operatore +=.

Analisi del codice:
Hai capito parzialmente l'operatore +=, ma hai fatto un errore critico nella prima aggiunta.

Errori riscontrati:
- Riga 9: `messaggio = " a tutti "`
  - Problema: Hai usato `=` invece di `+=`
  - Questo SOSTITUISCE il contenuto di messaggio invece di aggiungerci qualcosa
  - Risultato: "Buongiorno" viene perso, rimane solo " a tutti "

- Riga 12: `messaggio += "!"` (CORRETTO!)

Cosa dovevi scrivere:
```python
messaggio = "Buongiorno"
messaggio += " a tutti"
messaggio += "!"
print(messaggio)
```

Spiegazione:
L'operatore `+=` significa "aggiungi a quello che c'è già". È come dire: prendi il valore attuale di `messaggio` e aggiungi questa nuova parte.
- `=` SOSTITUISCE il valore (dimentica il vecchio)
- `+=` AGGIUNGE al valore (mantiene il vecchio e aggiunge nuovo)

Se usi `=` invece di `+=`, perdi tutto quello che avevi prima!

---

## Esercizio 5
Punteggio: 0/5

Obiettivo: Costruire un indirizzo email aggiungendo parti con +=.

Analisi del codice:
Hai usato `=` al posto di `+=` in TUTTE le righe. Questo è un errore concettuale grave.

Errori riscontrati:
- Riga 9: `email = "@"` doveva essere `email += "@"`
- Riga 12: `email = "esempio"` doveva essere `email += "esempio"`
- Riga 15: `email = ".com"` doveva essere `email += ".com"`

Risultato del tuo codice: `email` conterrà solo ".com" perché ogni volta hai SOSTITUITO il valore invece di AGGIUNGERE.

Cosa dovevi scrivere:
```python
email = "mario"
email += "@"
email += "esempio"
email += ".com"
print(email)
```

Spiegazione:
Immagina di costruire una torre con i mattoncini:
- `=` significa "butta via la torre e metti solo questo mattoncino"
- `+=` significa "aggiungi questo mattoncino alla torre esistente"

Per costruire "mario@esempio.com" devi AGGIUNGERE ogni pezzo, non sostituirlo ogni volta!

---

## Esercizio 6
Punteggio: 0/5

Obiettivo: Usare l'operatore += per costruire una frase progressivamente.

Analisi del codice:
Anche qui hai usato `=` invece di `+=`, e la sintassi della concatenazione è errata.

Errori riscontrati:
- Riga 15: `frase = " python è " " un linguaggio " " - fantastico "`
  - Problema 1: Hai usato `=` invece di `+=` (sostituisci invece di aggiungere)
  - Problema 2: Hai messo tutte le parti in una sola riga invece di aggiungere progressivamente
  - Problema 3: Hai scritto "python" minuscolo invece di usare il "Python" già nella variabile

Cosa dovevi scrivere:
```python
frase = "Python"
frase += " è"
frase += " un linguaggio"
frase += " fantastico"
print(frase)
```

Spiegazione:
"Progressivamente" significa PASSO dopo PASSO. Devi aggiungere ogni pezzo UNO alla volta usando `+=`, non mettere tutto insieme in una riga. Parti da "Python", poi aggiungi " è", poi aggiungi " un linguaggio", poi aggiungi " fantastico". Ogni aggiunta si costruisce su quella precedente.

---

## Esercizio 7
Punteggio: 0/5

Obiettivo: Calcolare e stampare la lunghezza di una stringa.

Analisi del codice:
Hai frainteso completamente il concetto di `len()`. Hai scritto valori fissi invece di calcolare dinamicamente la lunghezza.

Errori riscontrati:
- Riga 6: `parola = "Peogrammazione "` (errore di battitura: "Programmazione")
- Riga 9: `lunghezza =output= (9)`
  - Problema 1: Sintassi errata `output=` non è valido
  - Problema 2: Hai scritto `9` come valore fisso invece di usare `len(parola)`
  - Problema 3: "Programmazione" ha 14 caratteri, non 9

- Riga 12: `print("La parola ha", 9 , "caratteri")`
  - Problema: Hai scritto `9` fisso invece di usare la variabile `lunghezza`

Cosa dovevi scrivere:
```python
parola = "Programmazione"
lunghezza = len(parola)
print("La parola ha", lunghezza, "caratteri")
```

Spiegazione:
La funzione `len()` CALCOLA automaticamente quanti caratteri ci sono in una stringa. Non devi contare tu manualmente e scrivere il numero! Python lo fa per te. Usi `len(parola)` per dire a Python: "conta i caratteri di questa parola e metti il risultato nella variabile lunghezza". Poi usi la variabile `lunghezza` nel print, così il programma funziona con QUALSIASI parola, non solo "Programmazione".

---

## Esercizio 8
Punteggio: 0/5

Obiettivo: Chiedere una frase all'utente e calcolare quanti caratteri contiene.

Analisi del codice:
Stessi errori dell'esercizio 7: valori fissi invece di calcolo dinamico.

Errori riscontrati:
- Riga 6: `frase = input=("Inserisci una frase: ")`
  - Problema: Sintassi errata, scrivi `frase = input(...)` non `frase = input=(...)`

- Riga 9: `numero_caratteri = output= (10)`
  - Problema: Hai scritto `10` fisso invece di `len(frase)`

- Riga 12: `print("La frase contiene", 10, "caratteri")`
  - Problema: Hai scritto `10` fisso invece di usare `numero_caratteri`

Cosa dovevi scrivere:
```python
frase = input("Inserisci una frase: ")
numero_caratteri = len(frase)
print("La frase contiene", numero_caratteri, "caratteri")
```

Spiegazione:
L'utente può inserire QUALSIASI frase. "Ciao mondo" ha 10 caratteri, ma "Buongiorno" ne ha 10 diversi! Non puoi scrivere un numero fisso. Devi usare `len(frase)` che conta automaticamente i caratteri della frase inserita dall'utente, qualunque essa sia.

---

## Esercizio 9
Punteggio: 0/5

Obiettivo: Calcolare la lunghezza di nome e cognome separatamente.

Analisi del codice:
Hai raccolto gli input ma non hai calcolato le lunghezze correttamente, e il print non usa le variabili.

Errori riscontrati:
- Riga 18: `numero = caratteri = output= (12)`
  - Problema: Sintassi completamente errata
  - Dovevi creare DUE variabili separate: `lunghezza_nome = len(nome)` e `lunghezza_cognome = len(cognome)`

- Riga 20-22: `print("Marco ", "5 ")` e `print("Bianchi ", "7 ", )`
  - Problema: Hai scritto valori fissi invece di usare le variabili
  - Il formato output è sbagliato, mancano le etichette corrette

Cosa dovevi scrivere:
```python
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
lunghezza_nome = len(nome)
lunghezza_cognome = len(cognome)
print("Nome:", nome, ", Lunghezza:", lunghezza_nome)
print("Cognome:", cognome, ", Lunghezza:", lunghezza_cognome)
```

Spiegazione:
Questo esercizio richiede di calcolare DUE lunghezze diverse: una per il nome e una per il cognome. Devi creare due variabili separate e calcolare `len(nome)` e `len(cognome)`. Poi nel print devi mostrare il nome inserito dall'utente (non "Marco" fisso) e la lunghezza calcolata (non "5" fisso). Il programma deve funzionare con QUALSIASI nome e cognome.

---

## Esercizio 10
Punteggio: 4.5/5

Obiettivo: Convertire un nome in maiuscolo.

Analisi del codice:
Ottimo lavoro! Hai usato correttamente il metodo `.upper()`. C'è solo un piccolo dettaglio.

Errore minore:
- Riga 6: `nome = "luca "` (hai aggiunto uno spazio alla fine)
- Doveva essere: `nome = "luca"` (senza spazio)
- L'output sarà "LUCA " invece di "LUCA"

Questo è solo un errore di battitura minore (-0.5 punti). La logica del codice è perfettamente corretta!

---

## Esercizio 11
Punteggio: 5/5

Obiettivo: Convertire una parola in minuscolo.

Analisi del codice:
Perfetto! Hai completato correttamente l'esercizio usando il metodo `.lower()`. Il codice funziona senza errori.

Ottimo lavoro su questo esercizio!

---

## Esercizio 12
Punteggio: 2/5

Obiettivo: Convertire nome in maiuscolo e cognome in minuscolo.

Analisi del codice:
Hai capito come usare `.upper()` e `.lower()` (righe 19-21 corrette), ma l'output è completamente sbagliato.

Errori riscontrati:
- Riga 19-21: `nome_maiuscolo` e `cognome_minuscolo` sono calcolati correttamente! (BENE!)
- Riga 23: `print("mario ")`
  - Problema: Hai scritto "mario" fisso invece di usare `nome_maiuscolo`
- Riga 24: `print("ROSSI ")`
  - Problema: Hai scritto "ROSSI" fisso invece di usare `cognome_minuscolo`
- Inoltre, l'output è AL CONTRARIO (mario minuscolo, ROSSI maiuscolo)
- Mancano le etichette "Nome:" e "Cognome:"

Cosa dovevi scrivere:
```python
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
nome_maiuscolo = nome.upper()
cognome_minuscolo = cognome.lower()
print("Nome:", nome_maiuscolo)
print("Cognome:", cognome_minuscolo)
```

Spiegazione:
Hai fatto la parte difficile correttamente (calcolare le conversioni), ma poi non hai usato le variabili nel print! Hai calcolato `nome_maiuscolo` che contiene il nome in maiuscolo, quindi devi stampare QUELLA variabile, non scrivere "mario" di nuovo. È come preparare una torta e poi non servirla!

---

## Esercizio 13
Punteggio: 2/5

Obiettivo: Confrontare la lunghezza di due parole.

Analisi del codice:
Hai capito la struttura if/else, ma hai usato valori fissi invece di calcolare dinamicamente le lunghezze.

Errori riscontrati:
- Riga 12: `lunghezza1 = len=(4)`
  - Problema: Sintassi errata `len=` e valore fisso `4`
  - Cosa dovevi scrivere: `lunghezza1 = len(parola1)`

- Riga 15: `lunghezza2 = len=(6)`
  - Problema: Sintassi errata `len=` e valore fisso `6`
  - Cosa dovevi scrivere: `lunghezza2 = len(parola2)`

- Riga 18: `if 4 > 6:`
  - Problema: Hai scritto numeri fissi invece di `lunghezza1 > lunghezza2`

- Riga 21: Output dice "La seconda parola è più lunga " ma manca "o uguale"

Cosa dovevi scrivere:
```python
parola1 = input("Inserisci la prima parola: ")
parola2 = input("Inserisci la seconda parola: ")
lunghezza1 = len(parola1)
lunghezza2 = len(parola2)
if lunghezza1 > lunghezza2:
    print("La prima parola è più lunga")
else:
    print("La seconda parola è più lunga o uguale")
```

Spiegazione:
Il confronto deve essere tra le VARIABILI `lunghezza1` e `lunghezza2`, non tra numeri fissi. Python deve decidere in base alle parole inserite dall'utente, non in base a "4" e "6". Se confronti `4 > 6` la risposta sarà sempre False, indipendentemente da cosa scrive l'utente!

---

## Esercizio 14
Punteggio: 0/5

Obiettivo: Verificare se una password ha lunghezza valida (tra 8 e 16 caratteri).

Analisi del codice:
L'esercizio presenta errori logici gravi nella validazione della password.

Errori riscontrati:
- Riga 9: `lunghezza_password = len(3)`
  - Problema: Hai scritto `len(3)` invece di `len(password)`
  - `len(3)` non ha senso, devi calcolare la lunghezza della variabile `password`

- Riga 12-17: La logica delle condizioni è completamente sbagliata
  - Riga 12: `if lunghezza_password > 3:` (doveva essere `< 8`)
  - Riga 14: `if lunghezza_password > 21:` (doveva essere `elif lunghezza_password > 16:`)
  - Riga 16: `if lunghezza_password < 9:` (doveva essere `else:`)
  - Hai usato `if` tre volte invece di `if/elif/else`

Cosa dovevi scrivere:
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

Spiegazione:
La password deve essere tra 8 e 16 caratteri:
- Se è MINORE di 8 → troppo corta
- Se è MAGGIORE di 16 → troppo lunga
- Altrimenti (tra 8 e 16) → valida

Devi usare `elif` (non `if` di nuovo) per evitare che Python controlli tutte le condizioni anche quando una è già vera. E devi usare `else` per il caso "tutto ok", non un altro `if`.

---

## Esercizio 15
Punteggio: 0/5

Obiettivo: Validare un codice usando .strip() e confronto.

Analisi del codice:
L'esercizio non è stato compreso. Hai scritto due blocchi separati con valori fissi invece di usare la logica if/else.

Errori riscontrati:
- Riga 16: `codice = strip=("ABC123")`
  - Problema: Sintassi errata, `strip=` non esiste
  - Cosa dovevi scrivere: `codice_pulito = codice.strip()`

- Riga 14-18 e 20-24: Hai scritto DUE blocchi separati con input diversi
  - Problema: Dovevi chiedere l'input UNA sola volta e usare if/else per decidere cosa stampare

Cosa dovevi scrivere:
```python
codice = input("Inserisci il codice: ")
codice_pulito = codice.strip()
if codice_pulito == "ABC123":
    print("Codice corretto")
else:
    print("Codice errato")
```

Spiegazione:
Il metodo `.strip()` rimuove gli spazi all'inizio e alla fine di una stringa. Serve per "pulire" l'input dell'utente. Ad esempio, se l'utente scrive "  ABC123  " (con spazi), `.strip()` lo trasforma in "ABC123". Poi confronti il codice pulito con "ABC123": se sono uguali stampi "Codice corretto", altrimenti "Codice errato". NON devi chiedere l'input due volte!

---

## Esercizio 16
Punteggio: 2/5

Obiettivo: Verificare un username ignorando spazi e maiuscole/minuscole.

Analisi del codice:
Hai capito `.strip()` e `.lower()` (righe 9-12 corrette), ma la logica if è completamente sbagliata.

Errori riscontrati:
- Riga 9-12: `.strip()` e `.lower()` usati CORRETTAMENTE! (BRAVO!)
- Riga 15: `if input > "admin ":`
  - Problema 1: `input` è una funzione, non la variabile (devi usare `username_pulito`)
  - Problema 2: Hai usato `>` invece di `==` (confronto di uguaglianza)
  - Problema 3: Non serve lo spazio in "admin " perché hai già fatto `.strip()`

- Riga 17: `if input <"ADMIN ":`
  - Stessi problemi della riga 15

Cosa dovevi scrivere:
```python
username = input("Inserisci lo username: ")
username_pulito = username.strip()
username_pulito = username_pulito.lower()
if username_pulito == "admin":
    print("Accesso consentito")
else:
    print("Accesso negato")
```

Spiegazione:
Hai preparato correttamente `username_pulito` (pulito e minuscolo), ma poi non l'hai usato nel confronto! Devi verificare se `username_pulito` è UGUALE (`==`) a "admin". L'operatore `>` serve per confrontare quale è maggiore/minore (es. numeri o ordine alfabetico), non per vedere se due stringhe sono uguali. E `input` è il nome della funzione, mentre la TUA variabile si chiama `username_pulito`.

---

## Esercizio 17
Punteggio: 1/5

Obiettivo: Verificare se la parola "python" è contenuta in una frase.

Analisi del codice:
Hai preparato correttamente la frase in minuscolo, ma la condizione if è incompleta.

Errori riscontrati:
- Riga 9: `frase_minuscola = frase.lower()` (CORRETTO!)
- Riga 12: `if "python" :`
  - Problema: Condizione incompleta, manca `in frase_minuscola`
  - Così com'è, Python valuta solo se la stringa "python" esiste (sempre True), non se è contenuta nella frase

Cosa dovevi scrivere:
```python
frase = input("Inserisci una frase: ")
frase_minuscola = frase.lower()
if "python" in frase_minuscola:
    print("Python trovato!")
else:
    print("Python non trovato")
```

Spiegazione:
L'operatore `in` verifica se una stringa è contenuta dentro un'altra. Devi scrivere `"python" in frase_minuscola` che significa "la parola python è contenuta nella frase?". Se scrivi solo `if "python":` senza il `in`, Python controlla solo se la stringa "python" esiste (e esiste sempre!), non se è nella frase dell'utente. È come chiedere "esiste la parola python nel vocabolario?" invece di "la parola python è in questa frase specifica?".

---

## Esercizio 18
Punteggio: 0/5

Obiettivo: Contare quante volte appare la lettera 'a' in una frase e verificare se sono più di 3.

Analisi del codice:
Esercizio non completato. Hai iniziato convertendo in minuscolo, ma manca tutto il resto.

Errori riscontrati:
- Riga 9-12: Il blocco di output atteso è stato modificato/cancellato
- Riga 18-20: Hai solo raccolto l'input e convertito in minuscolo
- Manca: il conteggio con `.count('a')`
- Manca: il print con "La lettera 'a' appare [numero] volte"
- Manca: l'if per verificare se >3 volte

Cosa dovevi scrivere:
```python
frase = input("Inserisci una frase: ")
frase_minuscola = frase.lower()
numero_a = frase_minuscola.count('a')
print("La lettera 'a' appare", numero_a, "volte")
if numero_a > 3:
    print("Ci sono molte 'a'!")
else:
    print("Ci sono poche 'a'")
```

Spiegazione:
Il metodo `.count('a')` conta automaticamente quante volte la lettera 'a' appare nella stringa. Devi salvare questo numero in una variabile, stamparlo, e poi usare un if per verificare se è maggiore di 3. Hai fatto solo il primo passo (conversione in minuscolo), ma manca tutto il resto dell'esercizio.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Validare un URL verificando che inizi con "http://" o "https://" e finisca con ".com" o ".it".

Analisi del codice:
Esercizio non svolto. Il file contiene solo il testo della traccia.

Cosa dovevi scrivere:
```python
url = input("Inserisci un URL: ")

# Verifica inizio
inizia_ok = url.startswith("http://") or url.startswith("https://")

# Verifica fine
finisce_ok = url.endswith(".com") or url.endswith(".it")

# Verifica entrambe le condizioni
if inizia_ok and finisce_ok:
    print("URL valido")
else:
    print("URL non valido")
```

Spiegazione:
Questo esercizio richiede di usare due metodi:
- `.startswith()` verifica se una stringa INIZIA con un certo prefisso
- `.endswith()` verifica se una stringa FINISCE con un certo suffisso

Devi controllare ENTRAMBE le condizioni (inizio E fine) usando `and`. Solo se entrambe sono vere l'URL è valido.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Validare un indirizzo email verificando simbolo '@', lunghezza minima 5, e finale '.com' o '.it'.

Analisi del codice:
Esercizio non svolto. Il file contiene solo il testo della traccia.

Cosa dovevi scrivere:
```python
email = input("Inserisci un indirizzo email: ")
email_pulita = email.strip().lower()

contiene_chiocciola = "@" in email_pulita
lunghezza_ok = len(email_pulita) >= 5
finisce_ok = email_pulita.endswith(".com") or email_pulita.endswith(".it")

if contiene_chiocciola and lunghezza_ok and finisce_ok:
    print("Email valida")
else:
    print("Email non valida")
```

Spiegazione:
Questo è l'esercizio più complesso perché richiede di verificare TRE condizioni contemporaneamente:
1. Contiene '@' (usando `in`)
2. Ha almeno 5 caratteri (usando `len()` e `>=`)
3. Finisce con '.com' o '.it' (usando `.endswith()`)

Solo se TUTTE e TRE le condizioni sono vere (collegate con `and`), l'email è valida. Prima di tutto questo, devi pulire l'email con `.strip()` (rimuove spazi) e `.lower()` (converte in minuscolo) per rendere il controllo più affidabile.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Hai capito correttamente i metodi `.upper()` e `.lower()` (esercizi 10, 11)
- Sei riuscito a completare alcuni esercizi guidati base
- Mostri comprensione della struttura if/else in alcuni casi

Aree da migliorare (CRITICHE):
1. **Operatore += vs =**: Devi capire la differenza fondamentale tra sostituire (`=`) e aggiungere (`+=`)
2. **Uso delle variabili**: Non devi scrivere valori fissi quando hai variabili. Se hai calcolato `lunghezza = len(parola)`, usa `lunghezza`, non scrivere `9`
3. **Funzione len()**: Serve a CALCOLARE automaticamente, non a contenere numeri fissi
4. **Operatore in**: Devi completare la condizione con `"testo" in variabile`, non solo `"testo"`
5. **Sintassi corretta**: Troppi errori di sintassi come `output=`, `len=`, `input=` che bloccano l'esecuzione
6. **Logica if/elif/else**: Devi usare la sequenza corretta, non tre `if` separati
7. **Operatori di confronto**: `==` per uguaglianza, non `>` o `<` quando non servono

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 2** (concatenazione con input) - CRITICO
- **Esercizio 3** (uso variabili invece di valori fissi) - CRITICO
- **Esercizio 4** (operatore +=) - CRITICO
- **Esercizio 5** (operatore +=) - CRITICO
- **Esercizio 6** (operatore += progressivo) - CRITICO
- **Esercizio 7** (funzione len()) - CRITICO
- **Esercizio 8** (funzione len() con input) - CRITICO
- **Esercizio 9** (len() multiplo e formato output) - CRITICO
- **Esercizio 13** (len() e confronto dinamico) - CRITICO
- **Esercizio 14** (logica if/elif/else) - CRITICO
- **Esercizio 15** (metodo .strip() e validazione) - CRITICO
- **Esercizio 16** (confronto con ==) - CRITICO
- **Esercizio 17** (operatore in completo) - CRITICO
- **Esercizio 18** (metodo .count() e logica completa) - NON SVOLTO
- **Esercizio 19** (metodi .startswith() e .endswith()) - NON SVOLTO
- **Esercizio 20** (validazione multipla complessa) - NON SVOLTO

Valutazione generale:
Il punteggio di 25/100 indica lacune molto gravi nella comprensione dei concetti fondamentali sulle stringhe. Gli errori principali sono:

1. **Confusione tra valori fissi e calcolo dinamico**: Scrivi numeri fissi (es. `9`) invece di usare funzioni che calcolano (es. `len(parola)`). Questo significa che non hai capito che un programma deve funzionare con QUALSIASI input, non solo con i valori dell'esempio.

2. **Mancata comprensione dell'operatore +=**: Usi `=` (sostituisci) invece di `+=` (aggiungi), perdendo i dati precedenti. Questo è un concetto fondamentale che devi assolutamente padroneggiare.

3. **Non usi le variabili che hai creato**: Calcoli correttamente le conversioni (es. `nome_maiuscolo`), ma poi non le usi nel print. È come cucinare un piatto e poi buttarlo via!

4. **Errori di sintassi gravi**: Costrutti come `output=`, `len=`, `input=` non esistono in Python e causano errori bloccanti.

5. **Esercizi non completati**: Gli ultimi 3 esercizi (18, 19, 20) sono i più importanti per il riepilogo, ma non sono stati svolti.

**Raccomandazione urgente**: Devi rivedere TUTTO il materiale sulle stringhe partendo dalle basi. In particolare:
- Rileggi la teoria sulla differenza tra `=` e `+=`
- Rivedi come funziona `len()` e perché restituisce un valore che va salvato in una variabile
- Esercitati a usare le variabili invece di scrivere valori fissi
- Studia gli operatori `in`, `==`, e la logica `if/elif/else`
- Pratica i metodi delle stringhe: `.strip()`, `.upper()`, `.lower()`, `.count()`, `.startswith()`, `.endswith()`

Non puoi progredire agli argomenti successivi senza aver consolidato questi concetti base. Ti consiglio di rifare TUTTI gli esercizi seguendo attentamente le soluzioni corrette fornite in questa correzione, e di chiedere aiuto al docente per chiarire i dubbi.

Devi acquisire la mentalità che un programma deve funzionare con QUALSIASI dato inserito dall'utente, non solo con valori fissi degli esempi. Questo è il concetto più importante della programmazione.
