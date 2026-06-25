import tkinter as tk

# SOLID: Abstract Factory
# Principiul Open/Closed: Putem adauga usor o FabricaButoaneFr sau FabricaButoaneEs
# FARA a modifica logica de baza a Fabricii Abstracte (creaza_buton).
# Single Responsibility Principle: Fiecare fabrica concreta e responsabila de generarea setului UI doar pentru limba ei.

class FabricaButoane:
    def creaza_buton(self, master: tk.Tk) -> tk.Button:
        pass

class FabricaButoaneRo(FabricaButoane):
    def creaza_buton(self, master: tk.Tk) -> tk.Button:
        return tk.Button(master, text="Salut! Apasa-ma", fg="white", bg="blue", 
                         font=("Arial", 12, "bold"), command=lambda: print("[RO] Ai apasat butonul in Romana!"))

class FabricaButoaneEn(FabricaButoane):
    def creaza_buton(self, master: tk.Tk) -> tk.Button:
        return tk.Button(master, text="Hello! Click me", fg="white", bg="red", 
                         font=("Arial", 12, "bold"), command=lambda: print("[EN] You clicked the English button!"))

class AbstractFactoryGUI:
    @staticmethod
    def get_factory(limba: str) -> FabricaButoane:
        if limba.lower() == "ro":
            return FabricaButoaneRo()
        elif limba.lower() == "en":
            return FabricaButoaneEn()
        else:
            raise ValueError("Limba necunoscuta suportata: doar 'ro' sau 'en'")

def main():
    print("--- Executie Py306 (Fabrica de Fabrici GUI) ---")
    
    # Parametru teoretic primit in apel
    limba_selectata = "ro" # sau "en"
    
    fabrica = AbstractFactoryGUI.get_factory(limba_selectata)
    
    root = tk.Tk()
    root.title("Abstract Factory GUI Test")
    root.geometry("300x200")
    
    buton_rezultat = fabrica.creaza_buton(root)
    buton_rezultat.pack(expand=True)
    
    # root.mainloop() in mediul de test poate rula interactiv
    # pentru scrip-urile automate, nu dam mainloop.

if __name__ == "__main__":
    main()
