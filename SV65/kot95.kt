// EXPLICATIE SOLID:
// Single Responsibility Principle (SRP): Clasa 'SalaDeCurs' are doar responsabilitatea gestionarii
// resurselor interne ale salii. Orice alta operatie (ex: facturare) va trebui scrisa in alta clasa.
// Open/Closed Principle: Enum-ul tipurilor de echipament permite adaugarea usoara de noi modele
// fara a distruge structura existenta a functiilor adauga/sterge.

enum class TipEchipament {
    PROIECTOR, TABLA_INTELIGENTA, CALCULATOR, BANCUTA, CATEDRA
}

class SalaDeCurs(val nume: String) {
    // Folosim o harta (Map) incapsulata pentru stocarea datelor referitoare la obiecte
    private val echipamente = mutableMapOf<TipEchipament, Int>()

    fun adaugaEchipament(tip: TipEchipament, cantitate: Int) {
        val curent = echipamente.getOrDefault(tip, 0)
        echipamente[tip] = curent + cantitate
    }

    fun stergeEchipament(tip: TipEchipament, cantitate: Int): Boolean {
        val curent = echipamente.getOrDefault(tip, 0)
        if (curent >= cantitate) {
            echipamente[tip] = curent - cantitate
            return true
        }
        return false // Eroare, nu poti sterge ceva ce nu ai in cantitatea respectiva
    }

    fun afiseazaInventar() {
        println("--- Inventar $nume ---")
        if (echipamente.isEmpty()) {
            println("Sala este goala.")
        } else {
            for ((tip, cant) in echipamente) {
                println("- $tip: $cant bucati")
            }
        }
        println("----------------------")
    }
}

fun main() {
    println("--- Executie Kot95 (OOP Sala Curs cu Enum) ---")
    val sala = SalaDeCurs("Laborator Informatica (L201)")
    
    sala.adaugaEchipament(TipEchipament.CALCULATOR, 30)
    sala.adaugaEchipament(TipEchipament.TABLA_INTELIGENTA, 1)
    sala.adaugaEchipament(TipEchipament.PROIECTOR, 1)
    
    sala.afiseazaInventar()
    
    sala.stergeEchipament(TipEchipament.CALCULATOR, 5) // Scoatem 5 defecte la reparat
    sala.afiseazaInventar()
}
