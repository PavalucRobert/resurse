import itertools
import os

# Conceptul de Closure presupune retinerea si protejarea starii interne
# a variabilelor declarate in contextul exterior, atunci cand sunt folosite de o functie interioara.

def factory_generator_fisiere():
    # Starea closure-ului folosind un contor infinit oferit de itertools
    # Counterul isi va aminti intotdeauna starea si la urmatorul next() va continua de unde a ramas.
    contor = itertools.count(start=1, step=1)
    
    def genereaza_fisier(s1: str, s2: str) -> str:
        # Preluam indexul retinand starea generatorului
        index = next(contor)
        
        nume_fisier = f"{s1}-{index}-{s2}.tmp"
        
        # Simulam crearea pe hard disk a fisierului cerut
        cale_completa = os.path.join(os.getcwd(), nume_fisier)
        with open(cale_completa, 'w') as f:
            f.write(f"Acesta este un fisier temporar: {nume_fisier}\\n")
            
        print(f"Generatorul s-a oprit la index={index} si a creat: {nume_fisier}")
        return nume_fisier
        
    return genereaza_fisier

def main():
    print("--- Executie Py356 (Closure si Itertools Counter) ---")
    
    generator = factory_generator_fisiere()
    
    f1 = generator("data", "log")
    f2 = generator("dump", "backup")
    f3 = generator("temp", "cache")
    
    # Curatare pe hard disk ca sa nu lasam fisiere in urma
    for f in [f1, f2, f3]:
        if os.path.exists(f):
            os.remove(f)

if __name__ == "__main__":
    main()
