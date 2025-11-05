# Correzione Verifica Funzioni Base - Bortolozzo Manuel

Punteggio Totale: 50/100

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
Punteggio: 4/5

Obiettivo: Menu con funzioni e logica condizionale.

Analisi del codice:
Hai completato l'esercizio correttamente e il programma funziona. Hai definito tutte le funzioni e implementato la logica condizionale.

Nota:
Ci sono alcuni piccoli errori di ortografia nell'output:
- Riga 12: hai scritto "1.visualizza prodotti" (manca lo spazio dopo il punto)
- Riga 13: hai scritto "2. aggiungi" (minuscolo invece di maiuscolo)
- Riga 14: hai scritto "3. esci" (minuscolo invece di maiuscolo)
- Riga 20: hai scritto "proditti" invece di "Prodotti" e tutto in minuscolo

Questi sono errori minori di formattazione che non compromettono la funzionalita, ma e importante prestare attenzione ai dettagli.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Riepilogo funzioni senza parametri - programma cinema.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte e quattro le funzioni richieste e le hai chiamate correttamente nel programma principale. Il codice e ben strutturato.

---

## Esercizio 5
Punteggio: 5/5

Obiettivo: Funzioni con un parametro.

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente le funzioni con un parametro, implementato i calcoli richiesti e chiamato le funzioni passando i parametri corretti.

---

## Esercizio 6
Punteggio: 1/5

Obiettivo: Funzioni con parametro e calcoli.

Analisi del codice:
Hai tentato di completare l'esercizio ma c'e un errore CRITICO che impedisce al codice di funzionare.

Errore riscontrato:
- Riga 10: Cosa hai scritto: `def calcola_area_quadrato(area):`
- Problema: Il parametro della funzione si chiama `area` ma dovrebbe chiamarsi `lato`
- Riga 11: Usi la variabile `lato` che non esiste come parametro

Codice errato:
```python
def calcola_area_quadrato(area):
    area = lato * lato  # ERRORE: 'lato' non e definito!
    print("L'area del quadrato è:", area)
```

Codice corretto:
```python
def calcola_area_quadrato(lato):
    area = lato * lato
    print("L'area del quadrato è:", area)
```

Spiegazione:
I parametri di una funzione sono come delle "scatole" in cui metti i valori quando chiami la funzione. Se chiami la funzione con `calcola_area_quadrato(lato)` (riga 27), devi avere un parametro chiamato `lato` nella definizione della funzione. Alla riga 10 hai chiamato il parametro `area`, ma poi alla riga 11 usi `lato` che non esiste, quindi Python da errore: "NameError: name 'lato' is not defined".

Nota positiva: La seconda funzione `converti_euro_dollari` e corretta.

---

## Esercizio 7
Punteggio: 4/5

Obiettivo: Funzioni con logica condizionale.

Analisi del codice:
Hai completato l'esercizio e il codice funziona correttamente. Hai implementato bene la logica condizionale con if/else e if/elif/else.

Nota:
- Riga 25: hai scritto `print ("temperatura_piacevole")` invece di `print("Temperatura piacevole")`. Hai usato underscore e minuscole invece del testo richiesto. Il codice funziona ma non segue esattamente la traccia.
- L'indentazione alla riga 27-28 e un po' irregolare ma non compromette il funzionamento.

---

## Esercizio 8
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con un parametro - gestione abbonamenti palestra.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia.

Cosa dovevi fare:
Definire tre funzioni:
1. stampa_nome_abbonato(nome) - che stampa il nome dell'abbonato
2. calcola_costo_mensile(ore_settimanali) - che calcola e stampa il costo (ore * 15)
3. verifica_livello(anni_esperienza) - che verifica e stampa il livello in base agli anni

E scrivere il programma principale che chiede i dati all'utente e chiama tutte e tre le funzioni.

Questo era un esercizio di riepilogo importante che mette insieme i concetti degli esercizi 5, 6 e 7.

---

## Esercizio 9
Punteggio: 5/5

Obiettivo: Funzioni con due parametri.

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente le funzioni con due parametri e le hai chiamate passando i parametri nel modo giusto.

---

## Esercizio 10
Punteggio: 5/5

Obiettivo: Funzioni con tre parametri.

Analisi del codice:
Esercizio completato perfettamente. Hai gestito correttamente le funzioni con tre parametri, implementando sia i calcoli (media) che l'output formattato.

---

## Esercizio 11
Punteggio: 5/5

Obiettivo: Funzioni con parametri e calcoli.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente entrambe le formule matematiche richieste (perimetro rettangolo e totale con IVA).

---

## Esercizio 12
Punteggio: 4/5

Obiettivo: Funzioni con parametri e logica.

Analisi del codice:
Hai completato l'esercizio e il codice funziona correttamente. La prima funzione `verifica_login` e perfetta.

Nota sulla seconda funzione:
- Riga 23: hai scritto correttamente `print(f"{a} e maggiore di {b}")`
- Riga 25: hai scritto `print(f"{b} e maggiore di {a}")` invece di `print(f"{a} e minore di {b}")`

