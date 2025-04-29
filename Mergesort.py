# Implement Merge Sort(The program should report the number of comparisons)

def merge_sort(arr):
    comparisons = [0]  # Using a list to keep track of the number of comparisons (mutable)
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1  # One comparison for each pair of elements
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Append any remaining elements from the left or right sublists
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        
        # Divide the array into two halves
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        
        # Merge the two sorted halves and return the result
        return merge(left, right)
    
    # Call the recursive merge_sort function
    sorted_arr = merge_sort_recursive(arr)
    return sorted_arr, comparisons[0]

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr, comparisons = merge_sort(arr)
print("Sorted Array:", sorted_arr)
print("Number of Comparisons:", comparisons)
