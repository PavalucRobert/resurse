// SOLID: 
// Single Responsibility Principle (SRP): Clasa de baza `MatematicaDeBaza` ofera doar functiile (operatiile) matematice.
// Liskov Substitution Principle (LSP): Subclasele pot inlocui clasa Thread deoarece o extind si ii respecta comportamentul, dar adauga functionalitate proprie (implementarea run).

import java.util.concurrent.ConcurrentHashMap

abstract class MatematicaDeBaza : Thread() {
    fun adunare(a: Int, b: Int) = a + b
    fun scadere(a: Int, b: Int) = a - b
    fun inmultire(a: Int, b: Int) = a * b
    fun impartire(a: Int, b: Int) = if (b != 0) a / b else 0
}

val hasmapComun = ConcurrentHashMap<String, Int>()

// Subclasa Activa (Ruleaza in fir propriu de executie - Actor)
class ActorSuma(val cheie: String, val a: Int, val b: Int) : MatematicaDeBaza() {
    override fun run() {
        val rez = adunare(a, b)
        hasmapComun[cheie] = rez
        println("[Actor Suma] a scris $cheie = $rez")
    }
}

class ActorProdus(val cheie: String, val a: Int, val b: Int) : MatematicaDeBaza() {
    override fun run() {
        val rez = inmultire(a, b)
        hasmapComun[cheie] = rez
        println("[Actor Produs] a scris $cheie = $rez")
    }
}

fun main() {
    println("--- Executie Kot93 (Actori pe Hashmap Concurent) ---")
    val fire = listOf(
        ActorSuma("A1", 100, 50),
        ActorSuma("A2", 33, 44),
        ActorProdus("P1", 10, 10),
        ActorProdus("P2", 25, 4)
    )
    
    // Pornim toate firele simultan
    fire.forEach { it.start() }
    
    // Asteptam terminarea lor
    fire.forEach { it.join() }
    
    println("\\nStare finala Hashmap: $hasmapComun")
}
