# Escribir un programa que solicite al usuarion dos numeros
# y muestre por pantalla la tabla de multiplicar del multiplicador

table = int(input("Enter the multiplication table: \n"))
limit = int(input("Up to what number?: \n"))

for i in range(0, limit):
    print("{} x {} = {}".format(i, table, i*table))
