#A1 write a non-recursive and recursive program to calculate Fibonacci numbers and analyze their time and space complexity
import time

# Recursive Fibonacci
def fib_rec(n):
    global rec_steps
    rec_steps += 1
    return n if n < 2 else fib_rec(n-1) + fib_rec(n-2)

# Iterative Fibonacci
def fib_iter(n):
    a, b, steps, s = 0, 1, 0, []
    for _ in range(n):
        s.append(a)
        a, b, steps = b, a+b, steps+1
    return s, steps

n = int(input("Enter n for Fibonacci series: "))

# Recursive
rec_steps = 0
t1 = time.time()
rec_series = [fib_rec(i) for i in range(n)]
t2 = time.time()
print(f"\nRecursive (n={n}): {rec_series}")
print(f"Steps: {rec_steps}, Time: {t2 - t1:.6f}s")

# Iterative
t1 = time.time()
itr_series, itr_steps = fib_iter(n)
t2 = time.time()
print(f"\nIterative (n={n}): {itr_series}")
print(f"Steps: {itr_steps}, Time: {t2 - t1:.6f}s")

#Iterative time complexity=o(n)
#Recursive time complexity=o(2^n)
#Iterative space complexity=O(1)
#Recursive space complexity=O(n)