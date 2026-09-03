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

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: no existe raiz de un numero negativo"
    return numero ** 0.5

def porcentaje(numero, porcentaje):
    return numero * (porcentaje / 100)

def promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

print("Bienvenido a la calculadora")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print ("####### Opciones #######") 
print ("1. Sumar")
print ("2. Restar")
print ("3. Multiplicar")
print ("4. Dividir")
print ("5. Potencia")
print ("6. Raíz Cuadrada")
print ("7. Porcentaje")
print ("8. Promedio")
print ("########################")

operacion = input("Seleccione la operación que desea realizar (1/2/3/4/5/6/7/8): ")

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
elif operacion == "5":
    resultado = potencia(numero1, numero2)
    print(f"El resultado de la potencia es: {resultado}")
elif operacion == "6":
    resultado = raiz_cuadrada(numero1)
    print(f"El resultado de la raíz cuadrada es: {resultado}")
    
elif operacion == "7":
    porcentaje_input = float(input("Ingrese el porcentaje que desea calcular: "))
    resultado = porcentaje(numero1, porcentaje_input)
    print(f"El {porcentaje_input}% de {numero1} es: {resultado}")
elif operacion == "8":
    lista = []
    while True:
        num = input("Ingrese un numero (o 'fin' para terminar): ")
        if num == "fin":
            break
        lista.append(float(num))
    resultado = promedio(lista)
    print(f"El promedio es: {resultado}")
else:
    print("Operación no válida")