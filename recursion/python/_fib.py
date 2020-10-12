
def fib1(n):

    if n == 0 or n == 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    
    def fib_memo(n, memo):
    
        if n == 0 or n == 1:
            return n

        if n not in memo:
            memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

        return memo[n]

    return fib_memo(n,[0]*(n+1))



x = 3
print(fib1(x))

print(fib2(x))

