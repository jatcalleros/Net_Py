# Solicitar al usuario que ingrese 3 numeros, el programa debera mostrar al final
# cual numero es el mayor y cual es el menor y los debera acomodar de menor a
# mayor

num_1 = int(input("Ingrese el primer numero: \n"))
num_2 = int(input("Ingrese el segundo numero: \n"))
num_3 = int(input("Ingrese el tercer numero: \n"))

Low = 0
Mid = 0
High = 0

if num_2 > num_1 < num_3:
    Low = num_1
    if num_2 < num_3:
        Mid = num_2
        High = num_3
    else:
        Mid = num_3
        High = num_2
elif num_1 > num_2 < num_3:
    Low = num_2
    if num_1 < num_3:
        Mid = num_1
        High = num_3
    else:
        Mid = num_3
        High = num_1
else:
    if num_1 > num_3 < num_2:
        Low = num_3
        if num_1 < num_2:
            Mid = num_1
            High = num_2
        else:
            Mid = num_2
            High = num_1


print("El numero mayor es {2}. El numero menor es {0}.Los numeros de menor a mayor son {0} {1} {2}".format(
    Low, Mid, High))
