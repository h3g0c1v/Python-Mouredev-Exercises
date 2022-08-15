# /*
#  * Reto #31
#  * AÑOS BISIESTOS
#  * Fecha publicación enunciado: 01/08/22
#  * Fecha publicación resolución: 08/08/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
#  * - Utiliza el menor número de líneas para resolver el ejercicio.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

first_year = int(input("\nIntroduce un año, y te daré los 30 próximos años bisiestos: "))
thirty_leap_year = first_year + (30*4)
counter = 00

while (first_year < thirty_leap_year):
    counter = counter + 1
    first_year = first_year + 4
    print("\n[", counter, "]", "El próximo año bisiesto a", first_year - 4, "es el", first_year)
