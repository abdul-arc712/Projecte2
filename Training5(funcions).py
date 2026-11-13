#Exercici 1. Calculadora de preus
def calcular_preu(preu_peces, ma_obra):
    preu = preu_peces + ma_obra
    return preu

preu = calcular_preu(45, 30)
print("Cost total:", preu, "€")

#Exercici 2. Funcions amb condicions
def aplicar_descompte(preu, tipus_client):
    tipus = tipus_client
    if tipus == "particular":
        return preu
    elif tipus == "empresa":
        return preu * 0.90 
    elif tipus == "client habitual":
        return preu * 0.85
    else:
        print("El tipus de client no es valid")
        return preu

#Exercici 3. Funcions que criden altres funcions
def calcular_iva(preu):
    return preu * 0.21
def calcular_factura(preu, tipus_client):
    preu_descompte = aplicar_descompte(preu, tipus_client) 
    iva = calcular_iva(preu_descompte)
    total = preu_descompte + iva
    return total

#Exercici 4. Programa complet: servei tècnic
def mostrar_menu():
    print("\n===== SERVEI TÈCNIC INFORMÀTIC =====")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")
def nova_reparacio():
    nom = input("Nom del client: ")
    peces = float(input("Cost de les peces (€): "))
    ma_obra = float(input("Cost de la mà d'obra (€): "))
    tipus = input("Tipus de client (Particular / Empresa / Client habitual): ")

#Utilitzant els funcions anteriors
    preu = calcular_preu(peces, ma_obra)
    preu_descompte = aplicar_descompte(preu, tipus)
    descompte = preu - preu_descompte
    iva = calcular_iva(preu_descompte)
    total = calcular_factura(preu, tipus)

#La Factura
    print("\n--- FACTURA ---")
    print("Client:", nom)
    print("Preu inicial:", preu, "€")
    print("Descompte aplicat:", descompte, "€")
    print("IVA (21%):", iva, "€")
    print("Total a pagar:", total, "€")
    return total

#Variables
reparacions = 0
facturacio = 0
opcio = ""

# Bucle menu
while opcio != "4":
    mostrar_menu()
    opcio = input("Selecciona una opció: ")

    if opcio == "1":
        total = nova_reparacio()
        reparacions = reparacions + 1
        facturacio = facturacio + total
    elif opcio == "2":
        print("Nombre de reparacions:", reparacions)
    elif opcio == "3":
        print("Facturació acumulada:", facturacio, "€")
    elif opcio == "4":
        print("Fins aviat!")
    else:
        print("Opció no vàlida.")