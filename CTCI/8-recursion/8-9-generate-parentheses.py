class Solution(object):
    # 22 https://leetcode.com/problems/generate-parentheses/
    # Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    def generate(self, n):
        paren = []
        def backtrack(p, l, r):
            if r == n:
                paren.append(''.join(p))
            else:
                if l > r:
                    backtrack(p + ")", l, r+1)
                if l < n:
                    backtrack(p + "(", l+1, r)
                    
        p = ""   
        backtrack(p, 0, 0)
        
        return paren

def main():
    obj = Solution()

    n = 3
    print(obj.generate(n))


if __name__ == "__main__":
    main()