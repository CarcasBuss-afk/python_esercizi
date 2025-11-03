# LOG PROGETTAZIONE - ESERCIZI FUNZIONI PYTHON

**Data:** 2025-10-28
**Argomento:** Struttura esercizi sulle funzioni Python
**Livelli:** Base (20 esercizi) + Intermedio (30 esercizi)

---

## DECISIONI PRESE

### Struttura generale
- **Livello BASE:** 20 esercizi
- **Livello INTERMEDIO:** 30 esercizi
- **Livello AVANZATO:** NON incluso in questa fase

### Argomenti esclusi (troppo avanzati)
- ❌ Ricorsione
- ❌ Lambda functions
- ❌ *args e **kwargs
- ❌ Higher-order functions
- ❌ Nested functions e closures

### Argomenti inclusi negli INTERMEDI
- ✅ Parametri con valori default
- ✅ Return multiplo (tuple unpacking)
- ✅ Scope delle variabili (locale vs globale)
- ✅ Funzioni che chiamano funzioni (composizione)
- ✅ Validazione input con if/else
- ✅ Funzioni con liste e dizionari
- ✅ Documentazione (docstring)
- ✅ Try/except negli avanzati (intermedi finali)

### Caratteristiche
- **Mix di applicazioni:** matematica + stringhe + logica + gestione dati
- **Type hints:** NO (troppo avanzato)
- **Gestione errori:** Validazione con if/else + try/except solo negli ultimi esercizi intermedi
- **Temi:** Misti (calcoli, gestione dati, validazioni, mini-progetti)

---

## STRUTTURA DETTAGLIATA

### LIVELLO BASE (20 esercizi)

#### Tipologia 1: Definizione e chiamata - Senza parametri (es01-03)
**Concetto:** Sintassi base `def nome():` e chiamata
- es01: Guidato - Prima funzione con print, spiegazione sintassi completa
- es02: Intermedio - Creare 3 funzioni diverse senza aiuto
- es03: Riepilogo - Menu che chiama funzioni diverse

#### Tipologia 2: Funzioni con 1 parametro (es04-06)
**Concetto:** Passare un valore alla funzione
- es04: Guidato - Funzione con parametro, spiegazione parametri
- es05: Intermedio - Calcoli con parametro (quadrato numero)
- es06: Riepilogo - Classificazione dati (età → categoria)

#### Tipologia 3: Funzioni con parametri multipli (es07-09)
**Concetto:** 2-3 parametri, ordine importa
- es07: Guidato - Due parametri, spiegazione ordine
- es08: Intermedio - Calcolo area rettangolo
- es09: Riepilogo - Presentazione completa (nome, età, città)

#### Tipologia 4: Return statement (es10-12)
**Concetto:** Differenza print vs return
- es10: Guidato - Spiegazione return, quando usarlo
- es11: Intermedio - Calcolo con return (sconto)
- es12: Riepilogo - Convertitore valute

#### Tipologia 5: Usare valori ritornati (es13-15)
**Concetto:** Catturare e usare il valore ritornato
- es13: Guidato - `risultato = funzione()`, usare il valore
- es14: Intermedio - Media di 3 numeri
- es15: Riepilogo - Calcolatrice base (4 operazioni)

#### Tipologia 6: Funzioni con stringhe (es16-17)
**Concetto:** Elaborazione stringhe in funzioni
- es16: Guidato - Inversione stringa con return
- es17: Intermedio - Contare vocali

#### Tipologia 7: Riepilogo generale (es18-20)
**Concetto:** Mettere insieme tutti i concetti base
- es18: Validatore password semplice
- es19: Sistema voti (numero → giudizio)
- es20: Calcolatrice IMC (indice massa corporea)

---

### LIVELLO INTERMEDIO (30 esercizi)

#### Tipologia 1: Parametri con valori default (es01-03)
**Concetto:** `def func(param=valore_default):`
- es01: Guidato - Parametri opzionali, spiegazione
- es02: Intermedio - Potenza con esponente default 2
- es03: Riepilogo - Formattatore prezzo (valuta, decimali opzionali)

#### Tipologia 2: Return multiplo (es04-06)
**Concetto:** `return a, b, c` e tuple unpacking
- es04: Guidato - Return multiplo, spiegazione tuple
- es05: Intermedio - Statistiche lista (min, max, media)
- es06: Riepilogo - Analisi stringa completa

#### Tipologia 3: Scope variabili (es07-09)
**Concetto:** Variabili locali vs globali
- es07: Guidato - Scope, spiegazione local/global
- es08: Intermedio - Contatore globale
- es09: Riepilogo - Gioco con punteggio globale

#### Tipologia 4: Funzioni che chiamano funzioni (es10-12)
**Concetto:** Composizione, modularità
- es10: Guidato - Chiamare funzione da altra funzione
- es11: Intermedio - Sistema conversione temperature
- es12: Riepilogo - Calcolatrice con funzioni separate per operazioni

#### Tipologia 5: Validazione input (es13-15)
**Concetto:** Controllo parametri, return True/False
- es13: Guidato - Funzione validazione con if/else
- es14: Intermedio - Validatore email
- es15: Riepilogo - Validatore form completo

#### Tipologia 6: Funzioni con liste (es16-18)
**Concetto:** Elaborare collezioni
- es16: Guidato - Somma, media di lista
- es17: Intermedio - Filtrare lista (pari/dispari)
- es18: Riepilogo - Gestione voti (statistiche complete)

