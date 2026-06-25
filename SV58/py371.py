import threading

# EXPLICATII SOLID:
# Single Responsibility Principle (SRP): Clasa de baza ofera doar logica pura (matematica), 
# in timp ce subclasele active preiau responsabilitatea de a rula asincron in fire de executie si a sincroniza in Hashmap.
# Liskov Substitution (LSP): Subclasele pot fi tratate direct ca Thread-uri native din Python.

class OperatiiPureBaza:
    """Clasa ce ofera functii pure, fara stare sau side effects."""
    @staticmethod
    def adunare(a, b):
        return a + b

    @staticmethod
    def inmultire_binara_16biti(a, b):
        # Limitarea logica binara la 16 biti se face prin aplicarea mastii 0xFFFF
        return (a * b) & 0xFFFF

# Memorie partajata (Hashmap) si element de sincronizare (Semafor)
hashmap_comun = {}
semafor_hashmap = threading.Semaphore(1)

class SubclasaActivaAdunare(threading.Thread, OperatiiPureBaza):
    def __init__(self, cheie, val1, val2):
        super().__init__()
        self.cheie = cheie
        self.val1 = val1
        self.val2 = val2

    def run(self):
        rezultat = self.adunare(self.val1, self.val2)
        
        # Accesam hasmap-ul comun in siguranta folosind semaforul
        semafor_hashmap.acquire()
        try:
            hashmap_comun[self.cheie] = rezultat
            print(f"[Fir Adunare] S-a scris {self.cheie} = {rezultat}")
        finally:
            semafor_hashmap.release()

class SubclasaActivaInmultire16(threading.Thread, OperatiiPureBaza):
    def __init__(self, cheie, val1, val2):
        super().__init__()
        self.cheie = cheie
        self.val1 = val1
        self.val2 = val2

    def run(self):
        rezultat = self.inmultire_binara_16biti(self.val1, self.val2)
        
        # Utilizare alternativa prin bloc context-manager pentru acquire/release automat pe semafor
        with semafor_hashmap:
            hashmap_comun[self.cheie] = rezultat
            print(f"[Fir Inmultire16] S-a scris {self.cheie} = {rezultat}")

def main():
    print("--- Executie Py371 (Threading, Semaphore si Hashmap comun) ---")
    
    # 300 * 400 = 120000. 120000 in binar & 0xFFFF = 54464
    fire = [
        SubclasaActivaAdunare("op_adunare_1", 1500, 2000),
        SubclasaActivaInmultire16("op_inm16_1", 300, 400),
        SubclasaActivaAdunare("op_adunare_2", 99, 1)
    ]
    
    for f in fire:
        f.start()
        
    for f in fire:
        f.join()
        
    print(f"\\nStarea finala a Hashmap-ului concurent: {hashmap_comun}")

if __name__ == "__main__":
    main()
