class HeapPQ():
    class _Item:
        def __init__(self,k,v):
            self._k = k
            self._v = v
            
    def __init__(self, I=None):
        if A == None:
            self._A = []
        else:
            self._A = List(A)#Copy
            for i in range(len(self._A)):
                self._bubble_up(i)
        self._A = []
        if I:
            for k,v in I:
                self.add(k,v)

    def __len__(self):
        return len(self._A)
    def is_empty(self):
        return len(self) == 0

    def _left(i):
        return (2 * i + 1)
    def _right(i):
        return (2 * i + 2)
    def _parent(i):
        return ((i - 1) // 2)
    def _swap(self,i,j):
        self._A[i],self._A[j] = self._A[j],self._A[i]
    def _valid(self,i):
        return i < len(self)
    
    def add(self,k,v):
        self._A.append( self._Item(k,v) )
        self._bubble_up(self, len(self._A)-1 )
        
    def _bubble_up(self,i):
        if i == 0:#root
            return
        elif self._A[i]._k < self._A[self._parent(i)]._k:
            self._swap(i, self._parent(i))
            self._bubble_up(self._parent(i))

    def min(self):
        if self.is_empty():
            return (None,None)
        return (self._A[0]._k, self._A[0]._v)

    def remove_min(self):
        rv = self.min()
        self._A[0] = self._A.pop()#moves k,v to root
        self._bubble_down(0)
        return rv

    def _bubble_down(self,i):
        l = self._left(i)
        r = self._right(i)
        smallest = i
        if self._valid(l) and (self._A[l]._k < self._A[smallest]._k):
            smallest = l
        if self._valid(r) and (self._A[r]._k < self._A[smallest]._k):
            smallest = r
        if i != smallest:
            self._swap(i,smallest)
            self._bubble_down(smallest)
        
        
