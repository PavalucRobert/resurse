import functools

# EXPLICATII SOLID:
# Single Responsibility (SRP): Memento stocheaza starea, Originatorul o modifica, Caretaker o gestioneaza (istoricul).
# Open/Closed: Putem adauga oricate operatii noi de modificare a starii fara a modifica structura de memento.

class Memento:
    """Memento salveaza starea interna a Originatorului."""
    def __init__(self, stare):
        # Folosim list(stare) pentru o copie a colectiei, sa nu salvam referinta mutabila
        self._stare = list(stare) if isinstance(stare, list) else stare
        
    def get_stare(self):
        return self._stare

class ProcesorColectie:
    """Originator: Creeaza memento continand starea si le foloseste pentru restaurare."""
    def __init__(self, colectie):
        self.colectie = colectie
        
    def aplica_f1(self):
        print("[Operatie] Se aplica f1(x): daca x e par, devine x+1")
        self.colectie = list(map(lambda x: x+1 if (isinstance(x, int) and x % 2 == 0) else x, self.colectie))
        
    def aplica_f2(self):
        print("[Operatie] Se aplica f2(x) = 3*x*x - 2*x + 1")
        self.colectie = list(map(lambda x: 3*x*x - 2*x + 1 if isinstance(x, int) else x, self.colectie))
        
    def aplica_f3(self):
        print("[Operatie] Se aplica f3(x,y) = x+y (Agregare/Reduce pe colectie)")
        if len(self.colectie) > 0:
            suma_totala = functools.reduce(lambda x, y: x + y, self.colectie)
            self.colectie = [suma_totala]
            
    def salveaza_stare(self) -> Memento:
        print(f"[Salvare] Memento creat cu starea: {self.colectie}")
        return Memento(self.colectie)
        
    def restaureaza_stare(self, memento: Memento):
        self.colectie = memento.get_stare()
        print(f"[Restore] Starea a revenit la: {self.colectie}")

class Istoric:
    """Caretaker: Pastreaza salvarile."""
    def __init__(self):
        self._salvari = []
        
    def adauga_salvare(self, memento: Memento):
        self._salvari.append(memento)
        
    def obtine_ultima_salvare(self) -> Memento:
        if self._salvari:
            return self._salvari.pop()
        return None

def main():
    print("--- Executie Py338 (Memento si Lambda pe Colectii) ---")
    colectie_initiala = [2, 3, 4, 5, 6]
    procesor = ProcesorColectie(colectie_initiala)
    istoric = Istoric()
    
    # Starea 0
    istoric.adauga_salvare(procesor.salveaza_stare())
    
    # Aplicam f1 (cele pare aduna 1: 2->3, 4->5, 6->7) => [3, 3, 5, 5, 7]
    procesor.aplica_f1()
    istoric.adauga_salvare(procesor.salveaza_stare())
    
    # Aplicam f2 (3*x^2 - 2x + 1)
    procesor.aplica_f2()
    istoric.adauga_salvare(procesor.salveaza_stare())
    
    # Aplicam f3 (x+y) pe toata colectia
    procesor.aplica_f3()
    print(f"Stare dupa reductie: {procesor.colectie}")
    
    # Restauram 1 pas
    print("\\n-- Cerere Restaurare din istoric --")
    procesor.restaureaza_stare(istoric.obtine_ultima_salvare())
    
    # Restauram inca 1 pas
    print("-- Cerere Restaurare din istoric --")
    procesor.restaureaza_stare(istoric.obtine_ultima_salvare())

if __name__ == "__main__":
    main()
