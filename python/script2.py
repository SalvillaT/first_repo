# numeros = [1,2,3,4,5,6,7,8,9,10]

# for num in numeros:
#     if num % 2 == 0:
#         print(num)


# def sumar_lista(numeros):
#     if type(numeros) != list:
#         return "Debes pasar una lista"
#     else:
#         suma = 0
#         for num in numeros:
#             suma += num
#         return suma

# print(sumar_lista([1, 2, 3, 4, 5]))
# # resultado esperado 15
# print(sumar_lista([7,5,9]))
# # resultado esperado 21

# print(sumar_lista(1))


# def sumar_dos(x):   
#     return x + 2

# numero = 5
# numero = sumar_dos(numero)
# print(numero)


# def mostrar_producto(*, nombre , precio):
#     print(f"El nombre del producto es {nombre} y su precio es {precio} euros")

# mostrar_producto(nombre = "TV Smart", precio = 200)
# mostrar_producto(precio = 200 , nombre = "TV Smart")


# def sumar_todos(*numeros):
#     print(f"Tipo de 'numeros': {type(numeros)}")
#     total = 0
#     for num in numeros:
#         total += num
#     return total

# print(sumar_todos(1, 2, 3)) 
# print(sumar_todos(50, 20, 30, 40, 10 )) 
# print(sumar_todos(5)) 


# def configurar_perfil(**opciones_perfil):
#     print(f"Tipo de 'opciones_perfil': {type(opciones_perfil)}") 
# configurar_perfil(nombre="Ana", edad=30, ciudad="Valencia")
# configurar_perfil(tema="oscuro", notificaciones=True)


# def procesar_datos(identificador, *valores, **opciones):
#     print(f"Identificador: {identificador}")
#     print(f"Valores adicionales (tupla): {valores}")
#     print(f"Opciones (diccionario): {opciones}")
# procesar_datos("producto_A", 10, 20, 30, color="rojo", tamaño="grande")


# def multiplicar_todos(*numeros):
#     print(f"Tipo de 'numeros': {type(numeros)}")
#     total = 1
#     for num in numeros:
#         total *= num
#     return total

# print(multiplicar_todos(2, 4, 6))
# # La suma total es: 48
# print(multiplicar_todos(1, 5, 10, 20))
# # La suma total es: 10000


# edad = int(input("Cual es tu edad: "))
# print(type(edad))
# print(f"tu edad es {edad}")


# print(round(3.14159))
# print(round(2.7)) 

# print(round(2.5)) 
# print(round(3.5)) 
# print(round(3.14159, 2))


# numeros = [1, 5, 8, 12, 15, 20]
# numero_objetivo = 12
# for num in numeros:
#     print(f"Comprobando el número: {num}")
#     if num == numero_objetivo:
#         print(f"¡Encontrado! El número {numero_objetivo} está en la lista.")
#         break 
#     print(f"El número {num} no es el objetivo.")
# print("Fin del programa después del bucle.")


# numeros = [1, 2, 3, 4, 5, 6, 7]
# for num in numeros:
#     if num % 2 == 0: 
#        print(f"Saltando el número par: {num}")
#        continue  
#     print(f"Procesando número impar: {num} (su cuadrado es {num * num})")
# print("Fin del programa después del bucle.")


# lista_edades = [15, 22, 17, 30, 65, 45, 70, 19]

# for edad in lista_edades:
#     if edad >= 65:
#         break
#     if edad >= 18:
#         print(edad)
       

intentos = 5
num = 0
numSecreto = 7

while num != numSecreto and intentos > 0:
    num = input("Introduca un numero del 1 al 10: ")
    if not num.isdigit():
        print("El dato introducido debe de ser un numero") 
        intentos -= 1
        print(f"Te quedan {intentos} intentos")
        continue
    elif int(num) != numSecreto:
        print("Numero equivocado")
        intentos -= 1
        print(f"Te quedan {intentos} intentos")
        continue
    elif int(num) == numSecreto:
        num = int(num)
        print("NUMERO SECRETO ENCONTRADO ERES UNA MAQUINA")
        print(type(num))


