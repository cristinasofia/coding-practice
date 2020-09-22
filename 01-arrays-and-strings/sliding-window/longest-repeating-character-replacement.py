# 424 https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        i, j = 0, 0
        d = collections.Counter()
        count = 0
        max_size = float('-inf')
        
        
        while j < len(s):
            
            d[s[j]] += 1
            count = max(count, d[s[j]])
            j += 1
            
            if j - i - count > k:
                d[s[i]] -= 1
                i += 1
            

            max_size = max(max_size, j - i)

                
        return max_size if max_size != float('-inf') else 0