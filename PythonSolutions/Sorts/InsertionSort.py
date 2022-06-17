import string
import random


def insertion_sort(array):
    # Loop through array
    for i in range(len(array)):
        # For every value go backwards through array until it reaches lower value or start of array
        for j in range(i, 0, -1):
            # if previous value is higher swap it for the current lower value
            if array[j-1] > array[j]:
                swap = array[j-1]
                array[j - 1] = array[j]
                array[j] = swap
            # if previous value is lower, the left half of array is sorted, go to next value
            else:
                break


# Get a randomized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for letter in alphabet:
    list_of_strings.append(letter)
random.shuffle(list_of_strings)

print(list_of_strings)
insertion_sort(list_of_strings)
print(list_of_strings)
