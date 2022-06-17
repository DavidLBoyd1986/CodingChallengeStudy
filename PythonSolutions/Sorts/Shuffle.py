import random
import string


def shuffle(array):
    array_length = len(array)
    for i in range(array_length):
        random_position = random.randint(0, i)
        swapped_item = array[random_position]
        array[random_position] = array[i]
        array[i] = swapped_item


# Get a randomized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for letter in alphabet:
    list_of_strings.append(letter)
print(list_of_strings)
shuffle(list_of_strings)
print(list_of_strings)
random.shuffle(list_of_strings)
print(list_of_strings)
