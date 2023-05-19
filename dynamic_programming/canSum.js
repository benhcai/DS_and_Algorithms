function canSum(target, array, memo = {}) {
  /*
    * n = length of array; m = target
    * Time O(m*n) with memoization; otherwise O(n**m)
    * Space O(m)
  */
  if (target === 0) return true;
  if (target < 0) return false

  if (target in memo) return memo[target]
  
  for (let num of array) {
    const rem = target - num;
    memo[rem] = canSum(rem, array, memo)
    if (memo[rem] === true) {
      return true
    }
  }

  return false;
}

const array = [7, 14];
const target = 300;
console.log(canSum(target, array));
