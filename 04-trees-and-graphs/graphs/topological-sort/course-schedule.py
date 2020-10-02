
def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    if numCourses <= 0:
        return [0]
    import collections
    neigh = collections.defaultdict(set)
    indeg = [0 for _ in xrange(numCourses)]
    
    for x, y in prerequisites:
        neigh[y].add(x)
        indeg[x] += 1
    
    res = []
    stack = [x for x in xrange(numCourses) if indeg[x] == 0]
    
    while stack:
        v = stack.pop()
        res.append(v)
        for n in neigh[v]:
            indeg[n] -= 1
            if indeg[n] == 0:
                stack.append(n)
        neigh.pop(v)
    
    return res if len(res) == numCourses else []