import datetime

# --- PATTERN OBSERVER ---
# SOLID: Open/Closed Principle - Daca dorim inca un mod de monitorizare (exemplu pe Email),
# cream EmailLogger(Observer) fara a altera clasele existente!

class Observer:
    def update(self, mesaj: str):
        pass

class FileLogger(Observer):
    def __init__(self, fisier_jurnal: str):
        self.fisier_jurnal = fisier_jurnal

    def update(self, mesaj: str):
        with open(self.fisier_jurnal, "a") as f:
            f.write(mesaj + "\n")
        print(f"[Logger a inregistrat] {mesaj}")

class Subject:
    def __init__(self):
        self._observers = []

    def adauga_observator(self, obs: Observer):
        self._observers.append(obs)

    def notifica_observatori(self, mesaj: str):
        for obs in self._observers:
            obs.update(mesaj)

# --- OBIECTUL PRINCIPAL (TARGET) ---
# SOLID: Single Responsibility Principle - Se ocupa doar de logica financiara.
class RecalcularePret(Subject):
    def __init__(self, pret_initial: float):
        super().__init__()
        self.pret = pret_initial
    
    def aplica_reducere(self, user: str, rata_reducere: float):
        pret_vechi = self.pret
        self.pret = self.pret - (self.pret * rata_reducere / 100)
        
        data_curenta = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mesaj = f"User: {user} | Data: {data_curenta} | Modificare pret: Reducere {rata_reducere}% de la {pret_vechi} la {self.pret}"
        
        # Observatorul (Logger) intra in actiune aici!
        self.notifica_observatori(mesaj)

# --- PATTERN PROXY ---
# Actioneaza ca un Firewall. Controleaza accesul spre obiectul real.
class ProxyRecalculare:
    def __init__(self, obiect_real: RecalcularePret):
        self.obiect_real = obiect_real
        self.utilizatori_autorizati = {
            "admin": "parola123",
            "manager": "securitate"
        }
        
    def aplica_reducere(self, user: str, parola: str, rata_reducere: float):
        if user in self.utilizatori_autorizati and self.utilizatori_autorizati[user] == parola:
            print(f"\n[{user}] Autentificare reușită.")
            self.obiect_real.aplica_reducere(user, rata_reducere)
        else:
            print(f"\n[{user}] Eroare de autentificare. Acces respins.")

def main():
    obiect_real = RecalcularePret(pret_initial=1000.0)
    
    # Atasam fisierul jurnal automat la logica pretului
    logger = FileLogger("jurnal_operatii.txt")
    obiect_real.adauga_observator(logger)
    
    # Introducem scutul Proxy
    proxy = ProxyRecalculare(obiect_real)
    
    # Testare
    proxy.aplica_reducere("hacker", "parola1", 50)
    proxy.aplica_reducere("admin", "parola123", 10)

if __name__ == "__main__":
    main()
