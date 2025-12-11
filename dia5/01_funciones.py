# FUNCIONES EN PYTHON
# Una funcion es un bloque de código reutilizable que realiza una tarea especifica
# Se define utilizando la palbra clave 'def', seguida del nombre de la funcion y parentesis


def saludar(nombre):
    """Funciones que saluda a una persona por su nombre."""
    return f"Hola, {nombre}"
    
nombre_usurario = input("Hola, ¿como te llamas?")
print(saludar(nombre_usurario))

def sumar(a,b):
    """Funcion que suma dos numeros"""
    resultado = a + b
    return resultado

num1 = float(input("Ingrese el primer numero1: "))
num2 = float(input("Ingrese el primer numero2: "))
resultado_suma = sumar(num1,num2)
print(f"La suma de {num1} + {num2} es:")


