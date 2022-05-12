import string
import random

# Get a randomlized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for i in alphabet:
    list_of_strings.append(i)
random.shuffle(list_of_strings)
print(list_of_strings)

# ShellSort

# Get the largest iteration_step
iteration_step = 1
array_length = len(list_of_strings)

while iteration_step < array_length/3:
    iteration_step = (iteration_step * 3) + 1

# Continue until an Insertion Sort is performed (i.e. iteration_step of 1
while iteration_step >= 1:
    # Starting at the iteration step value, go through all remaining values in array
    for i in range(iteration_step, array_length, 1):
        # Look backwards by iteration step until it reaches 0 or value looked at is smaller
        for j in range(i, 0, -iteration_step):
            # If value looked at is larger swap and continue looking back
            if list_of_strings[j-iteration_step] > list_of_strings[j]:
                swap = list_of_strings[j-iteration_step]
                list_of_strings[j-iteration_step] = list_of_strings[j]
                list_of_strings[j] = swap
            # If value looked at is smaller break and go to next value in array (continue 1st for loop)
            else:
                break

    iteration_step = int(iteration_step/3)

print(list_of_strings)