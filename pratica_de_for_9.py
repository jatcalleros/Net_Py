# dado un numero, cuente el numero total de digitos de un numero.
# por ejemplo, el numero es 75869, por lo que la salida deberia ser 5.

count = 0

user_input = str(input("Enter a number: \n"))

for i in user_input:
    count = count + 1
print("The number of digits your number has is {}".format(count))
