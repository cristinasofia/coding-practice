class Solution(object):
    def backspaceCompare(self, S, T):

        def build(x):
            stack = []

            for i in x:
                if i == '#' and stack:
                    stack.pop() # backspace on last element of stack
                elif i == '#':
                    continue # cannot pop an empty stack
                else:
                    stack.append(i) # append only characters
            
            return stack
        
        return build(S) == build(T)

def main():
    # Given two strings S and T, return if they are equal when both are typed into empty text editors. '#' means backspace character.
    
    S = "ab#c"
    T = "ad#c"
    # True. Both S and T become "ac"

    S2 = "a#c"
    T2 = "b"
    # False. S becomes "c" while T becomes "b"

    S3 = "y#fo##f"
    T3 = "y#f#o##f"
    # True. WATCH OUT FOR DOUBLE '#'

    obj = Solution()
    print(obj.backspaceCompare(S, T))
    print(obj.backspaceCompare(S2, T2))
    print(obj.backspaceCompare(S3, T3))

if __name__ == "__main__":
    main()