
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    i, j = 0, 0
    count = 0
    import collections
    d = collections.Counter()
    max_len = float('-inf')
    
    while j < len(s):
        d[s[j]] += 1
        if d[s[j]] > 1:
            count += 1
        j += 1

        if count > 0:
            d[s[i]] -= 1
            if d[s[i]] > 0:
                count -= 1
            i += 1

        max_len = max(max_len, j - i)
        
    return max_len


# 3 https://leetcode.com/problems/longest-substring-without-repeating-characters/

input1 = "abcabcbb"
# 3
input2 = "bbbbb"
# 1
input3 = "pwwkew"
# 3

