def bucketAlgorithm(graph,root):
    bucket=[]
    queue=[]
    bucket.append(root)
    queue.extend(graph[root])
    while len(queue)!=0:
        print(queue, bucket)
        adjacentVertex=queue.pop()
        if adjacentVertex not in bucket:
            bucket.append(adjacentVertex)
            queue.extend(graph[adjacentVertex])
    return bucket
graph = {'a': ['f','k','b'],'b': ['c','d','a'],'c':['k','b'],'d':['b','f', 'e'],
         'e':['d'],'f':['g','a','d'],'g':['f','h'],'h':['g','i'],'i':['j','k','h'],
         'j':['i'],'k':['i','a','c']}
root='a'

myBucket = bucketAlgorithm(graph,root)
print(myBucket)