"""Crear un programa que pida al usuario su nombre, apellido paterno, apellido 
materno, edad, peso y estatura, desplegarlos en pantalla junto con su Índice de 
Masa Corporal (IMC). 
El programa no puede permitir que ningún dato quede vacío, además de 
asegurarse de que en los campos de edad, peso y estatura el usuario 
introduzca una cifra. Todo esto antes de proceder con el cálculo del IMC 
siguiendo la fórmula: 
Peso / estatura2   -> Peso sobre estatura al cuadrado """


# Registro de datos
nombre = input("Ingrese su nombre: ")
apellido_paterno = input("Ingrese su apellido paterno: ")
apellido_materno = input("Ingrese su apellido materno: ")

edad = input("Ingrese su edad: ")

# entrada de datos

peso = float(input("Ingrese su peso: "))
estatura = float(input("Ingrese su estatura: "))

def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

imc = calcular_imc(peso, estatura)
clasificacion = clasificar_imc(imc)

# Desplegar resultados
print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno}")
print(f" Tu imc es: {imc:.2f} - Clasificación: {clasificacion}")
