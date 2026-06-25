import sys

# EXPLICATII SOLID:
# Open/Closed Principle (OCP): Sistemul e deschis pentru extensii. Putem crea oricand 'FatalErrorStrategy' 
# implementand interfata fara a atinge clasele existente.
# Strategy Pattern asigura schimbarea dinamica la runtime a comportamentului in functie de context.

class CustomWarning(Exception): pass
class CustomError(Exception): pass
class CustomCritical(Exception): pass

# --- STRATEGII ---
class ErrorStrategy:
    def handle_error(self, message: str):
        pass

class WarningStrategy(ErrorStrategy):
    def handle_error(self, message: str):
        with open("warnings.txt", "a") as f:
            f.write(f"[WARNING] {message}\\n")
        print(f"Bifat Warning. Scris in fisier.")

class ErrorStrategyImpl(ErrorStrategy):
    def handle_error(self, message: str):
        # 1-error -> afisez la consola si scriu in fisier de erori comune
        print(f"[EROARE COMUNA] {message}")
        with open("common_errors.txt", "a") as f:
            f.write(f"[ERROR] {message}\\n")

class CriticalStrategy(ErrorStrategy):
    def handle_error(self, message: str):
        # 0-critical -> fisier erori grave + oprire
        with open("critical_errors.txt", "a") as f:
            f.write(f"[CRITICAL] {message}\\n")
        print(f"!!! EROARE GRAVA (Nivel 0) !!! Programul este intrerupt: {message}")
        sys.exit(1)

# --- CONTEXT ---
class ErrorHandlerContext:
    def __init__(self, strategy: ErrorStrategy):
        self.strategy = strategy
        
    def set_strategy(self, strategy: ErrorStrategy):
        self.strategy = strategy
        
    def process(self, message: str):
        self.strategy.handle_error(message)

def main():
    print("--- Executie Py339 (Strategy Pattern pentru Erori) ---")
    
    # Simulam erorile cu context switcher
    context = ErrorHandlerContext(WarningStrategy())
    
    try:
        raise CustomWarning("Aceasta este o atentionare minora de configurare.")
    except CustomWarning as w:
        context.set_strategy(WarningStrategy())
        context.process(str(w))
        
    try:
        raise CustomError("Fisierul de configurare nu a fost gasit in /tmp!")
    except CustomError as e:
        context.set_strategy(ErrorStrategyImpl())
        context.process(str(e))
        
    try:
        raise CustomCritical("Kernel Panic - Baza de date a fost corupta!")
    except CustomCritical as c:
        context.set_strategy(CriticalStrategy())
        # Asta va opri sistemul
        try:
            context.process(str(c))
        except SystemExit:
            print("Sistemul s-a oprit cu succes la critical.")
            
if __name__ == "__main__":
    main()
