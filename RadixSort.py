#  Implement Radix Sort

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10  # Count array for digits (0 to 9)

    # Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] to indicate the actual position in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array (stable sort)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy output[] to arr[]
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr

    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Apply counting sort for each digit (exp: 1, 10, 100, ...)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original Array:", arr)
sorted_arr = radix_sort(arr)
print("Sorted Array:", sorted_arr)
