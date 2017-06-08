class Count():
    
    class _Item():
        def __init__(self, name, count):
            self._name = name
            self._count = count
    class _countPos():
        def __init__(self,pos):
            self._pos = pos
        def name(self):
            return self._pos.element()._name()
        def count(self):
            return self._pos.element()._count()
        
    def __init__(self):
        self._L = PositionalList()
    def insert(self,x):
        self._L.add_last(self._Item(x, 0))
        return self._countPos(self._L.last())
    def __iter__(self):
        p = self._L.first()#Front of PositionalList is most frequent
        while(p):
            yield self._countPos(p)
            p = self._L.after(p)
    def delete(self, cp):#takes countPos and deletes
        self._L.delete(cp._pos)
        cp._pos = None
    def _increment(self, cp):
        #element gives items
        cp._pos.element()._count += 1
        bef = self._L.before(cp._pos)
        while (cp._pos != self._L.front()) and (cp._pos.element()._count > bef.element()._count):
            #while because if you increment and it becomes greater than 2 equal positions
            item = cp._pos.element()
            self._L.add_before(bef,item)
            self._L.delete(cp._pos)
            cp._pos = self._L.before(bef)



    
