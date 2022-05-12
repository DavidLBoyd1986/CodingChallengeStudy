import string
import random

# Get a randomlized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for i in alphabet:
    list_of_strings.append(i)
random.shuffle(list_of_strings)
print(list_of_strings)

# Perform Selection sort
length_of_list = len(list_of_strings)
# Loop through list
for i in range(length_of_list):
    # Make the current position the min value
    min = list_of_strings[i]
    # For each loop, look ahead to find the lowest value, and exhange i for the lowest value (quadratic time)
    for j in range(i+1, length_of_list):
        # If the look ahead value is lower, make it min, and keep track of it's position for exchange
        if list_of_strings[j] < min:
            min_pos = j;
            min = list_of_strings[j]
    # Swap the value if the current value (i) isn't the minimum value
    if min != list_of_strings[i]:
        list_of_strings[min_pos] = list_of_strings[i]
        list_of_strings[i] = min
print(list_of_strings)

