# Escribir un programa que pida al usuario un numero entero
# positivo y muestre por pantalla todo los numeros impares
# desde 1 hasta ese numero separados por commas

user_input = int(input("Enter a whole number: \n"))

for i in range(0, user_input):
    if i % 2 != 0:
        print(i, end=", ")
