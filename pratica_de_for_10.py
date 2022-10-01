# Escribir un programa que pida al usuario un numero entero
# y muestre por pantalla un triangulo rectangulo.

# User is asked how many rows they wanted printed
user_input = int(input("How many rows would you like printed?: \n"))
print("*  "*20)

# Empty list is created
list = []

# start the count at 1.  With each iteration we add 2 and append it to the
# empty list. if user inputs 5, the element in the list would be [1,3,5,7,9]
count = 1

# This for loop adds elements to the list
for i in range(0, user_input):
    list.append(count)
    count = count + 2
# This for loop creates small lists from the original list and prints
# them in reverse order.
for i in range(1, user_input+1):
    iterated_list = list[:i]
    # Astrik (*) expands the list outside of the brackets.  if no
    # astrik placed, the list will be printed with brackes around it.
    print(*iterated_list[::-1])
