# Model Mediator

# EXPLICARE SOLID:
# 1. Dependency Inversion: Obiectele `Furnica` nu depind de clasele concrete ale celorlalte furnici, ci se leagă direct de clasa abstractă `Mediator`.
# 2. Open/Closed Principle: Sistemul poate fi extins ușor prin crearea unor alte clase Mediator sau tipuri noi de furnici, fără a modifica structura de bază care deja comunică impecabil.

class Mediator:
    def trimite(self, mesaj: str, expeditor):
        pass

class Musuroi(Mediator):
    def __init__(self):
        self.furnici = []
        
    def inregistreaza(self, furnica):
        self.furnici.append(furnica)
        
    def trimite(self, mesaj: str, expeditor):
        # Trimite la toata lumea, mai putin celui care a initiat mesajul
        for furnica in self.furnici:
            if furnica != expeditor:
                furnica.primeste(mesaj)

class Furnica:
    def __init__(self, nume: str, mediator: Mediator):
        self.nume = nume
        self.mediator = mediator
        self.mediator.inregistreaza(self)
        
    def comunica(self, mesaj: str):
        print(f"\\n[Furnica {self.nume}] strigă în rețea: '{mesaj}'")
        self.mediator.trimite(mesaj, self)
        
    def primeste(self, mesaj: str):
        print(f"   --> [Furnica {self.nume}] a receptionat apelul: '{mesaj}'")

def main():
    print("--- Executie Py341 (Mediator Pattern) ---")
    musuroi_principal = Musuroi()
    
    f1 = Furnica("Explorator", musuroi_principal)
    f2 = Furnica("Soldat-01", musuroi_principal)
    f3 = Furnica("Regina", musuroi_principal)
    
    f1.comunica("Am gasit mancare!")
    f2.comunica("Pericol! Inamici la granita!")
    f3.comunica("Drum bun, retrageti-va in siguranta.")

if __name__ == "__main__":
    main()
