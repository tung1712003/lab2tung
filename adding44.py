file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
file.close()
# Initialize variables to store sums
sum_first_125 = 0 sum_second_125 = 0
# Assuming each line contains one number, you can convert the lines to integers
numbers = [int(line.strip()) for line in lines]
sum_first_125 = sum(numbers[:125])
# Calculate the sum of the first 125 lines
# Calculate the sum of the second 125 lines
sum_second_125 = sum(numbers[125:250])
# Print the results
print("Sum of the first 125 lines:", sum_first_125)
print("Sum of the second 125 lines:", sum_second_125)