// SOLID: Dependency Inversion Principle (DIP) si Open/Closed Principle (OCP)
// Functia unica `operatieAfisare` depinde doar de abstractia `Afisabil`.
// Putem oricand adauga adaptoare pentru alte structuri complexe (de ex. un Map) fara a atinge clientul.

interface Afisabil {
    fun afiseaza()
}

// Adaptor ce inveleste un tip de date primitiv / simplu
class AdaptorSimplu(val data: Any) : Afisabil {
    override fun afiseaza() {
        println("[Tip Simplu] Valoare: $data")
    }
}

// Adaptor ce inveleste o structura de tip colectie
class AdaptorColectie(val data: Collection<*>) : Afisabil {
    override fun afiseaza() {
        println("[Tip Colectie] Valori: ${data.joinToString(" | ")}")
    }
}

// Operatia unica din cerinta care primeste doar obiectul general prin intermediul interfetei
fun operatieAfisare(element: Afisabil) {
    element.afiseaza()
}

fun main() {
    println("--- Executie Kot70 (Adapter Pattern) ---")
    
    val valoareInt = AdaptorSimplu(100)
    val valoareString = AdaptorSimplu("Salut SOLID")
    val listaComplexe = AdaptorColectie(listOf(1, 2, 3, "Patru", 5.0))
    
    operatieAfisare(valoareInt)
    operatieAfisare(valoareString)
    operatieAfisare(listaComplexe)
}
