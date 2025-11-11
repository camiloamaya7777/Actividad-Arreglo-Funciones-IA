4#Este codigo es para poder desarrollar cualquier tabal de multiplicar del 1 al 10, segundo la que quiera ingresar el usuario

AUTOR = "Camilo Guzman"

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero} (autor: {AUTOR})")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)