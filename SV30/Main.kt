import java.io.File

// SOLID: Single Responsibility Principle - Nodul stocheaza doar datele (cuvantul).
class Nod(val cuvant: String) {
    var stanga: Nod? = null
    var dreapta: Nod? = null
}

// Clasa specifica pentru Arbore (gestioneaza logica de ordonare alfabetica)
class ArboreBinar {
    var radacina: Nod? = null

    // Constrangere: adaugam cuvintele in ordine alfabetica
    fun adauga(cuvant: String) {
        radacina = adaugaRecursiv(radacina, cuvant)
    }

    private fun adaugaRecursiv(nodCurent: Nod?, cuvant: String): Nod {
        if (nodCurent == null) {
            return Nod(cuvant)
        }
        if (cuvant < nodCurent.cuvant) {
            nodCurent.stanga = adaugaRecursiv(nodCurent.stanga, cuvant)
        } else if (cuvant > nodCurent.cuvant) {
            nodCurent.dreapta = adaugaRecursiv(nodCurent.dreapta, cuvant)
        }
        return nodCurent
    }
}

// SOLID: Open/Closed Principle - putem adauga alti functori (alte reguli de afisare) fara sa modificam Arborele.
// Clasa specifica tip "Functor" (in Kotlin il simulam cu operatorul invoke)
class FunctorAfisare {
    operator fun invoke(nod: Nod?) {
        if (nod != null) {
            this(nod.stanga)
            println(nod.cuvant) // Vizitare In-Order pentru afisare sortata
            this(nod.dreapta)
        }
    }
}

fun main() {
    // 1. Creare fisier test "date.txt"
    val fisier = File("date.txt")
    fisier.writeText("acesta este un test simplu pentru arborele binar scris in kotlin")

    // 2. Extragere cuvinte si adaugare in arbore
    val arbore = ArboreBinar()
    val cuvinte = fisier.readText().split(" ")
    for (c in cuvinte) {
        arbore.adauga(c)
    }

    // 3. Utilizarea Functorului pentru afisare
    val afiseaza = FunctorAfisare()
    println("--- Cuvintele in ordine alfabetica ---")
    afiseaza(arbore.radacina)
}
