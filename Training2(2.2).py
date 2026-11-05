num1 = int(input("Introdueix el primer nombre enter: "))
num2 = int(input("Introdueix el segon nombre enter: "))

suma = num1 + num2
resta = num1 - num2
multiplicacio = num1 * num2

print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicació: {num1} * {num2} = {multiplicacio}")

if num2 != 0:
    divisio = num1 / num2
    print(f"Divisió: {num1} / {num2} = {divisio}")
else:
    print("Divisió: No es pot dividir entre 0.")