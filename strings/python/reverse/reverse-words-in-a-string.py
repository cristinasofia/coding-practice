# 151 https://leetcode.com/problems/reverse-words-in-a-string/

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    
    words = s.split(' ')
    ans = []
    for w in words:

        if len(w) == 0:
            continue
        ans.append(w)

    return " ".join(ans[::-1])

# 186 https://leetcode.com/problems/reverse-words-in-a-string-ii/

def reverseWords2(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    
    def helper(l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    
    l = 0
    for i, c in enumerate(s):
        if c.isspace():
            helper(l, i-1) # reverse word
            l = i + 1
            
    helper(l, len(s)-1) # reverse the last word
    helper(0, len(s)-1) # reverse entire array