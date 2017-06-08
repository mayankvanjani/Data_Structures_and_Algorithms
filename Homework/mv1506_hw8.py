'''
Mayank Vanjani mv1506
Homework 8
4/4/17
'''

import random

class BST:
    class _Node:
        def __init__(self,parent,left,right,data):
            self._left=left
            self._right=right
            self._parent=parent
            self._data=data

    class Position:
        def __init__(self, node, tree):
            self._node = node
            self._tree = tree
        def element(self):
            return self._node._data
        
    def __init__(self):
        self._root=None
        self._size = 0
        
    def insert(self,x):
        if self._root == None:
            self._root=BST._Node(None,None,None,x)
        else:
            self._rec_insert(self._root,x)
        self._size += 1
    def _rec_insert(self,n,x):
        if x<n._data:
            if n._left == None:
                n._left=BST._Node(n,None,None,x)
            else:
                self._rec_insert(n._left,x)
        else:
            if n._right == None:
                n._right=BST._Node(n,None,None,x)
            else:
                self._rec_insert(n._right,x)

    def search_le(self,x):
        if self._root==None:
            return None
        else:
            return self._rec_search_le(self._root,x)
    def _rec_search_le(self,n,x):
        if x<n._data:
            if n._left:
                return self._rec_search_le(n._left,x)
            else:
                return None
        else:
            if n._right:
                rv=self._rec_search_le(n._right,x)
                if rv:
                    return rv
                else:
                    return n._data
            else:
                return n._data

    ###Question 1###
    def iter_helper(self,pos):
        if not pos:
            yield None
        else:
            if pos._left:
                yield from self.iter_helper(pos._left)
            yield pos._data
            if pos._right:
                yield from self.iter_helper(pos._right)
        
    def __iter__(self):
        yield from self.iter_helper(self._root)

    ###Question 2###
    def search_ge(self,x): #smallest val in tree >= x
        if self._root==None:
            return None
        else:
            return self._rec_search_ge(self._root,x)
    def _rec_search_ge(self,n,x):
        if x == n._data:
            return x

        elif x < n._data:
            if n._left:
                return self._rec_search_ge(n._left,x)
            else:
                while n and x > n._data:
                    n = n._parent
                return n._data

        elif x > n._data:
            if n._right:
                return self._rec_search_ge(n._right,x)
            else:
                while n and x > n._data:
                    n = n._parent
                if n:
                    return n._data
                else:
                    return None

    ###Question 3###
    # Added size to init of BST
    def __len__(self):
        return self._size

    ###Question 4###
    #Create a list of data,depth tuples and loop over them to print
    def depth(self, p):
        if p == self._root:
            return 0
        else:
            return 1 + self.depth(p._parent)

    def create_pair(self,pos):
        return (pos._data, self.depth(pos))

    def unnest(self,X):
        ret = []
        for e in X:
            ret.extend(self.unnest(e) if isinstance(e,list) else [e])
        return ret
    
    def create_lst(self,p="init"):
        if p == "init":
            p = self._root
        left = right = []
        if p._left:
            left = self.create_lst(p._left)
        if p._right:
            right = self.create_lst(p._right)
        return self.unnest([left] + [self.create_pair(p)] + [right])

    def max_depth(self, pos="init"):
        if pos == "init":
            pos = self._root
        if pos._left and pos._right:
            return 1 + max(self.max_depth(pos._left),self.max_depth(pos._right))
        elif pos._left:
            return 1 + self.max_depth(pos._left)
        elif pos._right:
            return 1 + self.max_depth(pos._right)
        else:
            return 1
        
    def print(self):
        lst = self.create_lst()
        max_depth = self.max_depth()

        for i in range(max_depth):
            for pair in lst:
                if pair[1] == i:
                    print( str(pair[0]), end="" )
                else:
                    print(" "*len(str(pair[0])), end="")
            print()
            #if i <= max_depth:
                #print(i, max_depth)
            #print("end", i, lst[i], max_depth)
        print()

    ###Question 5###
    #Special cases in before/after when pos is a leaf
    def first(self):
        node = self._root
        while node._left:
            node = node._left
        if node == None:
            return None
        else:
            return self.Position(node, self)
    def last(self):
        node = self._root
        while node._right:
            node = node._right
        if node == None:
            return None
        else:
            return self.Position(node, self)
        
    def before(self,p):
        node = p._node
        if node and not node._left and not node._right:
            temp = node._data
            node = node._parent
            while node and node._data > temp:
                node = node._parent

        else:
            node = node._left
            while node and node._right:
                node = node._right
                
        if node == None:
            return None
        else:
            return self.Position(node, self)

    def after(self,p):
        node = p._node
        if node and not node._left and not node._right:
            temp = node._data
            node = node._parent
            while node and node._data < temp:
                node = node._parent

        else:
            node = node._right
            while node and node._left:
                node = node._left

        if node == None:
            return None
        else:
            return self.Position(node, self)

    ###Question 6###
    # Same as first part but return node converted to position instead of data
    def pos_ge(self,x):
        if self._root==None:
            return None
        else:
            node = self._rec_search_ge_pos(self._root,x)
            if node == None:
                return None
            else:
                return self.Position(node,self)
    def _rec_search_ge_pos(self,n,x):
        if x == n._data:
            return n

        elif x < n._data:
            if n._left:
                return self._rec_search_ge_pos(n._left,x)
            else:
                while n and x > n._data:
                    n = n._parent
                return n

        elif x > n._data:
            if n._right:
                return self._rec_search_ge_pos(n._right,x)
            else:
                while n and x > n._data:
                    n = n._parent
                if n:
                    return n
                else:
                    return None

    def pos_le(self,x):
        if self._root==None:
            return None
        else:
            node = self._rec_search_le_pos(self._root,x)
            if node == None:
                return None
            else:
                return self.Position(node,self)
    def _rec_search_le_pos(self,n,x):
        if x<n._data:
            if n._left:
                return self._rec_search_le_pos(n._left,x)
            else:
                return None
        else:
            if n._right:
                rv=self._rec_search_le_pos(n._right,x)
                if rv:
                    return rv
                else:
                    return n
            else:
                return n

    ###Question 7###
    # Range_pos is same as range just returning positions instead of data
    def range(self,x,y,pos="init"):
        if pos == "init":
            pos = self._root

        if pos._data >= x:
            if pos._left:
                yield from self.range(x,y,pos._left)
        if pos._data >= x and pos._data < y:
            #print("temp")
            yield pos._data
        if pos._data < y:
            if pos._right:
                yield from self.range(x,y,pos._right)

    def range_pos(self,x,y,pos="init"):
        if pos == "init":
            pos = self._root

        if pos._data >= x:
            if pos._left:
                yield from self.range_pos(x,y,pos._left)
        if pos._data >= x and pos._data < y:
            #print("test")
            yield self.Position(pos,self)
        if pos._data < y:
            if pos._right:
                yield from self.range_pos(x,y,pos._right)


                
