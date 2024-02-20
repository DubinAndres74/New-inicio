numero = int(input("Introduce un número: "))

es_par = numero % 2 == 0

if es_par:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")