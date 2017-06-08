class BinaryTree():
    class Node():
        def __init__(self, left, right, parent, data):
            self._left = left
            self._right = right
            self._parent = parent
            self._data = data
    class Position():
        def __init__(self, node, tree):
            self._node = node
            self._tree = tree
        def element(self):
            return self._node._data

    def root(self):
        return self.Position(self._root,self)
    def parent(self,p):
        return self.Position(p._node._parent,self)
    def left(self,p):
        return self.Position(p._node._left,self)
    def right(self,p):
        return self.Position(p._node._right,self)
    def sibling(self,p):
        #make sure not root
        if p != self.root():
            if p == self.left(self.parent(p)):
                return self.right(self.parent(p))
            else:
                return self.left(self.parent(p))
    def children(self,p):
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)
    def __init__(self):
        self._root = None
        self._size = 0

        
    #3/22/17
    def add_root(self,d):
        if self.is_empty():
            self._root = self.Node(None,None,None,d)
            self._size += 1
            return self.Position(self._root,self)
        else:
            print("Can't add root")
    def add_left(self,p,d):
        if not p._node._left:
            p._node._left = self.Node(None,None,p._node,d)
            self._size += 1
            return self.Position(p._node._left,self)
        else:
            print("Already a child there")
    def add_right(self,p,d):
        if not p._node._right:
            p._node._right = self.Node(None,None,p._node,d)
            self._size += 1
            return self.Position(p._node._right,self)
        else:
            print("Already a child there")
    #def replace just change data of position
    def delete(self,p):
        if num_children(p) == 2:
            print("Can't delete because 2 children")
        else:
            parent = p._node._parent #or self.parent(p)
            if p = self.right(parent):
                if self.isLeaf(p):
                    parent._node._right = None
                else:
                    if p._node._right:
                        parent._node._right = p._node._right
                        p._node._right._parent = parent._node
                    else:
                        parent._node._left = p._node._left
                        p._node._left._parent = parent._node
                p._node = None
                #could have validate position for each time you use p
                #need validation because you set the node of this position to None
                self._size -= 1
    def attach(self,p,t1,t2):
        if self.isLeaf(p):
            p._node._left = t1._root
            t1._root._parent = p._node
            p._node._right = t2._root
            t2._root._parent = p._node
            self._size += t1._size + t2._size
            t1._root = t2._root = None
            t1._size = t2._size = 0
        else:
            print("Can't attach")

    def rec_iter(self,p):
        yield p.element()#preorder
        l = self.left(p)
        r = self.right(p)
        if l:
            #recursive call to generator needs yield from
            yield from self.rec_iter(l)
            #yield p.element()#inorder
        if r:
            yield from self.rec_iter(r)
            #yield p.element()#postorder
            
    def __iter__(self):
        pass

    def level_order(self):
        #use append and popleft of deque in collections
        q = queue()
        q.enque(self._root)
        while not q.is_empty():
            p = q.dequeue()#p for pos, p._elem for elem
            yield p
            for child_pos in self.children(p):
                q.enque(child_pos)
            

class expression_tree():
    #((2+(6/2))*8)
    def __init__(self):
        self._T = BinaryTree()
    def rec_string(self,p):
        if self._T.isleaf(p):
            return str(p.element())
        else:
            return ("("+rec_string(self._T.left(p))+
                    str(p.element())+
                    rec_string(self._T.right(p)) + ")")

    #if inherited: no init from ._T so get rid of all ._T
    '''
    def rec_string(self,p):
        if self.isleaf(p):
            return str(p.element())
        else:
            return ("("+rec_string(self.left(p))+
                    str(p.element())+
                    rec_string(self.right(p)) + ")")
    '''
    def __str__(self):
        return self.rec_string(self._T.root())

    #better to join in a list of strings
    #change last line to just ["(",rec_string(self._T.left(p))...]
    #but this returns a list of lists because of internal recursion
    #use extend on recursive and append on "(" and ")" then join everything

    def eval_rec(self,p):
        if self._T.isleaf(p):
            return p.element()
        else:
            Lval = self.eval_rec(self._T.left(p))
            Rval = self.eval_rec(self._T.right(p))
            if p.element() == "+":
                return Lval + Rval
            elif p.element() == "-":
                return Lval - Rval
            elif p.element() == "*":
                return Lval * Rval
            elif p.element() == "/":
                return Lval / Rval
    def eval(self):
        self.eval_rec(self._T.root())

    def __init__(self,tokens):
        s = Stack()
        for t in tokens:
            if t in "+-*/":
                s.push(t)
            elif isinstance(t,int):
                T = BinaryTree()
                T.add_root(t)
                s.push(T)
            elif t == ")":
                RT = s.pop()
                op = s.pop()
                LT = s.pop()
                T = BinaryTree()
                T.add_root(op)
                T.attach(T.root(),LT,RT)
                s.push(T)
        self._T = s.pop()




    
            
