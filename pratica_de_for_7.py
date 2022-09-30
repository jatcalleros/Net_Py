# Escribir un programa que almanece en una lista los siguientes
# precios y muestre el mayor y menor

precios = [50, 75, 46, 22, 80, 65, 8]
max = precios[0]
min = precios[0]
print(max, min)
for i in range(1, len(precios)):
    if precios[i] > max:
        max = precios[i]
    if precios[i] < min:
        min = precios[i]
print(max, min)
