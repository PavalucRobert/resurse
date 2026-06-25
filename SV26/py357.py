# EXPLICATII SOLID:
# Single Responsibility Principle: Procesorul logic este creat strict pentru transformarea si aplatizarea dictionarelor imbricate.

class DataFlattener:
    @staticmethod
    def flatten(dictionar_sursa, prefix_curent=''):
        rezultat = {}
        for cheie, valoare in dictionar_sursa.items():
            # Construim cheia concatenata cu prefixul (pentru traseu/locatie)
            noua_cheie = f"{prefix_curent}_{cheie}" if prefix_curent else cheie
            
            if isinstance(valoare, dict):
                # Extindem apelul recursiv direct pe structura dict
                rez_copil = DataFlattener.flatten(valoare, noua_cheie)
                rezultat.update(rez_copil)
            elif isinstance(valoare, list):
                # Aplatizam si listele (imbinandu-le ca string, asa cum e standard la un flatten dict generic)
                rezultat[noua_cheie] = ", ".join(map(str, valoare))
            else:
                # Obiect terminal (frunza)
                rezultat[noua_cheie] = valoare
                
        return rezultat

def main():
    print("--- Executie Py357 (Data Flatten peste inregistrare ierarhica) ---")
    inregistrare = {
        'Nume': 'Bula',
        'Locatia': {
            'Oras': 'Pocreaca',
            'Tara': 'RO'
        },
        'Aptitudini': ['Baut', 'Femei']
    }
    
    print(f"Inregistrare Ierarhica Initiala: {inregistrare}")
    dictionar_plat = DataFlattener.flatten(inregistrare)
    
    print("\\nRezultatul Aplatizat:")
    for key, val in dictionar_plat.items():
        print(f" - {key}: {val}")

if __name__ == "__main__":
    main()
