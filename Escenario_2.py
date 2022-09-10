# Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.

num_1 = int(input("Ingrese el primer numero: \n"))
num_2 = int(input("Infgrese el seguneo numero: \n"))

if num_2 == 0:
    print("No se puede dividir por 0.")
else:
    result = num_1 / num_2
    print("El resultado es {}".format(result))
