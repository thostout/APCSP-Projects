# Loops Program #1: Counting
# Input integers and count how many are positive and negative there are
# Thomas Stout
# 1/5/26

integer_list = []

positives = 0
negatives = 0



for i in range(5):
    user_num = int(input("Please enter an integer: "))
    integer_list.append(user_num)


for n in integer_list:
    if n < 0:
        positives += 1
    else:
        negatives +=1

integer_list_len = len(integer_list)
integer_list_sum = sum(integer_list)

average = integer_list_sum/integer_list_len

print(f"You gave {positives} poastive numbers.")
print(f"You gave {negatives} posative numbers.")
print(f"The average of your numbers are {average}.")