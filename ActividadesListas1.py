# Escriba un programa que permita crear una lista de palabras.
# Para ello, el programa tiene que pedir un número y luego solicitarese
# número de palabras para crear la lista.
# Por último, el programa tiene que escribir la lista.

index = int(input(
    "How many words would you like to add to the list? Hint: the answer is 5\n"))
if index != 5:
    print("The answer is 5, run the program to try again!")
    exit
else:
    words = []
    input_1 = str(input("enter word 1: \n"))
    words.insert(0, input_1)

    input_2 = str(input("enter word 2: \n"))
    words.insert(1, input_2)

    input_3 = str(input("enter word 3: \n"))
    words.insert(2, input_3)

    input_4 = str(input("enter word 2: \n"))
    words.insert(3, input_4)

    input_5 = str(input("enter word 5: \n"))
    words.insert(4, input_5)

    print(words)