Spiegazione:
Le due frasi sono logicamente equivalenti (dire "B e maggiore di A" e lo stesso che dire "A e minore di B"), quindi il programma funziona. Pero la traccia richiedeva specificatamente di scrivere "[a] e minore di [b]". In futuro, quando completi un esercizio, segui esattamente le indicazioni della traccia anche se ci sono modi alternativi corretti.

---

## Esercizio 13
Punteggio: 0/5

Obiettivo: Funzioni con piu parametri e calcoli complessi.

Analisi del codice:
L'esercizio non e stato completato. Tutti gli spazi vuoti (___) sono rimasti invariati.

Cosa dovevi fare:
1. Definire la funzione `calcola_tempo_viaggio(distanza, velocita)` con formula: tempo = distanza / velocita
2. Definire la funzione `calcola_calorie(peso, minuti)` con formula: calorie = peso * minuti * 0.05
3. Chiamare entrambe le funzioni nel programma principale

---

## Esercizio 14
Punteggio: 0/5

Obiettivo: Funzioni con validazione.

Analisi del codice:
L'esercizio non e stato completato. Tutti gli spazi vuoti (___) sono rimasti invariati.

Cosa dovevi fare:
1. Definire la funzione `valida_voto(voto)` con if/else per verificare se promosso o bocciato
2. Definire la funzione `calcola_sconto_eta(prezzo, eta)` con if/elif/else per applicare sconti diversi in base all'eta
3. Chiamare entrambe le funzioni nel programma principale

Questo esercizio e importante perche combina funzioni, parametri e logica condizionale.

---

## Esercizio 15
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con parametri multipli - negozio online.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia.

Cosa dovevi fare:
Creare un programma completo per un negozio online con:
1. stampa_ordine(cliente, prodotto, quantita)
2. calcola_totale(prezzo, quantita, sconto)
3. verifica_disponibilita(quantita_richiesta, quantita_magazzino)

E scrivere il programma principale che chiede tutti i dati all'utente e chiama tutte le funzioni.

Questo e un esercizio di riepilogo molto importante che mette insieme tutti i concetti visti finora (funzioni con parametri multipli, calcoli, logica condizionale).

---

## Esercizio 16
Punteggio: 0/5

Obiettivo: Funzioni che restituiscono un valore con return.

Analisi del codice:
L'esercizio non e stato completato. Tutti gli spazi vuoti (___) sono rimasti invariati.

Cosa dovevi fare:
1. Definire la funzione `calcola_triplo(numero)` che RESTITUISCE (con return) il triplo
2. Definire la funzione `unisci_nomi(nome, cognome)` che RESTITUISCE il nome completo
3. Chiamare le funzioni e salvare i risultati in variabili prima di stamparli

Spiegazione del concetto di return:
```python
def calcola_triplo(numero):
    triplo = numero * 3
    return triplo  # RESTITUISCE il valore

# Nel programma principale:
risultato = calcola_triplo(5)  # risultato diventa 15
print(risultato)  # Stampa 15
```

Il `return` e diverso dal `print`:
- `print()` → mostra qualcosa sullo schermo
- `return` → restituisce un valore che puoi salvare e usare

---

## Esercizio 17
Punteggio: 0/5

Obiettivo: Usare i valori restituiti dalle funzioni.

Analisi del codice:
L'esercizio non e stato completato. Tutti gli spazi vuoti (___) sono rimasti invariati.

Cosa dovevi fare:
1. Definire la funzione `calcola_area_cerchio(raggio)` che restituisce l'area
2. Definire la funzione `converti_minuti_ore(minuti)` che restituisce le ore
3. Chiamare le funzioni, salvare i risultati in variabili e usarli per stampare messaggi

---

## Esercizio 18
Punteggio: 0/5

Obiettivo: Return con logica condizionale.

Analisi del codice:
L'esercizio non e stato completato. Tutti gli spazi vuoti (___) sono rimasti invariati.

Cosa dovevi fare:
1. Definire la funzione `trova_massimo(a, b)` che restituisce il numero piu grande
2. Definire la funzione `controlla_password(password)` che restituisce un messaggio in base alla lunghezza
3. Usare i valori restituiti nel programma principale

Questo esercizio combina `return` con `if/else`, un concetto molto importante.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Usare return in calcoli complessi.

Analisi del codice:
L'esercizio non e stato completato. Tutti gli spazi vuoti (___) sono rimasti invariati.

Cosa dovevi fare:
1. Definire la funzione `calcola_prezzo_finale(prezzo, sconto)` con formula complessa e return
2. Definire la funzione `calcola_imc(peso, altezza)` con formula IMC e return
3. Usare i valori restituiti nel programma principale

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con return - statistiche gioco.

Analisi del codice:
L'esercizio non e stato svolto. Il file e identico alla traccia.

Cosa dovevi fare:
Creare un programma completo per calcolare statistiche di un gioco:
1. calcola_punteggio_totale(livello1, livello2, livello3) - restituisce la somma
2. calcola_media_punteggi(totale, numero_livelli) - restituisce la media
3. verifica_vittoria(punteggio_totale) - restituisce un messaggio

