# /*
#  * Crea una función que reciba días, horas, minutos y segundos (como enteros)
#  * y retorne su resultado en milisegundos.
#  */

dias = int(input("Introduce el día: "))
horas = int(input("Introduce la hora: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))

dias_milisegundos = dias * 86400000
horas_milisegundos = horas * 3600000
minutos_milisegundos = minutos * 60000
segundos_milisegundos = segundos * 1000

total_milisegundos = dias_milisegundos + horas_milisegundos + minutos_milisegundos + segundos_milisegundos

print("En total son", total_milisegundos, "milisegundos")