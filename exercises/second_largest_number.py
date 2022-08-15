
# * Enunciado: Dado un listado de números, encuentra el SEGUNDO más grande.

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))
num5 = int(input("Introduce el quinto número: "))

lista = [num1, num2, num3, num4, num5 ]

lista.remove(max(lista))
print("El segundo numero mas grande de la lista es", max(lista))
