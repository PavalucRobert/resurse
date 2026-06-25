// SOLID: SRP - logica matematica este extrasa in extensii / functii pure pentru seturi.

fun runKot63() {
    println("--- Executie Kot63 (Produs Cartezian si Reuniune) ---")
    
    // Generam multimile A si B (20 elemente fiecare)
    val A = (1..20).toSet()
    val B = (21..40).toSet()
    
    // B U A (Reuniune)
    val B_reuniune_A = B.union(A)
    
    // A x B (Produs Cartezian)
    val AxB = A.flatMap { a -> B.map { b -> Pair(a, b) } }.toSet()
    
    // (A x B) x (B U A)
    // Deoarece multimile sunt mari (400 * 40 = 16000 elemente), vom lua doar primele 5 
    // pentru a popula dictionarul demonstrativ, altfel output-ul explodeaza.
    
    val rezultatCalcul = AxB.flatMap { perecheAxB -> 
        B_reuniune_A.map { elementReuniune -> 
            Pair(perecheAxB, elementReuniune) 
        } 
    }.take(5) // luam 5 elemente sa nu blocam consola
    
    // Depunere intr-un dictionar
    val dictionar = rezultatCalcul.associate { (pereche, element) ->
        "((A=${pereche.first}, B=${pereche.second}) x $element)" to Pair(pereche, element)
    }
    
    println("S-a calculat (AxB)x(BUA). Dimensiune totala teoretica: ${AxB.size * B_reuniune_A.size}")
    println("Dictionar (primele 5 elemente demonstrative):")
    dictionar.forEach { (cheie, valoare) ->
        println("Cheie: $cheie -> Valoare: $valoare")
    }
}