#### Tipologia 7: Funzioni con dizionari (es19-21)
**Concetto:** Creare e manipolare dizionari
- es19: Guidato - Creare dizionario da parametri
- es20: Intermedio - Gestione contatti
- es21: Riepilogo - Inventario prodotti

#### Tipologia 8: Documentazione (es22-24)
**Concetto:** Docstring, buone pratiche
- es22: Guidato - Come scrivere docstring, PEP8
- es23: Intermedio - Funzioni geometriche documentate
- es24: Riepilogo - Libreria stringhe documentata

#### Tipologia 9: Boolean e logica (es25-27)
**Concetto:** Funzioni predicato, return bool
- es25: Guidato - is_pari(), is_positivo()
- es26: Intermedio - Combinare condizioni complesse
- es27: Riepilogo - Sistema accessi multi-step

#### Tipologia 10: Mini-progetti (es28-30)
**Concetto:** Applicazioni complete con multiple funzioni
- es28: Gestione biblioteca (libri, prestiti)
- es29: Rubrica telefonica completa
- es30: Sistema bancario (deposito, prelievo, saldo)

---

## PATTERN DIDATTICO

### Progressione tripla per ogni tipologia:
1. **Guidato (es01, es04, es07, ...):**
   - Spiegazione completa del nuovo concetto
   - Codice quasi completo con pochi spazi
   - Commenti esplicativi

2. **Intermedio (es02, es05, es08, ...):**
   - Applicazione del concetto senza spiegazioni
   - Più spazi vuoti da completare
   - Richiede comprensione autonoma

3. **Riepilogo (es03, es06, es09, ...):**
   - Solo descrizione dello SCOPO
   - Studente scrive tutto da zero
   - Può combinare concetti precedenti

### Complessità crescente:
- **BASE:** Meccanica delle funzioni (sintassi, parametri, return)
- **INTERMEDIO:** Composizione e applicazioni (chiamate multiple, strutture dati)
- **AVANZATO (futuro):** Pattern avanzati (ricorsione, lambda, decoratori)

---

## FILOSOFIA DEGLI ESERCIZI

### Mix bilanciato di applicazioni:
- 30% matematica/calcoli (area, media, conversioni)
- 30% stringhe/testo (validazione, analisi, formattazione)
- 20% logica/controllo (condizioni, classificazioni)
- 20% gestione dati (liste, dizionari, mini-progetti)

### Focus su concetti pratici:
- ✅ Risolvere problemi reali
- ✅ Validazione input
- ✅ Modularità e riuso codice
- ✅ Buone pratiche (documentazione, nomi chiari)

### Evitare:
- ❌ Concetti troppo astratti per principianti
- ❌ Pattern funzionali avanzati
- ❌ Ottimizzazioni premature
- ❌ Teoria eccessiva senza pratica

---

## CONSIDERAZIONI TECNICHE

### Gestione errori:
- **BASE:** Nessuna gestione errori (input sempre valido)
- **INTERMEDIO:** Validazione con if/else
- **INTERMEDIO (ultimi esercizi):** Introduzione try/except per input utente

### Naming conventions:
- Funzioni: `snake_case` (es. `calcola_area`, `is_valido`)
- Parametri: nomi descrittivi (es. `nome`, `eta`, `prezzo`)
- Return: valori significativi

### Testing:
- Ogni esercizio include esempi di test nei commenti
- "Prova con: ..." per guidare lo studente

---

## COLLEGAMENTI CON ESERCIZI STRINGHE

### Riutilizzo concetti:
Gli esercizi funzioni possono **richiamare** concetti degli esercizi stringhe:
- Validazione password (stringhe intermedio + funzioni intermedio)
- Analisi testo (slicing stringhe + funzioni con return multiplo)
- Formattazione (stringhe avanzate + funzioni documentate)

### Progressione naturale:
1. **Stringhe BASE:** Operazioni dirette
2. **Stringhe INTERMEDIO:** Combinazioni e validazioni
3. **Stringhe AVANZATO:** Algoritmi complessi
4. **Funzioni BASE:** Incapsulare operazioni semplici
5. **Funzioni INTERMEDIO:** Incapsulare logica complessa stringhe
6. **Funzioni + Stringhe:** Librerie custom per elaborazione testo

---

## PROSSIMI PASSI

### Immediate:
1. [ ] Creare cartella `esercizi_funzioni_base/`
2. [ ] Implementare es01-20 (livello BASE)

### Future:
1. [ ] Creare cartella `esercizi_funzioni_intermedio/`
2. [ ] Implementare es01-30 (livello INTERMEDIO)
3. [ ] Valutare livello AVANZATO (ricorsione, lambda, decoratori)

### Considerazioni future:
- **Esercizi AVANZATI funzioni:** Includere ricorsione, lambda, *args/**kwargs?
- **Integrazione:** Esercizi misti stringhe + funzioni + liste?
- **Progetti finali:** Mini-applicazioni che usano tutto (giochi, gestori, utilità)?

---

## NOTE FINALI

Questa struttura garantisce:
- ✅ Progressione logica e graduale
- ✅ Consolidamento concetti prima di passare al successivo
- ✅ Mix teoria-pratica bilanciato
- ✅ Preparazione per concetti avanzati futuri
- ✅ Applicabilità a problemi reali

La struttura può essere **estesa** in futuro con:
- Esercizi AVANZATI (ricorsione, functional programming)
- Esercizi PRO (decoratori, generatori, context managers)
- Progetti integrati (applicazioni complete)
