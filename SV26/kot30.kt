// SOLID: Single Responsibility Principle
// Clasa ofera exact doua modalitati specifice pentru calculul matematic al sumei.

class Sumator {
    // Apel clasic cu toate argumentele simultan
    fun sumaDirecta(a: Int, b: Int, c: Int): Int {
        return a + b + c
    }

    // Varianta curried, intoarce functii intermediare
    fun sumaCurried(a: Int): (Int) -> ((Int) -> Int) {
        return { b -> 
            { c -> a + b + c }
        }
    }
}

fun main() {
    println("--- Executie Kot30 (Apelare curried vs direct) ---")
    val sumator = Sumator()
    
    val rezultatDirect = sumator.sumaDirecta(5, 10, 15)
    println("Rezultat Direct: $rezultatDirect")
    
    // In currying aplicam functiile pe rand
    val rezultatCurried = sumator.sumaCurried(5)(10)(15)
    println("Rezultat Curried: $rezultatCurried")
}
