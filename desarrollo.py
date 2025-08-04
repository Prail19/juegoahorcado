# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 19:55:25 2025

@author: K_Mendez
"""

import random

def obtener_palabra():
    """Obtiene una palabra aleatoria de una lista ampliada"""
    palabras = [
        'carro', 'ingenieria', 'universidad', 'pantalla', 'sol', 
        'internet', 'programacion', 'estrella', 'computadora', 'casa',
        'aguila', 'hardware', 'datos', 'inteligencia'
    ]
    return random.choice(palabras).upper()

def mostrar_ahorcado(intentos):
    """Muestra el estado del ahorcado según los intentos restantes"""
    etapas = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return etapas[intentos]

def revelar_letra(palabra, oculta):
    """Revela una letra aleatoria que no haya sido adivinada aún"""
    letras_no_adivinadas = [letra for letra in palabra if letra not in oculta]
    return random.choice(letras_no_adivinadas) if letras_no_adivinadas else None

def mostrar_progreso(oculta, letras_adivinadas):
    """Muestra el progreso actual del juego"""
    print("\n" + " ".join(oculta))
    print(f"\nLetras usadas: {', '.join(sorted(letras_adivinadas))}")

def jugar():
    """Función principal que maneja la lógica del juego"""
    palabra = obtener_palabra()
    oculta = ['_'] * len(palabra)
    letras_adivinadas = set()
    intentos = 6
    
    # Revelar letra inicial
    letra_pista = revelar_letra(palabra, oculta)
    if letra_pista:
        for i in range(len(palabra)):
            if palabra[i] == letra_pista:
                oculta[i] = letra_pista
        letras_adivinadas.add(letra_pista)
    
    print("¡Bienvenido al juego del Ahorcado!")
    print(f"\nPista: La palabra contiene la letra '{letra_pista}'")
    mostrar_progreso(oculta, letras_adivinadas)

    while intentos > 0 and '_' in oculta:
        print(mostrar_ahorcado(intentos))
        
        # Validación de entrada
        while True:
            intento = input("\nIngresa una letra: ").upper()
            if len(intento) != 1 or not intento.isalpha():
                print("Por favor ingresa una sola letra válida.")
            elif intento in letras_adivinadas:
                print("Ya has usado esa letra. Prueba con otra.")
            else:
                break
        
        letras_adivinadas.add(intento)
        acierto = False
        
        # Verificar si la letra está en la palabra
        for i in range(len(palabra)):
            if palabra[i] == intento:
                oculta[i] = intento
                acierto = True
        
        if not acierto:
            intentos -= 1
            print(f"\nLa letra '{intento}' no está en la palabra. Te quedan {intentos} intentos.")
        
        mostrar_progreso(oculta, letras_adivinadas)

    # Resultado final
    if '_' not in oculta:
        print("\n¡Felicidades! ¡Has ganado!")
        print(f"La palabra era: {palabra}")
    else:
        print(mostrar_ahorcado(0))
        print("\n¡Oh no! ¡Has perdido!")
        print(f"La palabra era: {palabra}")
    
    # Opción para jugar nuevamente
    jugar_de_nuevo = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_de_nuevo == 's':
        print("\n" + "="*50 + "\n")
        jugar()
    else:
        print("\n¡Gracias por jugar! Hasta la próxima.")

if __name__ == "__main__":
    jugar()