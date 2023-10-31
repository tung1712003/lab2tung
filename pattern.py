
pattern_size = 5  


for i in range(pattern_size):
    line = ''
    for j in range(pattern_size):
        if j == i or j == pattern_size - i - 1:
            line += 'X'
        else:
            line += ' '
    print(line * 2)
