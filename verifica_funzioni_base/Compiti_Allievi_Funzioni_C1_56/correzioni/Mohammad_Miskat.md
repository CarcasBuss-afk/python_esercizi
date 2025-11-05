# Correzione Verifica Funzioni Base - Mohammad Miskat

Punteggio Totale: 65/100

---

## Esercizio 1
Punteggio: 5/5

Obiettivo: Creare e chiamare funzioni senza parametri (mostra_benvenuto e mostra_orari).

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente entrambe le funzioni e le hai chiamate nel modo giusto. Ottimo lavoro.

---

## Esercizio 2
Punteggio: 5/5

Obiettivo: Creare funzioni e richiamarle multiple volte (stampa_separatore e stampa_titolo_corso).

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente le funzioni e le hai chiamate tre volte come richiesto. Il programma funziona correttamente.

---

## Esercizio 3
Punteggio: 5/5

Obiettivo: Menu con funzioni e logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte le funzioni richieste, implementato correttamente la logica condizionale con if/elif/else e chiamato le funzioni appropriate. Il codice e ben strutturato.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Riepilogo funzioni senza parametri - programma cinema.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte e quattro le funzioni richieste e le hai chiamate correttamente nel programma principale. Il codice funziona correttamente.

---

## Esercizio 5
Punteggio: 1/5

Obiettivo: Funzioni con un parametro.

Analisi del codice:
Hai completato la struttura dell'esercizio ma ci sono errori CRITICI che impediscono al codice di funzionare correttamente.

Errori riscontrati:

1. **Sintassi errata negli f-string (righe 10 e 18):**
   - Cosa hai scritto (riga 10): `print(f"Ciao", {nome}, ", benvenuto al corso!")`
   - Problema: Hai usato graffe `{}` separate invece di includerle nell'f-string
   - Cosa dovevi scrivere:
   ```python
   print(f"Ciao {nome}, benvenuto al corso!")
   ```
   oppure senza f-string:
   ```python
   print("Ciao", nome, ", benvenuto al corso!")
   ```

   - Riga 18: stesso errore con `{doppio}`

2. **Valore hardcoded invece di variabile (riga 27):**
   - Cosa hai scritto: `numero_int = int(4)`
   - Problema: Hai convertito il numero 4 invece della variabile `numero_utente`
   - Cosa dovevi scrivere:
   ```python
   numero_int = int(numero_utente)
   ```

Spiegazione:
Le f-string in Python funzionano cosi:
```python
# CORRETTO - f-string
nome = "Mario"
print(f"Ciao {nome}!")  # Le graffe devono essere DENTRO l'f-string

# SBAGLIATO - quello che hai fatto tu
print(f"Ciao", {nome}, "!")  # Python interpreta {nome} come un set, non come una variabile
```

---

## Esercizio 6
Punteggio: 1/5

Obiettivo: Funzioni con parametro e calcoli.

Analisi del codice:
Hai completato la struttura dell'esercizio ma ci sono errori CRITICI nella sintassi degli f-string.

Errori riscontrati:

Sintassi errata negli f-string (righe 12 e 20):
- Riga 12: `print(f"L'area del quadrato è:", {area})`
- Riga 20: `print(f"€", {euro}, " corrispondono a $", {dollari})`

Problema: Stai usando le graffe `{}` FUORI dall'f-string, non dentro. Python interpreta `{area}` come un set (tipo di dato), non come una variabile da inserire nella stringa.

Codice corretto:
```python
# Funzione 1:
print(f"L'area del quadrato è: {area}")

# Funzione 2:
print(f"€{euro} corrispondono a ${dollari}")
```

Spiegazione:
Quando usi f-string (con la `f` prima delle virgolette), le variabili devono essere inserite DENTRO la stringa con le graffe. Se invece non usi f-string, usi le virgole per separare le variabili:

```python
# Opzione 1: f-string
print(f"Il risultato e {valore}")

# Opzione 2: senza f-string
print("Il risultato e", valore)

# SBAGLIATO: mix confuso
print(f"Il risultato e", {valore})
```

---

## Esercizio 7
Punteggio: 5/5

Obiettivo: Funzioni con logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica condizionale con if/else e if/elif/else. Entrambe le funzioni funzionano correttamente.

---

## Esercizio 8
Punteggio: 4/5

Obiettivo: Riepilogo funzioni con un parametro - gestione abbonamenti palestra.

Analisi del codice:
Hai completato l'esercizio e il codice funziona. Hai definito tutte e tre le funzioni e scritto il programma principale.

