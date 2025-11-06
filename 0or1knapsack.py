# 0-1 Knapsack Problem using Dynamic Programming

def knapsack_01(values, weights, capacity, n):
    # Create DP table (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# --- MAIN PROGRAM STARTS HERE ---

n = int(input("Enter number of items: "))

values = []
weights = []

print("\nEnter value and weight for each item:")
for i in range(n):
    val = int(input(f"Value of item {i+1}: "))
    wt = int(input(f"Weight of item {i+1}: "))
    values.append(val)
    weights.append(wt)

capacity = int(input("\nEnter maximum capacity of knapsack: "))

max_value = knapsack_01(values, weights, capacity, n)
print("\nMaximum value in Knapsack =", max_value)
