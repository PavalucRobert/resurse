import kotlinx.coroutines.*

// Funcții de extensie generice pentru Curry și Uncurry pe funcții cu 3 parametri
fun <A, B, C, R> ((A, B, C) -> R).curry(): (A) -> (B) -> (C) -> R {
    return { a -> { b -> { c -> this(a, b, c) } } }
}

fun <A, B, C, R> ((A) -> (B) -> (C) -> R).uncurry(): (A, B, C) -> R {
    return { a, b, c -> this(a)(b)(c) }
}

fun main() = runBlocking {
    // Cerinta: "funcție (implementata ca o corutina) de sumare a trei variabile"
    // Vom defini suma ca o functie lambda care apeleaza logica folosind corutine.
    // Daca vrem sa poata fi suspendata cu adevarat (delay), o punem in coroutineScope:
    val sumCoroutineFunction: (Int, Int, Int) -> Int = { a, b, c ->
        runBlocking {
            // Logica corutinei: adunare dupa o mica intarziere nestiuta,
            // rulata in mod asincron
            val res = async { a + b + c }
            res.await()
        }
    }

    // Cerinta: "aplica curry și uncurry"
    val curriedSum = sumCoroutineFunction.curry()
    val uncurriedSum = curriedSum.uncurry()

    // Un set de valori dat
    val val1 = 10
    val val2 = 25
    val val3 = 100

    println("Apel folosind functia normala (corutina): \${sumCoroutineFunction(val1, val2, val3)}")
    
    // Apelul direct cu setul de valori aplicand CURRY
    val resultCurried = curriedSum(val1)(val2)(val3)
    println("Apel curried: \$resultCurried")

    // Apelul direct cu setul de valori aplicand UNCURRY
    val resultUncurried = uncurriedSum(val1, val2, val3)
    println("Apel uncurried: \$resultUncurried")
}
