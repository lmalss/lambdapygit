from pathlib import Path

file = Path ("tamagotchi.csv")

class Tamagotchi:
    def __init__ (self, nome : str, fame = 0, felicità = 100, stanchezza = 0):
        self.nome = nome
        self.fame = fame
        self.felicità = felicità
        self.stanchezza = stanchezza
    
    def nutri (self, quantita_cibo):
        if quantita_cibo < self.fame:
            self.fame -= quantita_cibo
            
        else:
            self.fame = 0
        
        self.stanchezza += quantita_cibo
        if self.stanchezza > 100:
            self.stanchezza = 100
            
    def gioca (self, tempo = 10):
        self.felicità += tempo
        if self.felicità > 100:
            self.felicità = 100
            
        self.stanchezza += tempo
        if self.stanchezza > 100:
            self.stanchezza = 100
            
    def dormi (self):
        self.fame = min(self.fame + 50, 100)
        self.felicità = max(self.felicità - 50, 0)
        self.stanchezza = max (self.stanchezza - 50 , 0)

    def __str__(self) -> str:
        return f"{self.nome} : \n- fame : {self.fame},  \n felicità : {self.felicità}, \n stanchezza: {self.stanchezza}"

class Adulti (Tamagotchi):
    def __init__ (self, nome : str, fame = 0,  felicità = 100, stanchezza = 0 ):
        super().__init__ (nome, fame, felicità, stanchezza)
    def gioca (self):
        print(f"{self.nome} gioca con moderazione.")
        self.felicita += 10
        self.stanchezza += 2
        print(f"(È adulto: regge bene il gioco. Stanchezza: {self.stanchezza})")
        
    def mangia(self):
        print(f"{self.nome} mangia, ma ha bisogno di più cibo.")
        self.fame -= 5
        print(f"(Fame attuale: {self.fame})")       
    
class Cuccioli (Tamagotchi):
    def __init__ (self, nome : str, fame = 0,  felicità = 100, stanchezza = 0 ):
        super().__init__ (nome, fame, felicità, stanchezza)
    # I cuccioli si stancano più velocemente quando giocano   
    def gioca(self):
        super().gioca()
        self.stanchezza += 5
        print(f"(È un cucciolo: si è stancato molto! Stanchezza: {self.stanchezza})")
    # Si riposano più velocemente (recuperano più energie)
    def dorme (self):
        print(f"{self.nome} dorme profondamente come un sasso.")
        self.stachezza -= 10
        if self.stachezza < 0: self.stanchezza = 0 
        print(f"(Stanchezza scesa rapidamente a {self.stanchezza})")
        

lista_tamagotchi = []

with file.open("r" , encoding="utf-8") as f:
    next(f)
    for riga in f:
        campi = riga.strip().split(',')
        nome = campi[0]
        fame = int(campi[1])
        felicità = int(campi[2])
        stanchezza = int(campi[3])
        new_tamagotchi= Tamagotchi (nome, fame, felicità, stanchezza)
        lista_tamagotchi.append (new_tamagotchi)
        
        
print (f"--- Tamagotchi ---")        
while True:
    print ("1 - stato")
    print ("2 - azioni")
    print ("3 - esci")
    print ("4 aggiungi tamagotchi")
    print ("5 rimuovi il tamagotchi")
    
    scelta = int(input(" scegli un azione"))
    if scelta == 3:
        break
    elif scelta == 1:
        for tamagotchi in lista_tamagotchi:
            print(tamagotchi)
    
    elif scelta == 2:
        
        nome_tamagotchi = input("quale tamagotchi scegli?")
        trovato = True
        
        print ("1 - nutri")
        print ("2 - gioca")
        print ("3 - dormi")
        print ("4 - esci")
        
        
        for tamagotchi in lista_tamagotchi:
            if tamagotchi.nome == nome_tamagotchi:
                scelta = input("cosa vuoi fare?")
                
                if scelta == "4":
                    continue
                elif scelta == "1":
                    quantita_cibo = int(input (" quanto cibo gli dai?"))
                    tamagotchi.nutri (quantita_cibo)
                    
                elif scelta == "2":
                    tempo = int(input("quanto tempo vuoi giocare ?"))
                    tamagotchi.gioca (tempo)
                    
                elif scelta == "3":
                    tamagotchi.dormi (dormi)
                break
        if not trovato :
            print (f"{nome_tamagotchi} : non trovato")    
                        
    elif scelta == "4":
        nome=input("nome del tamagotchi")
        new_tamagotchi = Tamagotchi(nome)
        lista_tamagotchi.append (new_tamagotchi)
    
    elif scelta == "5":
        nome = input ("nome del tamagotchi da rimuovere")
        for tamagotchi in lista_tamagotchi:
            if tamagotchi.nome == nome:
                lista_tamagotchi.remove (tamagotchi)
                

with file.open ("w" , encoding="utf-8") as f:
    f.write("nome,fame,felicità,stanchezza\n")
    for tamagotchi in lista_tamagotchi:
        f.write (f"{tamagotchi .nome},{tamagotchi.fame},{tamagotchi.felicità}, {tamagotchi.stanchezza}")
    
           
        
        
            
            
        
        
