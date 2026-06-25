import threading

# EXPLICATII SOLID:
# SRP (Single Responsibility): Operatiile matematice sunt pure in clasa de baza. Threading-ul este integrat
# separat in subclasele derivate (Active Object).
# LSP (Liskov Substitution): Orice Thread matematic isi va indeplini job-ul prin .start() in mod generic.

class FunctiiMatematicePure:
    @staticmethod
    def adunare(a, b): return a + b
    @staticmethod
    def scadere(a, b): return a - b
    @staticmethod
    def inmultire(a, b): return a * b
    @staticmethod
    def impartire(a, b): return a / b if b != 0 else 0

# Hashmap concurent
dictionar_comun = {}
# Lock (in loc de Semaphore, conform cerintei Py364)
lacat = threading.Lock()

class ThreadAdunare(threading.Thread, FunctiiMatematicePure):
    def __init__(self, cheie, a, b):
        super().__init__()
        self.cheie = cheie
        self.a = a
        self.b = b
        
    def run(self):
        rez = self.adunare(self.a, self.b)
        
        lacat.acquire()
        try:
            dictionar_comun[self.cheie] = rez
            print(f"[Thread Adunare] a scris: {self.cheie} = {rez}")
        finally:
            lacat.release()

class ThreadScadere(threading.Thread, FunctiiMatematicePure):
    def __init__(self, cheie, a, b):
        super().__init__()
        self.cheie = cheie
        self.a = a
        self.b = b
        
    def run(self):
        rez = self.scadere(self.a, self.b)
        
        with lacat: # context managerul automatizeaza acquire/release
            dictionar_comun[self.cheie] = rez
            print(f"[Thread Scadere] a scris: {self.cheie} = {rez}")

def main():
    print("--- Executie Py364 (Threaduri Subclase Active Hashmap cu Lock) ---")
    fire = [
        ThreadAdunare("op_suma1", 50, 50),
        ThreadScadere("op_scadere1", 200, 75),
        ThreadAdunare("op_suma2", 1, 9)
    ]
    
    for fir in fire:
        fir.start()
        
    for fir in fire:
        fir.join()
        
    print(f"\\nDictionar Final (sincronizat cu Lock): {dictionar_comun}")

if __name__ == "__main__":
    main()
