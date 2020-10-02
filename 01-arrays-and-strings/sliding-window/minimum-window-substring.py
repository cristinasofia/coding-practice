 # 76 https://leetcode.com/problems/minimum-window-substring/
    
def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    import collections
    d = collections.Counter(t)
    i, j = 0, 0
    minLen = float("inf")
    minStart = 0
    
    k = len(t)
    while j < len(s):
        d[s[j]] -= 1
        if d[s[j]] >= 0:
            k -= 1
        j += 1
        while k == 0:
            if j - i < minLen:
                minLen = j - i
                minStart = i
                
            d[s[i]] += 1
            if d[s[i]] > 0:
                k += 1
            i += 1

    return s[minStart:minStart+minLen] if minLen != float('inf') else ""
