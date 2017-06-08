'''
Mayank Vanjani mv1506
Homework 6
3/20/17
'''

#####UNCHANGED#####
class PList():
    class _Node():
        __slots__ = '_data','_prev','_next'
        def __init__(self, data, prev, next):
            self._data = data
            self._prev = prev
            self._next = next
    class Position():
        def __init__(self, plist, node):
            self._plist = plist
            self._node = node
        def data(self):
            return self._node._data
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self,other):
            return not (self==other)

    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("p must be a proper Position type")
        if p._plist is not self:
            raise ValueError("p does not belong to this Plist")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node
    def _make_position(self,node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self,node)
    
    def __init__(self):
        self._head = self._Node(None, None, None)
        self._head._next = self._tail = self._Node(None, self._head, None)
        self._size = 0
    def __len__(self):
        return self._size
    def __isempty(self):
        return self._size == 0
    def first(self):
        return self._make_position(self._head._next)
    def last(self):
        return self._make_position(self._tail._prev)
    def before(self,p):
        node = self._validate(p)
        return self._make_position(node._prev)
    def after(self,p):
        node = self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        pos = self._first
        while(pos):
            yield pos.data()
            pos = self._after(pos)
    def _insert_after(self,data,node):
        newNode = self._Node(data, node, node._next)
        node._next._prev = newNode
        node._next = newNode
        self._size += 1
        return self._make_position(newNode)
    def add_first(self,data):
        return self._insert_after(data, self._head)
    def add_last(self,data):
        return self._insert_after(data, self._tail._prev)
    def add_before(self, p, data):
        node = self._validate(p)
        return self._insert_after(data, node._prev)
    def add_after(self, p, data):
        node = self._validate(p)
        return self._insert_after(data, node)
    def delete(self,p):
        node = self._validate(p)
        data = node._data
        node._prev._next = node._next
        node._next._prev = node._prev
        node._prev = node._next = node._data = None
        self._size -= 1
        return data
    def replace(self,p,data):
        node = self._validate(p)
        olddata = node._data
        node._data = data
        return olddata
    def rev_itr(self):
        pos = self._last()
        while pos:
            yield pos.data()
            pos = self.before(pos)

#####FIXED VALIDATION#####
class Counters():
    class _Item():
        def __init__(self,name):
            self._name = name
            self._count = 0
    class Counter():
        def __init__(self,position):
            self._position = position
        def name(self):
            return self._position.data()._name
        def count(self):
            return self._position.data()._count

    def _validate(self,p):
        if p._plist is not self._L:
            raise ValueError("counter does not belong to this Counter")
        
    def __init__(self):
        self._L = PList()
    def new_counter(self,name):
        self._L.add_last(Counters._Item(name))
        return Counters.Counter(self._L.last())
    def delete_counter(self,counter):
        self._validate(counter._position)
        self._L.delete(counter._position)
        counter._position = None
    def increment_counter(self,counter):
        self._validate(counter._position)
        #print(type(counter._position))
        counter._position.data()._count += 1
        before_position = self._L.before(counter._position)
        while (before_position and before_position.data()._count < counter.count()):
            new_position = self._L.add_before(before_position,counter._position.data())
            self._L.delete(counter._position)
            counter._position = new_position
            before_position = self._L.before(counter._position)
    def __iter__(self):
        position = self._L.first()
        while position:
            yield Counters.Counter(position)
            position = self._L.after(position)

