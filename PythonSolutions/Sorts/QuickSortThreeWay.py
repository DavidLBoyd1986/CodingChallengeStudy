import string
import random


def quick_sort(array):
    random.shuffle(array)
    sort(array, 0, len(array) - 1)


def sort(array, low, high):
    # Base-case
    if low >= high:
        return
    lt = low
    gt = high
    eq = low+1
    partition = array[low]
    while eq <= gt:
        # If the eq element is lower than lt, swap it with lt, and increment lt and eq, to keep it left of lt
        if array[eq] < partition:
            exchange(array, lt, eq)
            lt += 1
            eq += 1
        # If the eq element is greater than lt, swap it with gt, and decrement gt, to keep it right of gt
        elif array[eq] > partition:
            exchange(array, eq, gt)
            gt -= 1
        # eq must equal lt, increment eq to keep the equal element b/w lt and eq
        else:
            eq += 1
    # Recursively sort the array left of lt, and then sort array right of gt
    sort(array, low, lt-1)
    sort(array, gt+1, high)


def exchange(array, low, high):
    swap = array[low]
    array[low] = array[high]
    array[high] = swap


# Get a randomized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for letter in alphabet:
    list_of_strings.append(letter)
random.shuffle(list_of_strings)
print(list_of_strings)
quick_sort(list_of_strings)
print(list_of_strings)
