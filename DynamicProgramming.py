# Dynamic Programming: Application to various problems (for reference; Weighted IntervalScheduling, Sequence Alignment, Knapsack), their correctness and analysis. Greedy Algorithms:Application to various problems, their correctness and analysis.

# Dynamic Programming Algorithms

# 1. Weighted Interval Scheduling (Dynamic Programming)
def weighted_interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort intervals by finish time

    def find_last_non_conflicting(i):
        for j in range(i-1, -1, -1):
            if intervals[j][1] <= intervals[i][0]:
                return j
        return -1

    n = len(intervals)
    dp = [0] * n
    dp[0] = intervals[0][2]  # The weight of the first interval

    for i in range(1, n):
        include = intervals[i][2] + (dp[find_last_non_conflicting(i)] if find_last_non_conflicting(i) != -1 else 0)
        exclude = dp[i-1]
        dp[i] = max(include, exclude)

    return dp[-1]

# 2. Sequence Alignment (Dynamic Programming)
def sequence_alignment(seq1, seq2, gap_penalty=-1, match_score=1, mismatch_penalty=-1):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i * gap_penalty
    for j in range(n + 1):
        dp[0][j] = j * gap_penalty

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = dp[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty)
            delete = dp[i-1][j] + gap_penalty
            insert = dp[i][j-1] + gap_penalty
            dp[i][j] = max(match, delete, insert)

    return dp[m][n]

# 3. 0/1 Knapsack Problem (Dynamic Programming)
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Greedy Algorithms

# 4. Fractional Knapsack Problem (Greedy)
def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    ratios = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    for ratio, weight, value in ratios:
        if capacity > 0 and weight <= capacity:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)
            break

    return total_value

# 5. Activity Selection Problem (Greedy)
def activity_selection(start, finish):
    n = len(start)
    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])  # Sort by finish time

    selected_activities = [activities[0]]
    last_finish_time = activities[0][1]

    for i in range(1, n):
        if activities[i][0] >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = activities[i][1]

    return selected_activities

# Testing the Algorithms

# 1. Weighted Interval Scheduling
intervals = [(1, 3, 5), (3, 5, 6), (0, 6, 5), (4, 7, 2), (3, 9, 8)]
print("Maximum weight from non-overlapping intervals:", weighted_interval_scheduling(intervals))

# 2. Sequence Alignment
seq1 = "AGGTAB"
seq2 = "GXTXAYB"
print("Sequence Alignment Score:", sequence_alignment(seq1, seq2))

# 3. Knapsack Problem (0/1 Knapsack)
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print("Maximum value in 0/1 Knapsack:", knapsack(weights, values, capacity))

# 4. Fractional Knapsack Problem
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value in Fractional Knapsack:", fractional_knapsack(weights, values, capacity))

# 5. Activity Selection Problem
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
print("Selected activities:", activity_selection(start, finish))
