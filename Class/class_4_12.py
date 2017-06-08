class Set():#Linear Probing
    def __init__(self):
        self._T = [None] * 10
        
    D = object()

    def __contains__(self,x):
        bucket = hash(x)%len(self._T)
        while self._T[bucket]:#loops until None
            if x == self._T[bucket]:
                return True
            b = (b+1)%len(self._T)
            
    def add(self,x):
        bucket = hash(x)%len(self._T)
        while self._T[bucket]:
            b = (b+1)%len(self._T)
        self._T[bucket] = x

    def discard(self,x):
        bucket = hash(x)%len(self._T)
        while self._T[bucket] and self._T[bucket] != x:
            b = (b+1)%len(self._T)
        if self._T[bucket] == x:
            self._T[bucket] = self.D

    def __iter__(self):
        for x in self._T:
            if x is not None and x is not self.D:
                yield x

    def resize(self,newsize):
        L = List(self)
        self._T = [None]*newsize
        for x in L:
            self.add(x)
