# SOLID: Facade Pattern - Boombox ascunde complexitatea diverselor subsisteme izolate.
# Single Responsibility Principle (SRP): Fiecare clasa din subsistem are o singura sarcina foarte bine determinata, 
# iar BoomboxFacade e de asemenea strict limitata la delegarea sarcinilor compuse, mentinand un design foarte decuplat.

# --- SUBSISTEME COMPLEXE ---
class CDPlayer:
    def play(self): print("[CD Player] Playing track...")
    def pause(self): print("[CD Player] Paused.")
    def fast_forward(self): print("[CD Player] Fast forwarding >>")
    def rewind(self): print("[CD Player] Rewinding <<")
    
class Radio:
    def turn_on(self): print("[Radio] Sistem pornit (Frecventa implicita).")
    def turn_off(self): print("[Radio] Sistem oprit.")
    def tune(self, frequency): print(f"[Radio] Frecventa a fost cautata si setata manual la {frequency} MHz.")

class Caseta:
    def record(self): print("[Casetofon] Inregistrarea fizica a inceput pe banda (REC).")
    
class Baterie:
    def get_status(self): return "Bateria Li-Ion este la 85% autonomie."

class ControlVolum:
    def set_volume(self, level): print(f"[Master Volum] Setat global la nivelul {level}/10.")

# --- FATADA PENTRU INTERACTIUNE USOARA (API Simplificat) ---
class BoomboxFacade:
    def __init__(self):
        # Aici sunt incapsulate subsistemele "dificile"
        self.cd = CDPlayer()
        self.radio = Radio()
        self.caseta = Caseta()
        self.baterie = Baterie()
        self.volum = ControlVolum()
        
    def actiune_party(self):
        print("\\n-- Boombox: Initializare Mod Party --")
        self.volum.set_volume(10)
        self.cd.fast_forward()
        self.cd.play()
        
    def actiune_ascultare_stiri(self):
        print("\\n-- Boombox: Initializare Mod Relaxare Stiri --")
        self.volum.set_volume(3)
        self.radio.turn_on()
        self.radio.tune(105.5)
        
    def inregistrare_radio(self):
        print("\\n-- Boombox: Mod Captura Audio din Radio --")
        self.radio.turn_on()
        self.caseta.record()
        
    def afiseaza_baterie(self):
        print(f"\\n[Boombox System] Status: {self.baterie.get_status()}")

def main():
    print("--- Executie Py333 (Facade Boombox) ---")
    sistem_boombox = BoomboxFacade()
    
    sistem_boombox.afiseaza_baterie()
    sistem_boombox.actiune_ascultare_stiri()
    sistem_boombox.inregistrare_radio()
    sistem_boombox.actiune_party()

if __name__ == "__main__":
    main()