Errore riscontrato:

Riga 29 - Output incompleto nella prima funzione:
- Cosa hai scritto: `print(nome)`
- Cosa dovevi scrivere: `print("Abbonato:", nome)` oppure `print(f"Abbonato: {nome}")`

La traccia richiedeva di stampare "Abbonato: [nome]", non solo il nome. Hai stampato solo il valore del nome senza l'etichetta "Abbonato:".

Nota: La seconda e terza funzione sono corrette. Il programma principale e ben strutturato.

---

## Esercizio 9
Punteggio: 1/5

Obiettivo: Funzioni con due parametri.

Analisi del codice:
Hai completato la struttura dell'esercizio ma ci sono errori CRITICI nella sintassi degli f-string.

Errori riscontrati:

Sintassi errata negli f-string (righe 10 e 17):
- Riga 10: `print(f"Studente:", {nome}, ", Corso:", {corso})`
- Riga 17: `print(f"La somma è:", {risultato})`

Problema: Stesso errore dell'esercizio 5 e 6. Le graffe `{}` devono essere DENTRO l'f-string, non fuori.

Codice corretto:
```python
# Funzione 1:
print(f"Studente: {nome}, Corso: {corso}")

# Funzione 2:
print(f"La somma è: {risultato}")
```

Questo errore si ripete in molti esercizi. E fondamentale che tu capisca la sintassi corretta degli f-string per continuare a programmare in Python.

---

## Esercizio 10
Punteggio: 1/5

Obiettivo: Funzioni con tre parametri.

Analisi del codice:
Hai completato la struttura dell'esercizio ma ci sono errori nella sintassi degli f-string.

Errore riscontrato:

Riga 18 - Sintassi errata nell'f-string:
- Cosa hai scritto: `print(f"Prodotto:", {nome}, ", Prezzo: €", {prezzo}, ", Quantità:", {quantita})`
- Cosa dovevi scrivere:
```python
print(f"Prodotto: {nome}, Prezzo: €{prezzo}, Quantità: {quantita}")
```

Nota positiva: La prima funzione (riga 12) e corretta perche non usa f-string.

---

## Esercizio 11
Punteggio: 4/5

Obiettivo: Funzioni con parametri e calcoli.

Analisi del codice:
Hai completato l'esercizio e le formule matematiche sono corrette.

Errore riscontrato:

Riga 12 - Sintassi errata nell'f-string:
- Cosa hai scritto: `print(f"Il perimetro è:", {perimetro})`
- Cosa dovevi scrivere:
```python
print(f"Il perimetro è: {perimetro}")
```

Nota positiva: La seconda funzione (riga 20) e corretta perche non usa f-string ma stampa diretta con virgole.

---

## Esercizio 12
Punteggio: 4/5

Obiettivo: Funzioni con parametri e logica.

Analisi del codice:
Hai completato l'esercizio e il codice funziona correttamente. La prima funzione e perfetta, la logica condizionale e corretta.

Errore riscontrato:

Riga 25 - Messaggio incompleto:
- Cosa hai scritto: `print(f"{a} minore di {b}")`
- Cosa dovevi scrivere: `print(f"{a} e minore di {b}")`

Manca la parola "e" tra `{a}` e "minore". La frase risulta grammaticalmente scorretta.

---

## Esercizio 13
Punteggio: 1/5

Obiettivo: Funzioni con piu parametri e calcoli complessi.

Analisi del codice:
Hai completato la struttura dell'esercizio e le formule matematiche sono corrette, ma ci sono errori nella sintassi degli f-string.

Errori riscontrati:

Sintassi errata negli f-string (righe 12 e 20):
- Riga 12: `print(f"Tempo di viaggio:", {tempo}, "ore")`
- Riga 20: `print(f"Calorie bruciate:", {calorie})`

Codice corretto:
```python
# Funzione 1:
print(f"Tempo di viaggio: {tempo} ore")

# Funzione 2:
print(f"Calorie bruciate: {calorie}")
```

---

## Esercizio 14
Punteggio: 5/5

Obiettivo: Funzioni con validazione.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente entrambe le funzioni con la logica condizionale if/elif/else e le formule degli sconti.

Nota: Hai chiamato la seconda funzione `calc_sconto_eta` invece di `calcola_sconto_eta`, ma hai mantenuto la coerenza chiamandola con lo stesso nome alla riga 43, quindi il codice funziona. In futuro, cerca di seguire esattamente i nomi richiesti nella traccia.

---

## Esercizio 15
Punteggio: 5/5

