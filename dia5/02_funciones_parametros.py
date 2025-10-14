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

saludar()      #Llama a la funcion sin parametro
print(potencia(3))    #Llama a la funcion con un parametro (exponente por defecto)
print(potencia(3,4))   #Llama a la funcion con ambos parametros
sum, resta = operaciones(5,3)     #Llama a la funcion con multiplos parametros
print(f"Suma: {sum}, resta: {resta}")


