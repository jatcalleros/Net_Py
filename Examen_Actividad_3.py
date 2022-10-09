user_list = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
num_count_1 = []
# for i in range(len(user_list)):
#     num = int(input("Please enter {} \n".format(i+1)))
#     user_list.append(num)

for i in range(len(user_list)):
    pairs = []
    num_count = user_list.count(user_list[i])
    pairs.append(user_list[i])
    pairs.append(num_count)
    if tuple(pairs) in num_count_1:
        continue
    num_count_1.append(tuple(pairs))


print(num_count_1)
