from queue import Queue

def rev(q):
#add code here
    stack = []
    while not q.empty():
        stack.append(q.queue[0])
        q.get()
        
    while len(stack)!=0:
        q.put(stack[-1])
        stack.pop()
        
    return q

