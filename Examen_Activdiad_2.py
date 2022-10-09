user_num = []

count = int(input("How many numbers do you want in your list?\n"))

for i in range(count):
    num = int(input("Please enter {}\n".format(i+1)))
    user_num.append(num)

var = int(input("The next list will contain numbers less than a value given.\nWhat number do you want that to be?\n"))

user_list_2 = []

for i in range(len(user_num)):
    if user_num[i] < var:
        user_list_2.append(user_num[i])

print(user_num)
print(user_list_2)
