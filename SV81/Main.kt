import java.io.File

// 1. Interfața dorită de client (Target)
interface UnifiedWriter {
    fun write(obj: Any, fileName: String)
}

// 2. Interfața veche/incompatibilă (Adaptee)
class StringFileWriter {
    fun writeString(text: String, fileName: String) {
        File(fileName).writeText(text)
        println("S-a scris în fișierul $fileName: \n$text\n")
    }
}

// 3. Adaptorul (Adapter) - face legătura între ele
class ObjectToFileAdapter(private val stringWriter: StringFileWriter) : UnifiedWriter {

    // Primește doar obiectul și numele fișierului, conform cerinței
    override fun write(obj: Any, fileName: String) {
        // Conversia (adaptarea) diferitelor tipuri de date la String
        val stringData = when (obj) {
            is Collection<*> -> obj.joinToString(separator = "\n") { "- $it" }
            is Array<*> -> obj.joinToString(separator = ", ")
            else -> obj.toString()
        }

        // Apelarea metodei din Adaptee
        stringWriter.writeString(stringData, fileName)
    }
}

// 4. Testare
fun main() {
    val adaptee = StringFileWriter()
    val adapter = ObjectToFileAdapter(adaptee)

    // Date simple
    adapter.write(100, "numar.txt")
    adapter.write("Salut", "text_simplu.txt")

    // Colecție
    val listaStudenti = listOf("Popescu Ion", "Ionescu Maria", "Vasile Ana")
    adapter.write(listaStudenti, "studenti.txt")
}