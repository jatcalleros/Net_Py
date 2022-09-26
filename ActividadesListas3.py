# Escriba un programa que permita crear una lista de palabras y que, a continuación,
# pida dos palabras y sustituya la primera por la segunda en la lista.


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


# Asks user which word they want to replace and what new word to replace it with.
old_word = str(input("Which word you like to replace from the list?: \n"))
# Saves index of old_word
new_word = str(input("What word would you like to replace it with?: \n"))


# If old_word not in the list, exit program.
if old_word not in words:
    print('That word is not in the list: Exiting now!')
else:
    # Saves index of old_word
    old_word_index = words.index(old_word)
   # Removes old_word
    words.remove(old_word)
    # adds new word in index of old_word
    words.insert(old_word_index, new_word)

print(words, "\n")
