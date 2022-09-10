# Escribir un programa que pregunte al usuario su renta anual y
# muestre por pantalla el tipo impositivo que le corresponde.

renta_anual = int(input("Ingresa tu renta anual: \n"))

impuesto = -100

if renta_anual <= 1000.00:
    impuesto = .05
elif 1000 < renta_anual <= 2000:
    impuesto = .15
elif 2000 < renta_anual <= 3500:
    impuesto = .20
elif 3500 < renta_anual <= 6000:
    impuesto = .30
else:
    if renta_anual > 6000:
        impuesto = .45

total = renta_anual * impuesto
print("El impositivo a pagar es de {} y tendra que pagar ${} pesos".format(
    impuesto, total))
