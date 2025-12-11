# PROGRAMA QUE SUME 2 NÚMEROS ENTEROS

# DATOS DE ENTRADA (INPUT)
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

# PROCESO
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
else:
    resultado = "Operación no válida"

# DATOS DE SALIDA (OUTPUT)
print(f"El resultado de {numero1} {operacion} {numero2} es: {resultado}")