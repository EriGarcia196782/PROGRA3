def convertir_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return convertir_a_binario(n // 2) + str(n % 2)


def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)


def calcular_raiz_cuadrada(n, i=1):
    if i * i > n:
        return i - 1
    return calcular_raiz_cuadrada(n, i + 1)


def raiz_cuadrada_entera(n):
    return calcular_raiz_cuadrada(n)

valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def convertir_a_decimal(romano, index=0):
    if index == len(romano):
        return 0
    if index < len(romano) - 1 and valores_romanos[romano[index]] < valores_romanos[romano[index + 1]]:
        return convertir_a_decimal(romano, index + 1) - valores_romanos[romano[index]]
    return convertir_a_decimal(romano, index + 1) + valores_romanos[romano[index]]


def suma_numeros_enteros(n):
    if n == 0:
        return 0
    return n + suma_numeros_enteros(n - 1)


def menu():
    while True:
        print("=====Menu Principal=====")
        print("Seleccione la opcion que desea utilizar")
        print("1. Convertir a Binario")
        print("2. Contar Digitos")
        print("3. Raiz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Numeros Enteros")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            num = int(input("Ingrese un numero: "))
            print(f"El numero binario es: {convertir_a_binario(num)}")
        elif opcion == "2":
            num = int(input("Ingrese un numero: "))
            print(f"El numero de digitos es: {contar_digitos(num)}")
        elif opcion == "3":
            num = int(input("Ingrese un numero: "))
            print(f"La raiz cuadrada entera es: {raiz_cuadrada_entera(num)}")
        elif opcion == "4":
            romano = input("Ingrese un numero romano (en mayusculas): ")
            print(f"El numero en decimal es: {convertir_a_decimal(romano)}")
        elif opcion == "5":
            num = int(input("Ingrese un numero: "))
            print(f"La suma de 0 a {num}: {suma_numeros_enteros(num)}")
        elif opcion == "6":
            break
        else:
            print("Seleccione una opcion valida")

menu()
