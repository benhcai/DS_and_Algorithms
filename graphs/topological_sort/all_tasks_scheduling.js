function print_orders(tasks, prerequisites) {
  const sortedOrder = [];

  if (tasks <= 0) return sortedOrder;

  // 1. Initialize the graph
  const inDegree = Array(tasks).fill(0);
  const graph = Array(tasks)
    .fill(0)
    .map(() => []);

  // 2. Build the graph
  for (const [parent, neigh] of prerequisites) {
    graph[parent].push(neigh);
    inDegree[neigh]++;
  }

  // 3. Find all initial sources
  const sources = [];
  for (let i = 0; i < inDegree.length; i++) {
    if (inDegree[i] === 0) sources.push(i);
  }

  const res = [];

  console.log(inDegree, graph, sources);

  function getAllSorts(sources, sortedOrder) {
    if (sortedOrder.length === inDegree.length) {
      return res.push([...sortedOrder]);
    }
    for (let i = 0; i < sources.length; i++) {
      const vertex = sources[i];
      sortedOrder.push(vertex);

      const sourcesNext = [...sources];
      for (const child of graph[vertex]) {
        inDegree[child]--;
        if (inDegree[child] === 0) sourcesNext.push(child);
      }

      // Remove the vertex @ current i val.
      sourcesNext.splice(sourcesNext.indexOf(vertex), 1);
      getAllSorts(sourcesNext, sortedOrder);

      sortedOrder.splice(sortedOrder.indexOf(vertex), 1);
      for (let p = 0; p < graph[vertex].length; p++) {
        inDegree[graph[vertex][p]]++;
      }
    }
  }

  getAllSorts(sources, sortedOrder);

  return res;
}

console.log("Task Orders: ");
console.log(
  print_orders(3, [
    [0, 1],
    [1, 2],
  ])
);

// console.log("Task Orders: ");
// console.log(
//   print_orders(4, [
//     [3, 2],
//     [3, 0],
//     [2, 0],
//     [2, 1],
//   ])
// );

console.log("Task Orders: ");
console.log(
  print_orders(6, [
    [2, 5],
    [0, 5],
    [0, 4],
    [1, 4],
    [3, 2],
    [1, 3],
  ])
);
