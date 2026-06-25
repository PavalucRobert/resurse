// Modelare Sala de Laborator cu Kotlin si OOP

// SOLID: Single Responsibility Principle
// -> Clasa 'Echipament' detine si se ocupa DOAR de datele despre sine (nume si ID).
// -> Clasa 'SalaLaborator' se ocupa DOAR de gestiunea (adaugare/eliminare) inventarului.
// Daca schimbam logica inventarului, clasa Echipament nu este afectata.

class Echipament(val nume: String, val id: Int) {
    override fun toString(): String {
        return "Echipament: $nume [ID: $id]"
    }
}

class SalaLaborator(val nume: String) {
    // Lista mutabila pentru a permite operatii pe obiecte
    private val inventar = mutableListOf<Echipament>()

    fun adaugaEchipament(e: Echipament) {
        inventar.add(e)
        println(" [+] Adaugat: $e in sala '$nume'")
    }

    fun eliminaEchipament(e: Echipament) {
        if (inventar.remove(e)) {
            println(" [-] Eliminat: $e din sala '$nume'")
        } else {
            println(" [!] Eroare: $e nu exista in '$nume'")
        }
    }

    fun afiseazaInventar() {
        println("\n=== Inventar $nume ===")
        if (inventar.isEmpty()) {
            println("Sala este goala.")
        } else {
            for (echipament in inventar) {
                println(" -> $echipament")
            }
        }
        println("=======================\n")
    }
}

fun main() {
    val laborator = SalaLaborator("Laborator Informatica (L1)")
    val pc1 = Echipament("PC Desktop", 101)
    val pc2 = Echipament("PC Desktop", 102)
    val proiector = Echipament("Videoproiector", 201)

    // Adaugam echipamente
    laborator.adaugaEchipament(pc1)
    laborator.adaugaEchipament(pc2)
    laborator.adaugaEchipament(proiector)

    // Afisare dupa adaugare
    laborator.afiseazaInventar()

    // Eliminam un echipament
    laborator.eliminaEchipament(pc2)

    // Afisare inventar actualizat
    laborator.afiseazaInventar()
}
