# Recursion
```python
    def foo_forward(n):
        if n == 0:
            return
        foo_forward(n-1)
        print(n)
```

```python
foo_forward(5)
    foo_forward(4)
        foo_forward(3)
            foo_forward(2)
                foo_forward(1)
                print(1)
            print(2)
        print(3)
    print(4)
print(5)

```

```python
    def foo_backward(n):
        if n == 0:
            return
        print(n)
        foo_backward(n-1)
```


```python
foo_backward(5)
    print(5)
        foo_backward(4)
            print(4)
                foo_backward(3)
                    print(3)
                        foo_backward(2)
                            print(2)
                                foo_backward(1)
                                    print(1)
```

**O(number of recursive calls * work per recursive call)**
O(n)

## Iteration
1. Reverse a string
```python
    # iterative
    def reverseString(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l +=1
            r -=1

    # recursion      
    def reverseString(self, s):
        
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1)
                
        
        helper(0, len(s)-1)
```
2. Reverse a singly linked list
```python
    # iterative
    def reverseList(self, head):
        
        prev = None
        while head:
            # swap:
            # curr, head = head, head.next
            curr = head
            head = head.next
            # swap:
            # curr.next, prev = prev, curr
            curr.next = prev
            prev = curr
        
        return prev

    # recursion
    def reverseList(self, head):
        
        if not head or not head.next:
            return head
        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev
```


## Permutations
$N!$
```python
    def backtrack(nums, path):
        if len(nums) == 0:
            output.append(path)
        else:
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
    
    output = []
    backtrack(nums, [])
```

## Subsets
$2^N$
```python
    def backtrack(nums, path):
        output.append(path)
        for i in range(len(nums)):
            backtrack(nums[i+1:], path + [nums[i]])
            
    output = []
    backtrack(nums, [])
```

## Combinations
$C^k_n = \frac{N!}{(N-k)! k!}$
```python
    def backtrack(nums, path, target):
        if target < 0:
            return
        elif target == 0:
            output.append(path)
        else:
            for i in range(len(nums)):
                backtrack(nums[i:], path + [nums[i]], target - nums[i])
    
    output = []
    backtrack(candidates, [], target)
    return output
```

## Palindrome

## Parentheses
```python
    paren = []
    def backtrack(p, l, r):
        if r == n:
            paren.append(''.join(p))
        else:
            if l > r:
                backtrack(p + ")", l, r + 1)
            if l < n:
                backtrack(p + "(", l, r - 1)
            
    p = ""   
    backtrack(p, 0, 0)
    
    return paren
```

# Dynamic Programming