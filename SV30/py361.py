# Sistem de rezervare Hostel - Decorator Pattern

# SOLID: Single Responsibility Principle - Clasa 'Camera' detine doar date, 'NotaDePlataCamera' genereaza factura de baza, iar Decoratorul face doar extensia ei.
# SOLID: Open/Closed Principle - Daca maine adaugam "Mic Dejun", facem un nou Decorator, fara a atinge clasele existente!

class Camera:
    def __init__(self, numar, pret_noapte):
        self.numar = numar
        self.pret_noapte = pret_noapte

    def __str__(self):
        return f"Camera {self.numar}"

# Componenta de Baza
class NotaDePlata:
    def genereaza_nota(self) -> float:
        pass

class NotaDePlataCamera(NotaDePlata):
    def __init__(self, camera: Camera, nopti: int):
        self.camera = camera
        self.nopti = nopti

    def genereaza_nota(self) -> float:
        cost = self.camera.pret_noapte * self.nopti
        print(f"Cazare {self.nopti} nopti in {self.camera}: {cost} lei")
        return cost

# Decoratorul OOP General
class DecoratorNota(NotaDePlata):
    def __init__(self, nota_baza: NotaDePlata):
        self.nota_baza = nota_baza

    def genereaza_nota(self) -> float:
        return self.nota_baza.genereaza_nota()

# Decoratorul Concret pentru fluxul suplimentar (Consum Bar)
class ConsumBarDecorator(DecoratorNota):
    def __init__(self, nota_baza: NotaDePlata, cost_bar: float):
        super().__init__(nota_baza)
        self.cost_bar = cost_bar

    def genereaza_nota(self) -> float:
        # Se executa fluxul de baza, apoi cel suplimentar
        cost_initial = super().genereaza_nota()
        cost_final = cost_initial + self.cost_bar
        print(f" + Consum din bar: {self.cost_bar} lei")
        print(f"TOTAL DE PLATA: {cost_final} lei")
        return cost_final

def main():
    # ADT (Abstract Data Type) -> folosim o lista pentru a retine camerele
    camere = [Camera(101, 150), Camera(102, 200)]
    
    # Alegem o camera si facem nota de baza
    camera_aleasa = camere[0]
    nota_baza = NotaDePlataCamera(camera_aleasa, nopti=3)
    
    # Aplicam Decoratorul pentru a adauga costul de bar
    nota_completa = ConsumBarDecorator(nota_baza, cost_bar=45.5)
    
    print("--- Generare Factura ---")
    nota_completa.genereaza_nota()

if __name__ == "__main__":
    main()
