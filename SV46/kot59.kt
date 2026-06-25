// SOLID: Single Responsibility Principle
// Clasa incapsuleaza strict algoritmul calculului matematic pentru produs cartezian
// folosind API-ul Kotlin.

class OperatiiMultimi {
    fun calculeazaIntersectieProduse() {
        // Cele 2 multimi cu 20 de elemente fiecare (initializate cu numere)
        val A = (1..20).toSet()
        val B = (10..29).toSet()
        
        println("A = $A")
        println("B = $B")
        
        // Calcul Produs Cartezian A x B utilizand lambda
        val AxB = A.flatMap { a -> B.map { b -> Pair(a, b) } }.toSet()
        
        // Calcul Produs Cartezian B x A
        val BxA = B.flatMap { b -> A.map { a -> Pair(b, a) } }.toSet()
        
        // Intersectia (A x B) ∩ (B x A)
        // Se va observa ca vor ramane doar perechile cu elemente din sectiunea comuna a lui A si B
        val intersectie = AxB.intersect(BxA)
        
        // Salvam in dictionar (Map) elementele rezultate, transformate in K-V
        val dictionarRezultat = intersectie.associate { it.first to it.second }
        
        println("\\nRezultatul intersectiei sub forma de dictionar:")
        dictionarRezultat.forEach { (cheie, valoare) ->
            println("Dictionar: [$cheie] -> $valoare")
        }
        
        println("Total perechi ramase in map: ${dictionarRezultat.size}")
    }
}

fun main() {
    println("--- Executie Kot59 (Lambda Calcul Colectii: Intersectie Produs Cartezian) ---")
    val operatii = OperatiiMultimi()
    operatii.calculeazaIntersectieProduse()
}
