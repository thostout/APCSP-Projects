import math
# Loops Program #3: Standard deviation
# Ask user to enter numbers, put them in list, then find standard deviation of numbers
# Thomas Stout
# 1/12/26
def stddev(inputs):
    mean = sum(inputs) / len(inputs)
    return math.sqrt(sum((x - mean) ** 2 for x in inputs) / len(inputs))

inputs = []

print("This program will find the standard deviaton of as many numbers as you want. Once you done input a negative number.")

while True:
    num = int(input("Enter a number: "))

    if num >= 0:
        inputs.append(num)
    else:
        break
result = round(stddev(inputs), 4)
print(f"The standard deviation in {result}")
