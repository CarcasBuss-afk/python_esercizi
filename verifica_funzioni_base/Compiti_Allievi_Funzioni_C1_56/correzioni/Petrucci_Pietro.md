# Correzione Verifica Funzioni Base - Petrucci Pietro

Punteggio Totale: 80/100

---

## Esercizio 1
Punteggio: 5/5

Obiettivo: Creare e chiamare funzioni senza parametri (mostra_benvenuto e mostra_orari).

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente entrambe le funzioni e le hai chiamate nel programma principale.

---

## Esercizio 2
Punteggio: 5/5

Obiettivo: Creare funzioni e richiamarle multiple volte (stampa_separatore e stampa_titolo_corso).

Analisi del codice:
Esercizio completato perfettamente. Hai definito correttamente le funzioni e le hai chiamate tutte e tre nel programma principale.

---

## Esercizio 3
Punteggio: 5/5

Obiettivo: Menu con funzioni e logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte le funzioni, implementato la logica condizionale con if/elif/else e chiamato le funzioni nel modo giusto.

---

## Esercizio 4
Punteggio: 5/5

Obiettivo: Riepilogo funzioni senza parametri - programma cinema.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte le funzioni richieste e le hai chiamate nel programma principale.

---

## Esercizio 5
Punteggio: 5/5

Obiettivo: Funzioni con un parametro.

Analisi del codice:
Esercizio completato correttamente. Hai definito entrambe le funzioni con parametri e le hai chiamate correttamente.

Nota: Hai usato f-string insieme a virgole nel print (es. `print(f"Ciao", nome_utente, ...)`), che è una sintassi mista ma funzionante. In futuro, scegli uno stile coerente: o f-string puro (`print(f"Ciao {nome_utente}...")`) o print con virgole senza f.

---

## Esercizio 6
Punteggio: 5/5

Obiettivo: Funzioni con parametro e calcoli.

Analisi del codice:
Esercizio completato correttamente. Hai implementato correttamente le formule e le funzioni.

Nota: Alla riga 29 hai chiamato la variabile `dollari` invece di `euro`, ma il valore passato è comunque corretto. È solo una scelta di naming non ottimale ma non causa errori.

---

## Esercizio 7
Punteggio: 5/5

Obiettivo: Funzioni con logica condizionale.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica condizionale con if/else e if/elif/else.

---

## Esercizio 8
Punteggio: 5/5

Obiettivo: Riepilogo funzioni con un parametro - gestione abbonamenti palestra.

Analisi del codice:
Esercizio completato perfettamente. Hai definito tutte le funzioni richieste, implementato la logica condizionale e scritto il programma principale completo che chiama tutte le funzioni.

---

## Esercizio 9
Punteggio: 5/5

Obiettivo: Funzioni con due parametri.

Analisi del codice:
Esercizio completato correttamente. Hai definito e chiamato correttamente le funzioni con due parametri.

Nota minore: Ci sono alcune virgole extra nell'output (es. `"Corso:, {corso}"`), ma non compromettono la funzionalità del programma.

---

## Esercizio 10
Punteggio: 5/5

Obiettivo: Funzioni con tre parametri.

Analisi del codice:
Esercizio completato correttamente. Hai gestito correttamente le funzioni con tre parametri e le chiamate.

Nota minore: Ci sono virgole extra nell'output della funzione stampa_prodotto, ma il programma funziona correttamente.

---

## Esercizio 11
Punteggio: 0/5

Obiettivo: Funzioni con parametri e calcoli.

Analisi del codice:
La prima funzione (calcola_perimetro_rettangolo) è corretta. La seconda funzione contiene un errore matematico grave.

Errore riscontrato:
```python
# Riga 19
totale = (prezzo * iva / 100)
```

Problema: Questa formula calcola SOLO l'importo dell'IVA, non il totale con IVA. Manca la somma del prezzo iniziale.

Cosa dovevi scrivere:
```python
totale = prezzo + (prezzo * iva / 100)
```

Spiegazione: Il totale con IVA è il prezzo originale PIÙ l'IVA aggiunta. La tua formula calcola solo la percentuale di IVA, ma non la somma al prezzo base.

