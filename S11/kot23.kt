import java.io.File
import kotlinx.coroutines.*
import java.util.Stack

// --- Memento Pattern ---
// Memento: Stochează starea textului
class TextMemento(val state: List<String>)

// Originator: Documentul de text care este modificat
class TextDocument(var words: MutableList<String>) {
    fun save(): TextMemento {
        return TextMemento(words.toList())
    }
    fun restore(memento: TextMemento) {
        words = memento.state.toMutableList()
    }
    override fun toString(): String = words.joinToString(" ")
}

// Caretaker: Gestionează mementourile pentru Undo
class Caretaker {
    private val istoric = Stack<TextMemento>()
    fun saveState(document: TextDocument) {
        istoric.push(document.save())
    }
    fun undo(document: TextDocument) {
        if (istoric.isNotEmpty()) {
            document.restore(istoric.pop())
        } else {
            println("Nu mai exista actiuni pentru undo.")
        }
    }
}

// --- Observer Pattern ---
interface WordObserver {
    // Returneaza cuvantul corectat sau null daca nu se doreste corectarea
    fun onWordError(wrongWord: String): String?
}

class UserInterfaceObserver : WordObserver {
    override fun onWordError(wrongWord: String): String? {
        // Observatorul "declanseaza intrebarea"
        println("\n[Observer] S-a gasit un cuvant gresit: '$wrongWord'. Introdu forma corecta (sau apasa Enter pentru a ignora, 'undo' pentru a anula ultima corectura):")
        // In mod normal am citi de la tastatura: readLine()
        // Pentru demonstratie automatizata, returnam o corectura "simulata" daca cuvantul e recunoscut:
        return when (wrongWord) {
            "salutt" -> "salut"
            "stdent" -> "student"
            "pogramare" -> "programare"
            "kottlin" -> "kotlin"
            "pytthon" -> "python"
            "undo" -> "undo"
            else -> null
        }
    }
}

class TextChecker {
    private val observers = mutableListOf<WordObserver>()
    fun addObserver(o: WordObserver) { observers.add(o) }
    
    fun notifyError(wrongWord: String): String? {
        for (obs in observers) {
            val response = obs.onWordError(wrongWord)
            if (response != null) return response
        }
        return null
    }
}

// --- Executia principala in Corutina ---
// Nota: Necesita biblioteca kotlinx-coroutines-core pentru compilare!
fun main() = runBlocking {
    val checker = TextChecker()
    checker.addObserver(UserInterfaceObserver())
    val caretaker = Caretaker()
    
    // Incarcare Dictionar
    val dictFile = File("dictionar.txt")
    val dictionar = if (dictFile.exists()) dictFile.readLines().map { it.lowercase() }.toSet()
                    else setOf("salut", "student", "programare", "kotlin", "python")
    
    // Incarcare Text
    val textFile = File("text.txt")
    val rawText = if (textFile.exists()) textFile.readText() else "salutt eu sunt un stdent la examen de pogramare in kottlin si pytthon"
    val doc = TextDocument(rawText.split("\\s+".toRegex()).toMutableList())
    
    println("Text initial: $doc")
    
    // Totul se realizează într-o corutină (launch)
    val job = launch(Dispatchers.Default) {
        var i = 0
        while (i < doc.words.size) {
            val word = doc.words[i]
            val wordLower = word.lowercase()
            
            // Cuvinte ignorate pt simplitate (care nu-s in dictionarul scurt, dar sunt corecte gramatical, de ex "eu", "sunt")
            if (wordLower.length > 3 && !dictionar.contains(wordLower)) {
                // Cuvant gasit in afara dictionarului => presupunem gresit
                val result = checker.notifyError(word)
                
                if (result == "undo") {
                    caretaker.undo(doc)
                    println("--- S-a facut UNDO. Text curent: $doc ---")
                    i-- // Re-verificam pozitia dupa undo
                    continue
                } else if (result != null) {
                    // Memento - salvam inainte de modificare
                    caretaker.saveState(doc)
                    doc.words[i] = result
                    println("Corectat in: $result")
                }
            }
            i++
            delay(100) // Simulare timp procesare corutina
        }
    }
    
    job.join()
    println("\nText final corectat: $doc")
    
    /* EXPLICATII SOLID & UML (in comentarii):
       - Single Responsibility Principle (SRP): TextDocument gestioneaza starea textului, Caretaker tine istoricul, TextChecker notifica. Niciuna nu face munca celeilalte.
       - Open/Closed Principle (OCP): Putem adauga noi observatori (de ex. un LoggerObserver) fara a modifica clasa TextChecker.
       
       DIAGRAMA CLASE SUMARA (UML conceptual):
       [WordObserver] <|.. [UserInterfaceObserver]
       [TextChecker] o--> [WordObserver] (relatie de agregare, Subject-Observer)
       [TextDocument] <.. [TextMemento] (creeaza)
       [Caretaker] o--> [TextMemento] (stocheaza istoricul)
       
       Main (Corutina) foloseste TextChecker si Caretaker pentru a prelucra TextDocument.
    */
}
