# 904 https://leetcode.com/problems/fruit-into-baskets/

def totalFruit(tree):
    """
    :type tree: List[int]
    :rtype: int
    """
    
    i = 0
    baskets = collections.Counter()
    max_fruit = float('-inf')
    
    for j, x in enumerate(tree):
        baskets[x] += 1
        while len(baskets) > 2:
            baskets[tree[i]] -= 1
            if baskets[tree[i]] == 0:
                del baskets[tree[i]]
            i += 1
            
        max_fruit = max(max_fruit, j - i + 1)
    
    
    return max_fruit