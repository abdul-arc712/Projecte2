num1 = float(input("El primer nombre: "))
num2 = float(input("El segon nombre: "))
num3 = float(input("El tercer nombre: "))


if num1>num2 and num1>num3:
    print(f"El nombre mes gran es: {num1}")
elif num2>num1 and num2>num3:
    print(f"El nombre mes gran es: {num2}")
else:
    print(f"El nombre mes gran es: {num3}")