import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.locks.ReentrantLock
import kotlin.concurrent.thread
import kotlin.concurrent.withLock

// Clasa de baza pentru operatii
open class Operatie(val harta: ConcurrentHashMap<String, Int>, val mutex: ReentrantLock)

// Subclasa activa pentru adunare
class Adunare(harta: ConcurrentHashMap<String, Int>, mutex: ReentrantLock) : Operatie(harta, mutex) {
    fun executa() {
        mutex.withLock {
            val a = harta["a"] ?: 0
            val b = harta["b"] ?: 0
            harta["suma"] = a + b
            println("Am adunat $a + $b = ${harta["suma"]}")
        }
    }
}

// Subclasa activa pentru inmultire
class Inmultire(harta: ConcurrentHashMap<String, Int>, mutex: ReentrantLock) : Operatie(harta, mutex) {
    fun executa() {
        mutex.withLock {
            val a = harta["a"] ?: 0
            val b = harta["b"] ?: 0
            harta["produs"] = a * b
            println("Am inmultit $a * $b = ${harta["produs"]}")
        }
    }
}

fun main() {
    val hartaComuna = ConcurrentHashMap<String, Int>()
    hartaComuna["a"] = 10
    hartaComuna["b"] = 5
    
    val mutex = ReentrantLock()

    // Cele doua obiecte active
    val opAdunare = Adunare(hartaComuna, mutex)
    val opInmultire = Inmultire(hartaComuna, mutex)

    // Lansam firele de executie (procesare simultana)
    val fir1 = thread { opAdunare.executa() }
    val fir2 = thread { opInmultire.executa() }

    // Asteptam terminarea firelor
    fir1.join()
    fir2.join()

    println("Rezultat final harta: $hartaComuna")
}

// Principiul SOLID aplicat aici: 
// - Single Responsibility Principle: Fiecare clasa are un singur scop (clasa Adunare doar aduna, clasa Inmultire doar inmulteste).
// - Open/Closed Principle: Putem adauga usor o clasa Impartire fara a modifica logica de baza.
