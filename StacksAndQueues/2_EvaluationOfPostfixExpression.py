from numpy import str_


class evalpostfix:

    def __init__(self):
        self.stack = []
        self.top = -1

    def pop(self):
        if self.top==-1:
            return 
        else:
            self.top = self.top - 1
            return self.stack.pop()

    def push(self,i):
        self.top = self.top + 1
        self.stack.append(i)

    def func(self,ab):
        for i in ab:
            #   print("I: ",i)
            try:
                self.push(int(i))
            except ValueError:
                val1 = self.pop()
                val2 = self.pop()
                #print(f'Value1 = {val1} & value2 = {val2}')
                if i == '/':
                    self.push(val2/val1)
                else:
                    switcher = {'+':val2+val1, '*':val2*val1, '-':val2-val1, '^':val2**val1}
                    self.push(switcher.get(i))
        
        return int(self.pop())

str = '100 200 + 2 / 5 * 7 +'

str_convert = str.split(' ')

# for i in str_convert:
#     print(i)
obj = evalpostfix()

print(obj.func(str_convert))