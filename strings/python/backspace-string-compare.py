
def backspaceCompare(S, T):

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

def backspaceCompare_withoutStack(S, T):

    def build(x):
        a = []
        skip = 0

        for i in reversed(x):
            if i == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                a.append(i) # append only characters
        
        return a
    
    return build(S) == build(T)


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

print(backspaceCompare(S, T))
print(backspaceCompare(S2, T2))
print(backspaceCompare(S3, T3))

# O(len(S) + len(T))

