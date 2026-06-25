import tkinter as tk
from tkinter import ttk, messagebox

# Aplicatie Tkinter pentru Gestiunea Angajatilor
class FereastraAngajat:
    def __init__(self, root):
        self.root = root
        self.root.title("Introducere Date Angajat")
        self.root.geometry("400x350")
        
        self.creare_meniu()
        self.creare_formular()

    def creare_meniu(self):
        menubar = tk.Menu(self.root)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Salveaza", command=self.salveaza)
        filemenu.add_separator()
        filemenu.add_command(label="Iesire", command=self.root.quit)
        
        menubar.add_cascade(label="Fisier", menu=filemenu)
        self.root.config(menu=menubar)

    def creare_formular(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Companie:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_companie = tk.Entry(frame)
        self.entry_companie.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Departament:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_departament = tk.Entry(frame)
        self.entry_departament.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Nume:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_nume = tk.Entry(frame)
        self.entry_nume.grid(row=2, column=1, pady=5)

        tk.Label(frame, text="Luna Naștere:").grid(row=3, column=0, sticky="w", pady=5)
        luni = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", 
                "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]
        self.combo_luna = ttk.Combobox(frame, values=luni, state="readonly")
        self.combo_luna.current(0)
        self.combo_luna.grid(row=3, column=1, pady=5)

        tk.Label(frame, text="Funcție:").grid(row=4, column=0, sticky="w", pady=5)
        self.entry_functie = tk.Entry(frame)
        self.entry_functie.grid(row=4, column=1, pady=5)

        tk.Label(frame, text="Salariu:").grid(row=5, column=0, sticky="w", pady=5)
        self.entry_salariu = tk.Entry(frame)
        self.entry_salariu.grid(row=5, column=1, pady=5)

        btn_salvare = tk.Button(frame, text="Salveaza Date", command=self.salveaza)
        btn_salvare.grid(row=6, column=0, columnspan=2, pady=15)

    def salveaza(self):
        nume = self.entry_nume.get()
        luna = self.combo_luna.get()
        if not nume:
            messagebox.showwarning("Avertisment", "Numele este obligatoriu!")
            return
        
        print(f"SALVAT: {nume}, Luna nasterii: {luna}")
        messagebox.showinfo("Succes", f"Angajatul {nume} a fost salvat cu succes!")

def app_gui():
    root = tk.Tk()
    app = FereastraAngajat(root)
    root.mainloop()

if __name__ == "__main__":
    app_gui()