#---------------------------------------------------------#                
###TEST CASES###

T=BST()
L=list(range(10,100,10))
#L=list(range(10,100,2))
#print("L:",L)
random.shuffle(L)
#L = [50,40,20,10,30,70,60,90,80]

print("\nL:",L)
print("\nPut all elements of L into a BST:")
for i in L:
    T.insert(i)

print("BST L in order:", end="  ")
for i in T:
    print(i, end=" ")
print("\n\n")

for i in range(5,100,10):
    print("Searching Greater than or Equal To", i, ": Found", T.search_ge(i))
    print("Searching Less than or Equal To", i, ": Found", T.search_le(i))
    print()

print("Length:", len(T), "nodes" )
print("L:",L)
print()
#print(T.create_pair(T._root._left))
#print(T.create_lst())
T.print()

if T.first():
    print("FIRST:",T.first().element())
    if T.after(T.first()):
        print("After First:", T.after(T.first()).element())#
    else:
        print("No element after", T.first().element())
    if T.before(T.first()):
        print("Before First:", T.before(T.first()).element())
    else:
        print("No element before", T.first().element())#
else:
    print("No First Element")
    
if T.last():
    print("LAST:",T.last().element())
    if T.after(T.last()):
        print("After Last:", T.after(T.last()).element())
    else:
        print("No element after", T.last().element())#
    if T.before(T.last()):
        print("Before Last:", T.before(T.last()).element())#
    else:
        print("No element before", T.last().element())
else:
    print("No Last Element")    
print()

nums = [5,50,55,95]
for i in nums:
    if T.pos_ge(i):
        print("Element of Position >=", i, ":", T.pos_ge(i).element())
    else:
        print("No Element >=", i)
    if T.pos_le(i):
        print("Element of Position <=", i, ":", T.pos_le(i).element())
    else:
        print("No Element <=", i)
print()

print("Normal Iteration with Data:")
for i in T.range(10,90):
    print(i, end=" ")
print()
print("New Iteration with Position and element():")
for i in T.range_pos(10,90):
    #print(type(i))
    print(i.element(), end=" ")
print("\n")

print("Range 0-100:")
for i in T.range(0,100):
    print(i, end=" ")
print()
print("With Positions:")
for i in T.range_pos(0,100):
    print(i, "=>", i.element())
print()
print("Range 10-90:")
for i in T.range(10,90):
    print(i, end=" ")
print()
print("With Positions:")
for i in T.range_pos(10,90):
    print(i, "=>", i.element())
print()
print("Range 100-200:")
for i in T.range(100,200):
    print(i, end=" ")
print()
print("With Positions:")
for i in T.range_pos(100,200):
    print(i, "=>", i.element())
print("\n")

###Question 8###
print("TREE IN QUESTION 8")
T = BST()
start = 32
stop = 2 * start - 1
T.insert(start)
while start > 1:
    temp = (start // 2)

    while temp <= stop:
        T.insert(temp)
        temp += start

    start = start // 2

T.print()

###Question 9###
print("TREE IN QUESTION 9")
T = BST()
for i in range(10):
    T.insert(i)
    T.insert(20-i)
T.print()




