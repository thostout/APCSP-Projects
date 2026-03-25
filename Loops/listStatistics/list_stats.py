# List Statistics
# generat 100 random nums, orint the,, give stats about the nums
# Thomas Stout
# 3/25/26

import random

# generate the random 100 nums
nums = []

for i in range(100):
    nums.append(random.randint(1,100))

#counts how many odds and evens there are
even_nums = 0
odd_nums = 0

# loops through list fo rodds and even
for n in nums:
    if n % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

# find max and min numbers
minimum_num = min(nums)
maximum_num = max(nums)

# gets sum of list of nums
total = 0

for x in nums:
    total += x


print(nums)
print(f"There are {even_nums} even numbers.")
print(f"There are {odd_nums} odd numbers.")

print(f"The minimum number is {minimum_num}.")
print(f"The maximum number is {maximum_num}.")

print(f"The sum of all the values is {total}")