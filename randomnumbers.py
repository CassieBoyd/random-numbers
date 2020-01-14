# Use the following code to create a list of 10 random numbers. Each number will be between 0 and 6.

# import random

# my_randoms = list()
# for i in range(10):
#     my_randoms.append(random.randrange(1, 6))

# Then iterate a different list of numbers that are sequential from 1 to 10. Use the following code as your starting point.

import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

# my_randoms is set to an empty list.
my_randoms = list()

# for each number in a range of 0-9, my_randoms is appended with a random number from a range of 1-5
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

print("Random List", my_randoms)

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)

# Iterate from 1 to 10
# The in keyword is used to check if a value is present in a sequence (list, range, string etc.). The in keyword is also used to iterate through a sequence in a for loop.
for number in numbers_1_to_10:
    # the_numbers_match = False

    # Iterate your random number list here
    # if number that's being evaluated is in my_randoms : print statement
    if number in my_randoms:
        print(f'{number} is in the random list')
# Otherwise, print this statement instead
    else: 
        print(f'{number} is not in the random list')

# if number == numbers_1_to_10:
#   the_numbers_match = True