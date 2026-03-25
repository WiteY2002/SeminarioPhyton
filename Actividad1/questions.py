import random
categorias = {
    "lenguajes": ["python", "java", "c"],
    "tipos de datos": ["entero", "cadena", "lista", "booleano","string",],
    "control": ["bucle", "condicional"],
    "conceptos": ["programa", "variable", "funcion"]
}

guessed = []
attempts = 6
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
#asignacion de palabra
word=random.choice(categorias[seleccion])
puntaje = len(word)
#inicio del juego 
print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
    progress = ""
  
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

else:
    puntaje=0
    print(f"¡Perdiste! La palabra era: {word}, puntaje: {puntaje}")