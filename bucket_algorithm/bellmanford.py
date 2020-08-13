def bellmanFordAlgorithm(graph, root):
    distance = {}
    parent ={}
    for keys in graph:
        distance[keys]=999
        # print(keys, distance[keys])
    distance[root] = 0
    parent[root] = ''
    for keys in graph:        # loop on vertices
        for v in graph[keys]:       # loop on edges
            parent[v[0]] = keys
            # print(v[0],parent[v[0]])
            # print(distance[v[0]])
            if distance[v[0]] > (distance[parent[v[0]]] + v[1]):
                distance[v[0]] = distance[parent[v[0]]] + v[1]
                # print(v[0],distance[v[0]])

    return distance
# graph= {'a':[('b',2),('f',3),('k',9)],'b':[('a',2),('c',2),('d',3)],'c':[('k',5),('b',2)],
#        'd':[('e',1),('f',2),('b',3)],'e':[('d',1)],'f':[('g',4),('a',3),('d',2)],
#        'g':[('f',4),('h',2)],'h':[('g',2),('j',4),('i',6)],'i':[('h',6),('j',3),('k',3)],
#        'j':[('h',4),('i',3)],'k':[('i',3),('a',9),('c',5)]}
# graph={'a':[('b',6),('c',3)],'b':[],'c':[('b',1),('d',2)],'d':[('b',7)]}
graph={'a':[('b',-1),('c',4)],'b':[('c',3),('d',2),('e',2)],'c':[('d',5)],'d':[('b',1)],'e':[('d',-3)]}
root = 'a'
distance=bellmanFordAlgorithm(graph, root)
print("Single source shortest path using Bellman Ford is;")
print(distance)