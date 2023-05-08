"""
Date: May 8th 2023
@author: Juan Pablo Brasdefer [225936] (juanbrasdefer) Fabian Pawelczyk [226921] (fpawelczyk)
"""

from bucket import *
import random

# Initialize a list with specific values
list = [8, 15, 2, 75, 1154, 11, 45, 206, 1, 23, 21, 72, 87, 3, 2]

print("The original list is:", list)
print("The sorted list is:", bucket_sort(list))


# Generate a random list of integers within a specified range and size
def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


# Check if a list is sorted in ascending order
def is_sorted(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


if __name__ == "__main__":
    # Set parameters for random list generation
    list_size = 15
    lower_bound = 1
    upper_bound = 1500

    # Generate and display the random list
    random_list = generate_random_list(list_size, lower_bound, upper_bound)
    print("The original random list is:", random_list)

    # Sort the random list using bucket_sort and display the result
    sorted_list = bucket_sort(random_list)
    print("The sorted random list is:", sorted_list)

    # Verify if the sorted list is indeed sorted
    if is_sorted(sorted_list):
        print("The list is sorted correctly.")
    else:
        print("The sorting algorithm failed.")

