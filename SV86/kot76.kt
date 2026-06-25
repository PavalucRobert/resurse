import java.io.File
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

// SOLID: Observer Pattern pentru extinderea functionalitatilor (ca Logger-ul)
// OCP: Daca vrem inca o notificare pe SMS, facem alt observer, nu spargem clasele curente!

interface Observer {
    fun update(message: String)
}

class FileLogger(private val fileName: String) : Observer {
    override fun update(message: String) {
        val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
        val timestamp = LocalDateTime.now().format(formatter)
        val logEntry = "[$timestamp] $message\\n"
        
        File(fileName).appendText(logEntry)
        println("Logger: Scris in fisier log '$fileName'")
    }
}

interface Subject {
    fun adaugaObserver(obs: Observer)
    fun notifica(mesaj: String)
}

interface IRecalculare {
    fun aplicaReducere(procent: Double, user: String)
}

class RecalcularePret(private var pretBaza: Double) : IRecalculare, Subject {
    private val observeri = mutableListOf<Observer>()

    override fun adaugaObserver(obs: Observer) {
        observeri.add(obs)
    }

    override fun notifica(mesaj: String) {
        for (obs in observeri) {
            obs.update(mesaj)
        }
    }

    override fun aplicaReducere(procent: Double, user: String) {
        val pretVechi = pretBaza
        pretBaza -= pretBaza * (procent / 100.0)
        
        val mesaj = "Userul $user a modificat pretul din $pretVechi in $pretBaza (reducere $procent%)"
        notifica(mesaj)
    }
}

class ProxyRecalculare(private val realSubject: RecalcularePret) : IRecalculare {
    private val adminCredentials = mapOf("admin" to "secreta123", "manager" to "1234")

    override fun aplicaReducere(procent: Double, user: String) {
        // Simulare validare parola (aici s-ar trimite si un hash/parola efectiv, dar respectam cerinta conceptual)
        if (adminCredentials.containsKey(user)) {
            println("Proxy: Acces validat pentru user '$user'.")
            realSubject.aplicaReducere(procent, user)
        } else {
            println("Proxy: ACCES INTERZIS! User '$user' nu are drepturi.")
            realSubject.notifica("Acces Neautorizat Respins pentru utilizatorul: $user")
        }
    }
}

fun main() {
    println("--- Executie Kot76 (Proxy + Observer Logger) ---")
    
    val fisierLog = "operatii_pret.txt"
    val obiectBaza = RecalcularePret(1000.0)
    
    val logger = FileLogger(fisierLog)
    obiectBaza.adaugaObserver(logger)
    
    val proxy = ProxyRecalculare(obiectBaza)
    
    // User ok
    proxy.aplicaReducere(20.0, "admin")
    
    // User invalid
    proxy.aplicaReducere(50.0, "hacker")
}
