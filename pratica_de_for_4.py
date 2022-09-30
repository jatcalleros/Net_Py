# Escribir un programa que pida al usuario un numero entero
# positivo y muestro por pantalla la cuenta atras desde ese numero
# hasta cero separados por comas.

user_input = int(input("Enter a whole number: \n"))

for i in range(user_input, 0, -1):
    print(i, end=', ')
