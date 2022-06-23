class twoStacks :

    def __init__(self,n):
        self.size = n
        self.arr = [None]*n
        self.top1 = -1
        self.top2 = self.size

    def push1(self,x):
        if self.top1 < self.top2-1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow")
            exit(1)

    def push2(self,x):
        if self.top1 < self.top2-1:
            self.top2 = self.top2 -1 
            self.arr[self.top2] = x
        else:
            print("Stack Overflow")
            exit(1)

    def pop1(self):
        if self.top1>=0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow")
            exit()

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow")
            exit()

n = int(input("Size: "))
ts = twoStacks(n)

ts.push1(5)
ts.push2(34)
print("Popped element: ",ts.pop2())
print("Popped element: ",ts.pop1())
ts.push2(28)
ts.push2(56)
print("Popped element: ",ts.pop2())