E scrivere il programma principale che chiama tutte le funzioni, salva i risultati e li stampa.

Questo e l'esercizio di riepilogo finale piu importante che unisce tutti i concetti della verifica: funzioni, parametri multipli, return, calcoli e logica condizionale.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione delle funzioni senza parametri (esercizi 1, 2, 4)
- Buona comprensione delle funzioni con parametri (esercizi 5, 9, 10, 11)
- Buona implementazione della logica condizionale (esercizi 3, 7, 12)
- I primi 12 esercizi mostrano una comprensione solida dei concetti base

Aree da migliorare:

1. **Attenzione ai parametri delle funzioni (CRITICO):**
   - Esercizio 6: hai confuso il nome del parametro causando un errore grave
   - Ricorda: il nome del parametro nella definizione deve corrispondere a quello che usi nel corpo della funzione
   - Esempio CORRETTO: `def funzione(x):` e poi usi `x` nel corpo, NON un'altra variabile

2. **Concetto di return (FONDAMENTALE):**
   - Non hai completato NESSUNO degli esercizi 16-20 che riguardano il `return`
   - Il `return` e un concetto ESSENZIALE per continuare a programmare
   - Senza capire il `return` non puoi scrivere funzioni che restituiscono valori

3. **Completare tutti gli esercizi:**
   - Hai completato solo 12 esercizi su 20
   - Gli esercizi di riepilogo (8, 15, 20) sono particolarmente importanti
   - Gli esercizi 13-20 coprono concetti avanzati che devi assolutamente imparare

4. **Attenzione ai dettagli:**
   - Esercizio 3: errori di ortografia nell'output
   - Esercizio 7: formato output diverso dalla traccia
   - Esercizio 12: messaggio corretto logicamente ma diverso dalla traccia

Esercizi da rifare OBBLIGATORIAMENTE:

**PRIORITA MASSIMA (errori critici o concetti fondamentali):**
- **Esercizio 6:** Correggere l'errore del parametro (lato vs area)
- **Esercizio 16:** Introduzione al return - FONDAMENTALE
- **Esercizio 17:** Usare valori restituiti - FONDAMENTALE
- **Esercizio 18:** Return con logica - FONDAMENTALE

**ALTA PRIORITA (esercizi di riepilogo e avanzati):**
- **Esercizio 8:** Riepilogo parametri
- **Esercizio 13:** Calcoli complessi
- **Esercizio 14:** Validazione
- **Esercizio 15:** Riepilogo parametri multipli
- **Esercizio 19:** Return con calcoli complessi
- **Esercizio 20:** Riepilogo finale con return

**BASSA PRIORITA (miglioramenti minori):**
- **Esercizio 3:** Correggere ortografia output
- **Esercizio 7:** Usare formato output corretto
- **Esercizio 12:** Seguire esattamente la traccia nei messaggi

Valutazione generale:
Hai dimostrato una buona comprensione dei concetti base delle funzioni Python (definizione, chiamata, parametri). I tuoi punti di forza sono negli esercizi 1-12, dove hai mostrato capacita solide. Tuttavia, hai due problemi principali:

1. **Errore critico nell'esercizio 6**: confondere i parametri e un errore grave che blocca l'esecuzione. Devi prestare molta attenzione ai nomi dei parametri.

2. **Mancanza completa del concetto di return**: non hai completato nessuno degli esercizi 16-20. Il `return` e un concetto FONDAMENTALE per la programmazione. Senza capirlo, non puoi progredire.

Cosa fare ora:

1. **Correggi immediatamente l'esercizio 6** - capire l'errore dei parametri e cruciale
2. **Studia il concetto di return** - chiedi spiegazioni al docente, guarda esempi
3. **Completa gli esercizi 16-20** - dedica tempo a questi esercizi, sono la base per tutto il resto
4. **Fai gli esercizi di riepilogo** - esercizi 8, 15, 20 sono essenziali per consolidare

Concetto chiave da studiare - Il Return:

```python
# Senza return (stampa solo):
def calcola_doppio_stampa(numero):
    risultato = numero * 2
    print(risultato)  # Stampa ma NON restituisce

calcola_doppio_stampa(5)  # Stampa: 10
x = calcola_doppio_stampa(5)  # x diventa None!

# Con return (restituisce il valore):
def calcola_doppio_return(numero):
    risultato = numero * 2
    return risultato  # RESTITUISCE il valore

x = calcola_doppio_return(5)  # x diventa 10
print(x * 3)  # Puoi usare il valore restituito: stampa 30
```

La differenza:
- `print()` → mostra sullo schermo (per l'utente)
- `return` → restituisce un valore (per il programma)

Hai fatto un miglioramento significativo rispetto alla prima consegna (dove avevi 0/100). Ora hai 48/100, che mostra che stai imparando i concetti base. Concentrati sul `return` e sugli esercizi rimanenti per migliorare ulteriormente.
