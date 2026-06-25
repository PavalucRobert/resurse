// SOLID: Single Responsibility Principle
// Clasa calculeaza operatiile matematice si nu face nimic altceva.
class CalculatorMultimi {
    fun calculeazaSiAfiseaza(A: Set<Int>, B: Set<Int>): Map<Int, Pair<Int, Int>> {
        // (A ∪ B)
        val reuniune = A.union(B)
        
        // (B ∩ A)
        val intersectie = B.intersect(A)
        
        // Produs cartezian: (A ∪ B) x (B ∩ A)
        // flatMap si map (lambda calcul) ne genereaza toate perechile
        val produsCartezian = reuniune.flatMap { a -> 
            intersectie.map { b -> Pair(a, b) }
        }
        
        // Transformam in dictionar avand cheia ca index si valoarea ca elementul in sine
        val dictionarResultat = produsCartezian.mapIndexed { index, pereche -> 
            index to pereche 
        }.toMap()
        
        return dictionarResultat
    }
}

fun main() {
    println("--- Executie Kot62 ---")
    val multimeaA = (1..20).toSet()     // 20 de elemente
    val multimeaB = (10..29).toSet()    // 20 de elemente
    
    val calculator = CalculatorMultimi()
    val dictionar = calculator.calculeazaSiAfiseaza(multimeaA, multimeaB)
    
    println("Dictionarul rezultat are dimensiunea: ${dictionar.size}")
    
    // Afisam 3 valori ca exemplu
    println("Test afisare index 0 -> ${dictionar[0]}")
    println("Test afisare index 50 -> ${dictionar[50]}")
}
