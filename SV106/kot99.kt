import java.io.File
import java.util.concurrent.ConcurrentHashMap

// Variabila in memorie comuna protejata la scrieri asincrone concurente
val dictionarComun = ConcurrentHashMap<Int, Int>()

// SOLID: Single Responsibility Principle
class ServerDaemon : Thread() {
    init {
        isDaemon = true // Server tip Daemon
    }

    override fun run() {
        println("[Server Daemon] Ruleaza in fundal...")
        incarcaFisier()
        lanseazaMuncitorii()
    }

    private fun incarcaFisier() {
        val fisier = File("date_numerice.txt")
        if (!fisier.exists()) {
            fisier.writeText("10\\n20\\n30\\n40\\n50\\n60\\n70\\n80")
        }
        val linii = fisier.readLines()
        linii.forEachIndexed { index, valoareStr ->
            dictionarComun[index] = valoareStr.toInt()
        }
        println("[Server Daemon] ${dictionarComun.size} valori incarcate in dicționarul comun.")
    }

    private fun lanseazaMuncitorii() {
        val constanta = 5
        val dimensiune = dictionarComun.size
        val mijloc = dimensiune / 2
        
        // Cream mai multe fire de procese (Worker threads) carora le distribuim subintervale
        val thread1 = WorkerNormal("Muncitor-1", 0, mijloc - 1, constanta)
        val thread2 = WorkerNormal("Muncitor-2", mijloc, dimensiune - 1, constanta)
        
        thread1.start()
        thread2.start()
        
        // Serverul asteapta finalizarea
        thread1.join()
        thread2.join()
        println("[Server Daemon] Procesare finalizata cu succes!")
    }
}

class WorkerNormal(name: String, private val startIdx: Int, private val endIdx: Int, private val constanta: Int) : Thread(name) {
    override fun run() {
        for (i in startIdx..endIdx) {
            val valoare = dictionarComun[i]
            if (valoare != null) {
                val rezultat = valoare * constanta
                dictionarComun[i] = rezultat // Actualizam valoarea concurenta
                println("[${Thread.currentThread().name}] Actualizat index $i: $valoare * $constanta = $rezultat")
            }
        }
    }
}

fun main() {
    println("--- Executie Kot99 (Fire Server Daemon) ---")
    val server = ServerDaemon()
    server.start()
    
    // Serverul daemon ar muri imediat cum termina main-ul, deci il asteptam special pentru logica testului
    server.join()
    
    println("\\n[Main] Dictionarul a fost actualizat perfect de fire: $dictionarComun")
}
