# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Print first n Fibonacci numbers
n = int(input("Enter number of terms: "))
for i in range(n):
    print(fibonacci_recursive(i), end=" ")



# Iterative Fibonacci
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Print first n Fibonacci numbers
n = int(input("Enter number of terms: "))
fibonacci_iterative(n)
