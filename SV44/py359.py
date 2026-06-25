# SOLID: Open/Closed Principle - Permite adaugarea a infinit de multe servicii 
# suplimentare (Mancare, Curatenie) scriind decoratori noi, FARA sa se atinga 
# structura originala a camerei de hostel.

class ComponentaCamera:
    def get_descriere(self) -> str:
        pass
    def get_cost(self) -> float:
        pass

class CameraHostel(ComponentaCamera):
    def __init__(self, numar: int, pret_baza: float):
        self.numar = numar
        self.pret_baza = pret_baza
        
    def get_descriere(self) -> str:
        return f"Camera {self.numar} (Hostel)"
        
    def get_cost(self) -> float:
        return self.pret_baza

# DECORATORUL DE BAZA
class ServiciuSuplimentarDecorator(ComponentaCamera):
    def __init__(self, camera: ComponentaCamera):
        self.camera = camera
        
    def get_descriere(self) -> str:
        return self.camera.get_descriere()
        
    def get_cost(self) -> float:
        return self.camera.get_cost()

# DECORATORUL CONCRET (Consum Bar)
class ConsumBarDecorator(ServiciuSuplimentarDecorator):
    def __init__(self, camera: ComponentaCamera, cost_bauturi: float):
        super().__init__(camera)
        self.cost_bauturi = cost_bauturi
        
    def get_descriere(self) -> str:
        return super().get_descriere() + " + Consum Extra (Bar Camera)"
        
    def get_cost(self) -> float:
        return super().get_cost() + self.cost_bauturi

class NotaDePlata:
    def __init__(self):
        self.camere = []
        
    def adauga_camera(self, camera: ComponentaCamera):
        self.camere.append(camera)
        
    def genereaza(self):
        total = 0
        print("=== NOTA DE PLATA HOSTEL ===")
        for c in self.camere:
            print(f"- {c.get_descriere()}: {c.get_cost()} RON")
            total += c.get_cost()
        print(f"\\nTOTAL GENERAL: {total} RON")
        print("============================")

def main():
    print("--- Executie Py359 (Decorator Flux Plati Hostel) ---")
    nota = NotaDePlata()
    
    # Rezervam o camera simpla
    cam1 = CameraHostel(101, 150.0)
    nota.adauga_camera(cam1)
    
    # Rezervam o camera la care musafirii au golit minibarul!
    cam2_baza = CameraHostel(102, 150.0)
    cam2_decorata = ConsumBarDecorator(cam2_baza, cost_bauturi=75.0)
    
    nota.adauga_camera(cam2_decorata)
    
    # Afisam fluxul
    nota.genereaza()

if __name__ == "__main__":
    main()
