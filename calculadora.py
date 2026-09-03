# Calculadora

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

print("Bienvenido a la calculadora")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print ("####### Opciones #######") 
print ("1. Sumar")
print ("2. Restar")
print ("3. Multiplicar")
print ("4. Dividir")
print ("########################")

operacion = input("Seleccione la operación que desea realizar (1/2/3/4): ")

if operacion == "1":
    resultado = sumar(numero1, numero2)
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "2":
    resultado = restar(numero1, numero2)
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "3":
    resultado = multiplicar(numero1, numero2)
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "4":
    try:
        resultado = dividir(numero1, numero2)
        print(f"El resultado de la división es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
else:
    print("Operación no válida")