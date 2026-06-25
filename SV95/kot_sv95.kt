// Design Pattern: Abstract Factory
// "Utilizand o fabrica abstracta sa se scrie un program Kotlin care permite crearea la cerere 
// a trei obiecte (student, profesor, secretar) acestea la randul lor permit crearea de obiecte specifice"

// Interfetele de baza
interface PersoanaUniversitate {
    fun detalii(): String
}

interface Student : PersoanaUniversitate {
    fun creazaSpecificStudent(tip: String): Student
}

interface Profesor : PersoanaUniversitate {
    fun creazaSpecificProfesor(tip: String): Profesor
}

interface Secretar : PersoanaUniversitate {
    fun creazaSpecificSecretar(tip: String): Secretar
}

// Clase Concrete - Baza
class StudentBaza(val desc: String = "Student generic") : Student {
    override fun detalii() = desc
    override fun creazaSpecificStudent(tip: String): Student {
        return when (tip.lowercase()) {
            "integralist" -> StudentBaza("Student Integralist")
            "restantier" -> StudentBaza("Student Restantier")
            "repetent" -> StudentBaza("Student Repetent")
            else -> StudentBaza("Student Necunoscut")
        }
    }
}

class ProfesorBaza(val desc: String = "Profesor generic") : Profesor {
    override fun detalii() = desc
    override fun creazaSpecificProfesor(tip: String): Profesor {
        return when (tip.lowercase()) {
            "prof" -> ProfesorBaza("Profesor Universitar (Prof)")
            "conf" -> ProfesorBaza("Conferentiar (Conf)")
            "sl" -> ProfesorBaza("Sef de Lucrari (SL)")
            "as" -> ProfesorBaza("Asistent Universitar (As)")
            else -> ProfesorBaza("Grad didactic necunoscut")
        }
    }
}

class SecretarBaza(val desc: String = "Secretar generic") : Secretar {
    override fun detalii() = desc
    override fun creazaSpecificSecretar(tip: String): Secretar {
        return when (tip.lowercase()) {
            "sef" -> SecretarBaza("Secretar Sef")
            "i" -> SecretarBaza("Secretar I")
            "ii" -> SecretarBaza("Secretar II")
            else -> SecretarBaza("Secretar Necunoscut")
        }
    }
}

// Abstract Factory
interface UniversitateFactory {
    fun creareStudent(): Student
    fun creareProfesor(): Profesor
    fun creareSecretar(): Secretar
}

// Concrete Factory
class FIIFactory : UniversitateFactory {
    override fun creareStudent(): Student = StudentBaza()
    override fun creareProfesor(): Profesor = ProfesorBaza()
    override fun creareSecretar(): Secretar = SecretarBaza()
}

fun main() {
    val fabrica: UniversitateFactory = FIIFactory()
    
    // Cream instantele de baza folosind Abstract Factory
    val studentBaza = fabrica.creareStudent()
    val profBaza = fabrica.creareProfesor()
    val secBaza = fabrica.creareSecretar()
    
    println("--- Creare obiecte specifice din cele de baza ---")
    val student1 = studentBaza.creazaSpecificStudent("integralist")
    val student2 = studentBaza.creazaSpecificStudent("restantier")
    
    val prof1 = profBaza.creazaSpecificProfesor("conf")
    val prof2 = profBaza.creazaSpecificProfesor("sl")
    
    val sec1 = secBaza.creazaSpecificSecretar("sef")
    
    println(student1.detalii())
    println(student2.detalii())
    println(prof1.detalii())
    println(prof2.detalii())
    println(sec1.detalii())
}
