# 159 https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

import collections

def lengthOfLongestSubstringTwoDistinct(self, s):
    
    if len(s) <= 2:
        return len(s)
    
    i, j = 0, 0
    max_len = float('-inf')
    d = collections.Counter()
    k = 0
    
    while j < len(s):
        d[s[j]] += 1
        if d[s[j]] == 1:
            k += 1
        j += 1

        if k > 2:
            d[s[i]] -= 1
            if d[s[i]] == 0:
                k -= 1
            i += 1
        
        max_len = max(max_len, j - i)                
        
    return max_len if max_len != float('-inf') else 0