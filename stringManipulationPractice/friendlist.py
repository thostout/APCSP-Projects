# Friend List
# friend list program
# 3/12/26
# Thomas Stout
import random

friends = []

print("Welcome! Please enter your friends first name. Press d when you are done.")

while True:
    names = input("Enter a friends name here: ")
    if names == 'd':
        break
    else:
        friends.append(names)

print(f"You have {len(friends)} friends.")
print("Here is your list of friends:")
for num, name in enumerate(friends):
    print(f"{num}. {name}")

