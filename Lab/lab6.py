#---------------The PList code I posted earlier---------

class PList:
    class _Node:
        __slots__='_data','_prev','_next'
        def __init__(self,data,prev,next):
            self._data=data
            self._prev=prev
            self._next=next
    class Position:
        def __init__(self,plist,node):
            self._plist=plist
            self._node=node
            self._position_check = plist._check
        def data(self):
            return self._node._data
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self,other):
            return not (self == other)

    class Checker:
        def __init__(self):
            self._check = True

    def _invalidate_positions(self):
        self._check._check = False
        self._check = self.Checker()
        #print(self._check._check)
        
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Position type")
        if p._plist is not self:
            raise ValueError('p does not belong to this PList')
        #print(p._position_check._check)
        if p._node._next is None or not p._position_check._check:
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self,node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self,node)

    def __init__(self):
        self._head=self._Node(None,None,None)
        self._head._next=self._tail=self._Node(None,self._head,None)
        x = self.Checker()
        self._check = x
        #self._size=0

    def __len__(self):
        counter = 0
        temp = self._head._next
        while temp:
            counter += 1
            temp = temp._next
        return counter-1
    
    def is_empty(self):
        return len(self)==0
    def first(self):
        return self._make_position(self._head._next)
    def last(self):
        return self._make_position(self._tail._prev)
    def before(self,p):
        node=self._validate(p)
        return self._make_position(node._prev)
    def after(self,p):
        node=self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        pos = self.first()
        while pos:
            yield pos.data()
            pos=self.after(pos)
    def _insert_after(self,data,node):
        newNode=self._Node(data,node,node._next)
        node._next._prev=newNode
        node._next=newNode
        #self._size+=1
        return self._make_position(newNode)
    def add_first(self,data):
        return self._insert_after(data,self._head)
    def add_last(self,data):
        return self._insert_after(data,self._tail._prev)
    def add_before(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node._prev)
    def add_after(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node)
    def delete(self,p):
        node=self._validate(p)
        data=node._data
        node._prev._next=node._next
        node._next._prev=node._prev
        node._prev=node._next=node._data=None
        #self._size-=1
        return data
    def replace(self,p,data):
        node=self._valdiate(p)
        olddata=node._data
        node._data=data
        return olddata
    def rev_itr(self):
        pos = self.last()
        while pos:
            yield pos.data()
            pos=self.before(pos)

    def __iadd__(self, other):
        self._tail._prev._next = other._head._next
        other._head._next._prev = self._tail._prev
        self._tail._prev = other._tail._prev
        other._tail._prev._next = self._tail
        other._head._next = other._tail
        other._tail._prev = other._head
        other._invalidate_positions()
        return self

    def split_after(self, pos):
        new = PList()
        new._head._next = pos._node._next#new head next = 3
        new._tail._prev = self._tail._prev#new tail prev = self tail prev
        pos._node._next._prev = new._head#prev 3 = new head
        self._tail._prev._next = new._tail#next 3 = new tail
        self._tail._prev = pos._node#self tail prev = pos
        pos._node._next = self._tail#next of 2 = self tail
        self._invalidate_positions()
        return new
        
    def split_before(self, pos):
        new = PList()
        new._head._next = pos._node#new head next = 2
        new._tail._prev = self._tail._prev#new tail prev = 3
        self._tail._prev._next = new._tail#3 next = new tail
        pos._node._prev._next = self._tail#1 next = self tail
        self._tail._prev = pos._node._prev#self tail prev = 1
        pos._node._prev = new._head#prev 2 = new head
        self._invalidate_positions()
        return new
    
#---------------CODE USED TO CHECK TESTS--------------------
def printList(L):
    print(" Forward:",list(L))
    print(" Backward:",list(L.rev_itr()))
    
def checkAnswer(taskno,testno,yours,correct):
    print("Task:",taskno," Test:",testno,end=" ")
    if yours==correct:
        print("Correct: ",yours)
    else:
        print("Wrong: ", yours," The correct answer is:")
        print(correct)
            
def checkList(taskno,testno,yours,correctforward):
    print("Task:",taskno," Test:",testno,end=" ")
    yoursforward=list(yours)
    yoursbackward=list(yours.rev_itr())
    correctbackward=correctforward.copy()
    correctbackward.reverse()
    if yoursforward==correctforward:
        if yoursbackward==correctbackward:
            print("Correct: ",yoursforward)
        else:
            print("Wrong! Your forward iterator is correct and gives ",
                  yoursforward,
                  " but your reverse iterator gives ",
                  yoursbackward)    
    else:
        print("Wrong. Your code gives ",yoursforward,
              " but the correct answer is:",correctforward)

