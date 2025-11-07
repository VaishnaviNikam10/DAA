def knapsack(value, weight, capacity):
    n = len(value)
    # Create DP table (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weight[i - 1] <= w:
                include = value[i - 1] + dp[i - 1][w - weight[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# ---------- MAIN PROGRAM ----------
n = int(input("Enter number of items: "))
value = []
weight = []

for i in range(n):
    v = int(input(f"Enter value of item {i + 1}: "))
    w = int(input(f"Enter weight of item {i + 1}: "))
    value.append(v)
    weight.append(w)

capacity = int(input("Enter knapsack capacity: "))

max_value = knapsack(value, weight, capacity)
print(f"\nMaximum value we can put in the bag = {max_value}")


#time complexity=O(n*capacity)
#space same
#ex ITEM   VALUE   WEIGHT
#    1     30      80
#    2     20      20
#    3     10      60
#FOR CAPACITY=100
#cant take all bcoz 80+20+60=160>100

# ITEM      TOTALWT         TOTALVALUE        FITS
#  1         80           30                YES
#  2         20           20                YES
#3           60           10                 YES
#1+2        80+20=100     30+20=50          YES
#1+3        80+60=140     30+10=40          NO
#2+3        20+60=80      20+10=30        YES
#MAX VALUE=50