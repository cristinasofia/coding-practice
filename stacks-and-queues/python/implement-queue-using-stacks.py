class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.a.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.b:
            while self.a:
                x = self.a.pop()
                self.b.append(x)
    
        return self.b.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.a:
            return self.a[0]    # front element either at front/bottom of stack a
        return self.b[-1]          # or at back/top of stack b

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.a and not self.b


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()