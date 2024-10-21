import random

NUM_DIGITS = 3  # (!) Prueba a cambiar esto.
MAX_GUESSES = 10  # (!) Prueba a cambiar esto 


def main():
    """Función principal que maneja la lógica del juego."""
    # TODO: Explicar las normas del juego
    
    while True:  # Main game loop.
        secretNum = getSecretNum()  # Esta función generará el número secreto.
        # TODO: Imprimir que el número ha sido generado.
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # TODO: Solicitar al usuario que ingrese una suposición válida.
            
            clues = getClues(guess, secretNum)  # Generar pistas con base en la suposición.
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Adivinó correctamente, salir del bucle.
            if numGuesses > MAX_GUESSES:
                # TODO: Informar al jugador que se ha quedado sin intentos.
                pass

        # Preguntar al jugador si desea jugar de nuevo.
        # TODO: Solicitar si quiere jugar de nuevo y gestionar la respuesta.
        pass

    # TODO: Despedida final cuando el jugador termine.
    pass


def getSecretNum():
    """Devuelve un número secreto de NUM_DIGITS dígitos únicos en formato de cadena."""
    numbers = list('0123456789')  # Crea una lista con los numeros del 1 al 9.
    random.shuffle(numbers)  # Los pone en orden aleatorio.
    # TODO: Implementar la lógica para generar un número aleatorio único.
    pass


def getClues(guess, secretNum):
    """Devuelve una cadena con las pistas pico, fermi, bagels para una pareja de suposición y número secreto."""
    # TODO: Implementar la lógica para generar las pistas basadas en la suposición.
    pass


# Si el programa se ejecuta directamente (en lugar de importarse), iniciar el juego:
if __name__ == '__main__':
    main()

