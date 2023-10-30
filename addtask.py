import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


frames = [
    "anh",
    "yeu",
    "em"
]


num_repeats = 3


for _ in range(num_repeats):
    for frame in frames:
        clear_console()
        print(frame)
        time.sleep(0.5)  
