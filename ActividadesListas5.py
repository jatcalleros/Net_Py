# Escriba un programa que permita crear una lista de plabras y que a continuacion
# cree una segunda lista igual a la primera, pero al reves (no se trata de escribir
# la lista al reves, sino de crear una lista distinta)


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

print(words, "\n")  # Prints the list

# Reverses the list using slicing and saves it in the variable "reversed_words"
reversed_words = words[::-1]


print(reversed_words)
