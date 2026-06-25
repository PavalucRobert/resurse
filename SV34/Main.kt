import java.io.File

fun main() {
    // 1. Creăm fișierul text cu câteva propoziții (cerința programatorului)
    val numeFisier = "subiect.txt"
    val fisier = File(numeFisier)
    fisier.writeText("Afară este foarte cald. Examenul la paradigme pare destul de simplu.")

    // 2. Citim conținutul fișierului
    val textOriginal = fisier.readText()
    println("Text original:\n$textOriginal\n")

    // 3. Procesarea colecției folosind lambda
    // Împărțim textul după spații pentru a obține o listă de cuvinte
    val cuvinte = textOriginal.split(Regex("\\s+"))

    val textProcesat = cuvinte.map { cuvant ->
        // Eliminăm temporar semnele de punctuație pentru o numărătoare corectă,
        // dar pentru simplitate la examen, verificăm direct lungimea token-ului.
        if (cuvant.length >= 4) {
            cuvant.drop(2) // Șterge primele 2 caractere
        } else {
            cuvant // Rămâne nemodificat dacă are sub 4 caractere
        }
    }.joinToString(" ") // Reconstruim propoziția punând spații între cuvinte

    // 4. Afișarea rezultatului
    println("Text procesat (fără primele 2 caractere la cuvintele lungi):\n$textProcesat")
}