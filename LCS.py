# Write a program to determine the LCS of two given sequences

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table in bottom-up fashion
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # Recover the LCS from the table
    i, j = m, n
    lcs_str = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_str.reverse()
    return ''.join(lcs_str), dp[m][n]

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
lcs_string, length = lcs(X, Y)
print("Sequence 1:", X)
print("Sequence 2:", Y)
print("Longest Common Subsequence:", lcs_string)
print("Length of LCS:", length)
