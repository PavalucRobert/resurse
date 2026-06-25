import tkinter as tk

def calculeaza_secventa():
    """Calculează punctele (i, S) pentru formula dată, în intervalul cerut."""
    n0 = 0
    S = n0
    i = 0
    puncte = []
    
    # Rulăm calculul atâta timp cât S este sub pragul maxim de 50
    while S < 50:
        S += i
        if 20 < S < 50:
            puncte.append((i, S))
        i += 1
        
    return puncte

def deseneaza_interfata():
    # Inițializare fereastră principală Tkinter
    root = tk.Tk()
    root.title("Grafic Secvență Pyt342")
    root.geometry("500x350")
    
    # Creăm un Frame (o zonă) pentru Canvas (grafic)
    frame_grafic = tk.Frame(root)
    frame_grafic.pack(side=tk.LEFT, padx=10, pady=10)
    
    canvas_w, canvas_h = 300, 300
    canvas = tk.Canvas(frame_grafic, width=canvas_w, height=canvas_h, bg="white", relief=tk.SUNKEN, bd=2)
    canvas.pack()
    
    # Creăm un Frame pentru "cutia" care va afișa valorile
    frame_cutie = tk.Frame(root)
    frame_cutie.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)
    
    eticheta_cutie = tk.Label(frame_cutie, text="Valori (i, S)", font=("Arial", 10, "bold"))
    eticheta_cutie.pack()
    
    # Folosim un Listbox pentru "cutia" în care afișăm datele separat
    cutie_valori = tk.Listbox(frame_cutie, width=15, font=("Courier", 10))
    cutie_valori.pack(expand=True, fill=tk.BOTH)
    
    # Preluăm datele calculate
    puncte = calculeaza_secventa()
    
    # Populăm cutia cu text și desenăm graficul
    if not puncte:
        cutie_valori.insert(tk.END, "Niciun punct în interval")
        return
        
    # Scalare pentru ca graficul să arate bine pe ecran
    scale_x = 25
    scale_y = 5
    offset_x = 20 # Să nu fie lipit de marginea din stânga
    
    for index, (i, S) in enumerate(puncte):
        # 1. Adăugăm în cutie
        cutie_valori.insert(tk.END, f" i={i} | S={S}")
        
        # 2. Desenăm liniile (dacă avem cu ce să le unim)
        if index < len(puncte) - 1:
            x1, y1 = puncte[index]
            x2, y2 = puncte[index+1]
            
            # Tkinter are originea (0,0) în stânga-sus, deci trebuie să inversăm axa Y
            cx1 = offset_x + (x1 * scale_x)
            cy1 = canvas_h - (y1 * scale_y)
            cx2 = offset_x + (x2 * scale_x)
            cy2 = canvas_h - (y2 * scale_y)
            
            # Tragem o linie albastră
            canvas.create_line(cx1, cy1, cx2, cy2, fill="blue", width=2)
            # Desenăm punctele (cercuri roșii)
            canvas.create_oval(cx1-4, cy1-4, cx1+4, cy1+4, fill="red")
            # Desenăm și ultimul punct
            if index == len(puncte) - 2:
                canvas.create_oval(cx2-4, cy2-4, cx2+4, cy2+4, fill="red")

    root.mainloop()

if __name__ == "__main__":
    deseneaza_interfata()