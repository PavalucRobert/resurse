import threading
import time

# SOLID: Single Responsibility Principle
# Fiecare subclasa defineste o operatie clara. Tipurile de operatii sunt derivate dintr-o clasa de baza.
# Folosim RLock (Reentrant Lock) pentru sectiunile critice, astfel incat firul curent sa poata re-dobandi lacatul la nevoie.

class ActiveHashMapProcessor(threading.Thread):
    def __init__(self, data_map, lock):
        super().__init__()
        self.data_map = data_map
        self.lock = lock

    def operatie_pura(self, a, b):
        # Clasa de baza stabileste sablonul, dar functia pura e abstractizata
        pass
        
    def run(self):
        # Procesam cate 2 elemente vecine din map (chei consecutive presupunem)
        keys = list(self.data_map.keys())
        for i in range(0, len(keys)-1, 2):
            k1, k2 = keys[i], keys[i+1]
            
            # Sectiune critica
            with self.lock:
                v1 = self.data_map[k1]
                v2 = self.data_map[k2]
                
                # Functie pura aplicata valorilor
                rez = self.operatie_pura(v1, v2)
                
                # Actualizam
                self.data_map[k1] = rez
            
            time.sleep(0.1) # Simulam un overhead

# Subclase active

class AdderThread(ActiveHashMapProcessor):
    def operatie_pura(self, a, b):
        return a + b

class SubtractorThread(ActiveHashMapProcessor):
    def operatie_pura(self, a, b):
        return a - b

class BinaryMultiplierThread(ActiveHashMapProcessor):
    def operatie_pura(self, a, b):
        # Inmultire binara pe 16 biti (trunchiere la 16 biti)
        rez = a * b
        return rez & 0xFFFF

def main():
    # Hashmap partajat
    data = {
        0: 10,
        1: 20,
        2: 30,
        3: 5,
        4: 100,
        5: 3
    }
    
    print("Dictionar initial:", data)
    
    # RLock permite re-dobandirea de catre acelasi fir daca e nevoie de o structura recursiva.
    shared_lock = threading.RLock()
    
    # Instantiem actorii / subclasele active
    t1 = AdderThread(data, shared_lock)       # va aplica + si va suprascrie
    t2 = SubtractorThread(data, shared_lock)  # va aplica - si va suprascrie
    t3 = BinaryMultiplierThread(data, shared_lock) # va aplica inmultire 16bit

    # Pornim firele
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print("Dictionar final:", data)

if __name__ == "__main__":
    main()
