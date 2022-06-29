function gridTraveler(m, n, memo={}) {
  if (m > n) {
    const temp = m
    m = n
    n = temp
  }
  const key = `${m},${n}`
  if (key in memo) {
    count++
    return memo[key]
  }
  if (m * n <= 1) return m * n
  memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
  return memo[key]
}

console.log(gridTraveler(5,5))
