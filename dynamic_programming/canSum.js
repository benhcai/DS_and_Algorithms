function canSum(target, array, memo = {}) {
  console.log('target', target)
  if (target === 0) return true;
  if (target < 0) return false
  if (memo[target]) console.log('memod')
  if (memo[target]) return memo[target]
  for (num of array) {
    rem = target - num;
    console.log(num, rem);
    if (rem < 0) continue;
    memo[rem] = memo[rem] || canSum(rem, array, memo)
    return memo[rem] 
  }

  return false;
}

array = [3, 4, 3];
target = 16;
console.log(canSum(target, array));
