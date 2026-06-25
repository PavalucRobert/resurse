// Listă Algebrică (Algebraic Data Type) implementată prin sealed classes
sealed class ListaAlgebrica<out T> {
    object Nil : ListaAlgebrica<Nothing>()
    data class Cons<out T>(val head: T, val tail: ListaAlgebrica<T>) : ListaAlgebrica<T>()
}

// Extensie pentru a itera usor o lista algebrica recursiva
fun <T> ListaAlgebrica<T>.forEach(action: (T) -> Unit) {
    var current = this
    while (current is ListaAlgebrica.Cons) {
        action(current.head)
        current = current.tail
    }
}

// SOLID: Single Responsibility Principle
class Echipament(val nume: String, val inventarId: Int) {
    override fun toString() = "Echipament: $nume [ID: $inventarId]"
}

class SalaLaborator(val nume: String) {
    // Modelam continutul folosind tipul algebric custom
    private var echipamente: ListaAlgebrica<Echipament> = ListaAlgebrica.Nil

    fun adaugaEchipament(e: Echipament) {
        echipamente = ListaAlgebrica.Cons(e, echipamente)
    }

    fun afiseazaInventar() {
        println("\n=== Inventar $nume ===")
        var count = 0
        echipamente.forEach { echipament ->
            println(" -> $echipament")
            count++
        }
        if (count == 0) println("Sala este goala.")
        println("======================\n")
    }
}

fun main() {
    val laborator = SalaLaborator("Laborator Fizica")
    val osciloscop = Echipament("Osciloscop Digital", 1001)
    val multimetru = Echipament("Multimetru Analog", 1002)

    laborator.adaugaEchipament(osciloscop)
    laborator.adaugaEchipament(multimetru)

    laborator.afiseazaInventar()
}
