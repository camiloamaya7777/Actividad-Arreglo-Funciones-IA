#Este programa es para poder adrivinar el numero el cual ingrese el usuario en un rango de 1-10

AUTOR = "Camilo Guzman"  

print(f"Juego: Python intentará adivinar tu número (autor: {AUTOR})")
print("Piensa en un número entre 1 y 10 (no lo digas).")

bajo = 1
alto = 10
adivinado = False

while not adivinado:
    intento = (bajo + alto) // 2  
    print(f"¿Tu número es {intento}?")
    respuesta = input("Escribe 'mayor', 'menor' o 'correcto': ").lower()

    if respuesta == "correcto":
        print(f"¡Genial! Python adivinó tu número: {intento}")
        adivinado = True
    elif respuesta == "mayor":
        bajo = intento + 1
    elif respuesta == "menor":
        alto = intento - 1
    else:
        print("Por favor, responde solo con 'mayor', 'menor' o 'correcto'.")

print("¡Fin del juego!")
