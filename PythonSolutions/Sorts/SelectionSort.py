import string
import random


def selection_sort(array):
    # Perform Selection sort
    array_length = len(array)
    # Loop through list
    for i in range(array_length):
        # Make the current position the min_value
        min_value = array[i]
        # For each value in loop, look ahead to find the min_value (quadratic time)
        for j in range(i + 1, array_length):
            # If the look ahead value is lower, make it min_value, and keep track of it's position for exchange
            if array[j] < min_value:
                min_pos = j
                min_value = array[j]
        # After nested loop, swap the first loop value if the value (i) isn't the min_value
        if min_value != array[i]:
            array[min_pos] = array[i]
            array[i] = min_value


# Get a randomized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for i in alphabet:
    list_of_strings.append(i)
random.shuffle(list_of_strings)

# Perform selection_sort
print(list_of_strings)
selection_sort(list_of_strings)
print(list_of_strings)
