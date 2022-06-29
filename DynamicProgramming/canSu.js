function canSum(target, array, seen = {}) {
  if (target === 0) return true;

  for (num of array) {
    rem = target - num;
    console.log(num, rem);
    if (rem < 0) continue;
    return canSum(rem, array, seen);
  }

  return false;
}

array = [2, 3, 4];
target = 8;
console.log(canSum(target, array));

