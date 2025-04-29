# Advanced Analysis Technique: Amortized analysis

class DynamicArray:
    def __init__(self):
        self.capacity = 2  # Initial capacity
        self.size = 0  # Initial size of the array
        self.array = [None] * self.capacity  # Array to hold elements

    def insert(self, value):
        if self.size == self.capacity:
            # When the array is full, double its capacity (resize)
            self._resize()

        # Insert the element and update size
        self.array[self.size] = value
        self.size += 1

    def _resize(self):
        # Double the capacity
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array  # Assign the new array

    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def __repr__(self):
        return str(self.array[:self.size])

# Example of Dynamic Array insertions
dynamic_array = DynamicArray()
insertions = 10  # Number of insertions

# Insert 10 elements and observe resizing
for i in range(insertions):
    dynamic_array.insert(i)
    print(f"Insert {i}: {dynamic_array}, Size: {dynamic_array.size}, Capacity: {dynamic_array.capacity}")

# Amortized Analysis:
# Resizing occurs at 2, 4, 8, ... sizes. The cost of resizing is O(n) for each resizing step.
# However, over multiple operations, the amortized cost of insertion is O(1).

# Amortized Cost Explanation:
# - For each series of n insertions, the number of resizing operations is log(n) (since doubling occurs each time).
# - The cost of resizing is spread out over all the insertions.
# - Thus, the amortized cost per insertion is constant: O(1).

# We can observe the resizing process through the printed outputs.

# Amortized Analysis Proof:
# Suppose we perform n insertions. The total work done is the sum of the costs of all the insertions, including the resizing operations.
# The work done during each doubling is at most O(n). 
# However, since doubling happens only log(n) times, the total work done is O(n log n). 
# Thus, the amortized cost per operation is O(1).

# You can further analyze the amortized cost using the potential method and the accounting method.
