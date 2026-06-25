// Kot65 - Utilizare functii de transformare specifice si lambda calcul

class GeneratorMultimi {
    fun genereazaA(): Set<Int> {
        val multimeA = mutableSetOf<Int>()
        for (n in 0..1000) {
            val numitor = 2 * n - 9
            if (numitor != 0) {
                val numarator = 8 * n - 18
                if (numarator % numitor == 0) {
                    val x = numarator / numitor
                    if (x >= 0) multimeA.add(x) // Apartine multimii numerelor naturale (N)
                }
            }
        }
        return multimeA
    }

    fun genereazaB(): Set<Int> {
        val multimeB = mutableSetOf<Int>()
        for (n in 0..1000) {
            val numitor = 3 * n - 8
            if (numitor != 0) {
                val numarator = 9 * n * n - 48 * n + 16
                if (numarator % numitor == 0) {
                    val x = numarator / numitor
                    multimeB.add(x) // Apartine multimii numerelor intregi (Z)
                }
            }
        }
        return multimeB
    }
}

fun main() {
    println("--- Executie Kot65 ---")
    val generator = GeneratorMultimi()
    
    val A = generator.genereazaA()
    val B = generator.genereazaB()
    println("A: $A")
    println("B: $B")
    
    // Produsul cartezian (A x B) 
    val produsCartezian = A.flatMap { a -> B.map { b -> Pair(a, b) } }.toSet()
    
    // Intersectia (B ∩ A)
    val intersectie = B.intersect(A)
    
    // Uniunea (A x B) U (B ∩ A) 
    // Tipul de date va fi Any deoarece avem perechi pe de-o parte si numere pe de alta.
    val reuniuneFinala: Set<Any> = produsCartezian.union(intersectie)
    
    // Depus intr-un HashMap si afisat
    val hashMapRezultat = hashMapOf<Int, Any>()
    reuniuneFinala.forEachIndexed { index, element -> 
        hashMapRezultat[index] = element
    }
    
    println("Hashmap-ul rezultat are ${hashMapRezultat.size} elemente.")
    println("Test afisare element index 0: ${hashMapRezultat[0]}")
}
