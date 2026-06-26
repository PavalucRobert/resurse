import multiprocessing
import time
import sys

# --- Mediator Pattern ---
# Mediator: Interfata Mediator defineste metoda de trimitere a mesajelor.
# Colleague: Clasele Profesor, Asistent, Student interactioneaza DOAR cu Mediatorul.
# Asistentul joaca rol de Mediator Concret, primind mesaje din cozi si rutandu-le.

class ParticipantProcess(multiprocessing.Process):
    def __init__(self, name, in_queue, out_queue):
        super().__init__()
        self.pname = name
        self.in_queue = in_queue    # De unde citeste mesaje
        self.out_queue = out_queue  # Unde trimite mesaje (catre Mediator)

    def run(self):
        # Definit de subclase
        pass

class Student(ParticipantProcess):
    def run(self):
        # Studentul trimite o intrebare catre profesor prin asistent
        print(f"[{self.pname}] Trimite intrebare catre Profesor...")
        self.out_queue.put({"from": self.pname, "to": "Profesor", "msg": "Cum aplicam SOLID la Mediator?"})
        
        # Asteapta raspuns
        response = self.in_queue.get()
        print(f"[{self.pname}] A primit raspuns: {response['msg']}")

class Profesor(ParticipantProcess):
    def run(self):
        # Profesorul asteapta intrebari si raspunde
        while True:
            req = self.in_queue.get()
            if req['msg'] == 'EXIT':
                break
            print(f"[{self.pname}] A primit de la {req['from']}: {req['msg']}")
            time.sleep(0.5) # Timp de gandire
            
            # Raspunde
            raspuns = "Mediatorul decupleaza obiectele colineare, respectand SRP."
            print(f"[{self.pname}] Trimite raspuns catre {req['from']}...")
            self.out_queue.put({"from": self.pname, "to": req['from'], "msg": raspuns})

class AsistentMediator(multiprocessing.Process):
    def __init__(self, in_queue, routing_table):
        super().__init__()
        self.in_queue = in_queue
        self.routing_table = routing_table # Dictionar: Nume -> Queue
        
    def run(self):
        print("[Asistent] Mediatorul a pornit si este gata sa ruteze mesaje.")
        active_students = len([k for k in self.routing_table.keys() if "Student" in k])
        
        while active_students > 0:
            msg = self.in_queue.get()
            sender = msg['from']
            target = msg['to']
            
            print(f"  [Asistent (Mediator)] Ruteaza mesaj de la {sender} catre {target}")
            if target in self.routing_table:
                self.routing_table[target].put(msg)
            
            # Daca e un raspuns pentru student, presupunem ca acel student a terminat
            if "Student" in target:
                active_students -= 1
                
        # Oprim profesorul
        self.routing_table["Profesor"].put({"from": "System", "to": "Profesor", "msg": "EXIT"})
        print("[Asistent] Toate mesajele au fost procesate. Mediator se opreste.")

if __name__ == "__main__":
    # Coada principala a mediatorului (Asistentul citeste de aici)
    mediator_queue = multiprocessing.Queue()
    
    # Cozile individuale (unde participantii asculta mesaje primite)
    prof_q = multiprocessing.Queue()
    s1_q = multiprocessing.Queue()
    s2_q = multiprocessing.Queue()
    
    # Routing table
    routing_table = {
        "Profesor": prof_q,
        "Student1": s1_q,
        "Student2": s2_q
    }
    
    # Creare participanti (Colectie Colleague)
    asistent = AsistentMediator(mediator_queue, routing_table)
    prof = Profesor("Profesor", prof_q, mediator_queue)
    s1 = Student("Student1", s1_q, mediator_queue)
    s2 = Student("Student2", s2_q, mediator_queue)
    
    # Pornire procese
    asistent.start()
    prof.start()
    s1.start()
    s2.start()
    
    # Asteapta terminarea
    s1.join()
    s2.join()
    prof.join()
    asistent.join()
    print("Sesiunea de mesagerie inter-proces s-a incheiat cu succes.")
    
    """
    EXPLICATII SOLID:
    - SRP (Single Responsibility): Clasa `Profesor` se ocupa doar de logica sa didactica (primeste si da raspunsuri).
      Clasa `AsistentMediator` se ocupa doar de rutarea mesajelor (Mediator). Ele nu se intercaleaza.
    - OCP (Open/Closed): Daca vrem sa adaugam "Student3" sau un "Secretar", extindem clasa ParticipantProcess si adaugam cheia in `routing_table` din main, fara sa modificam codul claselor existente!
    
    DIAGRAMA UML SUMARA:
    [ParticipantProcess] (abstract) <|-- [Profesor]
    [ParticipantProcess] <|-- [Student]
    [AsistentMediator] o--> [routing_table (Participant Queues)]
    
    Profesorul si Studentul interactioneaza bidirectional (Process-uri separate) dar comunica UNIC cu AsistentMediator prin `out_queue`.
    """
