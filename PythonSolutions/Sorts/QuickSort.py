import string
import random


def quick_sort(array):
    """
    Sorts the array in-place with an average speed of: N log N
    :param array: Array to be sorted
    :return: Sorts the array in-place, so the sorted array doesn't need to be returned
    """
    # Shuffle array to reduce chances of worst-case runtime
    random.shuffle(array)
    # Initiate sort, which is recursive
    sort(array, 0, len(array)-1)


def sort(array, low, high):
    """
    Partitions the array (see partition method) and then recursively sorts smaller segments of the array
    :param array: Array to be sorted
    :param low: Index of the low (left) side starting point. Will also be used as the partition index
    :param high: Index of the high (right) side starting point
    :return: Sorts the array in place, nothing is returned
    """
    # Checks for base case of array with size of 1
    if high <= low:
        return
    # Partition the array, and returns partition position in array
    partition_index = partition(array, low, high)
    sort(array, low, partition_index-1)
    sort(array, partition_index+1, high)


def partition(array, low, high):
    """
    Partition the array so:
    Everything left of partition is (< partition); everything right of partition is (> partition).
    :param array: Array to be sorted
    :param low: Index of the low (left) side starting point. Will also be used as the partition index
    :param high: Index of the high (right) side starting point
    :return:
    """
    # Set low and high indexes - REMEMBER THIS STEP - can't use low and high arguments provided
    partition_index = low
    low_index = low
    high_index = high
    while True:
        # increment low immediately so it's not on the partition index
        low_index += 1
        # Move low index until an element higher than the partition is reached
        while array[low_index] < array[partition_index]:
            if low_index == high:
                break
            low_index += 1
        # Move high index until an element lower than the partition is reached
        while array[partition_index] < array[high_index]:
            if high_index == low:
                break
            high_index -= 1
        # Check to verify the two indexes haven't met
        if low_index >= high_index:
            break
        # Swap elements
        swap(array, low_index, high_index)
    # Swap partition into low index
    swap(array, partition_index, high_index)
    return high_index


def swap(array, low, high):
    """
    Swaps the elements in array at indexes: low and high
    :param array: Array to be sorted
    :param low: Index of the low (left) side that is > partition, and will be swapped
    :param high: Index of the high (right) side that is < the partition, and will be swapped
    :return: Nothing. Swaps elements of array in place
    """
    swap_element = array[low]
    array[low] = array[high]
    array[high] = swap_element
    return


# Get a randomized list of all the letters in the alphabet
alphabet = string.ascii_lowercase
list_of_strings = []
for letter in alphabet:
    list_of_strings.append(letter)
random.shuffle(list_of_strings)

print(list_of_strings)
quick_sort(list_of_strings)
print(list_of_strings)