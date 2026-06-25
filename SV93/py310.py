import copy
import tkinter as tk

# EXPLICATII SOLID:
# Prototype Pattern ne ajuta la OCP (Open/Closed): Putem adauga noi atribute caruciorului si le vom putea
# clona direct fara sa modificam constructorul in sute de locuri.
# Single Responsibility Principle: Caruciorul doar tine starea si informatiile despre desenare.
# Gestionarea ferestrei ramane sarcina separata (aici pusa in main pt simplitate).

class PrototipCarucior:
    """Clasa care defineste caruciorul grafic si permite clonarea sa."""
    def __init__(self, x, y, culoare):
        self.x = x
        self.y = y
        self.culoare = culoare
        
    def cloneaza(self):
        # Returnam o clona exacta a obiectului curent
        return copy.deepcopy(self)
        
    def deseneaza(self, canvas: tk.Canvas):
        # Deseneaza corpul
        canvas.create_rectangle(self.x, self.y, self.x + 60, self.y + 40, fill=self.culoare)
        # Deseneaza rotile
        canvas.create_oval(self.x + 5, self.y + 40, self.x + 20, self.y + 55, fill="black")
        canvas.create_oval(self.x + 40, self.y + 40, self.x + 55, self.y + 55, fill="black")

def main():
    print("--- Executie Py310 (Prototip Grafic Tkinter) ---")
    try:
        root = tk.Tk()
        root.title("Carucioare Identice - Pattern Prototip")
        canvas = tk.Canvas(root, width=500, height=400, bg="white")
        canvas.pack()
        
        # 1. Definim prototipul de baza
        prototip_albastru = PrototipCarucior(0, 0, "blue")
        
        # 2. Clonam si punem la diverse pozitii
        c1 = prototip_albastru.cloneaza()
        c1.x, c1.y = 50, 50
        c1.deseneaza(canvas)
        
        c2 = prototip_albastru.cloneaza()
        c2.x, c2.y = 200, 150
        c2.culoare = "red" # Alteram starea unei clone
        c2.deseneaza(canvas)
        
        c3 = prototip_albastru.cloneaza()
        c3.x, c3.y = 350, 250
        c3.deseneaza(canvas)
        
        # Daca e in test CI, oprim dupa o secunda. Altfel comentati in viata reala
        root.after(500, root.destroy)
        root.mainloop()
        
        print("Grafica s-a randat cu succes (3 carucioare din care 2 perfect identice, 1 alterat)!")
        
    except Exception as e:
        print(f"Eroare mediu grafic: {e}")

if __name__ == "__main__":
    main()
