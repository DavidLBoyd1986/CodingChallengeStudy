
# Brute Force algorithm
# each for loop is O(n), those being nexted together make O(n^2)
# Complexity - O(n^2) because of the nested loop
def two_sum(nums: list[int], target: int) -> list[int]:
    for position_one in range(len(nums)):
        num_one = nums[position_one]
        for position_two in range(len(nums))[position_one+1:]:
            num_two = nums[position_two]
            if num_one + num_two == target:
                return [position_one, position_two]


# Hash Table Algorithm - Two Pass
# Add all the values to a HashMap, and then loop through list again looking for the needed value
# This is done on the 2nd pass by finding the complement needed for each value your on: complement = target - nums[i]
# Complexity - O(n) because you only traverse the list once.
def two_sum_hash_map(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i in range(len(nums)):
        # Add the number you're looking for as the key!!!!!
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


# Hash Table Algorithm - One Pass
# For each value check if the complement is in the HashMap, if it isn't add it to the hashmap
# By the end of the pass the complement would have to be in the HashMap
# Complexity = O(n)
def two_sum_one_pass_hash_map(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        # Don't need to check if it's current index because the index isn't matched until the end
        hashmap[nums[i]] = i


answer = two_sum([2, 5, 5, 11], 10)
print(answer)