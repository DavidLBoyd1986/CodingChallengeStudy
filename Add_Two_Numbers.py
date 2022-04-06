from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    value_one = ""
    value_two = ""
    # Loops to get the ListNode value, then move to the next, until you reach the end: None
    while l1 is not None:
        value_one = str(l1.val) + value_one
        l1 = l1.next
    while l2 is not None:
        value_two = str(l2.val) + value_two
        l2 = l2.next
    print(value_one)
    print(value_two)

    # Calculate the total, and then change it to a string
    total = int(value_one) + int(value_two)
    total = str(total)
    print(total)

    # Create the answer by recursively adding the value and previous answer as ListNode
    answer = None
    for i in total:
        answer = ListNode(int(i), answer)
    print(answer)

    return answer


# Create the ListNodes for input
# Basic Testcases
test_input_one_list = [2, 4, 3]
test_input_two_list = [5, 6, 4]
test_input_one = None
test_input_two = None

for i in test_input_one_list:
    test_input_one = ListNode(i, test_input_one)
for i in test_input_two_list:
    test_input_two = ListNode(i, test_input_two)

# Testcases with variable length and same numbers
test_input_three_list = [9, 9, 9, 9, 9, 9, 9]
test_input_four_list = [9, 9, 9, 9]
test_input_three = None
test_input_four = None

for i in test_input_three_list:
    test_input_three= ListNode(i, test_input_three)
for i in test_input_four_list:
    test_input_four = ListNode(i, test_input_four)

answer_one = add_two_numbers(test_input_three, test_input_four)


# This adds the list together as if you were doing addition of two large numbers on paper
def add_two_numbers_official_way(l1 : Optional[ListNode], l2 : Optional[ListNode]) -> Optional[ListNode]:
    # Add each interval together until both lists are None, have a variable for the carry
    carry = 0
    reverse_answer = None
    while l1 is not None or l2 is not None:
        # Get the value from ListNodes, if ListNode is None make value 0
        if l1 is None:
            val_one = 0
        else:
            val_one = l1.val
            l1 = l1.next
        if l2 is None:
            val_two = 0
        else:
            val_two = l2.val
            l2 = l2.next
        # Get column total. If it's over nine, divide by 10,
        # total is remainder, and carry 1; else add total to answer
        column_total = val_one + val_two + carry
        if column_total >= 10:
            column_total = column_total % 10
            carry = 1
            reverse_answer = ListNode(column_total, reverse_answer)
            # Reset the column total otherwise if it's the last column
            # The if statement below won't add the carry
            column_total = 0
        else:
            reverse_answer = ListNode(column_total, reverse_answer)
            carry = 0
        # If at end of problem and there is still a remainder to carry add it
        if (l1 is None and l2 is None) and (column_total == 0 and carry > 0):
            column_total = carry
            reverse_answer = ListNode(column_total, reverse_answer)
    # Reverse the answer to get the return value
    answer = None
    while reverse_answer is not None:
        answer = ListNode(reverse_answer.val, answer)
        reverse_answer = reverse_answer.next
    return answer


answer_two = add_two_numbers_official_way(test_input_one, test_input_two)
print("Answer is below")
while answer_two is not None:
    print(answer_two.val)
    answer_two = answer_two.next

answer_three = add_two_numbers_official_way(test_input_three, test_input_four)
print("Answer is below")
while answer_three is not None:
    print(answer_three.val)
    answer_three = answer_three.next
