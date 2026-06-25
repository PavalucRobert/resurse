import threading

# SOLID: Single Responsibility Principle - Logica aplicatiei e separata clar 
# Clasa ProcesorDictionar are grija de accesul concurent. Calculul in sine poate fi usor extras.

class ProcesorDictionar:
    def __init__(self, X: dict, Y: dict):
        self.X = X
        self.Y = Y
        # Utilizam RLock pentru a proteja suprascrierea concurenta asupra lui Y, in caz de alte extinderi
        self.lock = threading.RLock()
        
    def calculeaza_element(self, cheie):
        # Protejam sectiunea critica (chiar daca preiau chei diferite, e un mod curat de scriere safe-thread)
        with self.lock:
            if cheie in self.X and cheie in self.Y:
                x = self.X[cheie]
                y = self.Y[cheie]
                # Formula f(x,y) = x*y + y + 1
                rezultat = (x * y) + y + 1
                
                # Suprascriere in Y
                self.Y[cheie] = rezultat
                print(f"[Thread-Cheie-{cheie}] f({x}, {y}) = {rezultat}")

    def procesare_paralela(self):
        threaduri = []
        for cheie in self.X.keys():
            t = threading.Thread(target=self.calculeaza_element, args=(cheie,))
            threaduri.append(t)
            t.start()
            
        for t in threaduri:
            t.join()

def main():
    dict_X = {1: 5, 2: 10, 3: 2}
    dict_Y = {1: 2, 2: 4, 3: 10}
    
    print(f"X initial: {dict_X}")
    print(f"Y initial: {dict_Y}")
    
    procesor = ProcesorDictionar(dict_X, dict_Y)
    procesor.procesare_paralela()
    
    print(f"Y dupa procesare in paralela (Threading cu RLock): {procesor.Y}")

if __name__ == "__main__":
    main()
