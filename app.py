# Desarrollar un programa que dado un numero entero positivo n
# calcule e imprima (separados por espacios) n/2 si es par o 3n + 1 si es
# impar. El programa debe repetir el proceso con el numero resultado
# de dicha operación mientras este sea diferente de 1. Por ejemplo para
# el numero 3 debe imprimir 10 5 16 8 4 2 1


def calcular_sucesion(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:  # Si el número es par
            n = n // 2
        else:  # Si el número es impar
            n = 3 * n + 1
    print(1)  # Imprimir el último número de la secuencia (1)


# Imprimir un listado con los números del 1 al 100 cada uno con su
# respectivo cuadrado.

for numero in range(1, 101):
    cuadrado = numero ** 2
    print(numero, cuadrado)


# Diseñar una función que permita calcular una aproximación de la
# función seno alrededor de 0 para cualquier valor x ∈ R (x dado en
# radianes), utilizando los primeros n términos de la serie de Maclaurin

import math

def aproximacion_seno(x, n):
    resultado = 0
    signo = 1

    for i in range(1, n+1):
        termino = signo * (x ** (2*i - 1)) / math.factorial(2*i - 1)
        resultado += termino
        signo *= -1

    return resultado

# Ejemplo de uso
valor_x = 0.5
terminos = 5
aproximacion = aproximacion_seno(valor_x, terminos)

print("Aproximación del seno de", valor_x, "utilizando", terminos, "términos:", aproximacion)


# Desarrollar un algoritmo que determina si una cadena de caracteres es
# frase palíndrome, esto es, si es palíndrome al eliminarle espacios,
# tíldes, signos de puntuación y al considerar mayúsculas=minúsculas.

import re

def es_palindromo(frase):
    # Eliminar espacios, tildes y signos de puntuación
    frase = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())

    # Verificar si la frase es un palíndromo
    return frase == frase[::-1]

# Ejemplo de uso
cadena = input("Ingrese una frase: ")
if es_palindromo(cadena):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")