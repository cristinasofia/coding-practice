class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s
        
        dp = [[ 0 for _ in range(n)] for _ in range(n)]
        max_len = float('-inf')
        st = 0
    
        for i in reversed(range(n-1)):
            for j in range(i, n):
                if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    
                if dp[i][j] and max_len < j - i + 1:
                    max_len = max(max_len, j - i + 1)
                    st = i
        return s[st:st+max_len]