from typing import Optional


class Dipendente:
    def __init__(
        self, nome : str, cognome : str, codice_fiscale: str,
        paga : Optional [int] = None , orario : Optional [int] = None
    ):
        self.nome: str = nome
        self.cognome: str = cognome
        self.codice_fiscale = codice_fiscale
        self.paga : Optional [int] = paga
    
        
    def stipendio (self, orario : int) -> float:
        if self.paga:                                      # Se la paga è oraria (come nel dipendente base)
            return orario * self.paga
        return 0


class Manager(Dipendente):
    def __init__(self, nome: str, cognome: str, codice_fiscale : str, paga_base: int, sottoposti: int, bonus: int):
        super().__init__(nome, cognome, codice_fiscale, paga_base)
        self.sottoposti : int = sottoposti
        self.bonus = bonus                      # Salviamo il bonus come attributo
    
    def stipendio (Self, orario : int) -> float:        # Accetta "ore" per compatibilità, anche se magari non le usa
        return self.paga + (self.bonus * self.sottoposti)
                          
        
class Commerciale(Dipendente):
    def __init__(self, nome: str, cognome: str, codice_fiscale : str, paga_base :int, fatturato : int, provvigione : int):
        super().__init__(nome, cognome, codice_fiscale, paga_base) 
        self.fatturato = fatturato
        self.provvigione = provvigione          # Salviamo la % come attributo
        
    def stipendio (self, orario: int) -> float:
        calcolo_provvigione = (self.fatturato * self.provvigione) /100
        return self.paga + calcolo_provvigione

class Azienda :
    def __init__(self, nome: str,):
        self.nome = nome
        self.dipendenti : list[Dipendente] = []
    
    def assumi(self, dipendente):
        self.dipendenti.append(dipendente)
    
    def stampa_tutti_i_dipendenti ( self):
        print (f"--- Dipendenti di : {self.nome} ---")
        for dipendenti in self.Dipendenti:
            print (f" {dipendenti.nome} {dipendenti.cognome}")

    def totale_stipendi (self, orario_standard: int):
        totale = 0
        
        for dipendente in self.dipendenti:  #magia del Polimorfismo
                                            # Chiamo lo stesso metodo su tutti. Python capirà da solo quale versione eseguire (Manager, Commerciale o base)
            stipendio = dipendente.stipendiio (orario_standard)
            totale += stipendio
        return totale
        
        
        # Creazione Azienda
azienda = Azienda("Tech Corp")
azienda.assumi(Dipendente)
azienda.assumi(manager)
azienda.assumi(Commerciale)

dipendente1 = Dipendente ("Alessio","Alaimo", "LMALSS01R19B429T", paga = 12 ) # 12 euro/ora
dipendente2 = Dipendente ("Lucia", "Bella", "LCABLL725391146P", paga = 12)  # 12 euro/ora
dipendente3 = Dipendente ("Mario", "Gianni", "MROGNN62839847Y", paga = 12)  # 12 euro/ora
manager = Manager ("Paolo", "Nicchia", " PLNCC683458353H", paga_base= 1500, sottoposti= 10, bonus=100)
commerciale = Commerciale ("Vincenzo", "Bellini", "VNCBLL8153460P", paga_base = 1200, fatturato = 50000, provvigione = 10)


costo_totale = azienda.calcola_costo_totale_stipendi(160)   #Calcolo totale (Assumendo 160 ore lavorative standard per chi è a ore)

print (f" costo_totale stipendi questo mese : {costo:totale} €")
