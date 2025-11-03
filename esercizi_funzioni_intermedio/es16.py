# SFIDA! Se questo esercizio ti sembra troppo difficile, puoi passare al successivo
# Riepilogo es11-15
""" SCOPO: Sistema completo di registrazione con validazione multipla.

Crea un sistema che chiede all'utente di registrarsi validando tutti i campi.

Definisci queste funzioni di validazione:

1. valida_nome(nome)
   - Lunghezza tra 2 e 30 caratteri
   - Solo lettere e spazi
   - RESTITUISCE (valido, messaggio)

2. valida_email(email)
   - Contiene esattamente una '@'
   - Contiene almeno un '.' dopo la '@'
   - Lunghezza >= 5
   - RESTITUISCE (valido, messaggio)

3. valida_password(password)
   - Lunghezza >= 8
   - Contiene maiuscola, minuscola e numero
   - RESTITUISCE (valido, messaggio)

4. valida_eta(eta_stringa)
   - È un numero
   - Età >= 18 e <= 120
   - RESTITUISCE (valido, messaggio)

5. registra_utente()
   - Chiede: nome, email, password, età
   - Valida TUTTI i campi usando le funzioni sopra
   - Se un campo non è valido, mostra l'errore e chiedi di nuovo quel campo
   - Quando tutti i campi sono validi, stampa:
     "✓ Registrazione completata!"
     "Nome: [nome]"
     "Email: [email]"
     "Età: [età]"

Il programma deve:
- Chiamare registra_utente()
- Gestire la validazione campo per campo
- Non andare avanti finché un campo non è valido

Suggerimento: usa un ciclo while per ogni campo che continua a chiedere
finché il campo non è valido.

Esempio:
  while True:
      nome = input("Nome: ")
      valido, messaggio = valida_nome(nome)
      if valido:
          break
      else:
          print(messaggio)
"""
