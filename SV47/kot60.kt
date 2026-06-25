// SOLID: Single Responsibility Principle
// Clasa incapsuleaza logica matematica (A x B) U (B x B) si maparea ei in dictionar.

class OperatiiReuniune {
    fun calculeaza() {
        val A = (1..20).toSet()
        val B = (10..29).toSet()

        // Calcul A x B (Produs Cartezian folosind functii specifice de colectii: flatMap, map)
        val AxB = A.flatMap { a -> B.map { b -> Pair(a, b) } }.toSet()
        
        // Calcul B x B
        val BxB = B.flatMap { b1 -> B.map { b2 -> Pair(b1, b2) } }.toSet()
        
        // Reuniune (A x B) U (B x B)
        val reuniune = AxB.union(BxB)
        
        // Rezultatul depus intr-un dictionar. 
        // Observatie: Intr-un dictionar cheile sunt unice. Prin `associate` cand exista mai multe perechi 
        // cu aceeasi prima valoare, se va suprascrie si ramane doar ultima in dictionar.
        val dictionar = reuniune.associate { it.first to it.second }
        
        println("Dimensiune A x B: ${AxB.size} perechi.")
        println("Dimensiune B x B: ${BxB.size} perechi.")
        println("Dimensiune (A x B) U (B x B) (setul reunit): ${reuniune.size} perechi.")
        println("Dimensiune Dictionar Final: ${dictionar.size} elemente unice.")
        println("Primele 5 elemente din dictionar: ${dictionar.entries.take(5)}")
    }
}

fun main() {
    println("--- Executie Kot60 (Reuniune Produse Carteziene in Kotlin) ---")
    val op = OperatiiReuniune()
    op.calculeaza()
}
