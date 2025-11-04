# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Panoramica del Repository

Questo è un repository di **esercizi didattici Python** per l'apprendimento progressivo, organizzato per argomenti e livelli di difficoltà. Gli esercizi sono progettati per studenti principianti/intermedi.

## Struttura del Repository

```
python_esercizi/
├── esercizi_Stringhe_base/          # Esercizi base sulle stringhe
├── esercizi_stringhe_intermedio/    # Esercizi intermedi sulle stringhe
├── esercizi_stringhe_avanzati/      # Esercizi avanzati sulle stringhe
├── esercizi_funzioni_base/          # Esercizi base sulle funzioni (20 esercizi)
├── esercizi_funzioni_intermedio/    # Esercizi intermedi sulle funzioni (30 esercizi)
├── verifica_funzioni_base/          # Test di verifica sulle funzioni
├── es01.py - es21.py                # Esercizi sulle stringhe (root)
└── LOG_PROGETTAZIONE_ESERCIZI_FUNZIONI.md  # Documentazione filosofia didattica
```

## Filosofia degli Esercizi

### Pattern Didattico "Triplo"

Ogni argomento segue una progressione a 3 livelli:

1. **Guidato (es01, es04, es07, ...):**
   - Spiegazione completa del concetto
   - Codice quasi completo con pochi spazi da completare
   - Commenti esplicativi dettagliati

2. **Intermedio (es02, es05, es08, ...):**
   - Applicazione del concetto senza spiegazioni
   - Più spazi vuoti da completare
   - Richiede comprensione autonoma

3. **Riepilogo (es03, es06, es09, ...):**
   - Solo descrizione dello scopo
   - Studente scrive tutto da zero
   - Può combinare concetti precedenti

### Formato Standard degli Esercizi

Tutti i file `.py` seguono questo formato:
- **Spazi da completare**: `________` indica dove lo studente deve scrivere codice
- **Commenti MAIUSCOLO**: indicano che lo studente deve scrivere codice autonomamente
- **Intestazione standard**: ogni file inizia con istruzioni chiare
- **Sezione SCOPO**: descrive l'obiettivo dell'esercizio
- **Commenti didattici**: spiegano concetti e sintassi

Esempio:
```python
# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGNIFICA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO del programma: ... """
```

## Argomenti Coperti

### Esercizi Funzioni - Base (20 esercizi)
1. Definizione e chiamata senza parametri (es01-03)
2. Funzioni con 1 parametro (es04-06)
3. Parametri multipli (es07-09)
4. Statement `return` (es10-12)
5. Usare valori ritornati (es13-15)
6. Funzioni con stringhe (es16-17)
7. Riepilogo generale (es18-20)

### Esercizi Funzioni - Intermedio (30 esercizi)
1. Parametri con valori default (es01-03)
2. Return multiplo e tuple unpacking (es04-06)
3. Scope variabili (locale vs globale) (es07-09)
4. Composizione (funzioni che chiamano funzioni) (es10-12)
5. Validazione input con if/else (es13-15)
6. Funzioni con liste (es16-18)
7. Funzioni con dizionari (es19-21)
8. Documentazione e docstring (es22-24)
9. Funzioni booleane e logica (es25-27)
10. Mini-progetti integrati (es28-30)

### Argomenti Esclusi (troppo avanzati per il target)
- ❌ Ricorsione
- ❌ Lambda functions
- ❌ *args e **kwargs
- ❌ Higher-order functions
- ❌ Nested functions e closures
- ❌ Type hints

## Come Eseguire gli Esercizi

```bash
# Eseguire un singolo esercizio
python esercizi_funzioni_base/es01.py

# Eseguire un esercizio dalla root
python es01.py
```

## Convenzioni di Codice

- **Naming funzioni**: `snake_case` (es. `calcola_area`, `is_valido`)
- **Parametri**: nomi descrittivi in italiano (es. `nome`, `eta`, `prezzo`)
- **Indentazione**: 4 spazi
- **Gestione errori**:
  - Base: nessuna gestione (input sempre valido)
  - Intermedio: validazione con `if/else`
  - Intermedio avanzato: `try/except` per input utente

## Tipologie di Applicazioni

Gli esercizi coprono un mix bilanciato:
- 30% matematica/calcoli (area, media, conversioni)
- 30% stringhe/testo (validazione, analisi, formattazione)
- 20% logica/controllo (condizioni, classificazioni)
- 20% gestione dati (liste, dizionari, mini-progetti)

## File di Supporto

- **LOG_PROGETTAZIONE_ESERCIZI_FUNZIONI.md**: documentazione completa della filosofia didattica, progressione degli argomenti e decisioni di design
- **File CSV**: rubriche di valutazione per le verifiche
- **File .zip**: archivi degli esercizi per distribuzione

