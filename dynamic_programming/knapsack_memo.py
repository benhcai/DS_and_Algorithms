def knapsack(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]

    def recur(id, capacity):
        if capacity == 0 or id == len(profits):
            return 0
        
        if dp[id][capacity] != -1:
            return dp[id][capacity]

        include = 0
        if capacity - weights[id] >= 0:
            include = profits[id] + recur(id + 1, capacity - weights[id])

        exclude = recur(id + 1, capacity)

        dp[id][capacity] = max(include, exclude)
        return dp[id][capacity]

    return recur(0, capacity)

def main():
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()