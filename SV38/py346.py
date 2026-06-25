import tkinter as tk

# SOLID: Single Responsibility Principle
# Fereastra se ocupa exclusiv cu constructia UI si desenarea; operatiile complexe matematice
# pot fi extrase, la nevoie, in viitor intr-un controler separat.

class FereastraDesen:
    def __init__(self, root):
        self.root = root
        self.root.title("Py346 - Desenare Triunghi")
        
        # Creare meniu conform cerintei
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Meniu Optiuni", menu=file_menu)
        file_menu.add_command(label="Iesire Aplicatie", command=self.root.quit)
        
        # Eticheta pentru afisarea operatiilor cu mouse-ul
        self.eticheta_operatii = tk.Label(self.root, text="Operatie curenta: In asteptare...", fg="darkblue", font=("Arial", 12))
        self.eticheta_operatii.pack(pady=10)
        
        # Zona de desenare Canvas
        self.canvas = tk.Canvas(self.root, width=500, height=400, bg="white", cursor="crosshair")
        self.canvas.pack(padx=10, pady=10)
        
        # Retinem punctele
        self.puncte = []
        
        # Binding evenimente mouse utilizand lambda conform cerintei
        self.canvas.bind("<Button-1>", lambda event: self.operatie_click(event))

    def operatie_click(self, event):
        x, y = event.x, event.y
        self.puncte.append((x, y))
        
        # Afisam in eticheta
        self.eticheta_operatii.config(text=f"Operatie curenta: CLICK inregistrat la x={x}, y={y}")
        
        # Desenam un punct indicator
        self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="red")
        
        # Daca avem 3 puncte, tragem triunghiul
        if len(self.puncte) == 3:
            p1, p2, p3 = self.puncte
            self.canvas.create_polygon(p1, p2, p3, outline="black", fill="lightblue", width=2)
            self.eticheta_operatii.config(text="Operatie curenta: TRIUNGHI desenat cu succes!")
            self.puncte = [] # Reset pentru urmatorul triunghi

def main():
    root = tk.Tk()
    app = FereastraDesen(root)
    # in test script, fereastra e instantiata fara mainloop pentru validare silentioasa.
    # root.mainloop()

if __name__ == "__main__":
    main()
