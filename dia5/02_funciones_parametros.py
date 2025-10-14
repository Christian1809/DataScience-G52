# PARAMETROS EN FUNCIONES



# Eejemplo sin parametro
def saludar():
    print("Hola, ¿como estas?")

# Funciones con parametros por defecto

def potencia(base, exponente = 2):
    return base ** exponente

# Funcion con multiples retornos
def operaciones(a, b):
    sum = a + b
    resta = a - b
    return sum, resta

saludar()
print(potencia(3))
print(potencia(3,4))
sum, resta = operaciones(5,3)
print(f"Suma: {sum}, resta: {resta}")