Obiettivo: Riepilogo funzioni con parametri multipli - negozio online.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte e tre le funzioni richieste con parametri multipli, implementato la formula per il totale e la logica condizionale per la disponibilita. Il programma principale chiede tutti i dati necessari e chiama le funzioni correttamente.

Ottimo lavoro! In questo esercizio hai usato correttamente gli f-string senza gli errori visti negli esercizi precedenti.

---

## Esercizio 16
Punteggio: 5/5

Obiettivo: Funzioni che restituiscono un valore con return.

Analisi del codice:
Esercizio completato perfettamente. Hai compreso correttamente l'uso di `return` per restituire valori dalle funzioni. Entrambe le funzioni restituiscono i valori corretti e il programma principale salva e usa questi valori correttamente.

---

## Esercizio 17
Punteggio: 4/5

Obiettivo: Usare i valori restituiti dalle funzioni.

Analisi del codice:
Hai completato l'esercizio e il codice funziona correttamente. Hai compreso l'uso del `return` e hai salvato i valori restituiti nelle variabili.

Nota:
Hai usato nomi diversi per le funzioni:
- Traccia richiedeva: `calcola_area_cerchio` → Tu hai scritto: `calcola_area`
- Traccia richiedeva: `converti_minuti_ore` → Tu hai scritto: `converti_numeri`

Il codice funziona perche sei stato coerente (hai chiamato le funzioni con i nomi che hai definito), ma in futuro segui esattamente i nomi richiesti dalla traccia. I nomi delle funzioni dovrebbero essere descrittivi di quello che fanno.

---

## Esercizio 18
Punteggio: 2/5

Obiettivo: Return con logica condizionale.

Analisi del codice:
Hai completato parzialmente l'esercizio ma c'e un errore CONCETTUALE GRAVE nella seconda funzione.

Prima funzione (trova_massimo): CORRETTA - usi correttamente return con if/else.

Seconda funzione - Errore concettuale (righe 19-23):
- Cosa hai scritto:
```python
def controllo_password(password):
    if len(password) >= 8:
        print("Password sicura")
    else:
        print("Password debole")
```

- Problema: Usi `print` invece di `return`. La traccia richiedeva ESPLICITAMENTE di RESTITUIRE il messaggio, non stamparlo.

- Cosa dovevi scrivere:
```python
def controllo_password(password):
    if len(password) >= 8:
        return "Password sicura"
    else:
        return "Password debole"
```

Conseguenza dell'errore:
- Riga 33: `sicurezza = controllo_password(pwd)`
- La variabile `sicurezza` diventa `None` perche la funzione non restituisce nulla
- Riga 34: `print(sicurezza)` stampa `None` invece del messaggio

Spiegazione:
Questo e un errore concettuale importante. Devi capire la differenza tra `print` e `return`:
- `print()` → mostra qualcosa sullo schermo ma NON restituisce nulla alla variabile
- `return` → restituisce un valore che puo essere salvato e usato

Esempio:
```python
# Con print (SBAGLIATO per questo esercizio):
def funzione_print():
    print("Ciao")

x = funzione_print()  # x diventa None, ma "Ciao" appare sullo schermo
print(x)  # Stampa: None

# Con return (CORRETTO):
def funzione_return():
    return "Ciao"

x = funzione_return()  # x diventa "Ciao"
print(x)  # Stampa: Ciao
```

---

## Esercizio 19
Punteggio: 5/5

Obiettivo: Usare return in calcoli complessi.

Analisi del codice:
Esercizio completato correttamente. Hai implementato correttamente entrambe le formule matematiche complesse e usato `return` per restituire i valori calcolati. Il programma principale salva e usa correttamente i valori restituiti.

Nota: Hai chiamato la seconda funzione `calc_imc` invece di `calcola_imc`, ma hai mantenuto la coerenza quindi il codice funziona. In futuro, segui esattamente i nomi richiesti dalla traccia.

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con return - statistiche gioco.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia.

Cosa dovevi fare:
Creare un programma completo per calcolare statistiche di un gioco:
1. `calcola_punteggio_totale(livello1, livello2, livello3)` - restituisce la somma dei tre punteggi
2. `calcola_media_punteggi(totale, numero_livelli)` - restituisce la media
3. `verifica_vittoria(punteggio_totale)` - restituisce "Hai vinto!" se >= 150, altrimenti "Riprova"

E scrivere il programma principale che chiama tutte le funzioni, salva i risultati e li stampa.

