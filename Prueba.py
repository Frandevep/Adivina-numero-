import random

# Generamos un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

print("🎯 ¡Adivina el número entre 1 y 100!")

while True:
    intento = int(input("Ingresa tu número: "))
    intentos += 1

    if intento < numero_secreto:
        print("🔼 El número es mayor. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("🔽 El número es menor. Intenta de nuevo.")
    else:
        print(f"🎉 ¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break
