file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
file.close()

sum_first_125 = 0 sum_second_125 = 0

numbers = [int(line.strip()) for line in lines]
sum_first_125 = sum(numbers[:125])

sum_second_125 = sum(numbers[125:250])

print("Sum of the first 125 lines:", sum_first_125)
print("Sum of the second 125 lines:", sum_second_125)
