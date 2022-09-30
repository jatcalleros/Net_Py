# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interes anual y el nuemero de anos, y muestre por
# pantall el capital obtenido en la inversion cada ano que dura la inversion.

P = float(input("Enter the principal amount you wish to invest \n"))
t = int(input("How many years do you wish invest? \n"))


for i in range(0, t):
    interest = P * .06
    P = P + interest
    print(P)
