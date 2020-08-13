import random
def mst(tree,bucket,graph,adjacent):
    count=0
    while len(bucket) !=0:
        if adjacent in graph.get(bucket[count]):
            tree.append((bucket[count],'--',adjacent[1],'--',adjacent[0]))
            break
        else:
            count+=1
    return tree


def baaltiWithTree(graph,root):
    bucket = []
    queue = []
    distance= {}
    distance[root] = 0
    bucket.append(root)
    queue.extend(graph[root])
    tree=[]
    while len(queue) != 0:
        # print("Queue and bucket are")
        # print(Q, bucket)
        less=min(queue, key = lambda t: t[1])
        if less not in bucket:
            get_index=queue.index(less)
            chosen= queue.pop(get_index)
            adjacentVertex =chosen[0]
            #print(adjacentVertex)
            if adjacentVertex not in bucket:
                tree=mst(tree,bucket,graph,chosen)
                bucket.append(adjacentVertex)
                queue.extend(graph[adjacentVertex[0]])
                distance[adjacentVertex] = distance[root]+chosen[1]
    values=distance.values()
    total=sum(values)
    return total,tree
# prims mst
# graph={'a':[('b',2),('c',9),('d',1)], 'b':[('a',2),('c',4)], 'c':[('b',4), ('a',9),('d',5)], 'd':[('a',1),('c',5)]}
graph={'a':[('b',2),('f',3),('k',9)],'b':[('a',2),('c',2),('d',3)],'c':[('k',5),('b',2)],'d':[('e',1),('f',2),('b',3)],'e':[('d',1)],'f':[('g',4),('a',3),('d',2)],'g':[('f',4),('h',2)],'h':[('g',2),('j',4),('i',6)],'i':[('h',6),('j',3),('k',3)],'j':[('h',4),('i',3)],'k':[('i',3),('a',9),('c',5)]}
root=random.choice(list(graph))
print("Root: ", root)
distance, tree = baaltiWithTree(graph, root)
# print("distance is")
# print(distance)
MST = 0
for i in tree:
    MST = MST+i[2]
    print(i[0], i[1], i[2], i[3], i[4], 'MST', MST, '\n')
