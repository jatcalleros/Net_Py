# Escriba un programa que permita crear una lista de palabras y que, a continuación,
# pida una palabra y diga cuántas veces aparece esa palabra en la lista.

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

print("The word {} appears {} times".format(input_1, words.count(words[0])))
print("The word {} appears {} times".format(input_2, words.count(words[1])))
print("The word {} appears {} times".format(input_3, words.count(words[2])))
print("The word {} appears {} times".format(input_4, words.count(words[3])))
print("The word {} appears {} times".format(input_5, words.count(words[4])))
