print ("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")
print (" ")

# Hacer un diccionario de traducción español-inglés, se van a introducir las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.


def crear_diccionario(traducciones):
    diccionario = {}
    for par in traducciones.split(','):
        palabra, traduccion = par.split(':')
        diccionario[palabra.strip()] = traduccion.strip()
    return diccionario

def traducir_frase(diccionario, frase):
    palabras = frase.split()
    traduccion = []
    
    for palabra in palabras:
        if palabra in diccionario:
            traduccion.append(diccionario[palabra])
        else:
            traduccion.append(palabra)  # Dejar sin traducir si no está en el diccionario

    return ' '.join(traduccion)

# Introducir las traducciones
traducciones = input("Introduce las traducciones (formato 'español:inglés', separados por comas): ")
diccionario = crear_diccionario(traducciones)

# Pedir la frase a traducir
frase = input("Introduce la frase en español que quieres traducir: ")
resultado = traducir_frase(diccionario, frase)

print("La traducción es:", resultado)