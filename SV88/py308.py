import tkinter as tk

# FORME: Principiul SOLID - Single Responsibility: fiecare clasa are un singur scop: sa deseneze o forma
class Cerc:
    def deseneaza(self, canvas):
        canvas.create_oval(50, 50, 150, 150, outline="blue", width=3)

class Dreptunghi:
    def deseneaza(self, canvas):
        canvas.create_rectangle(50, 50, 200, 150, outline="red", width=3)

class Patrat:
    def deseneaza(self, canvas):
        canvas.create_rectangle(50, 50, 150, 150, outline="green", width=3)

# FABRICI DE FORME: Principiul SOLID - Open/Closed: putem adauga noi forme fara a schimba codul de baza
class FabricaCerc:
    def creaza_forma(self):
        return Cerc()

class FabricaDreptunghi:
    def creaza_forma(self):
        return Dreptunghi()

class FabricaPatrat:
    def creaza_forma(self):
        return Patrat()

# FABRICA DE FABRICI (Abstract Factory)
class FabricaDeFabrici:
    @staticmethod
    def obtine_fabrica(tip):
        if tip == "CERC":
            return FabricaCerc()
        elif tip == "DREPTUNGHI":
            return FabricaDreptunghi()
        elif tip == "PATRAT":
            return FabricaPatrat()
        return None

def main():
    root = tk.Tk()
    root.title("Fabrica de Fabrici - Simplu")
    
    canvas = tk.Canvas(root, width=250, height=200, bg="white")
    canvas.pack()
    
    # Alegem fabrica dorita (de exemplu CERC, PATRAT sau DREPTUNGHI)
    fabrica = FabricaDeFabrici.obtine_fabrica("CERC")
    
    if fabrica:
        forma = fabrica.creaza_forma()
        forma.deseneaza(canvas)
        
    root.mainloop()

if __name__ == "__main__":
    main()
