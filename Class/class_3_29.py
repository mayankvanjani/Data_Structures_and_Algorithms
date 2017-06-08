class BST(): #Binary Search Tree without inheritance
    class _Node():
        def __init__(self,par,L,R,data):
            self._parent = par
            self._left = L
            self._right = R
            self._data = data

    def __init__(self):
        self._root = None

    def insert(self, x):
        if self._root == None:
            self._root = self._Node(None,None,None,x)
        else:
            self._insert_rec(self._root,x)
    def _insert_rec(self,n,x):
        if n._data < x:#Right Recursion
            if n._right:
                self._insert_rec(n._right,x)
            else:
                n._right = self._Node(n,None,None,x)
        else:#Left Recursion
            if n._left:
                self._insert_rec(n._left,x)
            else:
                n._left = self._Node(n,None,None,x)
            
    def delete(self,x): #has to be in tree
        n = self._root
        while n._data != x:
            if x < n._data:
                n = n._left
            else:
                n = n._right

        #2 children
        elif n._left and n._right:
            srs = n._right
            while srs._left:
                srs = srs._left
                
            n._data = srs._data
        n = srs#use ordering to have this before other deletes
        #n ends up as a child with 1 or no children => just del
        
        #leaf
        if n._left==None and n._right==None:
            if n = self._root:
                self._root = None
            elif n == n._parent._left:
                n._parent._left = None
            elif n == n._parent._right:
                n._parent._right = None
        #1 child
        #another special case if n is the root
        elif (n._left==None and n._right):
            n._right._parent = n._parent
            if n==self._root:
                self._root = n._right
            elif n == n._parent._left:
                n._parent._left = n._right
            elif n == n._parent._right:
                n._parent._right = n._right
                
        elif (n._left and n._right==None):
            n._left._parent = n._parent
            if n==self._root:
                self._root = n._left
            elif n == n._parent._left:
                n._parent._left = n._left
            elif n == n._parent._right:
                n._parent._right = n._left
        '''
        #2 children
        elif n._left and n._right:
            srs = n._right
            while srs._left:
                srs = srs._left
                
            n._data = srs._data
        n = srs#use ordering to have this before other deletes
        #n ends up as a child with 1 or no children => just del
        '''
        
    def _rec_find_le(self,n,x):
        if x > n._data:
            if n._right:
                rv = self._rec_find_le(n._right,x)
                if rv:
                    return rv
                else:
                    return n._data
            return n._data
        else:
            if n._left:
                lv = self._rec_find_le(n._left,x):
                if lv:
                    return lv
                else:
                    return None
            return None
        
    def find_le(self,x):#less than or equal to or biggest thing <= x
        #find ge is symmetric code least thing >= x
        if self._root == None:
            return None
        else:
            return self._rec_search_le(n._left,x)
    
    
