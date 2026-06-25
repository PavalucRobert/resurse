# Modelul Lanț de Responsabilități (Chain of Responsibility)

# SOLID: Single Responsibility Principle - Fiecare handler se ocupa DOAR de nivelul sau de alerta.
# SOLID: Open/Closed Principle - Putem adauga noi niveluri (de ex. Pompieri pentru nivel 6) fara a modifica clasele de baza.

class Handler:
    def __init__(self, succesor=None):
        self.succesor = succesor

    def set_succesor(self, succesor):
        self.succesor = succesor
        return succesor

    def trateaza(self, nivel, mesaj):
        if self.succesor:
            self.succesor.trateaza(nivel, mesaj)

class NatoHandler(Handler):
    def trateaza(self, nivel, mesaj):
        if nivel == 0:
            print(f"[NATO - Nivel 0] Mesaj: {mesaj}")
        else:
            super().trateaza(nivel, mesaj)

class CsatHandler(Handler):
    def trateaza(self, nivel, mesaj):
        if nivel == 1:
            print(f"[CSAT - Nivel 1] Mesaj: {mesaj}")
        else:
            super().trateaza(nivel, mesaj)

class SieHandler(Handler):
    def trateaza(self, nivel, mesaj):
        if nivel == 2:
            print(f"[SIE - Nivel 2] Mesaj: {mesaj}")
        else:
            super().trateaza(nivel, mesaj)

class SriHandler(Handler):
    def trateaza(self, nivel, mesaj):
        if nivel == 3:
            print(f"[SRI - Nivel 3] Mesaj: {mesaj}")
        else:
            super().trateaza(nivel, mesaj)

class PolitieHandler(Handler):
    def trateaza(self, nivel, mesaj):
        if nivel == 4:
            print(f"[Politie - Nivel 4] Mesaj: {mesaj}")
        else:
            super().trateaza(nivel, mesaj)

class PazniciHandler(Handler):
    def trateaza(self, nivel, mesaj):
        if nivel == 5:
            print(f"[Paznici - Nivel 5] Mesaj: {mesaj}")
        else:
            print("Mesaj neprocesat: Nivel necunoscut.")

def main():
    # Creare lant: Nato -> Csat -> Sie -> Sri -> Politie -> Paznici
    nato = NatoHandler()
    csat = CsatHandler()
    sie = SieHandler()
    sri = SriHandler()
    politie = PolitieHandler()
    paznici = PazniciHandler()

    # Legam nodurile intre ele
    nato.set_succesor(csat).set_succesor(sie).set_succesor(sri).set_succesor(politie).set_succesor(paznici)

    # Simulare mesaje
    nato.trateaza(5, "Vizitator suspect in muzeu")
    nato.trateaza(0, "Atac iminent")
    nato.trateaza(3, "Spionaj cibernetic")

if __name__ == "__main__":
    main()