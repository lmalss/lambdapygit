
contatti_rubrica: dict[str, list[str]] = {}
print ("rubrica telefonica ")
while True:
  print("\nScegli un opzione:")
  print("1. aggiungere un nuovo contatto per nome")
  print("2. cerca un contatto per nome")
  print("3. Aggiungi o rimuovi un numero a un contatto")
  print("4. Modifica il nome di un contatto")
  print("5. Cerca a chi appartiene un numero")
  print("0. esci")
  
  scelta = input("scegli:")
  
  if scelta == "1":
    while True:
      print("\n[Modalità Aggiungi Contatto]")
      nome = input("inserisci il nome del nuovo contatto")
      if nome == "0":
          break       
        
      if nome in contatti_rubrica :
        print("contatto esistente")
      else :
        while True:
          numero = input(f"inserisci il numero di {nome}: ")
          if numero.isnumeric():
            break
          
          else:
            print("Errore: Inserisci solo cifre numeriche.")
        contatti_rubrica[nome] = [numero]
        print(f"contatto {nome} aggiunto")
      
  elif scelta == "2":
    while True:
      print("\n[Modalità cerca contatto]")
      nome = input("inserisci il numero da cercare")
      # Usiamo .get() per cercare la chiave (il nome)
      numeri = contatti_rubrica.get(nome)
      
      if numeri: 
        print (f"numeri di {nome}:")
        for num in numeri:
          print (f"- {num}")
      else :
        print("contatto ' {nome}' non presente in rubrica")
      
  elif scelta =="3":
    while True:
      nome = input ("inserisci il nome del contatto da modificare:")
      scelta_modificacontatto = input ("scelta(1) aggiungi numero, scelta(2)rimuovi numero : ")
      if nome in contatti_rubrica:
        print("1. aggiungi numero")
        print("2. rimuovi numero")
        
      
      if scelta_modificacontatto == "1":
        numero = input ("inserisci numero da aggiungere")
        contatti_rubrica[nome].append(numero)
        print ("numero aggiunto")
      elif scelta_modificacontatto =="2":
        numero = input ("inserisci il numero da rimuovere")
        contatti_rubrica[nome].pop(numero)
        print("numero rimosso corettamente")
                                  
  elif scelta =="4":
    vecchio_nome = input ("nome attuale del contatto")
    if vecchio_nome in contatti_rubrica:
      nuovo_nome = input ("nome nuovo del contatto")
    else:
      print(f"contatto {vecchio_nome} non trovato")
      
    
  elif scelta =="5":
    numero_da_cercare = input ("cerca a chi appartiene il numero")
    for nome, lista_numeri in contatti_rubrica.items():
      if numero_da_cercare in lista_numeri:
        contatto_trovato = nome 
        break
      if contatto_trovato:
        print(f" il numero {numero_da_cercare} appartiene a {contatto_trovato}")
      else: 
        print(f"il numero {numero_da_cercare} non trovato ")
  elif scelta == "0":
    print("ciao")
    break
  
  else:
    print("scelta non valida")
    
  