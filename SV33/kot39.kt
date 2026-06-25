import java.io.File

// SOLID: Single Responsibility Principle
// Clasa curenta face fix o singura operatie clara: prelucrarea textului (Fara a sti de unde vine si cine o apeleaza).

class ProcesorText {
    fun extrageMijloc(caleFisier: String): List<String> {
        val text = File(caleFisier).readText()
        
        // Separam cuvintele (elimina semnele de punctuatie)
        val cuvinte = text.split("\\\\W+".toRegex())
        
        // Utilizare lambda calcul peste colecții:
        // 1. filter: selectează cuvintele care au minimum 4 caractere
        // 2. map: transformă fiecare cuvânt în substring-ul dorit (mijlocul)
        return cuvinte.filter { it.length >= 4 }
            .map { cuvant ->
                val mijloc = cuvant.length / 2
                // Exemplu: "test" -> len=4, mijloc=2. substring(1, 3) va fi "es"
                cuvant.substring(mijloc - 1, mijloc + 1)
            }
    }
}

fun main() {
    println("--- Executie Kot39 (Prelucrare Submultimi Lambda) ---")
    val caleFisier = "date_text.txt"
    val fisier = File(caleFisier)
    
    // Cream fisierul cu propozitiile din cod cerute
    if (!fisier.exists()) {
        fisier.writeText("Aceasta este o zi minunata pentru examene. Speram o reusita clara!")
    }
    
    val procesor = ProcesorText()
    val rezultat = procesor.extrageMijloc(caleFisier)
    
    println("Cuvintele prelucrate si extrase cele doua caractere din mijloc:")
    println(rezultat)
}
