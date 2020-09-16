class Solution(object):
    def fib1(self, n):

        if n == 0 or n == 1:
            return n
        else:
            return self.fib1(n-1) + self.fib1(n-2)
    
    def fib2(self, n):
        
        def fib_memo(n, memo):
        
            if n == 0 or n == 1:
                return n

            if n not in memo:
                memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

            return memo[n]

        return fib_memo(n,[0]*(n+1))


def main():
    obj = Solution()
    x = 3
    print(obj.fib1(x))

    print(obj.fib2(x))

if __name__ == "__main__":
    main()
