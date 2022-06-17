import string
import random


def shell_sort(array):
    # Get the largest iteration_step
    iteration_step = 1
    array_length = len(array)
    while iteration_step < array_length / 3:
        iteration_step = (iteration_step * 3) + 1

    # Continue until an Insertion Sort is performed (i.e. iteration_step of 1)
    while iteration_step >= 1:
        # Starting at the iteration step value, go through all remaining values in array
        for i in range(iteration_step, array_length, 1):
            # Look backwards by iteration step until it reaches 0 or value looked at is smaller
            for j in range(i, 0, -iteration_step):
                # If value looked at is larger swap and continue looking back
                if array[j-iteration_step] > array[j]:
                    swap = array[j-iteration_step]
                    array[j-iteration_step] = array[j]
                    array[j] = swap
                # If value looked at is smaller break and go to next value in array (continue 1st for loop)
                else:
                    break
        iteration_step = int(iteration_step / 3)


# Get a randomized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for letter in alphabet:
    list_of_strings.append(letter)
random.shuffle(list_of_strings)
print(list_of_strings)
shell_sort(list_of_strings)
print(list_of_strings)
