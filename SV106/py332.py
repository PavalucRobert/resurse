# Pattern: Composite (Meniuri)

# EXPLICATII SOLID:
# 1. Liskov Substitution Principle: O instanta Optiune sau MeniuComposite poate
# sa inlocuiasca la nevoie o ComponentaMeniu abstracta (avand metoda afiseaza comuna).

class ComponentaMeniu:
    def afiseaza(self):
        pass

class Optiune(ComponentaMeniu):
    def __init__(self, nume):
        self.nume = nume
        self.parinte = None

    def afiseaza(self):
        print(f"\\n   [X] Ai selectat optiunea finala executabila: {self.nume}")

class MeniuComposite(ComponentaMeniu):
    def __init__(self, nume):
        self.nume = nume
        self.copii = []
        self.parinte = None

    def adauga(self, componenta):
        componenta.parinte = self
        self.copii.append(componenta)

    def afiseaza(self):
        print(f"\\n=== Meniu: {self.nume} ===")
        for index, copil in enumerate(self.copii, start=1):
            nume_afisare = copil.nume if isinstance(copil, ComponentaMeniu) else "Necunoscut"
            print(f"{index}. {nume_afisare}")
        
        if self.parinte is not None:
            print("0. Înapoi")

        # Functia de selectie este dezactivata implicit in modul modul (pt automatizare)
        # dar in consola reala am rula o bucla de input.
        # selectie_utilizator() - mock

def main():
    print("--- Executie Py332 (Composite Pattern pentru UI CLI) ---")
    meniu_principal = MeniuComposite("Meniu Principal")
    
    # Submeniuri
    meniu_file = MeniuComposite("File")
    meniu_edit = MeniuComposite("Edit")
    
    # Optiuni frunza
    opt_new = Optiune("New File")
    opt_save = Optiune("Save")
    meniu_file.adauga(opt_new)
    meniu_file.adauga(opt_save)
    
    opt_copy = Optiune("Copy")
    meniu_edit.adauga(opt_copy)
    
    # Construim structura arbore
    meniu_principal.adauga(meniu_file)
    meniu_principal.adauga(meniu_edit)
    
    meniu_principal.afiseaza()
    print("\\n(Pentru navigare s-ar apela input() recursiv ca la structura web!)")

if __name__ == "__main__":
    main()
