function is_scheduling_possible(tasks, prerequisites) {
  // do bfs khan algorithm
  const graph = Array(tasks).fill(0).map(_ => [])
  const indegree = Array(tasks).fill(0)

  // create adjacency list
  for (const [pre, child] of prerequisites) {
    graph[pre].push(child)
    indegree[child]++
  }

  // find initial sources,
  // sources: dequeue of nodes
  const sources = []
  for (let i = 0; i < indegree.length; i++) {
    if (indegree[i] === 0) {
      sources.push(i)
    }
  }

  // bfs
  // reduce children indregree vals for indgree pres with val of 0
  const res = []
  while (sources.length > 0) {
    console.log(sources)
    const node = sources.shift()
    res.push(node)
    for (const neighbor of graph[node]) {
      indegree[neighbor]--
      if (indegree[neighbor] === 0) sources.push(neighbor)
    }
  }

  // If something "further down" in the graph points back to a upper node,
  // then that node will have too many indegrees and not be pushed onto sources.
  // This means the while loop will end early and res.length < tasks.
  console.log(res)
  if (res.length !== tasks) return false

  return true;
}

console.log(`Is scheduling possible: ${is_scheduling_possible(3, [
  [0, 1],
  [1, 2],
])}`);
console.log(`Is scheduling possible: ${is_scheduling_possible(3, [
  [0, 1],
  [1, 2],
  [2, 0],
])}`);
console.log(`Is scheduling possible: ${is_scheduling_possible(6, [
  [2, 5],
  [0, 5],
  [0, 4],
  [1, 4],
  [3, 2],
  [1, 3],
])}`);

