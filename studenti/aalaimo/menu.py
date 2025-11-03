totale = 0.00

print("\n--- CAFE EXPRESS ---")

while True: 
      
    print ("\n--- MENU ---")
    print ("caffe:  1.00")
    print ("caffe macchiato:   1.20")
    print ("caffe espresso: 1.20")
    print ("caffe corto:   0.80")
    print ("the caldo:   1.50")
    print ("cappuccino:   2.00")
    print ("acqua:  1.00") 
    print ("brioche:  1.20")   
    print ("the freddo:  2.00")
    print ("------------")
    print ("digita 'stop' per terminare e pagare")
        
    print (f" totale attuale è : {totale:.2f}")
    scelta_utente = input ("scegli qualcosa da ordinare\n")
    
    if scelta_utente == "caffe":
        prezzo = 1.00
        print(f"hai scelto : caffe. prezzo: {prezzo:.2f}")
        totale = totale + prezzo
        
        
    elif scelta_utente == "caffe macchiato":
        prezzo = 1.20
        print(f"hai scelto : caffe macchiato. prezzo: {prezzo:.2f}") 
        totale = totale + prezzo
        
    elif scelta_utente == "caffe espresso":
        prezzo = 1.20
        print(f"hai scelto : caffe espresso. prezzo: {prezzo:.2f}")
        totale = totale + prezzo

        
    elif scelta_utente == "caffe corto":
        prezzo = 0.80
        print(f"hai scelto : caffe corto. prezzo: {prezzo:.2f}")
        totale = totale + prezzo
        
        
    elif scelta_utente == "the caldo":
        prezzo = 1.50
        print(f"hai scelto : the caldo. prezzo: {prezzo:.2f}")
        totale = totale + prezzo
        
        
    elif scelta_utente == "cappuccino":
        prezzo = 2.00
        print(f"hai scelto : cappuccino. prezzo: {prezzo:.2f}")
        totale = totale + prezzo
        
        
    elif scelta_utente == "the freddo":
        prezzo = 2.00
        print(f"hai scelto : the freddo. prezzo: {prezzo:.2f}")
        totale = totale + prezzo
        
        
    elif scelta_utente == "acqua":
        prezzo = 1.00
        print(f"hai scelto : acqua. prezzo: {prezzo:.2f}")
        totale = totale + prezzo
        
        
    elif scelta_utente == "brioche":
        prezzo = 1.20
        print(f"hai scelto : brioche. prezzo: {prezzo:.2f}")
        totale = totale + prezzo
        
    elif scelta_utente == "admin":
        print("\n--- 🔐 MODALITÀ ADMIN ---")
        prodotto_da_modificare = input("Quale prodotto vuoi modificare? ")
    
    elif scelta_utente == "stop":
        print ("ordine terminato")
        break
    
    else :
        print(f"scegli qualcosa nel menu")
    
print ("\n--- CONTO ----")
print (f"il totale da pagare è : {totale:.2f}")
print ("grazie per averci scelto")

 