# 784 https://leetcode.com/problems/letter-case-permutation/

def letterCasePermutation(S):
    """
    :type S: str
    :rtype: List[str]
    """
    
    def backtrack(i, path):
        if i == len(S):
            output.append(path)
        else:
            if S[i].isalpha():
                backtrack(i + 1, path + S[i].upper())
                backtrack(i + 1, path + S[i].lower())
            else:
                backtrack(i + 1, path + S[i])        
                
    
    output = []
    backtrack(0, "")
    
    return output