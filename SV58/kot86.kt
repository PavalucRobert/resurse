// SOLID: 
// Open/Closed Principle: Putem adauga oricand noi clase de oameni (ex: Ana) extinzand interfata sau abstractizarea.
// Liskov Substitution Principle: Oricare dintre Ion, Vasile, Alex poate fi folosit in locul tipului de baza Om, fara sa strice logica aplicatiei.
// Polymorphism: Interogarea comportamentului (mananca, bea) la runtime ofera rezultate diferite prin suprascriere.

abstract class Om(val nume: String) {
    abstract fun mananca(): String
    abstract fun bea(): String
    abstract fun danseaza(): String
}

class Ion : Om("Ion") {
    override fun mananca() = "mere"
    override fun bea() = "bere"
    override fun danseaza() = "femei"
}

class Vasile : Om("Vasile") {
    override fun mananca() = "pere"
    override fun bea() = "vodca"
    override fun danseaza() = "barbati"
}

class Alex : Om("Alex") {
    override fun mananca() = "prajituri brune"
    override fun bea() = "vin"
    override fun danseaza() = "sefi"
}

// Analizatorul - primeste o colectie de tipul de baza 'Om' si aplica logica dorita
class Analizator(val grupulDeOameni: List<Om>) {
    fun cuCineDanseaza(numeOm: String): String {
        val om = grupulDeOameni.find { it.nume.equals(numeOm, ignoreCase = true) }
        return om?.danseaza() ?: "Nu exista acest om in grup."
    }
}

fun main() {
    println("--- Executie Kot86 (Polimorfism pe Grup de Oameni) ---")
    val oameni = listOf(Ion(), Vasile(), Alex())
    val analizator = Analizator(oameni)
    
    println("Q: Cu cine poate dansa Vasile?")
    println("A: Vasile danseaza cu: ${analizator.cuCineDanseaza("Vasile")}")
    
    println("\\nQ: Ce pot manca barbatii?")
    // Deoarece Ion, Vasile si Alex sunt barbati (bazat pe datele initiale), mapam mancarea lor:
    val mancareaBarbatilor = oameni.map { it.mananca() }.toSet().joinToString(", ")
    println("A: Barbatii pot manca: $mancareaBarbatilor")
}
