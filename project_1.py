"""
Adivina el número
"""
import random

numero_usuario = int(input("Ingrese un número del 1 al 3: "))
numero_maquina = random.randint(1,3)


if numero_usuario == numero_maquina:
    print("Muy bien, adivinaste el número.")
else:
    print("No adivinaste el número")

print("Gracias por jugar")