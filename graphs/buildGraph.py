from pythonds.graphs import Graph

wfile = ["pope", "rope", "nope", "hope", "lope", "mope", "cope", "pipe", "pape", "pore", "pose", "poke", "pops"]

def buildGraph(wordFile):
    combs = {}
    graph = Graph()
    for word in wfile:
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:]
            if bucket in combs:
                combs[bucket].append(word)
            else:
                combs[bucket] = [word]
                
    for bucket in combs.keys():
        for word1 in combs[bucket]:
            for word2 in combs[bucket]:
                if word1 != word2:
                    graph.addEdge(word1, word2)
    return combs

graph = buildGraph(wfile)
print('end')