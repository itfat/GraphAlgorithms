def dijstraAlgorithm(graph, root):
    bucket=[]
    queue=[]
    distance = {}
    parent ={}
    distance[root] = 0
    parent[root]=''
    bucket.append(root)
    queue.extend(graph[root])  # priority queue is implemented
    for v in graph[root]:
        parent[v[0]] = root
        # print(v[0],parent[v[0]])
    while len(queue)!=0:
        less = min(queue, key=lambda t: t[1])
        # print("Less is:",less)
        if less not in bucket:
            get_index = queue.index(less)
            chosen = queue.pop(get_index)
            adjacentVertex = chosen[0]
            if chosen[1]<0:
                return -1
            # print("AdjacentVertex is:",adjacentVertex)
            if adjacentVertex not in bucket:
                bucket.append(adjacentVertex)
                queue.extend(graph[adjacentVertex])
                # print(queue)
                for v in graph[adjacentVertex]:  # every bucket push gets the levels updated as well
                    parent[v[0]] = adjacentVertex
                # print("Prent is:",parent[adjacentVertex])
                distance[adjacentVertex] = distance[parent[adjacentVertex]] + chosen[1]
    return distance
# graph= {'a':[('b',2),('f',3),('k',9)],'b':[('a',2),('c',2),('d',3)],'c':[('k',5),('b',2)],
#        'd':[('e',1),('f',2),('b',3)],'e':[('d',1)],'f':[('g',4),('a',3),('d',2)],
#        'g':[('f',4),('h',2)],'h':[('g',2),('j',4),('i',6)],'i':[('h',6),('j',3),('k',3)],
#        'j':[('h',4),('i',3)],'k':[('i',3),('a',9),('c',5)]}
graph={'a':[('b',6),('c',3)],'b':[],'c':[('b',1),('d',2)],'d':[('b',7)]}
root = 'a'
distance=dijstraAlgorithm(graph, root)
print("Single source shortest path using Dijstra is;")
print(distance)