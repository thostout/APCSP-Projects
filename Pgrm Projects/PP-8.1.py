import random

my_list = []

for i in range(50):
    my_list.append(random.randint(0,50,))

#while True:
    #num = int(input("enter a num:" ))
    #if num <= 50 and num >=0:
   #    my_list.append(num)
    #else:
    #    break

my_dict = {}

for num in my_list:
    if num not in my_dict:
        my_dict[num] = 1
    else:
        my_dict[num] = my_dict[num] + 1

print()

for key in my_dict:
    print(f"Number: {key} appears {my_dict[key]}")