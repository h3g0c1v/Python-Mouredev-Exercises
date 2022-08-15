# /*
#  * Crea una función que reciba un texto y muestre cada palabra en una línea,
#  * formando un marco rectangular de asteriscos.
#  * - ¿Qué te parece el reto? Se vería así:
#  *   **********
#  *   * ¿Qué   *
#  *   * te     *
#  *   * parece *
#  *   * el     *
#  *   * reto?  *
#  *   **********
#  */

sentence = str(input("Introduce una frase y la marcare en un marco: "))
    
# using split() 
# to extract words from string 
palabras = sentence.split() 

print("******************")
for i in palabras:
    print("*",i,"        *")

print("*******************")