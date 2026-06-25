// Implementarea conceptului matematic de Functor peste un Map (Dictionar)
// Un functor trebuie sa implementeze operatia "fmap" (aici numita mapValues in stil Kotlin)
// care preia o functie de transformare si returneaza o structura similara fara a o altera pe cea originala.

class MapFunctor<K, V>(val continut: Map<K, V>) {
    
    // Functia de mapare (fmap) primeste un lambda
    fun <R> fmap(transformare: (V) -> R): MapFunctor<K, R> {
        val hartaTransformata = continut.mapValues { entry -> transformare(entry.value) }
        return MapFunctor(hartaTransformata)
    }
}

fun main() {
    println("--- Executie Kot38 (Functor peste HashMap) ---")
    
    // Initializam o harta de date
    val dictionarDate = mapOf("A" to 10, "B" to 20, "C" to 5)
    
    // O punem intr-un Functor
    val functor = MapFunctor(dictionarDate)
    
    // Aplicam transformarea lambda f(x) = 3x - 1 si conversia la String
    val functorRezultat = functor.fmap { x ->
        val calcul = 3 * x - 1
        "Rezultat procesare: $calcul" // se returneaza automat String in lambda
    }
    
    println("Harta initiala: ${functor.continut}")
    println("Dupa aplicarea functorului cu f(x)=3x-1:")
    
    // Afisare elemente
    functorRezultat.continut.forEach { (cheie, valoare) ->
        println("[$cheie] -> $valoare")
    }
}
