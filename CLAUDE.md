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
