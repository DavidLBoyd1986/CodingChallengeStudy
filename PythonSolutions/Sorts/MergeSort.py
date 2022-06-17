import string
import random


def merge_sort(array):
    # Call internal merge sort that includes start (low) and end (high) of array
    internal_merge_sort(array, 0, len(array)-1)


def internal_merge_sort(array, low, high):
    # Base case, return when array is length of 1
    if high <= low:
        return
    # Decrement recursive value
    mid = int(low + (high - low) / 2)
    # Recurse down left side of array
    internal_merge_sort(array, low, mid)
    # Recurse down right side of arrays
    internal_merge_sort(array, mid+1, high)
    merge(array, low, mid, high)


def merge(array, low, mid, high):
    # create a second array (length of values being merged) because main array can't be sorted in place
    aux = []
    for item in array[0:high+1]:
        aux.append(item)
    # create iterators for each side of the array
    left_side_iterator = low
    right_side_iterator = mid+1
    # Iterate through main array sorting the values from aux array
    for main_iterator in range(low, high+1):
        # If left side is finished, return right side
        if left_side_iterator > mid:
            array[main_iterator] = aux[right_side_iterator]
            right_side_iterator += 1
        # If right side is finished, return left side
        elif right_side_iterator > high:
            array[main_iterator] = aux[left_side_iterator]
            left_side_iterator += 1
        # If right side is less than left side, return right side item
        elif aux[right_side_iterator] < aux[left_side_iterator]:
            array[main_iterator] = aux[right_side_iterator]
            right_side_iterator += 1
        # else left side iterator must be less or equal so return it
        else:
            array[main_iterator] = aux[left_side_iterator]
            left_side_iterator += 1



# Get a randomized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for letter in alphabet:
    list_of_strings.append(letter)
random.shuffle(list_of_strings)

print(list_of_strings)
merge_sort(list_of_strings)
print(list_of_strings)