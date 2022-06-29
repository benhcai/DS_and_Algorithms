function canSum(target, array, seen={}) {
  num = array.pop()
  rem = Math.abs(target - num)
  if (num < target && rem in array) return true
  if (array.length === 0) return false
  seen[rem] = num
  return canSum(target, array, seen) 
}

array = [1, 2, 5, 8, 4, 7, 11]
target = 10
console.log(canSum(target, array))