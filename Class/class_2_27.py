class positionalList():
    __slots__ = ('_prev','_data','_next')
    class _Node():#Many nodes so slots is helpfull
        def __init__(self, prev, data, next):#should have set/get next and prev
            self._prev = prev
            self._data = data
            self._next = next
    __slots__ = ('_node','_list')
    class _Position():#Few Positions so slots not as useful
        def __init__(self, node, list):
            self._node = node
            self._list = list
        def element(self):
            return self._node._data            
            
    def __init__(self):
        self._len = 0
        self._head = self._Node(None, None, None)
        self._tail = self._Node(self._head, None, None)
        self._head._next = self._tail
    def __len__(self):
        return self._len
    def is_empty(self):
        return self._len == 0

    def _add_between(self,ln,rn,x):#For add_first, add_last, add_before, add_after
        #Constant time: constructor, equal, equal
        nn = self._Node(ln, x, rn)
        ln._next = nn
        rn._prev = nn
        self._len += 1
    def add_first(self,x):
        self._add_between(self._head, self._head._next, x)
    def add_last(self,x):
        self._add_between(self._tail._prev, self._tail, x)
    def add_before(self,p,x):
        self._add_between(p._node._prev, p._node, x)
    def add_after(self,p,x):
        self._add_between(p._node, p._node._next, x)

    def delete(self,p):
        '''
        p._node._prev._next = p._node._next
        p._node._next._prev = p._node._prev
        p._node._next = p._node._prev = None
        '''
        rn = p._node._next
        ln = p._node._prev
        mn = p._node
        ln._next = rn
        rn._prev = ln
        mn._next = mn._prev = None
        p._node = rn
        self._len -= 1

    def replace(self,p,x):
        p._node._data = x

    def first(self):
        return self._Position(self._head._next,self)
    def last(self):
        return self._Position(self._tail._prev,self)
    def before(self,p):
        np = self._Position(p._node._prev,self)
        if np._node == self._head:
            return None
        else:
            return np
    def after(self,p):
        np = self._Position(p._node._next,self)
        if np._node == self._tail:
            return None
        else:
            return np

    def __iter__(self):
        p = L.first()
        while p:
            yield(p.element())
            p = L._after()
        
        
        
