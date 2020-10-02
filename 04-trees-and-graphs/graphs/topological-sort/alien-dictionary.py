# https://leetcode.com/problems/alien-dictionary/

import collections
def alienOrder(words):
    """
    :type words: List[str]
    :rtype: str
    """
    
    neigh = collections.defaultdict(list)
    indeg = collections.Counter()
    for x, y in zip(words, words[1:]):
        for i, j in zip(x, y):
            indeg[j] = 0
            if i != j:
                neigh[i].append(j)
                indeg[j] += 1
                break
    """
    i comes before j:
        r : [t]
        e : [r]
        t : [f]
        w : [e]
    
    and indegrees means "how many letters come before j":
        r : 1
        t : 1
        f : 1
        e : 0
        w : 0
    """

    res = []
    stack = [x for x in indeg if indeg[x] == 0]
    while stack:
        v = stack.pop()
        res.append(v)
        for n in neigh[v]:
            indeg[n] -= 1
            if indeg[n] == 0:
                stack.append(n)
        neigh.pop(v)
    
    return "".join(res) if len(res) > 0 else ""