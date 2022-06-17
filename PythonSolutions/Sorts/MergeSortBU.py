import string
import random


def merge_sort_bu(array):
    array_length = len(array) - 1
    # Loop setting main iterator steps: 2, 4, 8, 16.... by iterating over half the main iterator size
    half_array = 1
    # ends when half_array > 2/3 array length because half_array is greater than half the length of the array
    # This means it had to iterate over entire array since it performed merge when half array was mid of array_length
    while half_array < array_length-(array_length/3):
        # Create aux array for this iteration step
        aux = []
        for item in array[0:array_length+1]:
            aux.append(item)
        # Loop through values in main array by iterator step,
        for i in range(0, array_length, half_array + half_array):
            # perform merge operation on iterator size
            merge(array, aux, i, i+half_array-1, min(i+half_array+half_array-1, array_length))
        half_array += half_array


def merge(array, aux, low, mid, high):
    left_i = low
    right_i = mid + 1
    # loop through main array
    for main_i in range(low, high+1):
        # If left array is done, take right item
        if left_i > mid:
            array[main_i] = aux[right_i]
            right_i += 1
        # If right array is done, take left item
        elif right_i > high:
            array[main_i] = aux[left_i]
            left_i += 1
        # if right side item less than left side item,take right side
        elif aux[right_i] < aux[left_i]:
            array[main_i] = aux[right_i]
            right_i += 1
        # left side must be less or equal to right, take left side item
        else:
            array[main_i] = aux[left_i]
            left_i += 1


# Get a randomized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for letter in alphabet:
    list_of_strings.append(letter)
random.shuffle(list_of_strings)

print(list_of_strings)
merge_sort_bu(list_of_strings)
print(list_of_strings)
