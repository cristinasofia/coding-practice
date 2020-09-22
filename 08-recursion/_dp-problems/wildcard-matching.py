#
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        rows = len(s) + 1
        cols = len(p) + 1
        dp = [[False for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = True
        
        for j in range(1, cols):
        	if p[j-1] == '*':
        		dp[0][j] = dp[0][j-1]
        
        """
            _   *   a   *   b
        _   T   T   F   F   F
        a
        d
        c
        e
        b
        """
            
        for i in range(1, rows):
            for j in range(1, cols):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
                    """
                        _   *   a   *   b
                    _       T
                    a           T
                    d
                    c
                    e
                    b
                    """

                elif p[j - 1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    
                    """
                        _   *   a   *   b
                    _               F     
                    a           T   T
                    d
                    c
                    e
                    b
                    """
                    
                    
        return dp[len(s)][len(p)]