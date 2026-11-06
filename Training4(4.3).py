for i in range(10):
    num = float(input("Introdueix un numero: "))
    if num < 0:
        print("Hi ha numero negatiu")
        break
else:
        print("No hi ha cap numero en negatiu")