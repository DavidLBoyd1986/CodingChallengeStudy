import string
import random

# Get a randomlized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for i in alphabet:
    list_of_strings.append(i)
random.shuffle(list_of_strings)
print(list_of_strings)

# InsertionSort
for i in range(len(list_of_strings)):
    for j in range(i, 0, -1):
        if list_of_strings[j-1] > list_of_strings[j]:
            swap = list_of_strings[j-1]
            list_of_strings[j - 1] = list_of_strings[j]
            list_of_strings[j] = swap
        else:
            break

print(list_of_strings)
