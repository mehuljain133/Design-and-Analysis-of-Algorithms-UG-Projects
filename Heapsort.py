# Implement Heap Sort (The program should report the number of comparisons) 

def heapify(arr, n, i, comparisons):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Compare left child with root
    if left < n and arr[left] > arr[largest]:
        comparisons[0] += 1  # Increment comparison count
        largest = left

    # Compare right child with largest so far
    if right < n and arr[right] > arr[largest]:
        comparisons[0] += 1  # Increment comparison count
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, comparisons)

def heap_sort(arr):
    n = len(arr)
    comparisons = [0]  # Using a list to store the comparison count

    # Build a max-heap (rearrange the array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, comparisons)

    # One by one extract elements from heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap current root with the last element
        heapify(arr, i, 0, comparisons)  # Call heapify on the reduced heap

    return arr, comparisons[0]

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr, comparisons = heap_sort(arr)
print("Sorted Array:", sorted_arr)
print("Number of Comparisons:", comparisons)