## Note per lo Sviluppo

Quando si creano o modificano esercizi:

1. **Mantenere il formato standard** con spazi `________` e commenti MAIUSCOLO
2. **Seguire la progressione Guidato → Intermedio → Riepilogo**
3. **Includere sempre la sezione SCOPO** all'inizio
4. **Fornire esempi di test** nei commenti (es. "Prova con: ...")
5. **Usare nomi in italiano** per variabili e funzioni (target: studenti italiani)
6. **Evitare concetti troppo avanzati** per mantenere la curva di apprendimento graduale

## Metodologia di Correzione Verifiche

Questa sezione documenta il processo e i criteri per correggere le verifiche degli studenti.

### Principi Generali di Correzione

**Filosofia**: La correzione deve essere formativa, non punitiva. L'obiettivo è aiutare lo studente a capire gli errori e migliorare.

**Punteggio**: 5 punti per esercizio (totale 100 punti per 20 esercizi)

**Approccio**: Flessibile sulla forma, rigoroso sulla funzionalità

### Criteri di Valutazione

#### ✅ Cosa NON deve essere penalizzato

1. **Variazioni di formato output** (se funzionalmente equivalenti)
   - Uso di f-string vs print con virgole
   - Print multipli invece di un'unica stringa (se contiene tutte le info richieste)
   - Spazi extra o mancanti nell'output
   - Esempio: `print("Ciao", nome)` vs `print(f"Ciao {nome}")` → entrambi accettabili

2. **Errori di battitura (typo)** che non compromettono la funzionalità
   - Nome variabile con errori ortografici ma usato consistentemente
   - Maiuscole/minuscole in output se il resto è corretto
   - Esempio: `verifica_maggiorene` invece di `verifica_maggiorenne` → se usato consistentemente, OK

3. **Scelte di implementazione diverse ma corrette**
   - Uso di variabili intermedie vs calcoli diretti
   - Ordine di definizione delle funzioni
   - Posizionamento del programma principale (se il codice funziona)

4. **Nomi di variabili diversi dalla traccia** (se chiari e appropriati)
   - Esempio: `risultato` vs `somma` per una variabile che contiene una somma → entrambi OK

#### ❌ Cosa DEVE essere penalizzato

1. **Errori che bloccano l'esecuzione del codice**
   - Sintassi errata (es. `30%` invece di `30`)
   - Variabile usata prima di essere definita
   - Parametri mancanti nelle chiamate a funzione
   - Nome di funzione errato nelle chiamate
   - Esempio: `print(sconto)` prima di `sconto = ...` → ERRORE GRAVE

2. **Logica errata che produce risultati sbagliati**
   - Formula matematica incompleta o errata
   - Condizioni if/elif/else sbagliate (es. `>=` invece di `>`)
   - Casi mancanti nella logica (es. manca `else`)
   - Ordine errato delle operazioni
   - Esempio: `totale = (prezzo * iva / 100)` invece di `prezzo + (prezzo * iva / 100)` → ERRORE

3. **Fraintendimento di concetti chiave**
   - Uso di `print` invece di `return` quando richiesto `return`
   - Confusione tra definizione e chiamata di funzione
   - Parametri nel posto sbagliato o numero errato
   - Esempio: funzione richiede `return` ma usa `print` → ERRORE CONCETTUALE

4. **Esercizi non completati**
   - File identico alla traccia con spazi vuoti (___) non compilati
   - Funzioni mancanti
   - Programma principale non scritto
   - Punteggio: 0/5

### Processo di Correzione

#### Fase 1: Preparazione
1. Leggere tutti i file di traccia (es01.py - es20.py) per comprendere i requisiti
2. Leggere tutti i file dello studente (es01.py - es20.py)
3. Confrontare ogni esercizio con la traccia corrispondente

#### Fase 2: Analisi Esercizio per Esercizio
Per ogni esercizio:

1. **Verifica funzionalità**:
   - Il codice si esegue senza errori?
   - Produce l'output corretto?
   - La logica è corretta?

2. **Identifica errori**:
   - Errori bloccanti (sintassi, variabili non definite)
   - Errori logici (formula sbagliata, condizioni errate)
   - Errori concettuali (return vs print, parametri)

3. **Assegna punteggio**:
   - 5/5: Completamente corretto (anche con variazioni di stile)
   - 4/5: Un errore minore non bloccante
   - 3/5: Errore significativo ma funzione parzialmente corretta
   - 2/5: Errore grave, funziona parzialmente
   - 1/5: Errore molto grave, quasi non funziona
   - 0/5: Non svolto o completamente errato

#### Fase 3: Documentazione nel File MD

Struttura del file di correzione:

