import os
os.system("clear") # si usas Windows, cambia 'clear' por 'cls'

# Variables de diferentes tipos, y mención a constantes

# variables
nombre = "Cuch"
edad = 14
esta_logueado = True
fin_de_semana = False

#constantes
PI = 3.14159
GRAVEDAD = 9.8

# Verificar el tipo de variable

x = 5
print("Es un número: " + str(isinstance(x, int)) )

empresa = "Hydroponic Corp."
print(type(empresa))    # imprime <class 'str'>

# Castear cualquier tipado a una cadena de texto

print("El valor de nombre es: " + nombre) # con strings no hay problema
print("El valor de edad es: " + str(edad)) # usamos str() para convertir números a texto
print("Valor de esta_logueado :" + str(esta_logueado))  # convertimos un Boolean

# Comparando valores de variables (OPERADORES DE COMPARACIÓN)

x = 2103
y = 1975

x == y  # Verdadero si x es igual a y
x != y  # Verdadero si x no es igual a y
x > y  # Verdadero si x es mayor que y
x < y  # Verdadero si x es menor que y
x >= y  # Verdadero si x es mayor o igual que y
x <= y  # Verdadero si x es menor o igual que y

# Operadores lógicos

expresion1 = ""
expresion2 = 0

expresion1 and expresion2 # Uso de AND
expresion1 or expresion2  # uso de OR
not expresion1            # uso de NOT

x = 5
y = 10

if x > 0 and y > 0:
    print("Ambas x e y son mayores que cero.")

if x > 0 or y > 0:
    print("Al menos una de las variables es mayor que cero.")

if not x < 0:
    print("x no es menor que cero.")


# Condicional simple

edad = 18
if int(edad) >= 18:
    print("Eres mayor de edad.")

nombre = "Cameron Howe"
if nombre == "Cameron Howe":
    print("Hola, Cameron.")

# Condicional if + else

nombre = "Cameron Howe"

if nombre == "Cameron Howe":
    print("Hola, " + nombre)
else:
    print("El nombre no coincide con el esperado.")


# if - elif

edad = input("Ingresa tu edad:")

if edad.isdigit() and int(edad) >= 18:
    print("Eres mayor de edad.")
elif not edad.isdigit():
    print("Por favor, ingresa un número válido como tu edad.")

# Funciones simples

def saludar():
    print("Hola, ¿cómo estás?")

# saludar() #👈 Descomentar para llamar a la función