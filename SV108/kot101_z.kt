import java.util.concurrent.ConcurrentHashMap

// Clasa memoizeaza valorile sirului Fibonacci intr-un ConcurrentHashMap.
// SRP: are o singura responsabilitate - calcul + cache pentru f(i) = f(i-1) + f(i-2).
class FibonacciMemoizat {
    private val cache = ConcurrentHashMap<Int, Long>()

    fun calculeaza(n: Int): Long {
        require(n >= 0) { "n trebuie sa fie >= 0" }
        if (n <= 1) return n.toLong()
        
        // if in cache, should be return 
        if (cache.containsKey(n)) {
            return cache[n]!!
        }
        
        // if not in cache, calculate and then store it 
        val rezultat = calculeaza(n - 1) + calculeaza(n - 2)
        cache[n] = rezultat
        return rezultat
    }

    fun dimensiuneCache(): Int = cache.size
}

fun main() {
    val fib = FibonacciMemoizat()
    println("Seria Fibonacci cu memoizare (ConcurrentHashMap):")
    for (i in 0..10) {
        println("f($i) = ${fib.calculeaza(i)}")
    }
    println("Valori salvate in cache: ${fib.dimensiuneCache()}")
}
