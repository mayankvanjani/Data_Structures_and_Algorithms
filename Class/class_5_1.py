class Trie():
    class _Node():
        def __init__(self):
            self._ch = {}
            #self._bool = False

    def __init__(self):
        self._root = None

    def prefix(self,s):
        n = self._root
        if not n: #no root
            return False
        for c in s:
            if c in n._ch: #found prefix
                n = n._ch[c]
            else: #fall off
                return False
                
        return True

    def add(self,s):#add "$" at end for special char
        n = self._root
        if not n: #no root
            n = self._root = self._Node()
        for c in s:
            if c in n._ch:
                n = n._ch[c]
            else: #make new child if not there
                n._ch[c] = self._Node()
                n = n._ch[c]

    
                
