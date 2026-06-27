import itertools

# Cerinta: "generator creat de programator să se genereze automat nume de fișiere temporare"
def file_name_generator(s1, s2):
    """
    Generator care foloseste functii din itertools pentru a produce index-ul.
    Returneaza sirul de caractere sub forma 's1-index-s2.tmp'.
    """
    # Utilizam itertools.count() pentru un numarator infinit incepand de la 1
    for index in itertools.count(1):
        yield f"{s1}-{index}-{s2}.tmp"

# Cerinta: "Metoda va primi, verifica unde a rămas generatorul și va întoarce următorul nume."
def get_next_filename(gen):
    """
    Metoda care primeste generatorul creat. Cand este apelata cu 'next()',
    sistemul stie unde a ramas generatorul automat in interiorul sau si ofera valoarea urmatoare.
    """
    return next(gen)

def main():
    # Primim numele la apelul metodei generatoare
    prefix = "log"
    sufix = "sesiune"
    generator_fisiere = file_name_generator(prefix, sufix)
    
    # Testam metoda verificand de 5 ori unde a ramas
    print("Testam generarea de nume de fisiere cu metoda `get_next_filename`:")
    for _ in range(5):
        urmatorul = get_next_filename(generator_fisiere)
        print(f"Urmatorul fisier generat este: {urmatorul}")

if __name__ == "__main__":
    main()
