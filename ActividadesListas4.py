# Escriba un programa que permita crear una lista de palabras y que,
# a continuacion, pida una palabra y elimine esa palabra de la lista.


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

print(words, "\n")  # Prints the list#

del_word = str(input("Which word would you like to delete from the list?: \n"))

if del_word not in words:
    print("That word is not in the list, exiting now!")
else:
    # Removes word from list
    words.remove(del_word)

print("Here is your new list", words)