```markdown
# Correzione Verifica Funzioni Base - [Nome Cognome]

Punteggio Totale: XX/100

---

## Esercizio N
Punteggio: X/5

Obiettivo: [Descrizione obiettivo]

Analisi del codice:
[Descrizione generale: cosa ha fatto lo studente]

[SE CI SONO ERRORI:]
Errore riscontrato:
- Riga X: [Codice errato]
- Problema: [Spiegazione chiara del problema]
- Cosa dovevi scrivere: [Codice corretto]

Spiegazione:
[Spiegazione pedagogica del concetto, non solo cosa è sbagliato ma PERCHÉ]

---

## Riepilogo e Raccomandazioni

Punti di forza:
- [Lista punti di forza]

Aree da migliorare:
- [Lista aree critiche con priorità]

Esercizi da rifare OBBLIGATORIAMENTE:
- [Lista esercizi con errori gravi]

Valutazione generale:
[Paragrafo conclusivo con valutazione complessiva e consigli]
```

#### Fase 4: Caratteristiche della Correzione

1. **Linguaggio chiaro e costruttivo**
   - Usa "hai fatto" non "hai sbagliato"
   - Spiega il "perché" non solo il "cosa"
   - Fornisci il codice corretto completo

2. **Esempi concreti**
   - Mostra sempre il codice errato e quello corretto
   - Usa esempi pratici per spiegare concetti
   - Indica numeri di riga specifici

3. **Spiegazioni pedagogiche**
   - Non dare per scontato che lo studente capisca l'errore
   - Spiega il concetto sottostante (es. "Python legge il codice dall'alto verso il basso")
   - Usa analogie quando utile (es. "come una ricetta di cucina")

4. **Priorità degli errori**
   - Evidenzia gli errori CRITICI (bloccanti)
   - Distingui tra errori gravi e minori
   - Fornisci una roadmap chiara per il recupero

### Esempi di Correzione

#### Esempio 1: Errore Accettabile (NO penalità)

**Traccia**: `print("Ciao [nome], benvenuto!")`

**Studente ha scritto**: `print(f"Ciao {nome}, benvenuto!")`

**Valutazione**: 5/5 - Funzionalmente equivalente, f-string è una scelta valida

---

#### Esempio 2: Errore Grave (penalità)

**Traccia**:
```python
def calcola_sconto(prezzo, percentuale):
    sconto = prezzo * percentuale / 100
    print("Sconto:", sconto)
```

**Studente ha scritto**:
```python
def calcola_sconto(prezzo, percentuale):
    print("Sconto:", sconto)
    sconto = prezzo * percentuale / 100
```

**Valutazione**: 1/5 - Usa variabile prima di definirla (errore bloccante)

**Feedback**:
```
Errore grave - Ordine delle istruzioni:
- Problema: Stai usando `sconto` nel print PRIMA di averla definita
- Python legge il codice dall'alto verso il basso
- Soluzione: CALCOLA prima, STAMPA dopo
```

---

#### Esempio 3: Errore Concettuale (forte penalità)

**Traccia richiede**: `return` per restituire valore

**Studente ha usato**: `print` invece di `return`

**Valutazione**: 1/5 - Fraintendimento concetto fondamentale

**Feedback**:
```
Concetto di return (CRITICO):
- `print()` → STAMPA sullo schermo
- `return` → RESTITUISCE valore utilizzabile
Senza capire il return non puoi progredire nella programmazione
```

### Casi Speciali

#### Studente con punteggio 0

Se uno studente non ha completato NESSUN esercizio:
- Punteggio: 0/100
- Feedback: enfatizzare l'urgenza, fornire supporto base, suggerire di parlare con il docente
- Includere esempi di codice base per ogni concetto
- Non essere punitivo ma chiaro sulla gravità

#### Studente eccellente (>90)

- Riconoscere il lavoro ottimo
- Indicare piccoli dettagli migliorabili se presenti
- Fornire sfide opzionali per approfondire

### Formato File

- **Nome file**: `[Cognome]_[Nome].md` (es. `Bosio_Fabio.md`)
- **Posizione**: cartella `correzioni/` dentro la directory della verifica
- **Encoding**: UTF-8
- **Nessun emoticon**: scrittura professionale e formale

### Checklist Finale

Prima di consegnare la correzione, verificare:

- [ ] Punteggio totale corretto (somma di tutti gli esercizi)
- [ ] Ogni esercizio ha: obiettivo, analisi, punteggio
- [ ] Gli errori gravi sono evidenziati come CRITICI
- [ ] Fornito codice corretto per ogni errore
- [ ] Sezione riepilogo completa con: punti di forza, aree da migliorare, esercizi da rifare
- [ ] Linguaggio costruttivo e pedagogico
- [ ] Nessun emoticon nel testo
- [ ] File salvato nella cartella `correzioni/`
