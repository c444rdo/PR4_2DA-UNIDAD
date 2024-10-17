print ("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")
print (" ")

# Crear un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

persona = {}

nombre = input("Ingresa tu primer nombre: ")
persona ['nombre'] = nombre
print (persona)

apellidos = input("Ingresa tus apellidos: ")
persona ['apellidos'] = apellidos
print (persona)

edad = input("Ingresa tu edad: ")
persona ['edad'] = edad
print (persona)

sexo = input("Ingresa tu sexo (M/F): ")
persona ['sexo'] = sexo
print (persona)

telefono = input("Ingresa tu número de telefono: ")
persona ['telefono'] = telefono
print (persona)

direccion = input("Ingresa tu dirección: ")
persona ['direccion'] = direccion
print (persona)