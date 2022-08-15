# /*
#  * Simula el funcionamiento de una máquina expendedora creando una operación
#  * que reciba dinero (array de monedas) y un número que indique la selección
#  * del producto.
#  * - El programa retornará el nombre del producto y un array con el dinero
#  *   de vuelta (con el menor número de monedas).
#  * - Si el dinero es insuficiente o el número de producto no existe,
#  *   deberá indicarse con un mensaje y retornar todas las monedas.
#  * - Si no hay dinero de vuelta, el array se retornará vacío.
#  */

products = ['Sandwich', 'Aquarius', 'Cheetos', 'Patatas', 'Conguitos', 'Oreo', 'Kinder Bueno']
price = ['20', '5', '10', '25', '50', '150', '200']

user = int(input("[*] Introduce el numero de producto que desea (0-6): "))

while(user < 0) or (user > 6):
    print("[!] El valor introducido no es valido")
    user = int(input("[!] Porfavor, introduce un valor valido (0-6): "))

print("El producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
user_price = int(input("[*] Introduce el precio en la maquina, porfavor: "))



if(user >= 0) and (user <= 6):

    if(user == 0):

        while(user_price < int(price[0])):

                quantity = int(price[0]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))
        
        if(user_price == int(price[0])):

            print("Ha recibido correctamente el producto con el precio exacto")
            print("Disfrute del producto :)")

        elif(user_price > int(price[0])):

            quantity = user_price - int(price[0])
            print("Se le ha devuelto", quantity, "€")
            print("Disfrute del producto :)")
            
    elif(user == 1):

        while(user_price < int(price[1])):

                quantity = int(price[1]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))

        if(user_price == int(price[1])):

            print("Ha recibido correctamente el producto con el precio exacto")
            print("Disfrute del producto :)")

        elif(user_price < int(price[1])):

            while(user_price < int(price[1])):

                quantity = int(price[1]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))

        elif(user_price > int(price[1])):

            quantity = user_price - int(price[1])
            print("Se le ha devuelto", quantity, "€")
            print("Disfrute del producto :)")

    elif(user == 2):

        while(user_price < int(price[2])):

                quantity = int(price[2]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))

        if(user_price == int(price[2])):

            print("Ha recibido correctamente el producto con el precio exacto")
            print("Disfrute del producto :)")

        elif(user_price < int(price[2])):

            while(user_price < int(price[2])):

                quantity = int(price[2]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))

        elif(user_price > int(price[2])):

            quantity = user_price - int(price[2])
            print("Se le ha devuelto", quantity, "€")
            print("Disfrute del producto :)")

    elif(user == 3):

        while(user_price < int(price[3])):

                quantity = int(price[3]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))

        if(user_price == int(price[3])):

            print("Ha recibido correctamente el producto con el precio exacto")
            print("Disfrute del producto :)")

        elif(user_price < int(price[3])):

            while(user_price < int(price[3])):

                quantity = int(price[3]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))

        elif(user_price > int(price[3])):

            quantity = user_price - int(price[3])
            print("Se le ha devuelto", quantity, "€")
            print("Disfrute del producto :)")

    elif(user == 4):

        while(user_price < int(price[4])):

                quantity = int(price[4]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))

        if(user_price == int(price[4])):

            print("Ha recibido correctamente el producto con el precio exacto")
            print("Disfrute del producto :)")

        elif(user_price < int(price[4])):

            while(user_price < int(price[4])):

                quantity = int(price[4]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))

        elif(user_price > int(price[4])):

            quantity = user_price - int(price[4])
            print("Se le ha devuelto", quantity, "€")
            print("Disfrute del producto :)")

    elif(user == 5):

        while(user_price < int(price[5])):

                quantity = int(price[5]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))

        if(user_price == int(price[5])):

            print("Ha recibido correctamente el producto con el precio exacto")
            print("Disfrute del producto :)")

        elif(user_price < int(price[5])):

            while(user_price < int(price[5])):

                quantity = int(price[5]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce el precio en la maquina, porfavor: "))

        elif(user_price > int(price[5])):

            quantity = user_price - int(price[5])
            print("Se le ha devuelto", quantity, "€")
            print("Disfrute del producto :)")

    elif(user == 6):

        while(user_price < int(price[6])):

            quantity = int(price[6]) - user_price
            print("El precio es insuficiente. Le quedan ", quantity, "€")
            print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
            print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
            user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))
            
        if(user_price == int(price[6])):

            print("Ha recibido correctamente el producto con el precio exacto")
            print("Disfrute del producto :)")

        elif(user_price < int(price[6])):

            while(user_price < int(price[6])):

                quantity = int(price[6]) - user_price
                print("El precio es insuficiente. Le quedan ", quantity, "€")
                print("[!] Se le ha devuelto las", user_price, "monedas introducidas")
                print("\nEl producto seleccionado es", products[user], "el precio para este producto es", price[user], "€")
                user_price = int(input("[*] Introduce de nuevo el precio en la maquina, porfavor: "))

        elif(user_price > int(price[6])):

            quantity = user_price - int(price[6])
            print("Se le ha devuelto", quantity, "€")
            print("Disfrute del producto :)")
