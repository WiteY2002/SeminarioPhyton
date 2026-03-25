import random
categorias = {
    "lenguajes": ["python", "java", "c"],
    "tipos de datos": ["entero", "cadena", "lista", "booleano","string"],
    "control": ["bucle", "condicional"],
    "conceptos": ["programa", "variable", "funcion"]
}
savedwords=[]
guessed = []
attempts = 6
continua=True

#selector de categorias
while True:
    print("categorias disponibles: ")
    for categoria in categorias:
        print()
        print(f" ----{categoria}----")
    seleccion=input (" selecciona una categoria: ").lower()
    if seleccion in categorias:
        break
    else:
      print("categoria no valida!")

#inicio del juego 
print("¡Bienvenido al Ahorcado!")
print()

palabras = random.sample(categorias[seleccion], len(categorias[seleccion]))

# recorrer palabras
for word in palabras:
    guessed = []
    attempts = 6
    puntaje = len(word)

    while continua:
        progress = ""
        puntaje = len(word) 
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        
        print(progress)

        if "_" not in progress:
            puntaje += 6
            print("¡Ganaste!")
            print(f"puntaje total: {puntaje}")
            opcion = input("\n¿Querés seguir? (Y/N): ").lower()
            if opcion != "y":
                continua = False
                break
            else:
                break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje-=1
            print("Esa letra no está en la palabra.")
        
        print()

        if attempts == 0:
            print(f"¡Perdiste! La palabra era: {word}")
            opcionf = input("\n¿Querés seguir? (Y/N): ").lower()
            if opcionf != "y":
                continua = False
            break
    if not continua:
        break
    else:
        print("se han terminado las palabras para esta categoria")
print("fin del juego!")