Esempio:
- Prezzo: 100€, IVA: 22%
- Tua formula: 100 * 22 / 100 = 22€ ✗ (solo l'IVA)
- Formula corretta: 100 + (100 * 22 / 100) = 122€ ✓ (prezzo + IVA)

---

## Esercizio 12
Punteggio: 5/5

Obiettivo: Funzioni con parametri e logica.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente la logica condizionale con AND e i confronti tra numeri.

---

## Esercizio 13
Punteggio: 5/5

Obiettivo: Funzioni con più parametri e calcoli complessi.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente entrambe le formule matematiche richieste.

Nota: Hai usato il nome variabile `formula` invece di `calorie` nell'esercizio, ma è solo una scelta di naming e non compromette la funzionalità.

---

## Esercizio 14
Punteggio: 5/5

Obiettivo: Funzioni con validazione.

Analisi del codice:
Esercizio completato correttamente. Hai implementato perfettamente la logica condizionale e i calcoli degli sconti.

Nota: Hai chiamato la funzione `validita_voto` invece di `valida_voto`, ma sei stato coerente (definizione e chiamata usano lo stesso nome), quindi il programma funziona.

---

## Esercizio 15
Punteggio: 5/5

Obiettivo: Riepilogo funzioni con parametri multipli - negozio online.

Analisi del codice:
Esercizio completato perfettamente! Hai definito correttamente tutte e tre le funzioni e scritto un programma principale completo che gestisce tutti gli input e chiama le funzioni nell'ordine corretto.

---

## Esercizio 16
Punteggio: 5/5

Obiettivo: Funzioni che restituiscono un valore con return.

Analisi del codice:
Esercizio completato perfettamente. Hai compreso correttamente l'uso di `return` per restituire valori dalle funzioni e hai salvato i risultati in variabili per usarli successivamente.

---

## Esercizio 17
Punteggio: 5/5

Obiettivo: Usare i valori restituiti dalle funzioni.

Analisi del codice:
Esercizio completato perfettamente. Hai implementato correttamente le funzioni con return e hai usato i valori restituiti nel programma principale.

Nota: Hai usato nomi di variabili diversi da quelli suggeiti (es. `areacerchio` invece di `area`, `minuts` invece di `ore`), ma il programma funziona correttamente.

---

## Esercizio 18
Punteggio: 0/5

Obiettivo: Return con logica condizionale.

Analisi del codice:
Hai tentato l'esercizio ma c'è un errore concettuale grave: le funzioni non usano `return`.

Errori riscontrati:

1. **Funzione trova_massimo - Manca return:**
   ```python
   # Righe 9-13
   def trova_massimo(a, b):
       if a > b:
           print(f"{a} è maggiore di {b}")
       else:
           print(f"{b} è maggiore di {a}")
   ```

   Problema: La funzione usa `print` invece di `return`. La consegna richiedeva di RESTITUIRE il numero maggiore, non di stamparlo.

   Cosa dovevi scrivere:
   ```python
   def trova_massimo(a, b):
       if a > b:
           return a
       else:
           return b
   ```

2. **Funzione controlla_password - Manca return:**
   ```python
   # Righe 19-23
   def controlla_password(password):
       if len(password) >= 8:
           print("Password sicura")
       else:
           print("Password debole")
   ```

   Problema: La funzione usa `print` invece di `return`. Dovrebbe restituire la stringa, non stamparla.

   Cosa dovevi scrivere:
   ```python
   def controlla_password(password):
       if len(password) >= 8:
           return "Password sicura"
       else:
           return "Password debole"
   ```

Conseguenze nel programma principale:
- Riga 29: `massimo = trova_massimo(num1, num2)` - la variabile `massimo` riceve `None` perché la funzione non restituisce nulla
- Riga 32: `sicurezza = controlla_password(pwd)` - la variabile `sicurezza` riceve `None`

Spiegazione concettuale:
Questo è un errore fondamentale sulla differenza tra `print` e `return`:
- **print()**: visualizza un valore sullo schermo
- **return**: restituisce un valore che può essere salvato e riutilizzato

Quando una funzione deve produrre un risultato da usare altrove, DEVE usare `return`. Il `print` è solo per mostrare informazioni all'utente, non per passare dati tra funzioni.

---

## Esercizio 19
Punteggio: 0/5

Obiettivo: Usare return in calcoli complessi.

Analisi del codice:
L'esercizio non è stato completato.

Parti completate:
- Prima funzione: scritta correttamente (calcola_prezzo_finale con return)

Parti mancanti:
- Seconda funzione: riga 20 manca il `return` (rimasto `______ ___`)
- Programma principale: righe 27-34 tutti gli spazi vuoti non completati

Cosa dovevi completare:
```python
def calcola_imc(peso, altezza):
    imc = peso / (altezza * altezza)
    return imc

# Programma principale
prezzo_scontato = calcola_prezzo_finale(prezzo_originale, percentuale_sconto)
print("Prezzo finale: €", prezzo_scontato)

peso_kg = int(input("Peso (kg): "))
altezza_m = float(input("Altezza (m): "))
imc = calcola_imc(peso_kg, altezza_m)
print("Il tuo IMC è:", imc)
```

---

## Esercizio 20
Punteggio: 0/5

Obiettivo: Riepilogo funzioni con return - statistiche gioco.

Analisi del codice:
L'esercizio non è stato svolto. Il file è completamente vuoto.

Cosa dovevi fare:
Definire tre funzioni che usano `return`:
1. calcola_punteggio_totale(livello1, livello2, livello3) - restituisce la somma
2. calcola_media_punteggi(totale, numero_livelli) - restituisce la media
3. verifica_vittoria(punteggio_totale) - restituisce un messaggio

E scrivere il programma principale che chiama tutte le funzioni, salva i risultati restituiti e li stampa.

---

## Riepilogo e Raccomandazioni

Punti di forza:
- Ottima comprensione delle funzioni senza parametri e con parametri (es01-10, 12-17)
- Eccellente gestione della logica condizionale (es03, 07, 08, 12, 14, 15)
- Buona capacità di implementare calcoli matematici nelle funzioni
- Completamento corretto degli esercizi di riepilogo (es04, 08, 15)
- Comprensione corretta del concetto di `return` negli esercizi 16-17

Aree da migliorare:

1. **Formule matematiche (CRITICO):**
   - Es11: Formula incompleta per calcolare totale con IVA
   - Devi prestare più attenzione alla logica matematica delle formule
   - Rileggi attentamente cosa chiede la consegna

2. **Differenza tra print e return (ERRORE CONCETTUALE):**
   - Es18: Hai usato `print` invece di `return`
   - Devi capire quando una funzione deve RESTITUIRE un valore (con return) vs quando deve solo VISUALIZZARLO (con print)
   - Regola: se il valore viene salvato in una variabile o usato in calcoli successivi, serve `return`

3. **Completamento degli esercizi:**
   - Hai lasciato incompleti 2 esercizi (es19 parziale, es20 vuoto)
   - Gli esercizi sul `return` sono fondamentali per progredire

Esercizi da rifare OBBLIGATORIAMENTE:
- **Esercizio 11:** Correggere la formula aggiungendo `prezzo +` prima del calcolo dell'IVA
- **Esercizio 18:** Riscrivere le funzioni usando `return` invece di `print`
- **Esercizi 19-20:** Completare entrambi gli esercizi

Esercizi da studiare come riferimento:
- I tuoi esercizi 16 e 17 sono ottimi esempi di uso corretto del `return`
- Usa questi come modello per capire come deve funzionare il return negli esercizi 18-20

Valutazione generale:
Hai dimostrato una solida comprensione dei concetti base e intermedi delle funzioni Python. I tuoi punti di forza sono la definizione di funzioni con parametri, la logica condizionale e il completamento sistematico degli esercizi fino al 17. Hai compreso correttamente il concetto di `return` negli esercizi 16-17, quindi sai come funziona. L'errore nell'esercizio 18 (uso di print invece di return) sembra essere una distrazione piuttosto che una mancanza di comprensione. L'errore principale è nell'esercizio 11 dove la formula matematica è incompleta - questo richiede più attenzione alla logica del problema. Completando gli ultimi esercizi e correggendo la formula dell'IVA, puoi facilmente raggiungere l'eccellenza.
