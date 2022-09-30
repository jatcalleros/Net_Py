# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todo los anos
# que ha comuplido desde 1 hasta su edad.

user_input = int(input("How old are you?: \n"))

print("The following is the number of birthdays you have had on this planet: \n")
for i in range(1, user_input):
    print(i, end=" ")
