import multiprocessing
import os

# SOLID: Single Responsibility Principle
# ProcesMuncitor se ocupa exclusiv de primirea pe coada si afisarea datelor.
# Functia 'main' joaca rol de 'Distribuitor'. Astfel sarcinile sunt perfect decouple-uite.

class ProcesMuncitor(multiprocessing.Process):
    def __init__(self, coada: multiprocessing.Queue, nume: str):
        super().__init__()
        self.coada = coada
        self.nume = nume

    def run(self):
        while True:
            # Preluam date de pe coada de comunicare Inter-Process (IPC)
            cuvant = self.coada.get()
            
            # Semnal standard de tip 'Poison Pill' pentru oprire thread/process
            if cuvant is None:  
                break
            
            # Executia efectiva impusa de cerinta
            print(f"[Proces-Worker: {self.nume}] Am primit cuvantul: {cuvant}")

def main():
    print("--- Executie Py378 (Multiprocessing & Cozi de Mesaje) ---")
    fisier = "date_multiprocessing.txt"
    if not os.path.exists(fisier):
        with open(fisier, "w") as f:
            f.write("Salutari din Python. Aplicatia trimite cate un cuvant ciclic la trei procese diferite exact ca la carte!")

    # 1. Initializam sistemul (3 cozi pentru 3 procese distincte)
    cozi = [multiprocessing.Queue() for _ in range(3)]
    procese = []
    
    # 2. Pornim independent procesele de sistem
    for i in range(3):
        nume_proces = f"Proces_Terminal_Numarul_{i+1}"
        p = ProcesMuncitor(cozi[i], nume_proces)
        procese.append(p)
        p.start()
        
    # 3. Distribuire in regim Ciclic (Round-Robin logic) din fisier
    with open(fisier, "r") as f:
        text = f.read()
        
    cuvinte = text.split()
    index_curent = 0
    
    for cuvant in cuvinte:
        cozi[index_curent].put(cuvant)
        index_curent = (index_curent + 1) % 3 # Resetare index (0, 1, 2, 0, 1...)
        
    # 4. Finalizarea mediului curent
    for coada in cozi:
        coada.put(None)
        
    for p in procese:
        p.join()
        
    print("Toate cele 3 procese si-au terminat rulajul in siguranta paralela!")

if __name__ == "__main__":
    main()
