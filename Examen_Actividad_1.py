user_list = []

print("Please enter 5 numbers: \n")

for i in range(5):
    num = int(input("Enter number {}.\n".format(i+1)))
    user_list.append(num)

print("* " * 20)
# ----------------------------------------Sum--------------------
sum = 0
for i in user_list:
    sum = sum + i
# --------------------------------------Median-------------------
median = sum / len(user_list)

# ---------------------------------Max Min Value---------------------
max = min = user_list[0]

for i in range(len(user_list)):
    if user_list[i] > max:
        max = user_list[i]
    if user_list[i] < min:
        min = user_list[i]


# ----------------------Neg count --------------------------------
count = 0

for i in range(len(user_list)):
    if user_list[i] < 0:
        count = count + 1

print("sum:  {}\nMedian:  {}\nMax:  {}\nMin:  {}\nNegative Count:  {}".format(
    sum, median, max, min, count))
