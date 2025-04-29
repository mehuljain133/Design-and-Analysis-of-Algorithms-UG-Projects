# Implement Insertion Sort (The program should report the number of comparisons) 

def insertion_sort(arr):
    n = len(arr)
    comparisons = 0  # Variable to count the number of comparisons

    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1  # Each time a comparison happens
        arr[j + 1] = key
        
        # If the while loop is not entered, it means no comparisons were made for this key
        if j >= 0:
            comparisons += 1  # To count the comparison where arr[j] <= key
    
    return arr, comparisons

# Example usage:
arr = [12, 11, 13, 5, 6]
sorted_arr, comparisons = insertion_sort(arr)
print("Sorted Array:", sorted_arr)
print("Number of Comparisons:", comparisons)
