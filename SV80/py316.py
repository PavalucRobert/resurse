from abc import ABC, abstractmethod

# EXPLICATII SOLID:
# Single Responsibility (SRP): Obiectul Student pastreaza starea lui, dar schimbarea logica dictata 
# de vointa profesorului este decuplata prin obiectele Comanda.
# Open/Closed: Putem instantia usor o clasa noua de tip "ComandaNotaZece" 
# fara a modifica nici clasa Profesor (Invoker), nici clasa Student (Receiver).

class Student:
    """Receiver - Obiectul care sufera schimbarea interna de stare."""
    def __init__(self, nume):
        self.nume = nume
        self.stare_interna = "Fericit"
        
    def modifica_stare(self, noua_stare):
        self.stare_interna = noua_stare
        print(f"[Student {self.nume}] Starea s-a schimbat in: -> {self.stare_interna}")

class Comanda(ABC):
    """Interfata comuna pentru Toate Comenzile"""
    @abstractmethod
    def executa(self):
        pass

class ComandaTestSurpriza(Comanda):
    def __init__(self, student: Student):
        self.student = student
        
    def executa(self):
        print(f"\\nComanda: Profesorul da un Test Surpriza pentru {self.student.nume}!")
        self.student.modifica_stare("Disperat")

class ComandaAnulareTest(Comanda):
    def __init__(self, student: Student):
        self.student = student
        
    def executa(self):
        print(f"\\nComanda: Profesorul anuleaza Testul pentru {self.student.nume}.")
        self.student.modifica_stare("Fericit si Usurat")

class Profesor:
    """Invoker - Cel care declanseaza operatiunile."""
    def da_comanda(self, comanda: Comanda):
        comanda.executa()

def main():
    print("--- Executie Py316 (Command Pattern) ---")
    s1 = Student("Ionel")
    profu = Profesor()
    
    print(f"Stare initiala: {s1.nume} este {s1.stare_interna}")
    
    cmd_test = ComandaTestSurpriza(s1)
    cmd_anulare = ComandaAnulareTest(s1)
    
    profu.da_comanda(cmd_test)
    profu.da_comanda(cmd_anulare)

if __name__ == "__main__":
    main()
