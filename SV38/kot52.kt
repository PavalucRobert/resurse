// SOLID: Single Responsibility Principle 
// Clasa contine doar logica matematica de combinatorica si analiza de multimi.

class AnalizatorSubmultimi {
    // Calcul de combinari C(n, k) pentru aflarea numarului de submultimi
    fun combinari(n: Long, k: Long): Long {
        if (k > n) return 0
        var rezultat = 1L
        for (i in 1..k) {
            rezultat = rezultat * (n - i + 1) / i
        }
        return rezultat
    }

    fun rezolva() {
        // Multimea de baza: A = {1, 2, ..., 100}
        val A = (1..100).toList()
        
        // INTERPRETAREA CERINTEI:
        // Expresia "care contin elementul 1 (in componenta numarului)"
        // sugereaza filtrarea numerelor care au CIFRA 1 in ele (ex: 1, 10, 11, etc.)
        
        // Aplicam operatii lambda si filtrari specifice peste colectia originala
        val numereCuCifra1 = A.filter { num -> num.toString().contains("1") }
        
        val n = numereCuCifra1.size.toLong()
        // Numarul de submultimi de 4 elemente posibile doar cu aceste numere este C(n, 4)
        val numarSubmultimiCifra1 = combinari(n, 4)
        
        // Alternativ: Daca cerinta se referea la "Submultimile de 4 din A care contin fix numarul intreg '1'"
        // Atunci luam fix elementul '1', si mai trebuie sa alegem 3 elemente din restul de 99.
        val numarSubmultimiNumarul1 = combinari(99, 3)
        
        println("Analiza Multimi:")
        println("Avem ${numereCuCifra1.size} numere care contin cifra '1' (ex: 1, 10, 11, 21...)")
        println("-> Submultimi de 4 elemente formate din ele: $numarSubmultimiCifra1")
        println("\\n-> Alternativa (submultimi din A ce contin obligatoriu valoarea intreaga 1): $numarSubmultimiNumarul1")
    }
}

fun main() {
    println("--- Executie Kot52 (Combinatorica ADT) ---")
    val analizator = AnalizatorSubmultimi()
    analizator.rezolva()
}
