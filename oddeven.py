import matplotlib.pyplot as plt
def calculate_sums(filename):
    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file]

    even_sum = sum(numbers[::2]) 
    odd_sum = sum(numbers[1::2])  

    total_sum = even_sum + odd_sum

    even_percentage = (even_sum / total_sum) * 100
    odd_percentage = (odd_sum / total_sum) * 100

    return even_percentage, odd_percentage
file_name = "sequence.txt"
even_percentage, odd_percentage = calculate_sums(file_name)
labels = ['Even', 'Odd']
sizes = [abs(even_percentage), abs(odd_percentage)]
colors = ['lightblue', 'lightcoral']
explode = (0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Percentage of Even and Odd Position Sums')
plt.axis('equal') 
plt.show()
