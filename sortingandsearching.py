# More on Sorting and Searching: Heapsort, Lower Bounds using decision trees, sorting inLinear Time - Bucket Sort, Radix Sort and Count Sort, Medians & Order Statistics, complexityanalysis and their correctness

import math

# 1. Heapsort (Comparison-based)
def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root (max) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr

# 2. Lower Bound using Decision Trees (Sorting Lower Bound)
# Lower bound of comparison-based sorting is Ω(n log n) as proven by decision tree complexity.
# Example: Decision tree visualization is beyond simple code implementation but its proof establishes that 
# any comparison-based sorting algorithm requires at least O(n log n) comparisons.

# 3. Bucket Sort (Linear Time Sorting)
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / len(arr) + 1  # Range of each bucket
    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_val) // bucket_range)
        buckets[index].append(num)

    # Sort each bucket and concatenate
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

# 4. Radix Sort (Linear Time Sorting)
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# 5. Count Sort (Linear Time Sorting)
def count_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    # Count occurrences of each number
    for num in arr:
        count[num] += 1

    # Modify count[] to store the actual positions
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# 6. Medians & Order Statistics (Quickselect Algorithm)
# Quickselect: A selection algorithm to find the k-th smallest element in an unordered list.
def quickselect(arr, k):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickselect_helper(arr, low, high, k):
        if low <= high:
            pivot_index = partition(arr, low, high)
            if pivot_index == k:
                return arr[pivot_index]
            elif pivot_index < k:
                return quickselect_helper(arr, pivot_index + 1, high, k)
            else:
                return quickselect_helper(arr, low, pivot_index - 1, k)
        return -1

    return quickselect_helper(arr, 0, len(arr) - 1, k)

# Test the Sorting and Searching Algorithms
arr = [64, 34, 25, 12, 22, 11, 90]

# 1. Heapsort
print("Heapsort:", heapsort(arr.copy()))

# 2. Bucket Sort
arr_bucket = [0.25, 0.45, 0.75, 0.85, 0.95, 0.55]
print("Bucket Sort:", bucket_sort(arr_bucket))

# 3. Radix Sort
arr_radix = [170, 45, 75, 90, 802, 24, 2, 66]
print("Radix Sort:", radix_sort(arr_radix))

# 4. Count Sort
arr_count = [4, 2, 2, 8, 3, 3, 1]
print("Count Sort:", count_sort(arr_count))

# 5. Medians & Order Statistics (Quickselect)
arr_order_stats = [3, 2, 1, 5, 4]
k = 2  # Looking for the 2nd smallest element
print(f"{k}-th smallest element (Quickselect):", quickselect(arr_order_stats.copy(), k-1))

# Complexity Analysis:
# 1. Heapsort: O(n log n) for both time complexity in the worst and average cases.
# 2. Bucket Sort: O(n + k), where n is the number of elements and k is the number of buckets.
# 3. Radix Sort: O(nk), where n is the number of elements and k is the number of digits in the largest number.
# 4. Count Sort: O(n + k), where n is the number of elements and k is the range of the input.
# 5. Quickselect: O(n) on average, but O(n^2) in the worst case if pivot selection is poor (can be improved with median-of-medians).