Questo era l'esercizio di riepilogo finale molto importante che univa tutti i concetti della verifica: funzioni, parametri multipli, return, calcoli e logica condizionale.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione delle funzioni senza parametri (esercizi 1, 2, 3, 4)
- Buona comprensione del concetto di `return` (esercizi 14, 15, 16, 19)
- Buona implementazione della logica condizionale (esercizi 7, 14, 15)
- Capacita di implementare formule matematiche correttamente
- Hai completato 19 esercizi su 20, mostrando impegno e dedizione

Aree da migliorare:

1. **Sintassi degli f-string (CRITICO - problema ripetuto):**
   - Errore presente in: esercizi 5, 6, 9, 10, 11, 13
   - Hai confuso la sintassi corretta degli f-string
   - Devi scrivere: `print(f"Testo {variabile}")` (graffe DENTRO la stringa)
   - NON: `print(f"Testo", {variabile})` (graffe FUORI)

2. **Concetto print vs return (CRITICO):**
   - Esercizio 18: hai usato `print` quando era richiesto `return`
   - Devi capire: `print` mostra sullo schermo, `return` restituisce un valore utilizzabile

3. **Attenzione ai dettagli:**
   - Esercizio 5: valore hardcoded `int(4)` invece di `int(numero_utente)`
   - Esercizio 8: output incompleto (manca "Abbonato:")
   - Esercizio 12: manca la parola "e" in una frase
   - Esercizi 14, 17, 19: nomi funzioni diversi dalla traccia

4. **Completare tutti gli esercizi:**
   - Esercizio 20 non completato

Esercizi da rifare OBBLIGATORIAMENTE:

**PRIORITA MASSIMA (errori critici che bloccano il funzionamento):**
- **Esercizio 5:** Correggere sintassi f-string e valore hardcoded
- **Esercizio 6:** Correggere sintassi f-string
- **Esercizio 9:** Correggere sintassi f-string
- **Esercizio 10:** Correggere sintassi f-string
- **Esercizio 13:** Correggere sintassi f-string
- **Esercizio 18:** Usare `return` invece di `print` nella seconda funzione

**ALTA PRIORITA:**
- **Esercizio 20:** Completare l'esercizio di riepilogo finale
- **Esercizio 8:** Aggiungere "Abbonato:" nell'output
- **Esercizio 11:** Correggere sintassi f-string
- **Esercizio 12:** Aggiungere "e" nella frase

**MEDIA PRIORITA (miglioramenti minori):**
- **Esercizio 17:** Usare nomi funzioni corretti dalla traccia

Valutazione generale:
Hai dimostrato una buona comprensione generale dei concetti delle funzioni Python. I tuoi punti di forza sono la logica condizionale, le formule matematiche e il concetto di `return`. Tuttavia, hai un problema RIPETUTO con la sintassi degli f-string che ha compromesso 6 esercizi. Questo e un errore tecnico che, una volta compreso, sara facile da correggere.

Concetto chiave da studiare - F-string corrette:

```python
# MODO 1: F-string (CONSIGLIATO)
nome = "Mario"
eta = 25
print(f"Ciao {nome}, hai {eta} anni")  # Graffe DENTRO la stringa

# MODO 2: Print con virgole (ALTERNATIVA)
print("Ciao", nome, ", hai", eta, "anni")  # Senza f, usa virgole

# MODO 3: Concatenazione (SCONSIGLIATO)
print("Ciao " + nome + ", hai " + str(eta) + " anni")

# SBAGLIATO - Quello che hai fatto tu:
print(f"Ciao", {nome}, ", hai", {eta}, "anni")  # Graffe FUORI (errore!)
```

Quando usi `f` prima delle virgolette, tutte le variabili devono essere inserite DENTRO la stringa con `{nomeVariabile}`. Se usi le graffe fuori dalla stringa, Python le interpreta come un set (tipo di dato) e il codice non funziona come previsto.

Cosa fare ora:

1. **Studia la sintassi corretta degli f-string** - questo risolverebbe 6 esercizi
2. **Ripassa il concetto di return vs print** - fondamentale per l'esercizio 18
3. **Rifare gli esercizi con priorita massima** - concentrati sugli errori critici
4. **Completa l'esercizio 20** - e importante per consolidare tutti i concetti

Hai un buon potenziale. Con 65/100 hai dimostrato di aver capito i concetti fondamentali. Correggendo l'errore ripetuto degli f-string, potresti facilmente arrivare a 85-90/100. Continua cosi e presta attenzione ai dettagli tecnici della sintassi Python.
