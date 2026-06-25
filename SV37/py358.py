# EXPLICATII SOLID:
# Open/Closed Principle: Logica de baza a rezervarii poate fi extinsa prin Decorator (waitlist_decorator) 
# fara sa o modificam direct in clasa originala.
# Single Responsibility: Entitatea Camera retine starea ei, ADT-ul SistemRezervari le gestioneaza, 
# iar Decoratorul e responsabil exclusiv de flow-ul cozii de asteptare.

class Camera:
    def __init__(self, numar):
        self.numar = numar
        self.ocupata = False
        
    def rezerva(self):
        self.ocupata = True
        
    def elibereaza(self):
        self.ocupata = False

class SistemRezervari:
    """ADT pentru gestiunea camerelor de hotel."""
    def __init__(self, camere):
        self.camere = camere
        
    def proceseaza_rezervare(self, client):
        for camera in self.camere:
            if not camera.ocupata:
                camera.rezerva()
                print(f"[Sistem] Camera {camera.numar} a fost rezervata pentru {client}.")
                return True
        print(f"[Sistem] Nicio camera disponibila pentru {client}.")
        return False

# Decorator care intercepteaza rezultatul false si adauga clientul in coada
def waitlist_decorator(functie_baza):
    coada_asteptare = []
    
    def wrapper(self, client):
        succes = functie_baza(self, client)
        if not succes:
            print(f"[Waitlist] Cererea nu a putut fi satisfacuta imediat. Clientul {client} adaugat pe lista de asteptare.")
            coada_asteptare.append(client)
        return succes
        
    # Atasam coada la functie pentru a o putea interoga din exterior
    wrapper.coada_asteptare = coada_asteptare
    return wrapper

class SistemRezervariHotel(SistemRezervari):
    @waitlist_decorator
    def proceseaza_rezervare(self, client):
        return super().proceseaza_rezervare(client)

def main():
    print("--- Executie Py358 (Decorator Waitlist Hotel) ---")
    c1 = Camera(101)
    sistem = SistemRezervariHotel([c1])
    
    sistem.proceseaza_rezervare("Ion (Client 1)")
    sistem.proceseaza_rezervare("Maria (Client 2)")
    sistem.proceseaza_rezervare("Vasile (Client 3)")
    
    print(f"\\nLista de asteptare: {sistem.proceseaza_rezervare.coada_asteptare}")

if __name__ == "__main__":
    main()