#####Question 2#####
class newCounters():
    '''
    newCounters has 1 connection to a PList of PLists
    Position changes: 1 connection to a position and inside PList,
         and the other to a position of a PList and the root PList
    '''
    class newCounter():#Keeps track of data and a count of data
        def __init__(self,name,count=0):
            self._name = name
            self._count = count
    class newPosition():
        def __init__(self,position1, position2):
            self._position1 = position1#node for counter and inner plist
            self._position2 = position2#node for inner plist and root plist

    def __init__(self):
        self._L = PList()
        new_list = PList() #the pList of 0 counts
        self._L.add_last(new_list)

    def new_counter(self, name):
        new = self.newCounter(name)
        node = self._L.last().data()
        node.add_last(new)
        pos = self.newPosition(node.last(),self._L.last())
        return pos
    
    def delete_counter(self, position ):
        node = position._position1
        position._position2.data().delete(node)
        
    def increment_counter(self, position):
        node = position._position1
        '''
        print("Node:", type(node))
        print("Nodedata:", type(node.data()))
        '''
        if not node or not node.data():
            #print("BROKEN Counter:", node, node.data(), node.data,"\n")
            print("BROKEN Counter\n")
            return

        name = node.data()._name
        node.data()._count += 1
        count = node.data()._count

        self.delete_counter(position)
        '''
        print("Len:", len(position._position2.data()))
        print(type(position._position2))
        print(self._L == position._position2._plist)
        print(type(self._L.after(position._position2)))
        '''
        #Empty PList Checking and Elimination
        next_node = self._L.before(position._position2)
        if len(position._position2.data()) == 0:
            self._L.delete(position._position2)

        if not next_node:
            #print("Case 1:", name, count)
            new_list = PList()
            counter = self.newCounter(name,count)
            new_list.add_last(counter)
            self._L.add_first(new_list)
            #print("TEST:",type(position._position2.data()))
            position._position1._plist = new_list
            position._position1._node = new_list.last()._node
            position._position2._node = self._L.first()._node
            #print(type(position._position2.data()))
            #print(type(position._position1._plist))
            #print(position._position2.data() == position._position1._plist)
            #print("Nothing after:", position._position1)
            
        elif next_node.data().last().data()._count == count:
            #print("Case 2:", name, count)
            #print(next_node.data())
            counter = self.newCounter(name,count)
            next_node.data().add_last(counter)
            position._position1._plist = next_node.data()
            position._position1._node = next_node.data().last()._node
            position._position2._node = next_node._node
            #print(position._position2.data() == position._position1._plist)
            #print("Same after:", position._position1)

        elif next_node.data().last().data()._count > count:
            #print("Case 3:", name, count)
            new_list = PList()
            counter = self.newCounter(name,count)
            new_list.add_first(counter)
            self._L.add_before(position._position2, new_list)
            position._position1._plist = new_list
            position._position1._node = new_list.first()._node
            position._position2._node = self._L.before(position._position2)._node
            #print(position._position2.data() == position._position1._plist)
            #print("Greater after:", position._position1)
            
    def __iter__(self):
        temp = self._L.last()
        #print("temp:", temp)
        counter = 0
        while temp:
            counter += 1
            temp_node = temp.data().first()#position to first
            #print(temp_node)
            while temp_node and temp_node.data():
                yield (str(temp_node.data()._name) +" "+ str(temp_node.data()._count))
                temp_node = temp.data().after(temp_node)
            #print()
            #print("size:", temp.data()._size)            
            temp = self._L.before(temp)
            #print("check")
        #print("num plists:", counter)

#####Question 3#####
print("TESTING OLD COUNTERS:")
C = Counters()
names = ("John","Guruprasad","Jason","Duc","Eric","Xinran","Kent","Leon","Ian")
counters = [C.new_counter(name) for name in names]
for i in range(1000):
    for cp in counters:
        C.increment_counter(cp)
for i in range(len(counters)):
    for j in range(i):
        C.increment_counter(counters[i])
C.delete_counter(counters[3])
for c in C:
    print(c.name(), c.count())

print("\n\nTESTING NEW COUNTERS:")
C = newCounters()
counters = [C.new_counter(name) for name in names]
for i in range(1000):
    for cp in counters:
        C.increment_counter(cp)
for i in range(len(counters)):
    for j in range(i):
        C.increment_counter(counters[i])
C.delete_counter(counters[3])
for c in C:
    print(c)
    
'''
#QUESTION 1#
print("\nTesting Old Counter ")
C = Counters()
D = Counters()
cc = C.new_counter("A counter in C")
D.increment_counter(cc)
'''

'''
print("\n\nTesting New Counter Now")
C = newCounters()
names = ["a","b","c","d","e"]
counters = [C.new_counter(name) for name in names]
for i in C:
    print(i)
    
print("After deleting b:")
C.delete_counter(counters[1])
for i in C:
    print(i)

print("After incrementing:")
C.increment_counter(counters[1])#b should exit automatically

#C.increment_counter(counters[0])#a
C.increment_counter(counters[0])#a
C.increment_counter(counters[4])#e
C.increment_counter(counters[4])#e
C.increment_counter(counters[2])#c
C.increment_counter(counters[2])#c
#C.increment_counter(counters[4])#e
#C.increment_counter(counters[4])#e

for i in C:
    print(i)
'''
