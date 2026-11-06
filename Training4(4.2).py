num = False

while True:
    nota = float(input("Introdueix una nota: "))

    if nota == -1:
        break
    elif nota == 10:
        num = True

if num == True:
    print("Hi ha un 10")
else:
    print("No hi ha cap 10")