#------------------------------------------------------
"""
To enable the test code for each task, change the booleans below. When you are
working on one task you may want to disable the others.
"""
testTask1=True
testTask2=True
testTask3=True
testTask4=True
testTask5=False

#------------------------TASK 1-----------------------
if (testTask1):
    print("\n------TASK 1------")
    L=PList()
    for i in range(5):
        L.add_first(i)
    printList(L) #Demo of the printList function, you may want to use to debug
    checkAnswer(1,1,len(L),5)
    checkAnswer(1,2,L.is_empty(),False)
    checkAnswer(1,3,len(PList()),0)
    checkAnswer(1,4,PList().is_empty(),True)

#------------------------TASK 2-----------------------
if (testTask2):
    print("\n------TASK 2------")
    L=PList()
    for i in range(5):
        L.add_first(i)
    L2=PList()
    for i in ("a","b","c","d","e"):
        L2.add_first(i)
    L+=L2
    checkList(2,1,L,[4, 3, 2, 1, 0, 'e', 'd', 'c', 'b', 'a'])
    checkList(2,2,L2,[])

#------------------------TASK 3----------------
if (testTask3):
    print("\n------TASK 3------")
    L=PList()
    for i in [1,2,"a","b"]:
        L.add_last(i)
    L2=L.split_after(L.after(L.first()))
    checkList(3,1,L,[1,2])
    checkList(3,2,L2,['a','b'])
    L3=L2.split_before(L2.last())
    checkList(3,3,L2,['a'])
    checkList(3,4,L3,['b'])
    L4=L3.split_before(L3.first())
    checkList(3,5,L3,[])
    checkList(3,6,L4,['b'])

#------------------------TASK 4-----------------------
if (testTask4):
    print("\n------TASK 4------")
    L=PList()
    for i in range(5):
        L.add_first(i)
    p=L.last()
    L2=L.split_before(L.before(p))
    try:
        q=L.before(p)
    except ValueError:
        print("Task: 4 Test:1 Correctly has an exception")
    else:
        print("Task: 4 Test:1 Wrong! No exception")
    try:
        q=L2.before(p)
    except ValueError:
        print("Task: 4 Test:2 Correctly has an exception")
    else:
        print("Task: 4 Test:2 Wrong! No exception")
    p=L.first()
    p2=L2.first()
    try:
        p=L.after(p)
        p2=L2.after(p2)
        L+=L2
        p=L.before(p)
    except ValueError:
        print("Task: 4 Test:3 Wrong! There should be no exception")
    else:
        print("Task: 4 Test:3 Correct, no exception")
    try:
        p2=L2.before(p2)
    except ValueError:
        print("Task: 4 Test:4 Correctly has an exception")
    else:
        print("Task: 4 Test:4 Wrong! No exception")

#------------------------TASK 5-----------------------
if (testTask5):
    print("\n------TASK 5------")
    L=PList()
    for i in range(5):
        L.add_first(i)
        
    #checking the basic flip operation
    L.flip()
    checkList(5,1,L, [0, 1, 2, 3, 4])
    L2=PList()
    for i in ("a","b","c","d","e"):
        L2.add_first(i)
    #checking the += works with flip
    L+=L2
    checkList(5,2,L,[0, 1, 2, 3, 4, 'e', 'd', 'c', 'b', 'a'])
    checkList(5,3,L2,[])
    
    #checking that split works with flip
    L=PList()
    for i in [1,2,"a","b"]:
        L.add_last(i)
    L.flip()
    L2=L.split_after(L.after(L.first()))
    checkList(5,4,L2,[2,1])
    checkList(5,5,L,['b','a'])
    L3=L2.split_before(L2.last())
    L.flip()
    checkList(5,6,L2,[2])
    checkList(5,7,L3,[1])
    L4=L3.split_before(L3.first())
    checkList(5,8,L3,[])
    checkList(5,9,L4,[1])
    
    #checking the positions move in the right direction always
    L=PList()
    for i in range(5):
        L.add_last(i)
    p=L.after(L.first())
    checkAnswer(5,10,(L.before(p).data(),L.after(p).data()),(0,2))
    L.flip()
    checkAnswer(5,11,(L.before(p).data(),L.after(p).data()),(2,0))
