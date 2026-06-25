from abc import ABC, abstractmethod

# 1. Receiver (Cel care suferă acțiunea)
class Student:
    def __init__(self, nume):
        self.nume = nume
        self.stare = "fericit"

    def schimba_stare(self, noua_stare):
        self.stare = noua_stare
        print(f"[Student {self.nume}] a devenit: {self.stare}")

# 2. Interfața Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# 3. Comenzi Concrete
class ComandaPicaExamen(Command):
    def __init__(self, student: Student):
        self.student = student

    def execute(self):
        print("Comandă executată: Anunță picarea examenului!")
        self.student.schimba_stare("disperat")

class ComandaDaRezolvare(Command):
    def __init__(self, student: Student):
        self.student = student

    def execute(self):
        print("Comandă executată: Oferă rezolvarea subiectelor!")
        self.student.schimba_stare("fericit")

# 4. Invoker (Cel care declanșează/stochează comanda)
class Coleg:
    def __init__(self, nume):
        self.nume = nume
        self.comenzi = [] # Poate stoca o istorie a comenzilor

    def adauga_comanda(self, comanda: Command):
        self.comenzi.append(comanda)

    def actioneaza(self):
        print(f"\nColegul {self.nume} ia atitudine...")
        for comanda in self.comenzi:
            comanda.execute()
        self.comenzi.clear()

# 5. Testare
if __name__ == "__main__":
    studentul_nostru = Student("Andrei")
    colegul_rau = Coleg("Mihai")
    
    # Colegul dă o veste proastă (se creează o comandă)
    comanda_rea = ComandaPicaExamen(studentul_nostru)
    colegul_rau.adauga_comanda(comanda_rea)
    
    # Colegul acționează
    colegul_rau.actioneaza() # Andrei devine disperat
    
    # Acum îl ajută
    comanda_buna = ComandaDaRezolvare(studentul_nostru)
    colegul_rau.adauga_comanda(comanda_buna)
    colegul_rau.actioneaza() # Andrei redevine fericit