from collections import deque


class Solution:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self,x):
        self.q1.append(x)
        self._top = x

    def pop(self):
        while len(self.q1) > 1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self):
        return self._top

    def isEmpty(self):
        return len(self.q1)==0