# 225 https://leetcode.com/problems/implement-stack-using-queues/

class MyStack(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.a.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.a) > 1:
            x = self.a.pop(0)
            self.b.append(x)
        top = self.a.pop(0)
        self.a, self.b = self.b, self.a
        return top

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.a[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.a and not self.b


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()