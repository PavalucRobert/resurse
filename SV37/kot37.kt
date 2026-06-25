// SOLID: Single Responsibility Principle
// Clasa Applicative se ocupa strict de impachetarea si aplicarea functiilor (aplicative functor pattern).
// OperatiiApplicative izoleaza operatiile matematice.

class Applicative<T>(val valoare: T) {
    // Comportament de Applicative Functor
    fun <R> applyFunc(functie: (T) -> R): Applicative<R> {
        return Applicative(functie(valoare))
    }
}

object OperatiiApplicative {
    fun sumCu(x: Int): (Int) -> Int = { it + x }
    fun mulCu(x: Int): (Int) -> Int = { it * x }
}

fun main() {
    println("--- Executie Kot37 (Applicative Functor / Generics) ---")
    val aplicativ = Applicative(10)
    println("Valoare initiala: ${aplicativ.valoare}")
    
    val rezultat1 = aplicativ.applyFunc(OperatiiApplicative.sumCu(5))
    println("Dupa sumCu(5): ${rezultat1.valoare}")
    
    val rezultat2 = rezultat1.applyFunc(OperatiiApplicative.mulCu(7))
    println("Dupa mulCu(7): ${rezultat2.valoare}")
}
