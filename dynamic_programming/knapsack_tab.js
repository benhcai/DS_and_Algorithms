function knapsack(profits, weights, capacity) {
    const dp = Array(profits.length).fill(0).map(() => Array(capacity + 1).fill(0))

    for (let c = 0; c < capacity + 1; c++) {
        if (c - weights[0] >= 0) {
            dp[0][c] = profits[0]
        }
    }

    for (let id = 1; id < profits.length; id++) {
        for (let c = 0; c < capacity + 1; c++) {
            const include = c - weights[id] >= 0
                ? profits[id] + dp[id - 1][c - weights[id]]
                : 0
            const exclude = dp[id - 1][c]
            dp[id][c] = Math.max(include, exclude)
        }
    }

    return dp[profits.length - 1][capacity]
}

function main() {
    console.log(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    console.log(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    console.log(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
}


main()