# Implement Randomized Quick sort (The program should report the number of comparisons)

import random

# Function to partition the array and count comparisons
def partition(arr, low, high, comparisons):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Pointer for the smaller element
    
    for j in range(low, high):
        comparisons[0] += 1  # Increment comparison count
        if arr[j] <= pivot:  # If current element is smaller than or equal to the pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    # Swap the pivot with the element at i + 1 to place it in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1  # Return the partition index

# Function to perform randomized quick sort
def randomized_quick_sort(arr, low, high, comparisons):
    if low < high:
        # Randomly select a pivot and swap it with the last element
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
        # Partition the array and get the pivot index
        pi = partition(arr, low, high, comparisons)
        
        # Recursively apply quick sort to the left and right subarrays
        randomized_quick_sort(arr, low, pi - 1, comparisons)
        randomized_quick_sort(arr, pi + 1, high, comparisons)

# Wrapper function for easier usage
def quick_sort(arr):
    comparisons = [0]  # List to hold the count of comparisons (mutable)
    randomized_quick_sort(arr, 0, len(arr) - 1, comparisons)
    return arr, comparisons[0]

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr, comparisons = quick_sort(arr)
print("Sorted Array:", sorted_arr)
print("Number of Comparisons:", comparisons)
