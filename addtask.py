import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define your animation frames
frames = [
    "anh",
    "yeu",
    "em"
]

# Number of times to repeat the animation
num_repeats = 3

# Animation loop
for _ in range(num_repeats):
    for frame in frames:
        clear_console()
        print(frame)
        time.sleep(0.5)  # Adjust the delay (in seconds) between frames as needed