let dp = []
function knapsack(profits, weights, capacity) {
    dp = Array(weights.length).fill(0).map(() => Array(capacity + 1).fill(-1))

    function recur(id, capacity) {
        if (capacity == 0 || id == weights.length) return 0

        if (dp[id][capacity] !== -1) return dp[id][capacity]

        const include = capacity - weights[id] >= 0
            ? profits[id] + recur(id + 1, capacity - weights[id])
            : 0

        const exclude = recur(id + 1, capacity)

        dp[id][capacity] = Math.max(include, exclude)
        return dp[id][capacity]
    }

    const maxProfit = recur(0, capacity)
    return maxProfit
}

console.log(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
// console.log(dp)
console.log(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))