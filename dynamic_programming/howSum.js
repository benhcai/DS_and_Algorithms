function howSum(targetSum, numbers, memo={}) {
  /*
    * m = targetSum; n = numbers.length
    * Brute force: 
    * - time: O(n^m * m)
    *   time: n^m - each level results in prev * n more time,
    *   this will occur m times as that is the number of levels.
    *   Additionally, spreading the memo at worst-case will be take m.
    * - space: O(m)
    * Memoization: 
    * - time: O(n*m^2); 
    * - space: O(m^2), quadratic not exponential.
    *   O(m) space from the m depth calls, 
    *   then O(m) as that is the max length of a memo value
    *
  */
  if (targetSum === 0) return []
  if (targetSum < 0) return null
  if (targetSum in memo) return memo[targetSum]
  for (let n of numbers) {
    const remainder = targetSum - n
    memo[remainder] = howSum(remainder, numbers, memo)
    if (memo[remainder] !== null) {
     return [...memo[remainder], n]
    }
  }
  return null
}

console.log(howSum(7,[2,3]))
console.log(howSum(7,[5, 3, 4, 7]))
console.log(howSum(7,[2, 4]))
console.log(howSum(300,[3,5,2]))

