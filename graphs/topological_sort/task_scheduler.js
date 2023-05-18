/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
  // make hash map of task counts
  // make hash map of cooldown init to 0
  // make total tasks count
  let total = 0
  let maxCount = -Infinity
  const taskCount = {}
  const cooldowns = {}
  for (const task of tasks) {
    total++
    if (!(task in taskCount)) taskCount[task] = 0
    taskCount[task]++
    maxCount = Math.max(maxCount, taskCount[task])
    cooldowns[task] = 0
  }

  const taskCountArr = []
  for (const key in taskCount) {
    taskCountArr.push([key, taskCount[key]])
  }
  taskCountArr.sort((a, b) => b[1] - a[1])

  // loop through hashmap of task counts
  // for task, if cooldown is 0
  // minus one count from all tasks
  // make cooldown n

  // if none are 0,
  // push idle
  // minus all from task counts
  const res = []
  console.log(taskCountArr)
  let current = maxCount
  while (maxCount > 0) {
    let hasFree = false
    for (const task of taskCountArr) {
      console.log(task, maxCount, current, cooldowns[task[0]])
      if (task[1] > 0 && task[1] === current && cooldowns[task[0]] <= 0) {
        total--
        res.push(task[0])
        hasFree = true
        task[1]--
        for (const task in cooldowns) {
          cooldowns[task[0]]--
        }
        cooldowns[task[0]] = n
        break
      }
    }
    if (hasFree) {
      maxCount--
      hasFree = false
      current = maxCount
      continue
    }
    console.log("after free")
    if (current === 0) {
      res.push("idle")
      for (const task in cooldowns) {
        cooldowns[task[0]]--
      }
      current = maxCount
    }
    current--
    console.log('curr', current)
  }
  console.log(res)
  return res.length
};

tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2

const ans = leastInterval(tasks, n)
console.log(ans)
