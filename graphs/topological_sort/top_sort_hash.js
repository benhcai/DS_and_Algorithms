function topologicalSort(vertices, edges) {
  const graph = {};
  const inDegree = {};
  // create graph
  // define indegree
  for (const [parent, child] of edges) {
    inDegree[child] = child in inDegree ? ++inDegree[child] : 1;
    if (!(parent in graph)) graph[parent] = [];
    graph[parent].push(child);
  }
  console.log("graph", graph);
  console.log("indegree", inDegree);

  const sources = [];
  for (const key in graph) {
    if (!(key in inDegree)) sources.push(Number.parseInt(key));
  }
  console.log("sources", sources);

  const sortedNodes = [];
  while (sources.length > 0) {
    const vertex = sources.shift();
    sortedNodes.push(vertex);
    console.log("v", vertex);
    if (vertex in graph) {
      for (const child of graph[vertex]) {
        console.log("child", child, "indegree ch", inDegree[child]);
        inDegree[child]--;
        if (inDegree[child] === 0) sources.push(child);
      }
    }
  }

  return sortedNodes;
}

const edges = [
  [3, 2],
  [3, 0],
  [2, 0],
  [2, 1],
];
console.log("edges", edges);
const a = topologicalSort(4, edges);
console.log(a);
