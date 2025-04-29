#Algorithm Design Techniques: Iterative technique: Applications to Sorting and Searching(review), their correctness and analysis. Divide and Conquer: Application to Sorting andSearching (review of binary search), merge sort, quick sort, their correctness and analysis. 

# Iterative Techniques: Binary Search and Bubble Sort

# Binary Search (Iterative)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Element found
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    return -1  # Element not found

# Bubble Sort (Iterative)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        if not swapped:
            break  # No swaps means the array is already sorted
    return arr

# Divide and Conquer Techniques: Merge Sort and Quick Sort

# Merge Sort (Divide and Conquer)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursively sort the left half
    right = merge_sort(arr[mid:])  # Recursively sort the right half
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort (Divide and Conquer)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Testing the algorithms
arr = [64, 34, 25, 12, 22, 11, 90]
target = 22

print("Original Array:", arr)

# Testing Binary Search
sorted_arr = sorted(arr)  # Sorting the array for binary search
print(f"Element {target} found at index {binary_search(sorted_arr, target)} using Binary Search.")

# Testing Bubble Sort
sorted_bubble = bubble_sort(arr.copy())
print("Sorted Array using Bubble Sort:", sorted_bubble)

# Testing Merge Sort
sorted_merge = merge_sort(arr.copy())
print("Sorted Array using Merge Sort:", sorted_merge)

# Testing Quick Sort
sorted_quick = quick_sort(arr.copy())
print("Sorted Array using Quick Sort:", sorted_quick)
