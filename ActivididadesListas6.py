# Escriba un programa que permita crear dos listas de palalbras y que a continuacion,
# escriba las siguientes listas (en las que no debe haber repiticiones).
#   --Lista de palabras que aperecen en las dos listas
#   --Lista de palabras que aparecen en la primer lista, pero no en la segunda
#   --Lista de palabras que aperecen en la segunda lista, pero no en la primera
#   --Lista de palabras que aparecen en ambas listas

# Two empty list are created
list_1 = []
list_2 = []

# 5 items for list_1
print("Enter 5 words for the first list: \n\n")
input_1 = str(input("enter word 1: \n"))
list_1.insert(0, input_1)

input_2 = str(input("enter word 2: \n"))
list_1.insert(1, input_2)

input_3 = str(input("enter word 3: \n"))
list_1.insert(2, input_3)

input_4 = str(input("enter word 2: \n"))
list_1.insert(3, input_4)

input_5 = str(input("enter word 5: \n"))
list_1.insert(4, input_5)

print("-~*"*10, "\n")

# 5 items for list_2
print("Enter 5 words for the second list: \n\n")
input_6 = str(input("enter word 1: \n"))
list_2.insert(0, input_6)

input_7 = str(input("enter word 2: \n"))
list_2.insert(1, input_7)

input_8 = str(input("enter word 3: \n"))
list_2.insert(2, input_8)

input_9 = str(input("enter word 2: \n"))
list_2.insert(3, input_9)

input_10 = str(input("enter word 5: \n"))
list_2.insert(4, input_10)

print("first list", list_1, "\n", "second_list", list_2)
# ---------------------- --Lista De plabras que aperecen en las dos listas--------------------
list_3 = list_1 + list_2

print("The following list is a concatination for list 1 and 2 -----", list_3, "\n")


# -------------------------Lista de palabras que aparecen en ambas listas --------------------

# list_4 contains elements found in both list_1 and list_2
list_4 = []

if list_1[0] in list_2:
    list_4.append(list_1[0])
if list_1[1] in list_2:
    list_4.append(list_1[1])
if list_1[2] in list_2:
    list_4.append(list_1[2])
if list_1[3] in list_2:
    list_4.append(list_1[3])
if list_1[4] in list_2:
    list_4.append(list_1[4])

print("The following list contians the elements repeated in both lists -----", list_4)

# ------------------------Lista de palabras que aparecen en la primer lista, pero no en la segunda

# Elements found in the first list but not in the second.
list_5 = []

if list_1[0] not in list_2:
    list_5.append(list_1[0])
if list_1[1] not in list_2:
    list_5.append(list_1[1])
if list_1[2] not in list_2:
    list_5.append(list_1[2])
if list_1[3] not in list_2:
    list_5.append(list_1[3])
if list_1[4] not in list_2:
    list_5.append(list_1[4])

print("The following list contians elements found in the first list but not in the second -----", list_5)

# ------------------------Lista de palabras que aparecen en la segunda lista, pero no en la primera ----
# list_6 contains elements found in list_2 but not in list_1
list_6 = []
if list_2[0] not in list_1:
    list_6.append(list_2[0])
if list_2[1] not in list_1:
    list_6.append(list_2[1])
if list_2[2] not in list_1:
    list_6.append(list_2[2])
if list_2[3] not in list_1:
    list_6.append(list_2[3])
if list_2[4] not in list_1:
    list_6.append(list_2[4])

print("The following list conatins elements found in the second list but not in the first -----", list_6)
