import kotlin.random.Random

// SOLID: Single Responsibility Principle
// Clasa 'CalculatorSume' are o singura responsabilitate: sa calculeze sumele patratelor cumulative.
class CalculatorSume {
    fun calculeaza(elemente: List<Int>): List<Long> {
        val b = mutableListOf<Long>()
        var sumaCurenta = 0L
        
        for (a in elemente) {
            val patrat = a.toLong() * a.toLong()
            sumaCurenta += patrat
            b.add(sumaCurenta)
        }
        return b
    }
}

fun main() {
    println("--- Testare SV39 Kot53 ---")
    
    // Generam A: 100 de elemente pare aleatoare (intre 2 si 1000)
    val multimeA = List(100) { Random.nextInt(1, 501) * 2 }
    
    val calculator = CalculatorSume()
    val b = calculator.calculeaza(multimeA)
    
    println("Am generat o multime A cu ${multimeA.size} elemente pare.")
    println("Primele 5 elemente din A: ${multimeA.take(5)}")
    println("Primele 5 sume partiale din b_n: ${b.take(5)}")
}
