import os
os.system("clear")

def mostrar_clima():
    print("Hoy se espera nubosidad variable y 20 grados de temperatura.")

def saludar():
    nombre = input("Ingresa tu nombre: ")
    print("Hola, " + nombre + ". ¿cómo estás?")
    mostrar_clima()

saludar()