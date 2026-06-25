import kotlin.random.Random

// SOLID: Single Responsibility - Clasa calculeaza doar produsul cartezian si atat.
class CalculatorCartezian {
    fun genereazaSiCalculeaza() {
        // Generam seturile cu numere aleatoare
        val A = List(15) { Random.nextInt(1, 100) }.toSet()
        val B = List(15) { Random.nextInt(1, 100) }.toSet()
        
        println("A = $A")
        println("B = $B")
        
        // A x B utilizand lambda calcul si functiile standard Kotlin peste colectii (flatMap + map)
        val produsCartezian = A.flatMap { a -> 
            B.map { b -> Pair(a, b) } 
        }.toSet()
        
        println("\\nProdusul Cartezian A x B a generat ${produsCartezian.size} perechi (elemente).")
        println("Exemplu primele 5 perechi din colectie:")
        produsCartezian.take(5).forEach { println(it) }
    }
}

fun main() {
    println("--- Executie Kot57 (Lambda pe Colectii Aleatoare) ---")
    val calc = CalculatorCartezian()
    calc.genereazaSiCalculeaza()
}
