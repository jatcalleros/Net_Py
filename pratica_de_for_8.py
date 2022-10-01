# Escriba un programa para imprimir todos los numeros
# primos entre 0 y 100 e imprima cuantos numeros primos hay

count = 0
print("All of the odd numbers between 0 and 100 are: \n")
for i in range(0, 100):
    if i % 2 != 0:
        print(i, end=" ")
        count += 1
print("\n", "*  "*30)
print("There are {} numbers in this series".format(count))
