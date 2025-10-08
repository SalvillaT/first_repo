# class Animal:
#     def __init__(self, nombre, edad):
#        self.nombre = nombre
#        self.edad = edad

#     def hacer_sonido(self):
#         print("El animal hace un sonido genérico.")


# mi_animal = Animal("Fido", 5)

# print(mi_animal.nombre)
# print(mi_animal.edad)

# mi_animal.hacer_sonido()



# class Empleado:
#     sueldo_base = 50000
#     def __init__(self, nombre, cargo):
#          self.nombre = nombre
#          self.cargo = cargo

#     @classmethod
#     def aumentar_sueldo_base(cls, porcentaje):
#         cls.sueldo_base += 1000
#         print(f"El nuevo sueldo base es: {cls.sueldo_base}")  

# empleado1 = Empleado("Ana", "Gerente")
# print(f"Sueldo de {empleado1.nombre}: {Empleado.sueldo_base}")

# Empleado.aumentar_sueldo_base(10)
# empleado2 = Empleado("Juan", "Peon")
# print(f"Sueldo de {empleado1.nombre}: {Empleado.sueldo_base}")


# class Matematica:
#     @staticmethod
#     def sumar(a, b):
#         return a + b
    
#     @staticmethod
#     def restar(a, b):
#         return a - b
    
#     @staticmethod
#     def multiplicar(a, b):
#         return a * b
    
# print(Matematica.sumar(5, 3))


# class Producto:
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio

#     def mostrarDetalles(self):
#         print(f"El nombre del producto es {self.nombre} y su precio es {self.precio} euros")

# class Electrodomestico(Producto):
#     def __init__(self, nombre, precio, marca):
#         super().__init__(nombre, precio)
#         self.marca = marca

#     def encender(self):
#         super().mostrarDetalles()
#         print(f"Ademas, {self.nombre} ha sido encendido")

# producto1 = Producto("Gafas de sol" , 49.99)
# producto1.mostrarDetalles()

# producto2 = Producto("GOMA MXP 50º", 45.50)
# producto2.mostrarDetalles()
 
# electrodomestico1 = Electrodomestico("Frigorifico" , 499.90  , "Phillips")
# electrodomestico1.encender()

# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre
        
#     def hacer_sonido(self):
#         print("El animal hace un sonido genérico.")

# class Perro(Animal):
    
#     def __init__(self, nombre, raza):
#         super().__init__(nombre)
#         self.raza = raza
    
#     def hacer_sonido(self): 
#         super().hacer_sonido()
#         print("AAAAAAAAAAAAAAAAAAA")

# animal_generico = Animal("Tommy")
# animal_generico.hacer_sonido() 

# perro = Perro("Tommy","husky")
# perro.hacer_sonido()


import misModulos.moduloPrueba as math

print(math.PI)