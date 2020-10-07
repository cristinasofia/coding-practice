# 139 https://leetcode.com/problems/word-break/

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    n = len(s)
    dp = [False for _ in range(n+1)]
    dp[0] = True

    for i in range(1, n+1):
        for w in wordDict:
            if dp[i-len(w)] and s[i-len(w):i] == w:
                dp[i] = True

    return dp[-1]

print(wordBreak("catsanddogs", ["cats", "and", "dogs"])) # True
print(wordBreak("catsanddogs", ["cats", "an", "dogs"])) # False