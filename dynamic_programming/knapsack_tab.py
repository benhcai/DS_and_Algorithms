def knapsack(profits, weights, capacity):
    # Table with id as rows and capacity as columns
    dp = [[0 for _ in range(capacity+1)] for _id in range(len(weights))]
    
    # Setup first row of table, base condition where id is 0
    for c in range(capacity + 1):
        if c - weights[0] >= 0:
            # if capacity still exists, we can add the profit
            dp[0][c] = profits[0]

    for id in range(1, len(weights)):
        for c in range(1, capacity + 1):
            include = 0

            if c - weights[id] >= 0:
                # here we add the current profit, plus,
                # the max profit possible from the previous iterations at the remaining capacity
                include = profits[id] + dp[id - 1][c - weights[id]]
            
            exclude = dp[id - 1][c]

            dp[id][c] = max(include, exclude)

    return dp[len(weights) - 1][capacity]

def main():
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()