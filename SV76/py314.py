import tkinter as tk

# EXPLICATIE SOLID:
# 1. Single Responsibility: O clasa deseneaza in sine liniile (API_Desenare), 
#    alta tine detaliile despre "ce este" o forma (Cerc, Dreptunghi).
# 2. Open/Closed Principle: Daca vrem o forma noua (Poligon) sau un stil nou (DesenareVerde),
#    adaugam o clasa noua FARA sa atingem sau modificam codul deja scris.

# --- IMPLEMENTATORI (Partea de desenare efectiva pe Canvas) ---
class API_Desenare:
    def deseneaza_cerc(self, canvas): pass
    def deseneaza_dreptunghi(self, canvas): pass
    def deseneaza_triunghi(self, canvas): pass

class DesenareRosie(API_Desenare):
    def deseneaza_cerc(self, canvas):
        canvas.create_oval(50, 50, 150, 150, outline="red", width=3)
        print("S-a desenat un Cerc Rosu.")
    
    def deseneaza_dreptunghi(self, canvas):
        canvas.create_rectangle(50, 50, 200, 150, outline="red", width=3)
        print("S-a desenat un Dreptunghi Rosu.")
    
    def deseneaza_triunghi(self, canvas):
        canvas.create_polygon(100, 50, 50, 150, 150, 150, outline="red", fill="", width=3)
        print("S-a desenat un Triunghi Rosu.")

class DesenareAlbastra(API_Desenare):
    def deseneaza_cerc(self, canvas):
        canvas.create_oval(50, 50, 150, 150, outline="blue", width=3)
        print("S-a desenat un Cerc Albastru.")
    
    def deseneaza_dreptunghi(self, canvas):
        canvas.create_rectangle(50, 50, 200, 150, outline="blue", width=3)
        print("S-a desenat un Dreptunghi Albastru.")
    
    def deseneaza_triunghi(self, canvas):
        canvas.create_polygon(100, 50, 50, 150, 150, 150, outline="blue", fill="", width=3)
        print("S-a desenat un Triunghi Albastru.")

# --- ABSTRACTIA (Logica Formei) ---
class Forma:
    def __init__(self, api_desenare: API_Desenare):
        self.api = api_desenare # Aici este Podul (Bridge) catre modul de desenare!

    def deseneaza(self, canvas):
        pass

class Cerc(Forma):
    def deseneaza(self, canvas):
        self.api.deseneaza_cerc(canvas)

class Dreptunghi(Forma):
    def deseneaza(self, canvas):
        self.api.deseneaza_dreptunghi(canvas)

class Triunghi(Forma):
    def deseneaza(self, canvas):
        self.api.deseneaza_triunghi(canvas)

def app_gui():
    root = tk.Tk()
    root.title("Design Pattern Bridge")
    
    canvas = tk.Canvas(root, width=250, height=200, bg="white")
    canvas.pack(pady=20)
    
    # Podul ne permite combinatii infinite:
    api_rosu = DesenareRosie()
    
    # Schimba aici in Cerc(api_rosu) sau Dreptunghi(api_rosu) etc.
    forma_mea = Triunghi(api_rosu)
    
    forma_mea.deseneaza(canvas)
    
    root.mainloop()

if __name__ == "__main__":
    app_gui()
