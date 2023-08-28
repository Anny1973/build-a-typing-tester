import random
import time

# Generate a random string of text
text = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(100))

# Start the timer
start_time = time.time()

# Get the user's input
user_input = input('Type the text: ')

# Stop the timer and calculate the typing speed
typing_speed = len(user_input) / (time.time() - start_time)

# Calculate the accuracy
accuracy = sum(x == y for x, y in zip(user_input, text)) / len(text) * 100

# Print the results
print('Typing speed:', typing_speed, 'wpm')
print('Accuracy:', accuracy, '%')
