# persona = {
#     "nombre": "Aurelio Garcia",
#  "hobbies": [
#   "Escalada",
#   "Lectura",
#   "Cocina"
#  ],
#  "contacto": {
#   "email": "aurelio@gmail.com",
#   "telefono": "123456789"
#  }
# }

# password = "mimamamemima"
# min = 8
# max = 20

# if len(password) < min:
#     print("La contrasenia es muy correcta")
# elif len(password) > max:
#     print("La contrasena es muy larga")
# elif len(password) > min and len(password) < max:
#     print("La contrasena es valida")


# vueltas = [1,2,3,4,5,6,7,8]

# for vuelta in vueltas:
#     print(f'Esta es la vuelta nº {vuelta}')

# colores = ["rojo", "verde", "azul", "amarillo"]

# for color in colores:
#     print(color)

# vueltas = [1,2,3,4,5,6,7,8]
# contador = 1
# while contador <= 5:
#     print(f"Estoy en la vuelta {vueltas[contador]}")
#     contador += 1

# numeros = [7,8,9,10,11]
# i = 0

# while i <= 4:
#     print(numeros[i])
#     i += 1

# productos = [
#     {"nombre": "Laptop", "categoria": "Electrónica", "precio": 799.99, "stock": 25},
#     {"nombre": "Auriculares Bluetooth", "categoria": "Accesorios", "precio": 59.99, "stock": 50},
#     {"nombre": "Cámara Digital", "categoria": "Fotografía", "precio": 399.99, "stock": 10},
#     {"nombre": "Smartwatch", "categoria": "Relojes", "precio": 149.99, "stock": 75},
#     {"nombre": "Teclado Mecánico", "categoria": "Accesorios", "precio": 89.99, "stock": 30}
# ]

# for produ in productos:
#     print(produ["nombre"])


# i = 0
# while i <= 2:
#     print(productos[i]["nombre"])
#     print("___")
#     i += 1

# for produ in productos:
#     if produ["precio"] > 100:
#         print(produ["nombre"])
#         print("++++++++")

# for produ in productos:
#     if produ["stock"] <= 25:
#         print(produ["nombre"])
#         print("********")


# def sum(a , b):
#     return a + b

# print(sum(3 , 8))

# def saludar(nombre):
#     return "Hola " + nombre

# nombre = input("Como te llamas? ")

# print(saludar(nombre))

# def grett(name, greeting = "Hello"):
#     if not name:
#         return greeting
#     else:
#         return f"{greeting} {name}"

# print(grett("Sofia"))
# print(grett("Salva","Buenos dias"))
# print(grett(""))



# def cuentaCaracteres(palabra):
#     if type(palabra) == str:
#         print("Tu palabra tiene " , len(palabra) , " caracteres")
#     else:
#         print("La variable debe de ser un String")


# cuentaCaracteres("Hola")

# primeraLetra = lambda palabra : palabra[0]

# palabra = input("Introduce una palabra o texto: ")
# print("La primera letra de tu palabra es: " , primeraLetra(palabra))

# def obtener_nombre_completo(nombre, apellido):
#     return nombre + " " + apellido
# def main():
#     usuarios = [
#         {"nombre": "Sofía" , "apellido" : "Tovar"},
#         {"nombre": "Luis", "apellido": "Martínez"},
#     ]

#     for usuario in usuarios:
#         completo = obtener_nombre_completo(usuario["nombre"], usuario["apellido"])
#         print(completo)
# main()

persona = {
    "nombre" : "Sofia",
	"edad" : 27,
	"altura" : 1.79,
	"hobbies" : ["basket" , "futbol" , "musica"],
	
}

if type(persona) == dict:
	print("apruebas 1")
else:
	print("suspendes 1")


if persona["nombre"] == "Sofia":
	print("apruebas 2")
else:
	print("suspendes 2")


if persona["edad"] >= 18:
	print("apruebas 3")
else:
	print("suspendes 3")


if type(persona["altura"])== float:
	print("apruebas 4")
else:
	print("suspendes 4")


if persona["hobbies"][1] == "futbol":
	print("apruebas 5")
else:
	print("suspendes 5")



pruebaDicc = {
	"x" : 7,
	"y" : "hola",
	"a" : {
		"b" : 3
	},
	"z" : [1 , 2 , "tutututa" , 4 , 5],

}

if type(pruebaDicc) == dict:
	print("apruebas 1")
else:
	print("suspendes 1")


if pruebaDicc["x"] == 7:
	print("apruebas 2")
else:
	print("suspendes 2")


if pruebaDicc["y"] == "hola":
	print("apruebas 3")
else:
	print("suspendes 3")


if pruebaDicc["a"]["b"] == 3:
	print("apruebas 4")
else:
	print("suspendes 4")


if pruebaDicc["z"][1] == 2:
	print("apruebas 5")
else:
	print("suspendes 5")


if type(pruebaDicc["z"][2]) == str:
	print("apruebas 6")
else:
	print("suspendes 6")


