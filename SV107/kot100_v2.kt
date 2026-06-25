import java.util.concurrent.ConcurrentHashMap

// EXPLICATII SOLID:
// Single Responsibility Principle - Bariera e izolata, raspunzand exclusiv de logica de sincronizare (wait, notifyAll).
// Principiul Inversiunii Dependentei (Dependency Inversion) - Subrutinele nu controleaza direct alte fire. 
//  Comunicarea se face prin contractul metodei `asteapta()` din `Bariera`.

class Bariera(private val numarAsteptat: Int) {
    private var fireAjunse = 0

    @Synchronized
    fun asteapta() {
        fireAjunse++
        if (fireAjunse == numarAsteptat) {
            println("[Bariera-Sync] Toate cele $numarAsteptat fire si-au terminat calculele partiale. Deblocam executia...")
            // Notificam toate firele aflate in stare de Wait!
            (this as Object).notifyAll()
        } else {
            println("[Bariera-Sync] Un fir a ajuns si intra in starea Wait... ($fireAjunse / $numarAsteptat)")
            // Blocare fir curent (Monitor Object)
            (this as Object).wait()
        }
    }
}

class FirSuma(val nume: String, private val start: Int, private val end: Int, private val map: ConcurrentHashMap<Int, Int>, private val bariera: Bariera) : Thread(nume) {
    var sumaLocala = 0

    override fun run() {
        for (i in start..end) {
            val v = map[i] ?: 0
            sumaLocala += v
        }
        println("[$nume] A calculat suma $sumaLocala pe intervalul [$start, $end]. Asteapta la bariera...")
        
        // Ne oprim in bariera pentru a nu avansa haotic in logica principala a aplicatiei
        bariera.asteapta()
        
        println("[$nume] Permisiune primita post-bariera. Incheiere operatiuni fir.")
    }
}

fun main() {
    println("--- Executie Kot100_v2 (Bariera Custom prin Object.wait / notifyAll) ---")
    val dict = ConcurrentHashMap<Int, Int>()
    for (i in 1..20) dict[i] = i * 10
    
    // Vom avea 2 fire si bariera asteapta 2 actiuni de la ele
    val bariera = Bariera(2)
    
    val firA = FirSuma("Thread-A", 1, 10, dict, bariera)
    val firB = FirSuma("Thread-B", 11, 20, dict, bariera)
    
    firA.start()
    firB.start()
    
    firA.join()
    firB.join()
    
    println("\\n[Procesul Principal] Ambele fire s-au strans, bariera a picat, suma paralela cumulata este: ${firA.sumaLocala + firB.sumaLocala}")
}
