# Fractional Knapsack Problem using Greedy Method with user input

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(values, weights, capacity):
    items = []
    for i in range(len(values)):
        items.append(Item(values[i], weights[i]))

    # Step 1: Sort items by value-to-weight ratio (descending order)
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0

    # Step 2: Pick items one by one
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0
            break  # knapsack is full

    return total_value


# --- MAIN PROGRAM STARTS HERE ---

n = int(input("Enter number of items: "))

values = []
weights = []

print("\nEnter value and weight for each item:")
for i in range(n):
    val = float(input(f"Value of item {i+1}: "))
    wt = float(input(f"Weight of item {i+1}: "))
    values.append(val)
    weights.append(wt)

capacity = float(input("\nEnter maximum capacity of knapsack: "))

max_value = fractional_knapsack(values, weights, capacity)

print("\nMaximum value in Knapsack =", round(max_value, 2))
