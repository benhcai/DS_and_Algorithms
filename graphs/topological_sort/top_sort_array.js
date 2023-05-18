function createAdjList(vertices, edges) {
  const graph = Array(vertices).fill(0)
  for (let i = 0; i < graph.length; i++) graph[i] = []
  return graph
}

function createInDegree(vertices) {
  const inDegree = Array(vertices).fill(0)
  return inDegree
}

function initializeGraphs(edges, graph, inDegree) {
  for (const [parent, child] of edges) {
    graph[parent].push(child)
    inDegree[child]++
  }
  console.log('graph', graph)
  console.log('ind', inDegree)
}

function getInitialSources(inDegree) {
  const sources = []
  for (let i = 0; i < inDegree.length; i++) {
    if (inDegree[i] === 0) sources.push(i)
  }
  console.log('sources', sources)
  return sources
}

function sortNodes(sources, graph, inDegree) {
  const sortedNodes = []
  while (sources.length > 0) {
    const vertex = sources.shift()
    sortedNodes.push(vertex)
    console.log(vertex, graph, graph[vertex], inDegree)
    for (const child of graph[vertex]) {
      inDegree[child]--
      console.log(inDegree)
      if (inDegree[child] === 0) sources.push(child)
    }
  }

  return sortedNodes
}

function topologicalSort(vertices, edges) {
  const graph = createAdjList(vertices, edges)
  const inDegree = createInDegree(vertices)
  initializeGraphs(edges, graph, inDegree)
  const initialSources = getInitialSources(inDegree)
  const sortedNodes = sortNodes(initialSources, graph, inDegree)
  return sortedNodes
}


const a = topologicalSort(4, [
  [3, 2],
  [3, 0],
  [2, 0],
  [2, 1],
]);

console.log(a)
