# -*- coding: utf-8 -*-
"""
Date: May 8th 2023
@author: Juan Pablo Brasdefer [225936] (juanbrasdefer) Fabian Pawelczyk [226921] (fpawelczyk)
"""

from math import log10, floor

# Get the exponent of a number in scientific notation
def get_exponent(number):
    base10 = log10(abs(number))
    return floor(base10)

# Recursive function to sort the buckets using the same bucket sort algorithm
def recursive_bucket_sort(array, exponent_diff):
    if len(array) <= 1 or exponent_diff < 0:  # Update the base case condition
        return array

    # Initialize buckets
    buckets = [[] for _ in range(10)]

    # Distribute elements into their respective buckets
    for num in array:
        bucket_index = (num // (10 ** exponent_diff)) % 10
        buckets[bucket_index].append(num)

    # Recursively sort buckets if necessary
    for i in range(10):
        if len(set(buckets[i])) > 1:
            buckets[i] = recursive_bucket_sort(buckets[i], exponent_diff - 1)

    # Merge the buckets to get the sorted array
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Main bucket sort function
def bucket_sort(array):
    if len(array) <= 1:
        return array

    # Calculate the exponent difference between the maximum and minimum values
    max_val = max(array)
    min_val = min(array)
    max_exponent = get_exponent(max_val)
    min_exponent = get_exponent(min_val)
    exponent_diff = max_exponent - min_exponent

    # Call the recursive bucket sort function with the initial exponent difference
    sorted_array = recursive_bucket_sort(array, exponent_diff)
    return sorted_array

# Test the bucket sort function with a sample array
if __name__ == "__main__":
    arr = [29, 25, 3, 49, 9, 37, 21, 43]
    print("Unsorted array:", arr)
    sorted_arr = bucket_sort(arr)
    print("Sorted array:", sorted_arr)
