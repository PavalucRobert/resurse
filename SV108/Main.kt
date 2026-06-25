import java.util.concurrent.ConcurrentHashMap

// SOLID: Single Responsibility Principle - Aceasta clasa are o singura responsabilitate: sa stocheze si sa returneze rezultate gata calculate, evitand munca repetitiva.
// SOLID: Open/Closed Principle - Clasa e generica (T, R) si primeste functia de calcul ca parametru. Se poate refolosi usor pentru orice alta formula.

class Memoizator<T, R>(private val functieCalcul: (T, (T) -> R) -> R) {
    // ConcurrentHashMap ne asigura accesul thread-safe in caz de multi-threading
    private val memorie = ConcurrentHashMap<T, R>()

    fun calculeaza(parametru: T): R {
        // computeIfAbsent stocheaza rezultatul in "memorie" daca nu exista, sau il preia direct daca a fost calculat deja.
        return memorie.computeIfAbsent(parametru) { cheie ->
            functieCalcul(cheie) { recursiv -> this.calculeaza(recursiv) }
        }
    }
}

fun main() {
    // Definim logica Fibonacci pentru f(i) = f(i-1) + f(i-2)
    val fibonacci = Memoizator<Int, Long> { n, apelRecursiv ->
        if (n <= 1) {
            n.toLong()
        } else {
            apelRecursiv(n - 1) + apelRecursiv(n - 2)
        }
    }

    println("Calculam seria Fibonacci cu Memoizare folosind ConcurrentHashMap:")
    for (i in 0..10) {
        println("f($i) = ${fibonacci.calculeaza(i)}")
    }
}