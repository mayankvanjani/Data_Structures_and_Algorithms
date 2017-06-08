class Stack:
    class _Node:
        def __init__(self,next,data):
            self._next = next
            self._data = data
            
    def __init__(self):
        self._top = None
        self._len = 0
    def push(self.x):
        self._top = self._Node(self._top,x)
        self._len += 1
    def pop(self):
        r = self._top._data
        self._top = self._top._next
        self._len -= 1
        return r
    def isempty(self):
        return self._top == None
    def __len__(self):
        return self._len

class Queue:
    class _Node:
        def __init__(self,next,data):
            self._next = next
            self._data = data
    def __init__(self):
        self._back = self._front = None
        self._len = 0
    def enqueue(self,x):
        newbox = self._Node(None,x)
        if self._back:
            self._back._next = newbox
        self._back = newbox
        self._len += 1
        if not self._front:
            self._front = self._back
    def dequeue(self):
        r = self._front._data
        self._front = self._front._next
        self._len -= 1
        if not self._front:
            self._back = None
        return r
    def __iter__(self):
        finger = self._front
        while finger:
            yield finger._data
            finger = finger._next
    def isempty(self):
        return self._len == 0
    def __len__(self):
        return self._len

    
